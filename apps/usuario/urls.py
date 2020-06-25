from django.urls import path
from . import views
urlpatterns = [
    path('login/', views.login_view, name="login"),
    path('logout/', views.logout_view, name="logout"),
    path('register/', views.register_view, name="register"),
    path('paginaPrincipal/', views.paginaPrincipal_view, name="paginaPrincipal"),
    path('answerQuestion/<int:id_question>/', views.answerQuestion_view, name="answerQuestion"),
    path('newQuestion/<int:id_User>/', views.newQuestion_view, name="newQuestion"),
    path('myquestions/<int:id_User>/', views.myquestions_view, name="myquestions"),
    path('deleteQuestion/<int:id_question>/', views.deleteQuestion_view, name="deleteQuestion"),
    path('answerMyQuestion/<int:id_question>/', views.answerMyQuestion_view, name="answerMyQuestion"),
    path('profile/<int:id_User>/', views.profile_view, name="profile"),
    path('publicProfile/<int:id_User>/', views.publicProfile_view, name="publicProfile"),
]