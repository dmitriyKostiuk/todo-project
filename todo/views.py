from bootstrap_datepicker_plus.widgets import DateTimePickerInput
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic


from .models import Task, Tag
from .forms import (
    TagForm, TaskForm)


def index(request):
    """View function for the home page of the site."""

    num_tasks = Task.objects.count()
    num_tags = Tag.objects.count()

    num_visits = request.session.get("num_visits", 0)
    request.session["num_visits"] = num_visits + 1

    context = {
        "num_tasks": num_tasks,
        "num_tags": num_tags,
        "num_visits": num_visits + 1,
    }

    return render(request, "todo/index.html", context=context)


def task_change_is_done(request, pk):
    task = Task.objects.get(id=pk)
    task.is_done = not task.is_done
    task.save()
    print(task.is_done)
    print("!!!!!!!!!!!!!!!!!!!!save task")
    return HttpResponseRedirect(reverse_lazy("todo:task-list"))


class TaskListView(generic.ListView):
    model = Task
    context_object_name = "task_list"
    template_name = "todo/task_list.html"
    queryset = Task.objects.all()
    paginate_by = 5


class TaskCreateView(generic.CreateView):
    model = Task
    fields = "__all__"
    success_url = reverse_lazy("todo:task-list")

    def get_form(self):
        form = super().get_form()
        form.fields["datetime"].widget = DateTimePickerInput(format="%Y-%m-%d")
        form.fields["deadline"].widget = DateTimePickerInput(format="%Y-%m-%d %H:%M")
        return form


class TaskDetailView(generic.DetailView):
    model = Task


class TaskUpdateView(generic.UpdateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy("todo:task-list")


class TaskDeleteView(generic.DeleteView):
    model = Task
    success_url = reverse_lazy("todo:task-list")


class TagListView(generic.ListView):
    model = Tag
    paginate_by = 5
    queryset = Tag.objects.all()


class TagDetailView(generic.DetailView):
    model = Tag


class TagCreateView(generic.CreateView):
    model = Tag
    form_class = TagForm
    success_url = reverse_lazy("todo:tag-list")


class TagUpdateView(generic.UpdateView):
    model = Tag
    form_class = TagForm
    success_url = reverse_lazy("todo:tag-list")


class TagDeleteView(generic.DeleteView):
    model = Tag
    success_url = reverse_lazy("todo:tag-list")


