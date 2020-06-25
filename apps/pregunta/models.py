from django.db import models
from apps.usuario.models import User
# Create your models here.
class Pregunta(models.Model):
    
    CATEGORIA1 = 'Arte y Humanidades'
    CATEGORIA2 = 'Belleza y Moda'
    CATEGORIA3 = 'Ciencias Sociales'
    CATEGORIA4 = 'Comida'
    CATEGORIA5 = 'Deportes'
    CATEGORIA6= 'Informatica'
    CATEGORIA7 = 'Hogar'
    CATEGORIA8 = 'Mascotas'
    CATEGORIA9 = 'Medio Ambiente'
    CATEGORIA10 = 'Politica'
    CATEGORIA11 = 'Salud'
    CATEGORIA12 = 'Entretenimiento'
    CATEGORIA13 = 'Restaurantes'
    CATEGORIA14 = 'Sociedad y Cultura'
    CATEGORIA15 = 'Viajes'
    CATEGORIA16 = 'Educacion'

    CATEGORY_CHOICES=[        
        (CATEGORIA1,'Arte y Humanidades'),
        (CATEGORIA2, 'Belleza y Moda'),
        (CATEGORIA3, 'Ciencias Sociales'),
        (CATEGORIA4, 'Comida'),
        (CATEGORIA5, 'Deportes'),
        (CATEGORIA6, 'Informatica'),
        (CATEGORIA7, 'Hogar'),
        (CATEGORIA8, 'Mascotas'),
        (CATEGORIA9, 'Medio Ambiente'),
        (CATEGORIA10, 'Politica'),
        (CATEGORIA11, 'Salud'),
        (CATEGORIA12, 'Entretenimiento'),
        (CATEGORIA13, 'Restaurantes'),
        (CATEGORIA14, 'Sociedad y Cultura'),
        (CATEGORIA15, 'Viajes'),
        (CATEGORIA16, 'Educacion')
    ] 
    id_User = models.ForeignKey(User, on_delete=models.CASCADE, related_name='get_question') 
    category = models.CharField(max_length=25, choices=CATEGORY_CHOICES, default=CATEGORIA1, blank = True)
    question = models.TextField(blank = False, null=False)
    publication_date = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return "{} - {}".format(self.id_User,self.question)

class Respuesta(models.Model):
    id_question = models.ForeignKey(Pregunta, on_delete=models.CASCADE, related_name='get_answer')
    id_answer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='get_respond')
    answer = models.TextField(blank = False,null=False)
    response_time = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return "{} - {}".format(self.id_answer,self.answer)
