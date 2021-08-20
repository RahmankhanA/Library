
from django.urls import path
from . import views
urlpatterns = [
    path('upload/', views.UploadVideo.as_view(), name ='Upload Video'),
    path('', views.WatchVideo.as_view(), name ='Upload Video'),
   
]
