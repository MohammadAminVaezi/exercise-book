from django.urls import path
from .views import NoteListView, NoteCreateView, NoteUpdateView, NoteDeleteView, NoteDetailView

app_name = 'note'
urlpatterns = [
    path('', NoteListView.as_view(), name='note-list'),
    path('create/', NoteCreateView.as_view(), name='note-create'),
    path('update/<int:pk>/', NoteUpdateView.as_view(), name='note-update'),
    path('delete/<int:pk>/', NoteDeleteView.as_view(), name='note-delete'),
    path('detail/<int:pk>/', NoteDetailView.as_view(), name='note-detail'),

]
