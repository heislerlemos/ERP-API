from tastypie import fields
from tastypie.resources import ModelResource
from erps.models import Rh

class RhResource(ModelResource):
    class Meta: 
        queryset = Rh.objects.all()
        resource_name = 'rh'
