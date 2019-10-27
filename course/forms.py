from django import forms
from.models import Course

class CourseForm(forms.ModelForm):
	Course = forms.CharField(widget=forms.TextInput(
		attrs={
			'class': 'forms-control',
			'placeholder': 'write a Course'
		}
		))
		
	class Meta:
		model = Course
		fields = "__all__"
		