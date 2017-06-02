from django import forms

class AddToDoListForm(forms.Form):
    name = forms.CharField(max_length=250, widget=forms.TextInput(attrs={'class': 'form-control'}))