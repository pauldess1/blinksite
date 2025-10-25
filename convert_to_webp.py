from PIL import Image
import os
import subprocess

# Répertoire contenant tes images statiques
IMG_DIR = "C:/Users/pauld/Desktop/Code/blinksite/static/images"

# Crée un sous-dossier "optimized" pour ne pas écraser les originaux
OUTPUT_DIR = os.path.join(IMG_DIR, "optimized")
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Extensions à traiter
VALID_EXTENSIONS = (".png", ".jpg", ".jpeg")

# Qualité de compression (0-100)
QUALITY = 85

def optimize_svg(file_path):
    name = os.path.basename(file_path)
    output_path = os.path.join(OUTPUT_DIR, name)
    subprocess.run([
        "scour",
        "-i", file_path,
        "-o", output_path,
        "--enable-id-stripping",
        "--enable-comment-stripping",
        "--shorten-ids",
        "--strip-xml-prolog",
        "--indent=none",
        "--remove-metadata",
        "--quiet"
    ])
    original_size = os.path.getsize(file_path) / 1024
    new_size = os.path.getsize(output_path) / 1024
    gain = (1 - new_size / original_size) * 100
    print(f"{name} optimisé : {original_size:.1f} Ko → {new_size:.1f} Ko ({gain:.1f}% gagné)")

def convert_image(path):
    name, ext = os.path.splitext(os.path.basename(path))
    if ext.lower() not in VALID_EXTENSIONS:
        return

    img = Image.open(path)
    # Garder alpha uniquement si existant
    if img.mode in ("RGBA", "LA") or (img.mode == "P" and "transparency" in img.info):
        img = img.convert("RGBA")
    else:
        img = img.convert("RGB")

    output_path = os.path.join(OUTPUT_DIR, f"{name}.webp")
    img.save(output_path, "webp", quality=QUALITY, method=6)  # compression standard
    original_size = os.path.getsize(path) / 1024
    new_size = os.path.getsize(output_path) / 1024
    gain = (1 - new_size / original_size) * 100
    print(f"{name}{ext} → {name}.webp : {original_size:.1f} Ko → {new_size:.1f} Ko ({gain:.1f}% gagné)")


def main():
    for file in os.listdir(IMG_DIR):
        file_path = os.path.join(IMG_DIR, file)
        if os.path.isfile(file_path):
            convert_image(file_path)

    for file in os.listdir(IMG_DIR):
        if file.lower().endswith(".svg"):
            optimize_svg(os.path.join(IMG_DIR, file))


convert_image("static/images/arthur.png")