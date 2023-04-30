from django import forms
from django.shortcuts import render, redirect
from Todo import models
from Todo.utils.functions import *

'''memorandum'''
class MemoModel(forms.ModelForm):
    class Meta:
        model = models.Memorandum
        fields = ['timeStamp', 'title', 'content',]
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

def memorandum_main(request):
    memos = models.Memorandum.objects.all()
    if request.method == 'GET':
        return render(request, 'memorandum_main.html', {'memos': memos})
    title = request.POST.get('title')
    content = request.POST.get('content')
    if len(title) != 0 or len(content) != 0:
        timeStamp = getDateTime()
        models.Memorandum.objects.create(title=title, content=content, timeStamp=timeStamp)
    return redirect('/memorandum/main/')

def memorandum_closer(request, id):
    row = models.Memorandum.objects.filter(id=id).first()
    if request.method == 'GET':
        form = MemoModel(instance=row)
        return render(request, 'memorandum_closer.html', {'form': form})
    form = MemoModel(data=request.POST, instance=row)
    if form.is_valid():
        form.save()
        return redirect('/memorandum/main/')
    return render(request, 'memorandum_closer.html', {'form': form})

def memorandum_delmemo(request, id):
    models.Memorandum.objects.filter(id=id).delete()
    return redirect('/memorandum/main/')

def memorandum_done(request, id):
    models.Memorandum.objects.filter(id=id).update(status=True)
    return redirect('/memorandum/main/')
