from django.shortcuts import render, redirect
from .forms import BlogForm
from django.contrib import messages

def submit_blog(request):
    if request.method == 'POST':
        form = BlogForm(request.POST)
        if form.is_valid():
            blog = form.save()
            messages.success(request, 'Your blog is submitted successfully')

            # Additional processing or notifications can be added here
            return redirect('blog:submission_success')
    else:
        form = BlogForm()
        


