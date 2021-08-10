from django.urls import path
from . import views

urlpatterns = [
    path('', views.getRoutes),

    path('notes/', views.getNotes),
    path('notes/create/', views.createNote),
    path('notes/<str:pk>/update/', views.updateNote),
    path('notes/<str:pk>/delete/', views.deleteNote),
    path('notes/<str:pk>/', views.getNote),

    path('country-name/', views.getCountry),
    path('country-name/create/', views.addCountry),
    path('country-name/<str:pk>/update/', views.updateCountry),
    path('country-name/<str:pk>/delete/', views.deleteCountry),
    path('country-name/<str:pk>/', views.getSingleCountry),

]