from django.shortcuts import render

# Create your views here.
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DeleteView
from django.views.generic.edit import FormMixin
from django import forms
from django.shortcuts import redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required

from .models import Task
from .forms import TaskForm


class TaskListCreateView(LoginRequiredMixin, FormMixin, ListView):
    template_name = 'tasks/task_list.html'
    model = Task
    context_object_name = 'tasks'
    form_class = TaskForm

    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)

    def get_success_url(self):
        return reverse_lazy('tasks:list')

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            Task.objects.create(user=request.user, title=form.cleaned_data['title'])
        return redirect(self.get_success_url())

class TaskDeleteView(LoginRequiredMixin, DeleteView):
    model = Task
    success_url = reverse_lazy('tasks:list')

    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)

@login_required
@require_POST
def toggle_done(request, pk):
    task = get_object_or_404(Task, pk=pk, user=request.user)
    task.is_done = not task.is_done
    task.save(update_fields=['is_done'])
    return redirect('tasks:list')
