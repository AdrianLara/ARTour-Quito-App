from tastypie.utils.timezone import now
from django.db import models

class Monumentos(models.Model):
	mid=models.CharField(max_length=20)
	nombre_texto=models.CharField(max_length=100)
	descripcion_texto=models.CharField(max_length=300)
	img_old=models.ImageField(upload_to='images/')
	image_790x160 = ImageSpecField(
        source='img_old',
        processors=[ResizeToFill(790, 160)],
        format='JPEG',
        options={'quality': 85}
    )
	def __str__(self):
		return self.nombre_texto