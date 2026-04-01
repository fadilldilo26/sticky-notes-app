from django.test import TestCase
from django.urls import reverse
from .models import Note # Assuming your model is named 'Note'


class StickyNoteTests(TestCase):

    def setUp(self):
        """Set up a sample note for testing."""
        self.note = Note.objects.create(
            title="Test Note",
            content="This is a test content"
        )


    # 1. Test CREATE
    def test_note_creation(self):
        self.assertEqual(self.note.title, "Test Note")
        self.assertEqual(Note.objects.count(), 1)
        

    # 2. Test READ (List View)
    def test_note_list_view(self):
        # Replace 'note_list' with the actual name of your URL pattern
        response = self.client.get(reverse('notes'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test Note")
        

    # 3. Test UPDATE
    def test_note_update(self):
        self.note.title = "Updated Title"
        self.note.save()
        self.assertEqual(self.note.title, "Updated Title")
        

    # 4. Test DELETE
    def test_note_delete(self):
        note_id = self.note.id
        self.note.delete()
        with self.assertRaises(Note.DoesNotExist):
            Note.objects.get(id=note_id)
