from django.shortcuts import render
from django.views.generic import View, ListView
from rest_framework import viewsets, permissions
from .models import Note, Task
from .serializers import NoteSerializer, TaskSerializer


def get_objects(clas_s):
    return clas_s.objects.all()


class MainPageView(View):
    template_name = 'mainpages/mainpage.html'

    def get(self, request):
        return render(request, template_name=self.template_name)


class NoteViewSet(viewsets.ModelViewSet):
    queryset = get_objects(Note)
    serializer_class = NoteSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)


class NoteHTMLView(ListView):
    model = Note
    template_name = 'notes/notes.html'

    def get_queryset(self):
        return Note.objects.filter(user=self.request.user)


class TaskViewSet(viewsets.ModelViewSet):
    queryset = get_objects(Task)
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)


class TaskHTMLView(ListView):
    template_name = 'tasks/tasks.html'
    model = Task

    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)
