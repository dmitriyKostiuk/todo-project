from django.db import models


class Task(models.Model):
    content = models.CharField(max_length=255, unique=False)
    datetime = models.DateField()
    deadline = models.DateTimeField()
    is_done = models.BooleanField()

    def __str__(self):
        return self.content


class Tag(models.Model):
    name = models.CharField(max_length=255, unique=False)
    tasks = models.ManyToManyField(Task,  blank=True)

    def __str__(self):
        return self.name