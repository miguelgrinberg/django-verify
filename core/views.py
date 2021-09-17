from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import UserCreationForm, VerifyForm
from . import verify
from .decorators import verification_required


@login_required
@verification_required
def index(request):
    return render(request, 'index.html')


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            #verify.send(form.cleaned_data.get('phone'))
            return redirect('index')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})


@login_required
def verify_code(request):
    if request.method == 'POST':
        form = VerifyForm(request.POST)
        if form.is_valid():
            code = form.cleaned_data.get('code')
            if True: #verify.check(request.user.phone, code):
                request.user.is_verified = True
                request.user.save()
                return redirect('index')
    else:
        form = VerifyForm()
    return render(request, 'verify.html', {'form': form})
