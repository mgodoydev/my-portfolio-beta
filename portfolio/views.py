from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.contrib import messages
from django.conf import settings

# Create your views here.
def home(request):
    return render(request, 'home.html')

def projects(request):
    return render(request, 'projects.html')
    
def skills(request):
    return render(request, 'skills.html')

def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        message = request.POST['message']
        
        # Envía el correo
        send_mail(
            f"Message from {name}",  # Asunto
            message,  # Cuerpo del correo
            email,  # De
            [settings.EMAIL_HOST_USER],  # A (enviar a tu propio correo)
            fail_silently=False,
        )
        
        messages.success(request, "Your message has been sent successfully!")
        return redirect('contact')  # Redirige a la página de contacto

    return render(request, 'contact.html')
