from tastypie import fields
from tastypie.resources import ModelResource
from tastypie.serializers import Serializer
from erps.models import Rh

class SerializedData(Serializer):
    def to_json(self, data, options=None):
        data = data['objects']
        return super (SerializedData, self).to_json(data, options)


class RhResource(ModelResource):
    class Meta: 
        queryset = Rh.objects.all()
        resource_name = 'rh'
        serializer = SerializedData()
