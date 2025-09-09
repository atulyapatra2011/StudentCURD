from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.Home, name='home'),
    path('', views.Dasgboard, name='Dashboard'),
    path('Student/', views.Add_Student, name='add_student'),
    path('StudentList/', views.Student_List, name='student_list'),
    path('EditStudent/<int:id>/', views.Edit_Student, name='edit_student'),
    path('DeleteStudent/<int:id>/', views.Delete_Student, name='delete_student'),
    path('pdf_student/<int:id>/pdf/',views.pdf_Student,name="pdf_student"),
    path('pdf_table/',views.pdf_table,name='pdf_table')
]