from django.urls import path
from . import views

urlpatterns = [
    path('', views.AnimalListView.as_view(), name='AllAnimals'),
    path('<int:pk>/', views.AnimalView.as_view(), name='GetAnimal'),
    path('add', views.AddAnimalView.as_view(), name='AddAnimal'),
    path('update/<int:pk>', views.UpdateAnimalView.as_view(), name='UpdateAnimal'),
    path('delete/<int:pk>', views.DeleteAnimalView.as_view(), name='DeleteAnimal')

]
