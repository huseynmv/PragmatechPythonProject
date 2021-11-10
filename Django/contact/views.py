from django import forms
from django.shortcuts import redirect, render
from . forms import ContactForm
from django.contrib import messages



def contact(request):
    form = ContactForm()
    if request.method == 'POST':
        form = ContactForm(data=request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.INFO, 'Successfully registered!')
            return redirect('/contact')
        else:
            messages.add_message(request, messages.INFO, 'Wrong email address! Use @gmail.com')
    return render(request, 'contact.html', {'form': form})