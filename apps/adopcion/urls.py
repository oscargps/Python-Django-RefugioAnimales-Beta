from apps.adopcion.views import index, SolicitudList, SolicitudCreate, SolicitudUpdate, SolicitudDelete
from django.urls import path


urlpatterns = [
   path('',index, name='index'),
   path('lista/', SolicitudList.as_view(), name='Lista' ),
   path('new/', SolicitudCreate.as_view(), name='new' ),
   path('update/<pk>', SolicitudUpdate.as_view(), name = 'update' ),
   path('delete/ <pk>', SolicitudDelete.as_view(), name = 'delete')
    
]