from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from .models import Artist, Song
from .forms import ArtistForm, SongForm
from django.contrib.auth.decorators import login_required
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

@login_required
def artist_detail(request, pk):
  artist = Artist.objects.get(id=pk)
  return render(request, 'artist_detail.html', {"artist":artist})

@login_required
def artist_create(request):
  if request.method == 'POST':
    form = ArtistForm(request.POST)
    if form.is_valid():
      artist = form.save(commit=False)
      artist.user = request.user
      artist.save()
      return redirect('artist_detail', pk=artist.pk)
  else:
    form = ArtistForm()
  return render(request, 'artist_form.html', {'form': form, 'header': 'New Artist'})

@login_required
def artist_edit(request, pk):
  artist = Artist.objects.get(id=pk)
  if request.method == 'POST':
    form = ArtistForm(request.POST, instance=artist)
    if form.is_valid():
      artist = form.save()
      return redirect('artist_detail', pk=artist.pk)
  else:
    form = ArtistForm(instance=artist)
  return render(request, 'artist_form.html', {'form': form, 'header':f'Edit{artist.name}'})

@login_required
def artist_delete(request, pk):
  Artist.objects.get(id=pk).delete()
  return redirect('artist_list')

@login_required
def song_create(request, pk):
  artist = Artist.objects.get(id=pk)
  if request.method == 'POST':
    form = SongForm(request.POST)
    if form.is_valid():
      song = form.save(commit=False)
      song.artist = artist
      song.save()
      return redirect('artist_detail', pk=song.artist.pk)
  else:
    form = SongForm()
  return render(request, 'artist_form.html', {'form': form, 'header': f'Add Song for {artist.name}'})

@login_required
def song_edit(request, pk):
  song = Song.objects.get(id=pk)
  if request.method == 'POST':
    form = SongForm(request.POST, instance=song)
    if form.is_valid():
      song = form.save()
      return redirect('artist_detail', pk=song.artist.pk)
  else:
    form = SongForm()
  return render(request, 'artist_form.html', {'form': form, 'header':f'Edit{song.title}'})

@login_required
def song_delete(request, pk):
  Song.objects.get(id=pk).delete()
  return redirect('song_list')


def profile(request):
  # get user from request
  user = request.user
  # all artists attached to user
  artists = Artist.objects.filter(user=user)
  # render profile page
  return render(request, 'profile.html', {'artists': artists})