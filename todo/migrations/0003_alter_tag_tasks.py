# Generated by Django 4.1.2 on 2022-10-26 12:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("todo", "0002_alter_tag_tasks"),
    ]

    operations = [
        migrations.AlterField(
            model_name="tag",
            name="tasks",
            field=models.ManyToManyField(blank=True, to="todo.task"),
        ),
    ]
