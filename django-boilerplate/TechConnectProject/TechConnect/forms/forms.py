
# TechConnect/forms/forms.py

from django import forms
from ..models.models import Chapter
from ..models.models import Opportunity
from ..models.models import BlogSubmission
from ..models.models import BlogPublication

class ChapterForm(forms.ModelForm):
    class Meta:
        model = Chapter
        fields = ['name_of_chapter', 'event_name', 'event_location', 'event_date', 'event_poster', 'event_description']

class OpportunityForm(forms.ModelForm):
    class Meta:
        model = Opportunity
        fields = ['title', 'key_details', 'description']

class BlogSubmissionForm(forms.ModelForm):
    class Meta:
        model = BlogSubmission
        fields = ['name', 'year_of_education', 'blog_title', 'blog_material']

class BlogPublicationForm(forms.ModelForm):
    class Meta:
        model = BlogPublication
        fields = ['name', 'year_of_education', 'blog_title', 'blog_material']