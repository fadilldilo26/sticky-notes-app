from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.note_list, name='notes'),
    path('create-note/', views.create_note, name='create_note'),
    path('update_note/<str:note_id>/', views.update_note, name='update_note'),
    path('delete_note/<str:note_id>/', views.delete_note, name='delete_note'),
]