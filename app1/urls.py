from django.urls import include, path

from . import views

urlpatterns1 = [
    path('home/', views.home),
]


from django.urls import path

from .views import upload_file

urlpatterns = [
    path('upload/', upload_file, name='upload_file'),
]+urlpatterns1
