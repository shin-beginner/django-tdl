from django.urls import reverse_lazy
from django.views import generic
from .models import Tdl
import random
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied

class IndexView(generic.ListView):
   model = Tdl

   def get_queryset(self):
       id = self.request.user.id
       return Tdl.objects.filter(author_id=id)

class ExecutionView(LoginRequiredMixin, generic.ListView):
  model = Tdl
  template_name = 'tdl/tdl_execution.html'

  def get_queryset(self):
#    return Tdl.objects.order_by('?')[:1]
        id = self.request.user.id
        pk = Tdl.objects.filter(author_id=id).values_list('pk', flat=True)
        pk_list = list(pk)
        pk_random = random.choice(pk_list)
        queryset = Tdl.objects.filter(pk=pk_random)

        return queryset

class CreateView(LoginRequiredMixin, generic.edit.CreateView):
  model = Tdl
  fields = ['item'] #__all__'

  def form_valid(self, form):
      form.instance.author = self.request.user
      return super(CreateView, self).form_valid(form)

class UpdateView(LoginRequiredMixin, generic.edit.UpdateView):
  model = Tdl
  fields = ['item'] #__all__'

  def dispatch(self, request, *args, **kwargs):
      obj = self.get_object()
      if obj.author != self.request.user:
          raise PermissionError('編集権限がありません')
      return super(UpdateView, self).dispatch(request, *args, **kwargs)

class DeleteView(LoginRequiredMixin, generic.edit.DeleteView):
  model = Tdl
  success_url = reverse_lazy('tdl:index')

  def dispatch(self, request, *args, **kwargs):
      obj = self.get_object()
      if obj.author != self.request.user:
          raise PermissionError('削除権限がありません')
      return super(Deletevies, self).dispatch(request, *args, **kwargs)