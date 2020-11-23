from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from api import views

urlpatterns = [
    url(r'^api/insumos/$', views.InsumosViewSet.as_view()),
    url(r'^api/insumos/name/(?P<name>.+)/$', views.InsumosNameFilterViewSet.as_view()),
    url(r'^api/insumos/price/(?P<price>[0-9]+)/$', views.InsumosPriceFilterViewSet.as_view()),
]
