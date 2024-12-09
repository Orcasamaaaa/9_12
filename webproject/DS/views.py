from audioop import reverse

from django.views.generic import *

from django.shortcuts import render
from .models import *
from django.urls import reverse_lazy
# Create your views here.

class CourseListView(ListView):
    model =  Course
    context_object_name = 'courses'
    template_name = 'list_courses.html'

def course_searchid(request):
    search = request.GET.get('code','')
    courses = Course.objects.filter(Course_id=search)
    context_object_name = {'courses':courses}
    return render(request,'course_search.html',{'courses':courses})


def course_searchname(request):
    search = request.GET.get('code','')
    courses = Course.objects.filter(Course_name=search)
    context_object_name = {'courses':courses}
    return render(request,'course_searchname.html',{'courses':courses})

class CourseUpdateView(UpdateView):
    model = Course
    fields = ['Course_name','Teacher_name']
    context_object_name = 'courses'
    template_name = 'edit.html'
    success_url = reverse_lazy('course_list')

class CourseDeleteView(DeleteView):
    model = Course
    success_url = reverse_lazy('course_list')
    context_object_name = 'course'
    template_name = "delete.html"