from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.http import HttpResponse, Http404
from django.shortcuts import redirect, render, get_object_or_404
from django.views.decorators.http import require_http_methods
from .models import Todo
from .todo import todos


# Create your views here.

def index(request):
    return render(request, 'index.html', {'todos': todos})

@login_required
def todo_list_view(request):
    qs = Todo.objects.filter(user=request.user)
    context = {
        "todos": qs
    }
    return render(request, "todos/list.html", context)


@require_http_methods(['POST'])
def search(request):
    search = request.POST['search']
    if len(search) == 0:
        return render(request, 'todos/todo.html', {'todos': todos})

    res_todos = []
    for i in todos:
        if search in i['title']:
            res_todos.append(i)
    return render(request, 'todos/todo.html', {'todos': res_todos}) 
