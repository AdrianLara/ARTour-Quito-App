from django.http import HttpResponse
from .models import Monumentos 


def index(request):
	output=Monumentos.objects.filter(pk=2)
	return HttpResponse(output)