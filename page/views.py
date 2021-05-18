from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect
from .models import todoModel
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView , DeleteView , UpdateView,FormView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import views as authview
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login


class todoList(LoginRequiredMixin, ListView):
	model = todoModel
	context_object_name='todo_lists'

	def get_context_data(self,**kwargs):
		context =super().get_context_data(**kwargs)
		context['todo_lists'] = context['todo_lists'].filter(user=self.request.user)
		context['count'] = context['todo_lists'].filter(completed=False).count()

		searched_data = self.request.GET.get('search-area') or ''
		if searched_data:
			context['todo_lists'] = context['todo_lists'].filter(title__icontains=searched_data)

		context['searched_data']=searched_data
		return context

class todoDetail(LoginRequiredMixin,DetailView):
	model = todoModel
	context_object_name='task'

class todoCreate(LoginRequiredMixin,CreateView):
	model = todoModel
	fields = ['title','discription',"created",'completed']
	success_url = reverse_lazy('todolist')

	def form_valid(self,form):
		form.instance.user = self.request.user
		return super(todoCreate,self).form_valid(form)

class todoUpdate(LoginRequiredMixin,UpdateView):
	model = todoModel
	fields = ['title','discription','completed']
	success_url=reverse_lazy('todolist')

class todoDelete(LoginRequiredMixin,DeleteView):
	model = todoModel
	success_url=reverse_lazy('todolist')

class CustomLoginView(authview.LoginView):
	model = todoModel
	template_name='page/login.html'
	redirect_authenticated_user=True

	def get_success_url(self):

		return reverse_lazy('todolist')

class RegisterPage(FormView):
    template_name = 'page/register.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('todolist')

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(RegisterPage, self).form_valid(form)

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('todolist')
        return super(RegisterPage, self).get(*args, **kwargs)

