from django.urls import path
from . import views

urlpatterns = [
    path('<int:id>', detail, name="detail"),
    path('rooms', rooms_list, name="rooms"),
    path('new', views.new, name="new")
]
