from django.urls import  include, path
from app import views


urlpatterns = [
   path('', views.HomeView.as_view({"get":"list","post":"create"})),
]