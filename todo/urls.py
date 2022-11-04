from django.urls import path

from .views import (
    index, TagCreateView, TagListView, TagUpdateView, TaskListView, TaskCreateView, TaskUpdateView, TaskDeleteView,
    TagDeleteView, TaskDetailView, task_change_is_done,
)

urlpatterns = [
    path("", index, name="index"),
    path(
        "tags/",
        TagListView.as_view(),
        name="tag-list",
    ),
    path(
        "tags/create/",
        TagCreateView.as_view(),
        name="tag-create",
    ),
    path(
        "tags/<int:pk>/update/",
        TagUpdateView.as_view(),
        name="tag-update",
    ),
    path(
        "tags/<int:pk>/delete/",
        TagDeleteView.as_view(),
        name="tag-delete",
    ),
    path("tasks/", TaskListView.as_view(), name="task-list"),
    path("tasks/<int:pk>/", TaskDetailView.as_view(), name="task-detail"),
    path("tasks/create/", TaskCreateView.as_view(), name="task-create"),
    path("tasks/<int:pk>/update/", TaskUpdateView.as_view(), name="task-update"),
    path("tasks/<int:pk>/delete/", TaskDeleteView.as_view(), name="task-delete"),
    path(
        "tasks/<int:pk>/task-change-is-done/",
        task_change_is_done,
        name="task-change-is-done",
    ),

]

app_name = "todo"
