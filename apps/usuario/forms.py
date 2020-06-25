from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ('user',)        
    
class UserForm(UserCreationForm):
    def clean_email(self):
        email = self.cleaned_data.get("email")
        user_count = User.objects.filter(email=email).count()
        if user_count > 0:
            raise forms.ValidationError("El correo no se encuentra disponible, por favor corrige e intenta de nuevo.")
        return email
    class Meta:
        model = User
        fields=('username','first_name','last_name','email')

        widgets = {
            'username':forms.TextInput(attrs={'required':True }),            
            'first_name':forms.TextInput(attrs={'required':True}),
            'last_name':forms.TextInput(attrs={'required':True}),
        }
    
    
