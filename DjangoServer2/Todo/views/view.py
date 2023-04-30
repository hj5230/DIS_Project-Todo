from django import forms
from django.shortcuts import render, redirect
from Todo import models
from Todo.utils.secure import md5
from Todo.utils.functions import *

class NoteModel(forms.ModelForm):
    class Meta:
        model = models.Notebook
        fields = ['timeStamp', 'head', 'body',]
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['timeStamp'].initial = getDateTime()
        for _, field in self.fields.items():
            field.widget.attrs = {
                'class': 'form-control',
                'style': 'margin-bottom: 15px',
                'placeholder': field.label,
                'autocomplete': 'off',
            }

def notebook_main(request):
    notes = models.Notebook.objects.all()
    if request.method == 'GET':
        return render(request, 'notebook_main.html', {'notes': notes})

def notebook_add(request):
    if request.method == 'GET':
        form = NoteModel()
        return render(request, 'notebook_add.html', {'form': form})
    form = NoteModel(data = request.POST)
    if form.is_valid():
        form.save()
        return redirect('/notebook/main/')
    return render(request, 'notebook_add.html', {'form': form})
