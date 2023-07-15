from django.shortcuts import render, redirect
from .forms import BlogPostForm
from django.contrib import messages

def blog_publish(request):
    if request.method == 'POST':
        form = BlogPostForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your blog is submitted successfully')
            return redirect('blog_published')
    else:
        form = BlogPostForm()

    return render({'form': form})

