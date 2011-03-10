from django import forms
from django.forms import ModelForm
from mits.models import Task

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
	
	

