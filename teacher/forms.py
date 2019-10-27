from django import forms
from.models import Teacher


class TeacherForm(forms.ModelForm):
	post = forms.CharField(widget=forms.TextInput(
		attrs ={
			'class':'form-control',
		}
		))
	class Meta:
		model = Teacher
		fields = "__all__"
			
		