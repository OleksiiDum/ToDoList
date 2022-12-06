from django import forms


class TodoForm(forms.Form):

    todo_header = forms.CharField(label="To Do", max_length=128)