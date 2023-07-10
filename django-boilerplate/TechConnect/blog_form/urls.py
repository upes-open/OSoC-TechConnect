from django.urls import path
from . import views

app_name = 'blog'
urlpatterns = [
    path('submit/', views.submit_blog, name='submit_blog'),
    path('submission-success/', views.submission_success, name='submission_success'),
]