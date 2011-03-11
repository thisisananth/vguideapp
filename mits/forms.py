from django import forms
from django.forms import ModelForm
from mits.models import Task
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class DecideForm(forms.Form):
	task1 = forms.CharField()
	poms1 = forms.DecimalField()
	task2 = forms.CharField()
	poms2 = forms.DecimalField()
	task3 = forms.CharField()
	poms3 = forms.DecimalField()
	
	
class TrackForm(ModelForm):
	class Meta:
		model = Task
		
	completed1 = forms.BooleanField(widget=forms.CheckboxInput,required=False)
	used_poms1 = forms.DecimalField(required=False,initial=0)
	completed2 = forms.BooleanField(widget=forms.CheckboxInput,required=False)
	used_poms2 = forms.DecimalField(required=False,initial=0)
	completed3 = forms.BooleanField(widget=forms.CheckboxInput,required=False)
	used_poms3 = forms.DecimalField(required=False,initial=0)
	
	

class LoginForm(forms.Form):
	username= forms.CharField()
	password= forms.CharField(widget=forms.PasswordInput())

class UserCreationFormExtended(UserCreationForm): 
    def __init__(self, *args, **kwargs): 
        super(UserCreationFormExtended, self).__init__(*args, 
**kwargs) 
        self.fields['first_name'].required = True 
        self.fields['last_name'].required = True 
    class Meta: 
        model = User 
        fields = ('username', 'email', 'first_name', 'last_name') 
	