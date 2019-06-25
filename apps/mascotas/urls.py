from apps.mascotas.views import  index,MascotaList,MascotaCreate,MascotaUpdate,MascotaDelete
from django.urls import path

urlpatterns = [
    path('',  MascotaList.as_view(), name='index'),
    path('new/',MascotaCreate.as_view(), name='new'),
    path('lista/', MascotaList.as_view(), name='lista'),
    path('update/<pk>/', MascotaUpdate.as_view(), name='update'),
    path('delete/<pk>/', MascotaDelete.as_view(), name='delete'),

    
]