from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.
from .models import Note

def note_list(request):
    notes = Note.objects.all()
    return render(request, 'notes/note_list.html', {'notes': notes})

def create_note(request):
    if request.method == 'POST':
        title = request.POST['title']
        content = request.POST['content']
        note = Note.objects.create(title=title, content=content)
        return redirect('notes')
    return render(request, 'notes/create_note.html')

def update_note(request, note_id):
    note = get_object_or_404(Note, pk=note_id)
    if request.method == 'POST':
        note.title = request.POST['title']
        note.content = request.POST['content']
        note.save()
        return redirect('notes')
    return render(request, 'notes/update_note.html', {'note': note})

def delete_note(request, note_id):
    note = get_object_or_404(Note, pk=note_id)
    if request.method == 'POST':
        note.delete()
        return redirect('notes')
    return render(request, 'notes/delete_note.html', {'note': note})