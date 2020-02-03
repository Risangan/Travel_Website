from django.urls import path
from django.contrib import admin
from django.contrib.auth.decorators import login_required
from . import views
from .models import Profile, Review
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # /search/
    path('', views.search, name='search'),

    # /search/
    path('search/', views.search, name='search'),

    # /loggedin/
    path('loggedin/', views.loggedin, name='loggedin'),

    # /review/
    path('review/', views.review, name='review'),

    # /ranking/
    path('ranking/', views.ranking, name='ranking'),

    # /makepost/
    path('makepost/', views.makepost, name='makepost'),

    # /loggedout/
    path('loggedout/', views.loggedout, name='loggedout'),

    # /country_review/
    path('country_review/', views.country_review, name='country_review'),

    # /signedup/
    path('signedup/', views.signedup, name='signedup'),

    # /login/
    path('login/', views.login, name='login'),

    # /signup/
    path('signup/', views.signup, name='signup'),

    # /view_review/
    path('view_review/<int:review_id>/', views.view_review, name='view_review'),

    # /noResults/
    path('noResults/', views.noResults, name='noResults'),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
