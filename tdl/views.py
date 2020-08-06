from django.urls import reverse_lazy
from django.views import generic
from .models import Tdl

class IndexView(generic.ListView):
   model = Tdl

class CreateView(generic.edit.CreateView):
  model = Tdl
  fields = '__all__'

class UpdateView(generic.edit.UpdateView):
  model = Tdl
  fields = '__all__'

class DeleteView(generic.edit.DeleteView):
  model = Tdl
  success_url = reverse_lazy('tdl:index')