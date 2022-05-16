from django.views.generic import edit, list, UpdateView, DetailView
from django.urls import reverse
from .models import Note
from .forms import NoteForm


class NoteListView(list.ListView):
    template_name = 'index.html'
    model = Note
    queryset = Note.objects.order_by('-updated_at')[:10]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = NoteForm()
        return context


class NoteCreateView(edit.CreateView):
    template_name = 'index.html'
    form_class = NoteForm

    def get_success_url(self):
        return reverse('note:note-list')


class NoteUpdateView(UpdateView):
    template_name = 'index.html'
    form_class = NoteForm
    queryset = Note.objects.all()

    def get_success_url(self):
        return reverse('note:note-list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['update'] = 'update'
        context['object_list'] = Note.objects.order_by('-updated_at')[:10]
        return context


class NoteDeleteView(edit.DeleteView):
    template_name = 'index.html'
    model = Note

    def get_success_url(self):
        return reverse('note:note-list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['delete'] = 'Are you sure?'
        context['form'] = NoteForm()
        context['object_list'] = Note.objects.order_by('-updated_at')[:10]
        return context


class NoteDetailView(DetailView):
    template_name = 'index.html'
    model = Note

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['detail'] = 'detail'
        context['form'] = NoteForm()
        context['object_list'] = Note.objects.order_by('-updated_at')[:10]
        return context
