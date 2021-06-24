from django.db import models
import barcode
import qrcode
from barcode.writer import ImageWriter
from io import BytesIO
from django.core.files import File
from PIL import Image, ImageDraw


# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=200)
    bar_code = models.ImageField(upload_to='images/', blank=True, null=True)
    qr_code = models.ImageField(upload_to='qr_codes/', blank=True, null=True)
    country_id = models.IntegerField(max_length=2, null=True)
    manufacture_id = models.IntegerField(max_length=6, null=True)
    number_id = models.IntegerField(max_length=4, null=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        qrcode_img = qrcode.make(self.name)
        canvas = Image.new('RGB', (290, 290), 'white')
        canvas.paste(qrcode_img)
        fname = f'qr_code-{self.name}.png'
        buffer = BytesIO()
        canvas.save(buffer, 'PNG')
        self.qr_code.save(fname, File(buffer), save=False)
        canvas.close()
        super().save(*args, **kwargs)

    def save(self, *args, **kwargs):
        EAN = barcode.get_barcode_class('ean13')
        ean = EAN(f"{self.country_id}{self.manufacture_id}{self.number_id}", writer=ImageWriter())
        buffer = BytesIO()
        ean.write(buffer)
        self.bar_code.save('barcode.png', File(buffer), save=False)
        return super().save(*args, **kwargs)
