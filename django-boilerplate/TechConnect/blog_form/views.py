from django.shortcuts import render, redirect
from .forms import BlogForm

def submit_blog(request):
    if request.method == 'POST':
        form = BlogForm(request.POST)
        if form.is_valid():
            blog = form.save()
            # Additional processing or notifications can be added here
            return redirect('blog:submission_success')
    else:
        form = BlogForm()


def submission_success(request):
    return render(request)