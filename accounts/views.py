from django.shortcuts import render, redirect
from django.views import View
from .forms import UserForm

def register(request):

    if request.method == 'POST':
        form = UserForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home-page')
    else:
        form = UserForm()

    return render(request, 'webpages/medicine_form.html', {'form': form})