from django.shortcuts import render
from .models import Student

# Create your views here.
def studentData(request):
    students = Student.objects.all().values()
    students1 = Student.objects.filter(student_name__startswith='H').values()
    students2 = Student.objects.filter(student_name__contains='r').values()
    # print(students[0])
    studentlist = []
    for j in range(len(students)):
        for i in students[j].values():
            studentlist.append(i)
    
    print(studentlist)


    context = {
        'students': studentlist
    }
    return render(request, 'orm/student.html', context)

