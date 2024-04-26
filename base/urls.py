
from django.urls import path
from . import views

urlpatterns = [
    path('', views.endPoint),
    path('advocates_list/', views.AdvocatesList),
    path('advocates/<str:username>/', views.AdvocateDetails),
]
