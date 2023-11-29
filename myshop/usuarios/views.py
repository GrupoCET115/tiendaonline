from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import RegisterUserForm
from django.core.mail import send_mail
from django.contrib.auth.forms import SetPasswordForm
from .models import *


def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request,username = username,password = password,)
        if user is not None:
            login(request,user)
            return redirect('shop:product_list')
        else:
            messages.error(request,("Lo sentimos, las credenciales que ingresaste no son correctas. Por favor, verifica tu nombre de usuario y contraseña e inténtalo de nuevo."))
            return redirect('usuarios:login')

    else:
        return render(request,'registration/login.html')

def register_user(request):
    context = {}
    if request.method == "POST":
        register_form = RegisterUserForm(request.POST)
        if register_form.is_valid():
            user = register_form.save()
            user.is_active = False
            user.save()
            request.session['id_user'] = user.pk
            return redirect('usuarios:autenticar')
        else:
            context['form'] = register_form
            messages.error(request,("Lo sentimos, no fue posible registrarte con estas credenciales. Por favor, intentalo nuevamente con otras credenciales"))
            return render(request,'registration/sign_up.html',context)
            
    else:
        context['form'] = RegisterUserForm()

    return render(request,'registration/sign_up.html',context)

def autenticar_usuario(request):
    
    admin_email = "alememe45@gmail.com"
    subject = "Codigo de autenticacion"
    contexto = {}
    try:
        #user_object = User.objects.get(pk=user_id)
        user_object = User.objects.get(pk=int(request.session.get('id_user')))

        if request.method == "POST":
            codigo_enviado = request.POST['code']
            ultimocodigo = str(CodigoAutenticacion.objects.filter(usuario=user_object).latest("creado").codigo)

            if str(codigo_enviado.strip()) == ultimocodigo:
                
                user_object.is_active = True
                user_object.save()
                user_object.backend = 'django.contrib.auth.backends.ModelBackend'

                if request.session.get('cambiar_contra') == True:
                    messages.success(request,"Su Usuario ha sido autenticado correctamente")
                    return redirect('usuarios:recuperar_contra')
                else:
                    login(request,user_object)
                    messages.success(request,"Su Contraseña ha sido modificada")
                    return redirect('usuarios:login')
            else:
                messages.error(request,"Le hemos enviado un nuevo codigo de autenticacion")
        else:
            codigo = CodigoAutenticacion(usuario=user_object)
            codigo.save()
            message = f'Tu codigo para autenticarte es: {str(codigo.codigo)} copialo y pega en la ventana del navegador'
            email_destino = codigo.usuario.email
            send_mail(subject,message,admin_email,[email_destino])
            contexto = {
                'email':user_object.email,
            }
    # Resto del código
    except User.DoesNotExist:
        messages.error(request,"Usuario no registado")
        return redirect("usuarios:register")

    return render(request,'registration/autenticar.html',contexto)

def recuperar_contra(request):
    contexto = {}
    id = request.session.get('id_user')
    user = get_object_or_404(User, pk=id)
        
    if request.method == 'POST':
        password_form = SetPasswordForm(user, request.POST)  # Agrega el formulario de cambio de contraseña
       
        if password_form.is_valid():
            password_form.save()  # Guarda los cambios de contraseña
            #update_session_auth_hash(request, user)  # Actualiza la sesión de autenticación
            return redirect('usuarios:login')
    else:
        password_form = SetPasswordForm(user)  # Crea el formulario de cambio de contraseña
        contexto['password_form'] = password_form  # Agrega el formulario de cambio de contraseña al contexto
        contexto['user_date_join'] = user.date_joined

    return render(request, 'registration/cambiar_contra.html',contexto)

def enviar_correo(request):
    if request.method == "POST":
        try:
            user_id = User.objects.get(email=request.POST['correo'])
            request.session['email_user'] = request.POST['correo']
            request.session['cambiar_contra'] = True
            request.session['id_user'] = user_id.pk
            return redirect('usuarios:autenticar')
        except User.DoesNotExist:
            messages.error(request,"Su correo no esta registrado")
            return redirect('usuarios:enviar_correo_recuperar_contra')
            
    contexto = {}
    return render(request,"registration/enviar_email.html",contexto)

        


