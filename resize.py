from PIL import Image
import os

source_dir = "static/images"
output_dir = os.path.join(source_dir, "responsive")
os.makedirs(output_dir, exist_ok=True)

# Tailles cibles
desktop_width = 700
mobile_width = 234

for filename in os.listdir(source_dir):
    if filename.lower().endswith(".webp"):
        input_path = os.path.join(source_dir, filename)
        img = Image.open(input_path)
        name, ext = os.path.splitext(filename)

        # Desktop
        if img.width > desktop_width:
            ratio = desktop_width / img.width
            new_height = int(img.height * ratio)
            img_desktop = img.resize((desktop_width, new_height), Image.LANCZOS)
        else:
            img_desktop = img.copy()
        img_desktop.save(os.path.join(output_dir, f"{name}-desktop.webp"), "WEBP", quality=85)

        # Mobile
        if img.width > mobile_width:
            ratio = mobile_width / img.width
            new_height = int(img.height * ratio)
            img_mobile = img.resize((mobile_width, new_height), Image.LANCZOS)
        else:
            img_mobile = img.copy()
        img_mobile.save(os.path.join(output_dir, f"{name}-mobile.webp"), "WEBP", quality=85)

        print(f"Images générées pour : {filename}")
