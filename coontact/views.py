from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.shortcuts import render, redirect
# Create your views here.
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Foydalanuvchi ro'yxatdan o'tkazilganda avtomatik ravishda tizimga kiring
            login(request, user)
            return redirect('home')  # O'zgartirishingiz kerak bo'lgan boshqa sahifa nomi
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})