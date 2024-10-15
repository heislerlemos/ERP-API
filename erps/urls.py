from django.urls import re_path, include
from . import views
from tastypie.api import Api
from erps.api import RhResource

#v1_api = Api(api_name='v1')
#v1_api.register(RhResource())

rh_resource = RhResource()

urlpatterns = [
    #re_path('', views.erps, name="erps"),
    re_path(r'^api/', include(rh_resource.urls)),
]
