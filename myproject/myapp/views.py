from django.shortcuts import render, redirect
from . import models
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.views.generic import ListView, CreateView, DeleteView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


def login(request):
    return render(request, 'myapp/login.html')


def register(request):
    if request.method == 'POST':
        # create a new form that contains the post data
        Form = UserCreationForm(request.POST)
        # check if the filled registeration form is valid
        if Form.is_valid():
            Form.save() # save the new user
            username = Form.cleaned_data.get('username') # fetch the username
            messages.success(request, f'account created for {username}') # display username with flash message
            return redirect('home')
    else: # request.method == 'GET'
        # create an empty form
        Form = UserCreationForm()

    return render(request, 'myapp/register.html', {'RegisterForm': Form})

# display all notes
class NoteListView(ListView):
    model = models.note
    template_name = 'myapp/home.html' # template path
    context_object_name = 'notesList'
    # order notes from newest to oldest
    ordering = ['-date_created']



# LoginRequiredMixin: the user must be logged in to create a note
class NoteCreateView(LoginRequiredMixin, CreateView):
    model = models.note
    template_name = 'myapp/create.html'

    # validate user loign before creating a note
    def form_valid(self, form):
        # set the author to the current logged in user before submition
        form.instance.author = self.request.user
        # run form_valid() from the parent class
        return super().form_valid(form)


    # date_created will be filled automatically
    fields = ['noteName', 'noteContent']

    # redirect to home page after creating a new note
    success_url = '/'


# UserPassesTestMixin: only update the note by the same user
class NoteUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = models.note
    template_name = 'myapp/create.html'


    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    # check if the current user is the same as the note author
    def test_func(self):
        note = self.get_object()
        if self.request.user == note.author:
            return True
        return False


    fields = ['noteName', 'noteContent']

    success_url = '/'


class NoteDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = models.note

    template_name = 'myapp/delete.html'

    def test_func(self):
        note = self.get_object()
        if self.request.user == note.author:
            return True
        return False
    
    success_url = '/'
