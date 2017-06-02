from django import forms

BASE_CHAR_FIELD = forms.CharField(max_length=250, widget=forms.TextInput(attrs={'class': 'form-control'}))

class AddToDoListForm(forms.Form):
    name = BASE_CHAR_FIELD


class TodoForm(forms.Form):
    name = BASE_CHAR_FIELD