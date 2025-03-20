from django.urls import path, include
from users.views.users import (
    UserListAPIView,
    form_view,
    lista_formularios
)

urlpatterns = [

    path('', form_view, name='data_view'),
    path('list/', lista_formularios, name='lista-formularios'),
]
