from django.test import TestCase
from django.urls import reverse
from .models import Note


class StickyNoteTests(TestCase):
    def setUp(self):
        """Create a sample note for testing."""
        Note.objects.create(title="Study Django", content="Finish the practical task.")

    def test_note_content(self):
        """Check if the note was saved correctly."""
        note = Note.objects.get(id=1)
        self.assertEqual(note.title, "Study Django")

    def test_homepage_status_code(self):
        """Check if the homepage loads (Status 200)."""
        response = self.client.get(reverse('note_list')) # Ensure 'index' matches your URL name
        self.assertEqual(response.status_code, 200)

