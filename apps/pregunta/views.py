from django.shortcuts import render
from .models import Pregunta, Respuesta
from django.shortcuts import get_object_or_404
from .forms import CategoryForm
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def category_view(request, category):
    category = category
    questions = Pregunta.objects.filter(category = category)
    answers = Respuesta.objects.all() 
    cantidad = Pregunta.objects.filter(category = category).count()
    return render(request, 'category.html', {'questions': questions,'category':category, 'answers':answers, 'cantidad':cantidad})