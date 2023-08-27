from django.urls import path
from . import views 
urlpatterns = [
    path('' , views.task_form.as_view() , name = "taskform") ,
    path('task_show/' , views.show_task , name = "show_task") ,
    path('delete/<int:pk>' , views.delete_task.as_view() , name = "delete") ,
    path('edit/<int:pk>' , views.edit_task.as_view() , name = "edit") ,
    path('mark_complete/<int:id>' , views.mark_completed , name ="mark_complete"),
    path('completed/' , views.completed , name='completed')
]