from django.urls import path
from .views import TodoView, AddTodo, EditTodoView, DeleteTodo
from django.views.decorators.csrf import csrf_exempt

urlpatterns = (
    path('', TodoView.as_view(), name='home'),
    path('add_product', AddTodo.as_view(), name='add_product'),
    path('edit_todo',csrf_exempt(EditTodoView.as_view()), name='edit_todo'),
    path('delete_todo', csrf_exempt(DeleteTodo.as_view()), name='delete_todo')
)