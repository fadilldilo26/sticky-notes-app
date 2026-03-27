from django.shortcuts import render, redirect
from .models import Note
from .forms import NoteForm
from django.shortcuts import get_object_or_404


def note_list(request):
    """View to list all notes."""
    notes = Note.objects.all().order_by('-created_at')
    return render(request, 'notes_app/index.html', {'notes': notes})

def add_note(request):
    """Handle the creation of a new note."""
    if request.method == "POST":
        form = NoteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('note_list')
    else:
        form = NoteForm()
    return render(request, 'notes_app/add_note.html', {'form': form})

def delete_note(request, note_id):
    """View to delete a specific note."""
    note = get_object_or_404(Note, id=note_id)
    if request.method == "POST":
        note.delete()
        return redirect('note_list')
    return render(request, 'notes_app/delete_confirm.html', {'note': note})

def edit_note(request, note_id):
    """View to edit an existing note."""
    note = get_object_or_404(Note, id=note_id) # Find the note or show 404
    
    if request.method == "POST":
        # 'instance=note' tells Django to update this specific note instead of creating a new one
        form = NoteForm(request.POST, instance=note)
        if form.is_valid():
            form.save()
            return redirect('note_list')
    else:
        # Pre-fill the form with the current note's data
        form = NoteForm(instance=note)
        
    return render(request, 'notes_app/edit_note.html', {'form': form, 'note': note})

