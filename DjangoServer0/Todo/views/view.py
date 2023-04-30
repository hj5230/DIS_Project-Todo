from django import forms
from django.shortcuts import render, redirect
from Todo import models
from Todo.utils.secure import md5
from Todo.utils.functions import *

'''website'''
def dashboard(request):
    return render(request, 'dashboard.html')

'''codebook'''
class TagModel(forms.ModelForm):
    class Meta:
        model = models.Codebook
        fields = ['tsp', 'tag', 'unm', 'pwd',]
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['tsp'].initial = getDate()
        for _, field in self.fields.items():
            field.widget.attrs = {
                'class': 'form-control',
                'style': 'margin-bottom: 15px',
                'placeholder': field.label,
                'autocomplete': 'off',
            }

def codebook_main(request):
    if request.method == 'GET':
        tags = models.Codebook.objects.all()
        return render(request, 'codebook_main.html', {'tags': tags})
    search = request.POST.get('search')
    matches = models.Codebook.objects.filter(tag__icontains = search)
    return render(request, 'codebook_main.html', {'tags': matches})

def codebook_addtag(request):
    if request.method == 'GET':
        form = TagModel()
        return render(request, 'codebook_addtag.html', {'form': form})
    form = TagModel(data = request.POST)
    if form.is_valid():
        form.save()
        return redirect('/codebook/main/')
    return render(request, 'codebook_addtag.html', {'form': form})
    
def codebook_deltag(request, id):
    models.Codebook.objects.filter(id=id).delete()
    return redirect('/codebook/main/')
