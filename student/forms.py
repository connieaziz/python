from django import forms
from.models import Student



class StudentForm(forms.ModelForm):
	class Meta:
		model = Student
		fields = "__all__"
			
# class Agreement(models.ModelForm):
# 	tos_agreed = models.BooleanForm(default=False)
# 	date_agreed = models.DateTimeField(blank=True, null=True)
# 		