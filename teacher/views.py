from django.shortcuts import render
from .forms import TeacherForm,Teacher
from django.http import HttpResponse


def add_teacher(request):
	if request.method=="POST":
		form=TeacherForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect("list_teachers")
		else:
			return HttpResponse("invalid data",status=400)
		
	else:
		form=TeacherForm()

	return render(request,"add_teacher.html",{"form":form})

def list_teachers(request):
	teachers=Teacher.objects.all()
	return render(request, "list_teachers.html",{"teachers":teachers})

def teacher_detail(request, pk):

	teacher=Teacher.objects.get(pk=pk)

	return render(request, "teacher_detail.html",{"teacher":teacher})

def edit_teacher(request, pk):
	
	teacher=Teacher.objects.get(pk=pk)

	if request.method== "POST":
		form=TeacherForm(request.POST, instance=teacher)

		if form.is_valid:
			form.save()
			return redirect("list_teachers")

	else:
		form=TeacherForm(instance=teacher)

	return render(request, "edit_teacher.html",{"form":form})
	# form = TeacherForm()
	# return render(request,"add_teacher.html",{"form":form})
# Create your views here.
