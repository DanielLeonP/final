from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.contrib.auth import logout
from .forms import UserForm, ProfileForm
from django.contrib import messages
from apps.pregunta.forms import PreguntaForm, AnswerForm
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404
from apps.pregunta.models import Pregunta, Respuesta
from .models import Profile
from django.contrib.auth.decorators import login_required
from django.db.models import Q
 

def login_view(request): #Inicio de sesión
    if request.method == 'POST':
        user = authenticate(
            username=request.POST['username'], password=request.POST['password'])
        if user is not None:
            login(request, user)
            
            return redirect('paginaPrincipal',)
        else:
            return render(request, 'login.html', {'form': AuthenticationForm()})
    else:
        form = AuthenticationForm()
        return render(request, 'login.html', {'form': form})


def logout_view(request): #Cerrar sesión
    logout(request)
    return redirect('login')   

def register_view(request): #Registrar usuario
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Listo')
        else:
            messages.error(request, 'No se pudo registrar, revisa que los datos sean correctos')
    form = UserForm()
    return render(request, 'register.html', {'form':form})

@login_required    
def paginaPrincipal_view(request): #Ver las preguntas recientes 
    id_User = request.user.id  
    questions = Pregunta.objects.exclude(id_User = id_User).order_by('-publication_date')[:6] 
    answers = Respuesta.objects.all()    
    cantidad = Pregunta.objects.exclude(id_User = id_User).count()
    return render(request, 'paginaPrincipal.html', {'questions':questions, 'answers':answers,'cantidad':cantidad})

@login_required
def answerQuestion_view(request, id_question):    #Responder alguna pregunta
    question = get_object_or_404(Pregunta, pk=id_question)
    id_answer = request.user.id
    if request.method == 'POST':
        form = AnswerForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Listo')
        else:
            messages.error(request, 'No se pudo realizar la pregunta, revisa que los campos esten llenos')
    form = AnswerForm(initial={'id_question': id_question, 'id_answer': id_answer})    
    return render(request, 'answerQuestion.html', {'form':form,'question':question })

@login_required
def newQuestion_view(request, id_User): #Crear nueva pregunta 
    if request.method == 'POST':
        form = PreguntaForm(request.POST)
        if form.is_valid():
            print(id_User)
            form.save()
            messages.success(request, 'Listo')
        else:
            messages.error(request, 'No se pudo realizar la pregunta, revisa que los campos esten llenos')
    form = PreguntaForm(initial={'id_User': id_User})
    return render(request, 'newQuestion.html', {'form':form})

@login_required
def myquestions_view(request, id_User):  #vista de mis preguntas
    user = request.user.get_username()
    cantidad = Pregunta.objects.filter(id_User = id_User).count()
    questions = Pregunta.objects.filter(id_User = id_User)#.all()
    return render(request, 'myquestions.html',{'questions': questions, 'user':user, 'cantidad':cantidad})

@login_required
def deleteQuestion_view(request, id_question): #Eliminar una de mis preguntas
    question = get_object_or_404(Pregunta, pk=id_question)
    answers = Respuesta.objects.filter(id_question = id_question)
    id_User = request.user.id
    question.delete()
    answers.delete()
    return redirect('myquestions', id_User)

@login_required
def answerMyQuestion_view(request, id_question):#Vista respuestas de mis preguntas
    question = get_object_or_404(Pregunta, pk=id_question)
    answers = Respuesta.objects.filter(id_question = id_question)
    return render(request, 'answerMyQuestions.html',{'question': question, 'answers':answers})

@login_required
def profile_view(request, id_User): #Vista para editar mi perfil
    profile, created = Profile.objects.get_or_create(
        user=request.user,
    )
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            if form.has_changed():
                new_profile = form.save(commit=False)
                new_profile.user_id = request.user.id
                new_profile.save()
                messages.success(request, 'Listo, perfil actualizado')
            else:
                messages.info(request, 'No has hecho cambios')
        else:
            messages.error(request, 'No se pudo actualizar tu perfil')
    form = ProfileForm(instance=profile)   
    return render(request, 'profile.html', {'form':form, 'profile':profile})  

def publicProfile_view(request, id_User):
    #vista publica de un perfil
    profile = get_object_or_404(Profile, user_id=id_User)
    return render(request, 'publicProfile.html', {'profile':profile})

