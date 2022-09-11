from django.shortcuts import render
from .models import Student
from django.http import JsonResponse, HttpResponse
from rest_framework.response import Response
from rest_framework import status
from django.core import serializers
from .serializers import SchoolSerializer, StudentSerializer
from rest_framework.decorators import api_view
from .forms import StudentForm
from django.views.decorators.csrf import csrf_exempt


# function based view
def index(request):

    return render(request, 'students/index.html')

@api_view(['GET'])
def query(request, id=None):
    if id:
        record = Student.objects.get(id=id)
        serializer = StudentSerializer(record)
        return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
    return Response({"status": "BAD REQUEST", "message": "id Required"}, status=status.HTTP_400_BAD_REQUEST )

def search(request):
    student_id = request.GET.get('student_id', None)
    student_name = request.GET.get('student_name', None)

    if student_id:
        record = Student.objects.get(id=student_id)
        serializer = StudentSerializer(record)
        if serializer.data:
            return JsonResponse(serializer.data)
        else:
            return JsonResponse({"message": "Student Not found"})

    elif student_name:
        names = student_name.split(" ")

        data = []
        for name in names:
            result = Student.objects.filter(first_name__contains=name)
            serializer = StudentSerializer(result, many=True)
            print(type(serializer.data))
            data.append(serializer.data)
        if data == []:
            return JsonResponse({"message": "Student Not found"})
        else:
            return JsonResponse(data, safe=False)
    return render(request, 'students/search.html')


@csrf_exempt
def student_create_view(request):

    form = StudentForm(request.POST or None, request.FILES or None)
    message = ""
    if form.is_valid():
        form.save()
        message = 'Student record saved successfully, create another!'
        form = StudentForm(None)

    return render(request, "students/create_student.html", {'form': form, 'message': message})
    