from django.db import models
from django.core.files import File
from PIL import Image, ImageDraw
from io import BytesIO
import qrcode


class Products(models.Model):
    id  = models.CharField(max_length=12, primary_key=True, unique=True, editable=False)
    name = models.CharField(max_length=120, blank=False)
    qr_code = models.ImageField(upload_to='qrcodes/', blank=True)
    created = models.DateTimeField(auto_now_add=True)
    edited = models.DateTimeField(auto_now=True)


    def __str__(self):
        return f'{self.name}'

    def save(self, *args, **kwargs):
        qrcode_img = qrcode.make(self.name)
        img_canvas = Image.new('RGB', (300, 300), 'white')
        draw = ImageDraw.Draw(img_canvas)
        img_canvas.paste(qrcode_img)
        img_file_name = f'qrcode_{self.name}'+'.png'
        buffer = BytesIO()
        img_canvas.save(buffer, 'PNG')
        self.qr_code.save(img_file_name, File(buffer), save=False)    # add save=False to avoid creation of infinite image files
        img_canvas.close()
        super().save(*args, **kwargs)
