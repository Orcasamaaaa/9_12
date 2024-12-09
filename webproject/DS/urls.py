from django.urls import path,include

from DS.views import *

urlpatterns = [
    path('course/',CourseListView.as_view(),name='course_list'),
    path('id_search',course_searchid,name='id_search'),
    path('name_search',course_searchname,name='name_search'),
    path('course/edit/<str:pk>',CourseUpdateView.as_view(),name='edit'),
    path('course/delete/<str:pk>',CourseDeleteView.as_view(),name='delete'),
]