from django.shortcuts import render, redirect
from .forms import JssForm
from .models import Jasoseol
from django.http import Http404 
from django.core.exceptions import PermissionDenied  
from django.contrib.auth.decorators import login_required
# import templates

# Create your views here.

def index(request):
    all_jss = Jasoseol.objects.all()
    return render(request, 'index.html', {'all_jss':all_jss})

def my_index(request):
    my_jss = Jasoseol.objects.filter(author=request.user)
    return render(request, 'index.html', {'all_jss':my_jss})


@login_required(login_url='/login/')
def create(request):

    if request.method == "POST":
        filled_form = JssForm(request.POST)
        if filled_form.is_valid():
            temp_from = filled_form.save(commit=False)
            temp_from.author = request.user
            temp_from.save()
            return redirect('index')
    jss_form = JssForm()
    return render(request, 'create.html', {'jss_form':jss_form})

@login_required(login_url='/login/')
def detail(request, jss_id):
    try:
        my_jss = Jasoseol.objects.get(pk=jss_id)
    except:
        raise Http404
    
    return render(request, 'detail.html', {'my_jss':my_jss})

def delete(request, jss_id):
    my_jss = Jasoseol.objects.get(pk=jss_id)
    if request.user == my_jss.author:
        my_jss.delete()
        return redirect('index')

    raise PermissionDenied

def update(request, jss_id):
    my_jss = Jasoseol.objects.get(pk=jss_id)
    jss_form = JssForm(instance=my_jss)
    if request.method == "POST":
        updated_form = JssForm(request.POST, instance=my_jss)
        if updated_form.is_valid():
            updated_form.save()
            return redirect ('index')
    return render(request, 'create.html', {'jss_form':jss_form})
   