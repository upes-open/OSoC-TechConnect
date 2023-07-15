from django.urls import path
from . import views

app_name = 'chapter'

urlpatterns = [
    path('blog/publish/', views.blog_publish, name='blog_publish')

]