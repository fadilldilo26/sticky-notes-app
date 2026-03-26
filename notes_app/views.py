from django.shortcuts import render, redirect, get_object_or_404
from .models import Note

# List and Create View
def note_list(request):
    notes = Note.objects.all().order_by('-created_at')
    
    if request.method == "POST":
        title = request.POST.get('title')
        content = request.POST.get('content')
        if title and content:
            Note.objects.create(title=title, content=content)
            return redirect('note_list')

    return render(request, 'notes_app/index.html', {'notes': notes})

# Update View
def note_edit(request, note_id):
    note = get_object_or_404(Note, id=note_id)
    if request.method == "POST":
        note.title = request.POST.get('title')
        note.content = request.POST.get('content')
        note.save()
        return redirect('note_list')
    return render(request, 'notes_app/edit_note.html', {'note': note})

# Delete View
def delete_note(request, note_id):
    note = get_object_or_404(Note, id=note_id)
    if request.method == "POST":
        note.delete()
    return redirect('note_list')