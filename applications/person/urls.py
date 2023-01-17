from django.urls import path, re_path, include
from .views import ListaPersonasView, ListAPIView, PersonListApiView

app_name = 'persona_app'

urlpatterns= [
    path(
        'persona/',
        ListaPersonasView.as_view(),
        name='personas'
    ),
    path(
        'api/persona/list/',
        PersonListApiView.as_view(),
    )
]