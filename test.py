from django.core.management.utils import get_random_secret_key  
secret = get_random_secret_key()
print(f"DJANGO_SECRET_KEY={secret}")