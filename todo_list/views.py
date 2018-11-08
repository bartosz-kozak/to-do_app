from django.shortcuts import render, redirect
from .models import List
from .forms import ListForm
from django.contrib import messages
from django.http import HttpResponseRedirect


# Create your views here.

def home(request):
    if request.method == "POST":
        form = ListForm(request.POST or None)

        if form.is_valid:
            form.save()
            all_ithem = List.objects.all
            messages.success(request, ('Nowe zadanie zostało dodane do listy !'))
            return render(request, 'home.html', {'all_ithem':all_ithem})
    else:
        all_ithem = List.objects.all
        return render(request, 'home.html', {'all_ithem':all_ithem})

def about(request):
    return render(request, 'about.html', {})

def delete(request, list_id):
    ithem = List.objects.get(pk=list_id)
    ithem.delete()
    messages.success(request, ('Zadanie zostało usunite z listy !'))
    return redirect('home')

def wykonanie(request, list_id):
    ithem = List.objects.get(pk=list_id)
    ithem.complited = True
    ithem.save()
    return redirect('home')

def do_wykonania(request, list_id):
    ithem = List.objects.get(pk=list_id)
    ithem.complited = False
    ithem.save()
    return redirect('home')

def edycja(request, list_id):
    ithem = List.objects.get(pk=list_id)
    if request.method == "POST":
        form = ListForm(request.POST or None, instance=ithem)

        if form.is_valid:
            form.save()
            messages.success(request, ('Zadanie zostało zmienione !'))
            return redirect('home')
    else:
        ithem = List.objects.get(pk=list_id)
        return render(request, 'edycja.html', {'ithem':ithem})

