from django.urls import reverse_lazy
from django.views import generic
from .models import Tdl
import random

class IndexView(generic.ListView):
   model = Tdl

class ExecutionView(generic.ListView):
  model = Tdl
  template_name = 'tdl/tdl_execution.html'

  def get_queryset(self):
#    return Tdl.objects.order_by('?')[:1]
    pk = Tdl.objects.values_list('pk', flat=True)
    pk_list = list(pk)
    pk_random = random.choice(pk_list)
    queryset = Tdl.objects.filter(pk=pk_random)

    return queryset

class CreateView(generic.edit.CreateView):
  model = Tdl
  fields = '__all__'

class UpdateView(generic.edit.UpdateView):
  model = Tdl
  fields = '__all__'

class DeleteView(generic.edit.DeleteView):
  model = Tdl
  success_url = reverse_lazy('tdl:index')