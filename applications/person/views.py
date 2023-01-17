# Create your views here.
from django.views.generic import TemplateView, ListView, CreateView, UpdateView, DetailView
from rest_framework.generics import ListAPIView, UpdateAPIView, DestroyAPIView, CreateAPIView
from .models import Person
from .serializers import PersonSerializer

class ListaPersonasView(ListView):
    model=Person
    template_name='persona/personas.html'
    context_object_name = 'personas'

    def get_queryset(self):
        return Person.objects.all()

class PersonListApiView(ListAPIView):
    serializer_class = PersonSerializer
    def get_queryset(self):
        return Person.objects.all()


