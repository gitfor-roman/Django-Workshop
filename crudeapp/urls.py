from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('add-student/',postStudent),
    path('add-teacher/',postTeacher),
    path('get-student/',getStudent),
    path('getsinglestudent/<id>',getSingleStudent),
    path('updatestudent/<id>',updateStudent),
    path('updateteacher/<id>',updateTeacher),
    path('deletestudent/<id>',deleteStudent),
    # path('edit-student/<id>',editStudentData),
    
]

