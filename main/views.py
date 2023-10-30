from django.shortcuts import render, redirect
from .models import Todo
from django.views import View


class TodoView(View):
    template_name = 'index.html'
    context = {}

    def get(self, request):
        try:
            todos = Todo.objects.filter(owner=request.user)
            self.context.update(todos)
            return render(request, self.template_name, self.context)
        finally:
            return render(request, self.template_name, self.context)


class AddTodo(View):
    template_name = 'add_todo.html'
    context = {}

    def get(self, request):
        return render(request, self.template_name, self.context)

    def post(self, request):
        text = request.POST.get('todo')
        expires_at = request.POST.get('expires_at')
        todo = Todo.objects.create(
            text=text,
            expires_at=expires_at
        )
        todo.save()
        return redirect('/home')


class EditTodoView(View):

    def post(self, request):
        text = request.POST.get('text')
        expires_at = request.POST.get('expires_at')
        todo = Todo.objects.get(id=token.id)
        todo.text = text
        todo.expires_at = expires_at
        todo.save()
        return redirect('/home')


class DeleteTodo(View):

    def post(self, request):
        todo = Todo.objects.get(id=todo.id)
        todo.delete()
        return redirect('/home')