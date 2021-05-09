from .forms import AccountCreationForm
from django.shortcuts import render, redirect


def account_registration(request):
    """Регистрации нового пользователя"""
    form = AccountCreationForm()
    if request.method == "POST":
        form = AccountCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            password = form.cleaned_data['password1']
            user.set_password(password)
            user.save()

    context = {'form': form}
    return render(request, 'accounts/registration.html', context)
