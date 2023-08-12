from django.shortcuts import render, redirect
from django.conf import settings
import requests
from .models.models import Chapter
from .forms.forms import ChapterForm
from .forms.forms import OpportunityForm
from .forms.forms import BlogSubmissionForm
from .forms.forms import BlogPublicationForm
from django.conf import settings


ms_identity_web = settings.MS_IDENTITY_WEB

def index(request):
    return render(request, "auth/status.html")

@ms_identity_web.login_required
def token_details(request):
    return render(request, 'auth/token.html')

@ms_identity_web.login_required
def call_ms_graph(request):
    ms_identity_web.acquire_token_silently()
    graph = 'https://graph.microsoft.com/v1.0/users'
    authZ = f'Bearer {ms_identity_web.id_data._access_token}'
    results = requests.get(graph, headers={'Authorization': authZ}).json()

    # trim the results down to 5 and format them.
    if 'value' in results:
        results ['num_results'] = len(results['value'])
        results['value'] = results['value'][:5]

    return render(request, 'auth/call-graph.html', context=dict(results=results))


def landing_page_view(request):
    return render(request, 'landingpage/landing_page.html')

def chapter_page_view(request):
    if request.method == 'POST':
        form = ChapterForm(request.POST)
        if form.is_valid():
            form.save()
            # return redirect('success_page')  # Replace 'success_page' with the URL name of the page after successful form submission
    else:
        form = ChapterForm()
    
    return render(request, 'chapter/Chap_create_a_post.html', {'form': form})


def opportunities_page_view(request):
    if request.method == 'POST':
        form = OpportunityForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = OpportunityForm()

    return render(request, 'opportunities/Form_for_opportunities.html', {'form': form})

def send_blog_view(request):
    if request.method == 'POST':
        form = BlogSubmissionForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = BlogSubmissionForm()
    
    return render(request, 'blog/send_blog/Form_to_send_blog.html', {'form': form})

def publish_blog_view(request):
    if request.method == 'POST':
        form = BlogPublicationForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = BlogPublicationForm()
    
    return render(request, 'blog/publish_blog/Form_to_publish_blog.html', {'form': form})

def blog_publish_page_view(request):
    return render(request, 'blog/Blog_and_publications_page_to_publish/Blog_and_publications_page_to_publish.html')

def blog_submit_page_view(request):
    return render(request, 'blog/Blog_and_publications_page_to_submit/Blog_and_publications_page_to_submit.html')

def chapters_and_clubs_view(request):
    return render(request, 'chapter/Chapters_and_clubs/Chapters_and_clubs.html')

def opportunity_page_view(request):
    return render(request, 'opportunities/Opportunity_page/Opportunity_page.html')







