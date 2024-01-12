from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name="index"),
    path('delete-emp/<int:emp_id>',views.delete_emp,name="delete_emp"),
    path('update-emp/<int:emp_id>',views.update_emp,name="update_emp"),
    path('do-update-emp/<int:emp_id>',views.do_update_emp,name="do_update_emp")
]