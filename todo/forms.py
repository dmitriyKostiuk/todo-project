from django import forms


from todo.models import Task, Tag
from todo.widgets import BootstrapDateTimePickerInput
from bootstrap_datepicker_plus.widgets import DateTimePickerInput, DatePickerInput


class TagForm(forms.ModelForm):
    tasks = forms.ModelMultipleChoiceField(
        queryset=Task.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False
    )

    class Meta:
        model = Tag
        fields = "__all__"


class TaskForm(forms.ModelForm):
    tags = forms.ModelMultipleChoiceField(
        queryset=Tag.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False
    )
    # deadline = forms.DateTimeField(
    #     # input_formats=['%d/%m/%Y'],
    #     widget=DatePickerInput(format="%d/%m/%Y")
    # )
    # datetime = forms.DateTimeField(
    #     # input_formats=['%d/%m/%Y'],
    #     widget=DatePickerInput(format="%d/%m/%Y")
    # )

    class Meta:
        model = Task
        fields = "__all__"
