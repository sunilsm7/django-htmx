from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from .todo import todos

# Create your views here.

def index(request):
    return render(request, 'index.html', {'todos': todos})


@require_http_methods(['POST'])
def search(request):
    search = request.POST['search']
    if len(search) == 0:
        return render(request, 'todo.html', {'todos': todos})

    res_todos = []
    for i in todos:
        if search in i['title']:
            res_todos.append(i)
    return render(request, 'todo.html', {'todos': res_todos}) 
