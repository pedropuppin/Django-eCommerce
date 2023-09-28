from PIL import Image
import os
from django.conf import settings

@staticmethod
def resize_image(image, new_width=800):
    img_full_path = os.path.join(settings.MEDIA_ROOT, image.name)
    img_pillow = Image.open(img_full_path)
    original_width, original_height = img_pillow.size
    
    if original_width <= new_width:
        img_pillow.close()
        return
    
    new_height = round((new_width * original_height) / original_width)
    
    new_img = img_pillow.resize((new_width, new_height), Image.LANCZOS)
    new_img.save(
        img_full_path,
        optimize=True,
        quality=50
    )
    print(f'Imagem {image.name} redimensionada com sucesso!')