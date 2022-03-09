from django.urls import path
from vehicle_app import views

urlpatterns = [
    path('order-list/', views.taskList, name="task-list"),
    path('order-detail/<str:pk>/', views.taskDetail, name="task-detail"),
    path('order-create/', views.taskCreate, name="task-create"),
    path('order-update/<str:pk>/', views.taskUpdate, name="task-update"),

]