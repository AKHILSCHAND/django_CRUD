from django.shortcuts import render
from .models import Student
from django.contrib import messages

# Create your views here.




# Create your views here.
def index(request):
    students = Student.objects.all()

    if request.method == "POST": 
        if "create" in request.POST:
            name = request.POST.get("name")
            email = request.POST.get("email")
            age = request.POST.get("age")
            gender = request.POST.get("gender")
            
            
            Student.objects.create(
                name=name,
                email=email,
                age=age,
                gender=gender
            )
            messages.success(request, "Student added successfully")
    
        elif "update" in request.POST:
            id = request.POST.get("id")
            name = request.POST.get("name")
            email = request.POST.get("email")
            age = request.POST.get("age")
            gender = request.POST.get("gender")

            student = Student.objects.get(id=id)
            student.name = name
            student.email = email
            student.age = age
            student.gender = gender
            student.save()
            messages.info(request, "student updated successfully")
    
        elif "delete" in request.POST:
            id = request.POST.get("id")
            Student.objects.get(id=id).delete()
            messages.success(request, "student deleted successfully")
        
    context = {"students": students}
    return render(request, "index.html", context=context)