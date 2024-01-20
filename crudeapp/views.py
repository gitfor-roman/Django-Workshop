from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import *


@api_view(['POST'])
# Create your views here.

def postStudent(request):                  #APi ko request
        try:
                request_data=request.data          #APi request bata aako data
                serializer = StudentSerializer(data=request_data,many=False)    
                if serializer.is_valid(raise_exception=True):
                        serializer.save()
                        return Response({'message':"student added successfully"})
        except Exception as e:
                return Response({"err": str(e)})
        
@api_view(['POST'])   
def postTeacher(request):
        # print(request.data)
        try:
                request_data=request.data
                serializer = TeacherSerializer(data=request_data,many=False)
                if serializer.is_valid(raise_exception=True):
                        serializer.save()
                        return Response({'message':"Teacher added successfully"})
        except Exception as e:
                return Response({"errgyvbgy": str(e)})
   
#for all students 

@api_view(['GET'])
def getStudent(request):
        students = Student.objects.all()
        serialized_data= StudentSerializer(students, many=True)
        return Response(serialized_data.data)

#for single student get
              
@api_view(['GET'])
def getSingleStudent(request,id):
        student= Student.objects.get(id=id)
        serialized_data= StudentSerializer(student, many=False)
        return Response (serialized_data.data)

        
@api_view(['POST'])
def updateStudent(request,id):
        try:
                student= Student.objects.get(id=id)
                serialized_data= StudentSerializer(student,many=False,data=request.data)
                if serialized_data.is_valid(raise_exception=True):
                        serialized_data.save()
                        return Response({"Message":"data updated succesfully","data": serialized_data.data})
        except Exception as e:
                return Response({"error":e})        
@api_view(['POST'])
def updateTeacher(request,id):
        try:
                teacher= Teacher.objects.get(id=id)
                serialized_data= TeacherSerializer(teacher,many=False,data=request.data)
                if serialized_data.is_valid(raise_exception=True):
                        serialized_data.save()
                        return Response({"Message":"data updated succesfully","data": serialized_data.data})
        except Exception as e:
                return Response({"error":e})

@api_view(['GET'])   
def deleteStudent(request,id):
        student= Student.objects.get(id=id)
        student.delete()
        return Response({"Message": "data deleted succesfully"})

                