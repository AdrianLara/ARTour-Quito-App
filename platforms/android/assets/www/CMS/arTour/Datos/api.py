from tastypie.resources import ModelResource
from Datos.models import Monumentos

class MonumentosResource(ModelResource):
	class Meta:
		queryset= Monumentos.objects.all()
		resource_name = 'monumentos'
		