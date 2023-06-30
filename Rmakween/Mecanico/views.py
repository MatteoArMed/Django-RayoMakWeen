from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login #esto es para validar las cuentas
from django.contrib.auth.models import User, Group #importamos la tabla usuarios de Django
from .models import Contacto, Mensajes, Atencion, ImagenesMecanicos #importamos la tabla Contacto para realizar el insert a ella
from django.contrib.auth.decorators import login_required

# Create your views here.

def admin(request):
    return render(request,'admin/')

def home(request):
    return render(request,'mecanico/home.html')

def datosContacto(request):
    if request.method != "POST":
        context ={'mensaje':'no es POST'}
        return render(request,'Mecanico/datosContacto.html',context)
    else:
        nombreContacto = request.POST["nombreContacto"]
        emailContacto = request.POST["emailContacto"]
        numeroContacto = request.POST["numeroContacto"]
        descripcionProblema = request.POST["descripcionProblema"]

        obj = Contacto.objects.create(
            Nombre_Contacto=nombreContacto,
            Correo_Contacto=emailContacto,
            Numero_Contacto=numeroContacto,
            Descripcion_Contacto=descripcionProblema)
        print('Datos guardados')
        context = {'mensaje':'Formulario enviado'} #este mensaje se muestra en la pagina de respuesta.
        return render(request,'Mecanico/datosContacto.html',context)

def login(request):
    if request.method != "POST":
        context = {'mensaje': 'Ingresa tus credenciales'}
        return render(request, 'registration/login.html', context)
    else:
        usuario = request.POST["usuario"]
        contrasenna = request.POST["contrasenna"]
        
        user = authenticate(request, username=usuario, password=contrasenna)
        if user is not None:
            auth_login(request, user)
            return redirect('home')  # Redireccionar a la página de inicio
        else:
            # Cuando las credenciales son invalidas envia un mensaje
            context = {'mensaje': 'Usuario o contraseña incorrectos'}
            return render(request, 'registration/login.html', context)

def error(request):
    return render(request,'Mecanico/error.html')

def registro(request):
    if request.method == "POST":
        usuario = request.POST["usuario"]
        contrasenna = request.POST["contrasenna"]
        correo = request.POST.get("correo")  

        # Verifica si ya existe un usuario con el mismo nombre de usuario
        if User.objects.filter(username=usuario).exists():
            context = {'mensaje': 'El nombre de usuario ya está registrado'}
            return render(request, 'Mecanico/error.html', context)

        # Verifica si ya existe un usuario con el mismo correo electrónico
        if User.objects.filter(email=correo).exists():
            context = {'mensaje': 'El correo electrónico ya está registrado'}
            return render(request, 'Mecanico/error.html', context)

        # Crear el nuevo usuario
        user = User.objects.create_user(username=usuario, 
                                        password=contrasenna, 
                                        email=correo,
                                        )
        user.is_active = True  # Dejamos al usuario activado al momento de la creación
        user.save()
        
        # Asignar el usuario al grupo 2
        grupo = Group.objects.get(id=2) #El id 2 corresponde al grupo Cliente
        user.groups.add(grupo)
        context = {'mensaje': '¡Usuario creado con éxito!'}
        return render(request, 'Mecanico/error.html', context)
        
    else:
        context = {'mensaje':'Ingresa tus credenciales de registro'}
        return render(request, 'Mecanico/registro.html', context)

def mecanico(request):

    mecanicos = User.objects.filter(groups__id=1)

    context = {'mecanico':mecanicos}

    return render(request,'mecanico/mecanico.html', context)

def tienda(request):
    if request.method != "POST":
        context = {'mensaje': 'No es POST'}
        print('Se carga la pagina')
        return render(request,'mecanico/tienda.html',context)
    else:
        correoMensaje       =   request.POST["correoMensaje"]
        descripcionMensaje =   request.POST["descripcionMensaje"]

        obj =   Mensajes.objects.create(
                    Correo_Mensaje=correoMensaje,
                    Descripcion_Mensaje=descripcionMensaje)
        print('Datos guardados')
        context = {'mensaje':'Formulario Enviado'}
        return render(request,'mecanico/datosContacto.html',context)

def Franchesco(request):
    user_id = 3  # ID del usuario específico
    mecanicos = User.objects.filter(id=user_id)
    atenciones = Atencion.objects.filter(user_id=user_id, id_Estado=1)
    context = {'atenciones': atenciones,'mecanico':mecanicos}
    return render(request,'mecanico/Franchesco.html',context)

def Yayo(request):
    user_id = 8  # ID del usuario específico
    mecanicos = User.objects.filter(id=user_id)
    atenciones = Atencion.objects.filter(user_id=user_id, id_Estado=1)
    context = {'atenciones': atenciones,'mecanico':mecanicos}
    return render(request,'mecanico/Yayo.html',context)

def Luigi(request):
    user_id = 9  # ID del usuario específico
    mecanicos = User.objects.filter(id=user_id)
    atenciones = Atencion.objects.filter(user_id=user_id, id_Estado=1)
    context = {'atenciones': atenciones,'mecanico':mecanicos}
    return render(request,'mecanico/Luigi.html',context)


