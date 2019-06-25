from django.urls import path
from apps.usuario.views import RegistroUsuario


urlpatterns = [ 
    path('',RegistroUsuario.as_view(), name='new_user')
]
