from django.urls import path
from . import views

urlpatterns = [
    path('elements/', views.element_list),
    path('elements/<int:pk>/', views.element_detail),
]
