from django.shortcuts import render, get_object_or_404, redirect
from django.http import Http404
from django.http import HttpResponse

from .models import ToDo, ToDoForm

#handle dates
from datetime import *

# Create your views here.

#View for main page
def index(request):
    #Get the five most pressing ToDo's
    todos = ToDo.objects.filter(done=False).order_by('-due_date')[:5]
    #Put them in an object to pass to our template engine
    context = {'todos': todos}
    #Render and return the index.html template with the information in context
    return render(request, 'firstapp/index.html', context)

#A view which shows details about the current todo
def detail(request, todo_id):
    if request.method == 'POST':
        todo = get_object_or_404(ToDo, pk=todo_id)
        if not isinstance(todo, Http404):
            done = request.POST.get('done', False)
            if(done == 'on'):
                todo.done = True;
            print todo
            todo.save()
            return redirect('/firstapp')
    #Get the todo that matches the id, otherwise prepare to return a 404 (not found) error
    todo = get_object_or_404(ToDo, pk=todo_id)
    context = {'todo': todo, 'id': todo_id}
    return render(request, 'firstapp/detail.html', context)

#View for creating a new todo,
def new(request):

    #This determines whether the user is submitting the form, a POST request
    if request.method == 'POST':
        form = ToDoForm(request.POST)

        if form.is_valid():
            text = request.POST.get('text')
            due_date_text =  request.POST.get('due_date')
            date_created =  datetime.today()
            done = False
            date_array = str(due_date_text).split("/")
            due_date = date(int(date_array[2]), int(date_array[0]), int(date_array[1])).isoformat()
            todo =ToDo.objects.create(text=text, due_date=due_date, date_created=date_created, done=done);
            form = ToDoForm(request.POST, instance=todo)
            form.save(commit=True)
            # The user will be shown the homepage.
            return redirect('/')
        else:
            # The supplied form contained errors - just print them to the terminal.
            print form.errors
    else:
        # If the request was not a POST, display the form to enter details.
        form = ToDoForm()
    return render(request, 'firstapp/new.html', {'form': form})
