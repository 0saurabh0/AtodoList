from django.shortcuts import render, redirect
from django import forms
from .models import Todo

class NewForm(forms.Form):
    title=forms.CharField(max_length=55)

# Create your views here.

def index(request):
    todo=Todo.objects.all()
    form=NewForm()
    if request.method=="POST":
        form=NewForm(request.POST)
        if form.is_valid():
            todo=Todo(title=form.cleaned_data["title"])
            todo.save()
        return redirect('index')
    context={'todos':todo, 'form':form}
    return render(request, 'todo_list.html', context)


def delete_todo(request, todo_id):
    todo = Todo.objects.get(id=todo_id)
    todo.delete()
    return redirect('index')

