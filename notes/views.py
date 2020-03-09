from django.http import Http404
from django.shortcuts import render, redirect
from .models import Note
from .forms import NoteForm

def home(request):
    try:
        notes = Note.objects.all()
    except Note.DoesNotExist:
        raise Http404("Note does not exist")

    form = NoteForm(request.POST or None)
    if form.is_valid():
        save_it = form.save(commit=False)
        save_it.save()

    context = {'notes': notes, 'form': form}
    return render(request, 'notes.html', context)

def delete_note(request, id):    

    Note.objects.filter(id=id).delete()
    return redirect('home')