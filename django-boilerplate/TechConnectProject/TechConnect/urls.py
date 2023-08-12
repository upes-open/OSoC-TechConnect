"""Sample URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static
from ms_identity_web.django.msal_views_and_urls import MsalViews

msal_urls = MsalViews(settings.MS_IDENTITY_WEB).url_patterns()

urlpatterns = [
    path('', views.landing_page_view, name='landing_page'),
    path('chapter/', views.chapter_page_view, name='chapter_page'),
    path('opportunities/', views.opportunities_page_view, name='oppor_page'),
    path('sendblog/', views.send_blog_view, name='sendblog_page'),
    path('publishblog/', views.publish_blog_view, name='publishblog_page'),

    path('publishpage/', views.blog_publish_page_view, name='blog_publish_page'),
    path('submitpage/', views.blog_submit_page_view, name='blog_submit_page'),
    path('chapterclubs/', views.chapters_and_clubs_view, name='chapterclubs'),
    path('opportunitiespage/', views.opportunity_page_view, name='opportunities_page'),


    # path('', views.index, name='index'),
    path('sign_in_status', views.index, name='status'),
    path('token_details', views.token_details, name='token_details'),
    # path('blog/', include('blog_form.urls', namespace='blog')),
    path(f'{settings.AAD_CONFIG.django.auth_endpoints.prefix}/', include(msal_urls)),
    *static(settings.STATIC_URL, document_root=settings.STATIC_ROOT),
]


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)