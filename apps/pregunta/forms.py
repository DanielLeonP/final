from django import forms
from .models import Pregunta, Respuesta

class PreguntaForm(forms.ModelForm):
    class Meta:
        model = Pregunta
        fields = '__all__'
        labels = {
            'id_User':''
        }
        widgets = {
            'id_User':forms.NumberInput(attrs={'hidden':True})
        }
class AnswerForm(forms.ModelForm):
    class Meta:
        model = Respuesta
        fields = '__all__'
        labels = {
            'id_question':'',
            'id_answer':''
        }
        widgets = {
            'id_question':forms.NumberInput(attrs={'hidden':True}),
            'id_answer':forms.NumberInput(attrs={'hidden':True}),            
        }


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Pregunta
        fields = ('category',)
        labels = {
            'category':'Oredenar por'
        }
        widgets = {
            'id_User':forms.NumberInput(attrs={'null':True}),
            'question':forms.TextInput(attrs={'null':True}),
            'publication_date':forms.DateTimeInput(attrs={'null':True}),

        }
  


