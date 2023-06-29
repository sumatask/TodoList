from . import views
from django.urls import path,include

urlpatterns = [
    
    path('',views.home,name='home'),
    path('add/',views.add,name='add'),
    path('delete/<int:taskid>/', views.delete, name='delete'),
    path('update/<int:id>/', views.update, name='update'),
    path('cbvhome/',views.TaskListview.as_view(),name='cbvhome'),
    path('cbvdetail/<int:id>/',views.TaskDetailview.as_view(),name='cvbdetail'),
    path('cbvupdate/<int:pk>/',views.TaskUpdateview.as_view(),name='cvbupdate'),
    path('cbvdelete/<int:pk>/', views.TaskDeleteview.as_view(), name='cvbupdelete')

]