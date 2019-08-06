from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Artist, Song
# Create your views here.

def home(request):
  return HttpResponse("You are home")

def json_res(request):
  return JsonResponse({ "status" : "Ok" })

def artist_list(request):
  artists = Artist.objects.all()
  return render(request, 'artist_list.html', {"artists": artists})

def song_list(request):
  songs = Song.objects.all()
  return render(request, 'song_list.html', {"songs": songs})

def artist_detail(request, pk):
  artist = Artist.objects.get(id=pk)
  return render(request, 'artist_detail.html', {"artist":artist})