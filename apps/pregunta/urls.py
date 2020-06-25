from django.urls import path
from . import views

urlpatterns = [
    path('category/<str:category>/', views.category_view, name="category"),
]