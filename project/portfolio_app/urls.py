from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('iris/', views.iris, name='iris'),
    path('casa/', views.casa, name='casa'),
    path('GA_CV.ENG.pdf/', views.descargar_cv_ingles, name='descargar_cv_ingles'),
]