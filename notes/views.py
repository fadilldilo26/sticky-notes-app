from django.shortcuts import render, get_object_or_404, redirect


# Create your views here.
from .models import Note


#Retrieves all notes and renders them in the note_list template
def note_list(request):
    notes = Note.objects.all()
    return render(request, 'notes/note_list.html', {'notes': notes})


# Handles the creation of a new note. If the request method is POST, it creates a new note with the provided title and content, then redirects to the note list view. If the request method is GET, it renders the create_note template.
def create_note(request):
    if request.method == 'POST':
        title = request.POST['title']
        content = request.POST['content']
        note = Note.objects.create(title=title, content=content)
        return redirect('notes')
    return render(request, 'notes/create_note.html')


# Handles the updating of an existing note. It retrieves the note based on the provided note_id. If the request method is POST, it updates the note's title and content with the provided data, saves the changes, and redirects to the note list view. If the request method is GET, it renders the update_note template with the current note data.
def update_note(request, note_id):
    note = get_object_or_404(Note, pk=note_id)
    if request.method == 'POST':
        note.title = request.POST['title']
        note.content = request.POST['content']
        note.save()
        return redirect('notes')
    return render(request, 'notes/update_note.html', {'note': note})


# Handles the deletion of a note. It retrieves the note based on the provided note_id. If the request method is POST, it deletes the note and redirects to the note list view. If the request method is GET, it renders the delete_note template with the current note data.
def delete_note(request, note_id):
    note = get_object_or_404(Note, pk=note_id)
    if request.method == 'POST':
        note.delete()
        return redirect('notes')
    return render(request, 'notes/delete_note.html', {'note': note})