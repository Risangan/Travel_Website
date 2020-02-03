from urllib.parse import quote_plus
from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from .models import Profile, Review
from .serializers import ProfileSerializer
from .serializers import ReviewSerializer
from rest_framework.response import Response
from django.contrib.auth.hashers import make_password, check_password
from django.db import IntegrityError
from django.template import RequestContext, loader
from django.http import HttpResponse, Http404

def login(request):
    return render(request, 'mysite/login.html')

def loggedin(request):
    if not ('username' in request.POST and 'password' in request.POST):
        return render(request,'mysite/login.html')
    else:
        username = request.POST['username']
        password = request.POST['password']
        try: user = Profile.objects.get(username=username)
        except Profile.DoesNotExist: raise Http404('User does not exist')       
        if user.check_password(password):           
            request.session['username'] = username
            request.session['password'] = password
            context = {
               'username': username,
               'logged_in' : 'username' in request.session
            }
            return render(request, 'mysite/loggedin.html', context)
        else:
            raise Http404(user)

def country_review(request):
    if 'country' in request.GET:
        land = request.GET['country']
        reviews = Review.objects.filter(country=land)
        if reviews.exists():
            context = {
    	        'reviews' : reviews,
                'logged_in' : 'username' in request.session,
                'country' : request.GET['country']
	        }
            return render(request, 'mysite/country_review.html', context )
        else:
            context = {
            'logged_in' : 'username' in request.session
            }
            return render(request, 'mysite/NoResults.html', context)
    else:
        raise Http404('Data is missing')

def loggedout(request):
    request.session.flush()
    return render(request, 'mysite/loggedout.html')

def makepost(request):
    context = { 
        'logged_in' : 'username' in request.session
    }
    return render(request, 'mysite/makepost.html', context)

def ranking(request):
    if 'word' in request.GET:
       word = request.GET['word']
       reviews = Review.objects.filter(country_review__contains=word)
       if reviews.exists():
           context = {
               'reviews' : reviews,
               'logged_in' : 'username' in request.session
           }
           return render(request, 'mysite/ranking.html', context )
       else:
           context = {
            'logged_in' : 'username' in request.session
           }
           return render(request, 'mysite/NoResults.html', context)
    else:
       try: 
           user_profile = Profile.objects.get(username = request.session['username'])
           reviews = Review.objects.filter(profile=user_profile)
       except Profile.DoesNotExist: raise Http404('User Does not exist')
       if reviews.exists():
           context = {
               'reviews' : reviews,
               'logged_in' : 'username' in request.session,
               'user_review' : True
           }
           return render(request, 'mysite/ranking.html', context )
       else:
           context = {
            'logged_in' : 'username' in request.session
           }
           return render(request, 'mysite/NoResults.html', context)

def review(request):
    if 'title' in request.POST and 'country_review' in request.POST:
        country = request.POST['country']
        title = request.POST['title']
        country_review = request.POST['country_review']
        share_string = quote_plus(country_review)
        Review.objects.create(
            country = country,
            title = title,
            country_review = country_review,
            profile = Profile.objects.get(username = request.session['username'])
        )
        context = {
            'country' : country,
            'title' : title,
            'country_review' : country_review,
            'logged_in' : 'username' in request.session,
            'share_string' : share_string
        }
        return render(request, 'mysite/review.html', context )
    else: 
        context = {
            'logged_in' : 'username' in request.session
        }
        return render(request, 'mysite/NoResults.html', context)

def search(request):
    context = {
        'logged_in' : 'username' in request.session
    }
    return render(request, 'mysite/search.html', context )

def signup(request):
    return render(request, 'mysite/signup.html')

def signedup(request):
    if 'username' in request.POST and 'password' in request.POST:
        username = request.POST['username']
        password = request.POST['password']
        Profile.objects.create(
            username = username,
            password = make_password(password)
        )
        return render(request, 'mysite/signedup.html')
    else: 
        raise Http404('Data missing')

def view_review(request, review_id):
    review = Review.objects.get(id = review_id)
    share_string = quote_plus(review.country_review)
    context = {
        'review' : review,
        'logged_in' : 'username' in request.session,
        'share_string' : share_string
    }
    return render(request, 'mysite/view_review.html', context)

def noResults(request):
    context = {
            'logged_in' : 'username' in request.session
        }
    return render(request, 'mysite/NoResults.html', conetext)