@login_required
def trabajosMecanico(request):
    mecanicos = User.objects.all()  # Obtener todos los mecánicos
    trabajos = Atencion.objects.filter(user=request.user)  # Filtrar trabajos por usuario actual

    if request.method == "POST":
        descripcionTrabajo = request.POST["descripcionTrabajo"]
        materialesTrabajos = request.POST["materialesTrabajos"]
        imagenTrabajo = request.FILES["imagenTrabajo"]

        user = request.user
        id_user = user.id

        obj = Atencion(
            Diagnostico_Atencion=descripcionTrabajo,
            MaterialesUsados=materialesTrabajos,
            Fotos_Atencion=imagenTrabajo,
            user=user,
            id_user_id=id_user,
            id_Estado=3,
            EstadoTrabajo='Pendiente de aprobación'
        )
        obj.save()
        print('Datos Enviados')
        context = {'mensaje': 'Formulario Enviado'}
        return render(request, 'mecanico/datosContacto.html', context)
    else:
        context = {
            'trabajos': trabajos,
            'mecanicos': mecanicos
        }
        print('No se enviaron datos')
        return render(request, 'mecanico/trabajosMecanico.html', context)  
    

@login_required
def administrarTrabajos(request):
    atenciones = Atencion.objects.all()
    mecanicos = User.objects.filter(groups__id=1)
    atenciones_counts = []
    for mecanico in mecanicos:
        atenciones_count = atenciones.filter(id_user=mecanico).count()
        atenciones_counts.append(atenciones_count)
    context = {'atenciones': atenciones, 'mecanicos': mecanicos, 'atenciones_counts': atenciones_counts}
    return render(request, 'mecanico/administrarTrabajos.html', context)

@login_required
def modificarTrabajo(request, pk):
    if pk != "":
        atencion = Atencion.objects.get(id=pk)
        mecanicos = User.objects.filter(groups__id=1)
        context = {'atencion': atencion, 'mecanicos': mecanicos}
        
        if request.method != "POST":
            print('Se carga la página')
            return render(request, 'mecanico/modificarTrabajo.html', context)

        if request.method == "POST":
            idAtencionMecanico = request.POST["idAtencionMecanico"]
            idMecanico = request.POST["idMecanico"]
            descripcionTrabajo = request.POST["descripcionTrabajo"]
            materialesUsados = request.POST["materialesUsados"]
            estadoTrabajo = request.POST["estadoTrabajo"]
            opcionSeleccionada = request.POST["opciones"]

            # Validamos si sube una nueva imagen, si no conserva la que tenia
            if 'imagenTrabajo' in request.FILES:
                imagenTrabajo = request.FILES['imagenTrabajo']
                atencion.Fotos_Atencion = imagenTrabajo

            if opcionSeleccionada == "1":# Trabajo aprobado
                atencion.id_Estado = 1
                estadoTrabajo   =   'Aprobado'      
            elif opcionSeleccionada == "2":# Trabajo rechazado
                atencion.id_Estado = 2
                estadoTrabajo   =    'Rechazado'    
            elif opcionSeleccionada == "3":# Trabajo pendiente
                atencion.id_Estado = 3              
                estadoTrabajo   =   'Pendiente'

            atencion.id = idAtencionMecanico
            atencion.user_id = idMecanico
            atencion.id_user_id = idMecanico
            atencion.Diagnostico_Atencion = descripcionTrabajo
            atencion.MaterialesUsados = materialesUsados
            atencion.EstadoTrabajo = estadoTrabajo
            atencion.id_Estado = opcionSeleccionada
            atencion.save()

            context = {'mensaje': 'Trabajo modificado'}
            print('Se envían datos')
            return render(request, 'mecanico/datosContacto.html', context)
        else:
            context = {'mensaje': 'Error, el trabajo no existe...'}
            return render(request, 'mecanico/error.html', context)
        
@login_required
def eliminarTrabajo(request,pk):
    context = {}
    try:
        trabajo = Atencion.objects.get(id=pk)

        trabajo.delete()
        print('Trabajo Eliminado')
        trabajos =  Atencion.objects.all()
        context ={'mensaje':'Trabajo Eliminado', 'trabajos':trabajos}
        return render(request,'mecanico/datosContacto.html',context)
    except:
        trabajos =  Atencion.objects.all()
        context={'mensaje':'El trabajo no existe','trabajos':trabajos}
        return render(request,'mecanico/administrarTrabajos.html',context)

@login_required
def verTrabajo(request):

    usuarioActual   =   request.user
    atenciones = Atencion.objects.filter(user=usuarioActual)
    mecanicos = User.objects.filter(groups__id=1)
    context = {'atenciones': atenciones, 'mecanicos': mecanicos}
    return render(request,'mecanico/verTrabajo.html',context)

@login_required
def verMensaje(request):
    contacto =  Contacto.objects.all()
    mensaje =  Mensajes.objects.all()
    context={'mensaje':mensaje,'contacto':contacto}
    return render(request,'mecanico/verMensaje.html',context)


