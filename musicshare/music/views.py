from django.shortcuts import render, redirect
from .models import Song
from .forms import SongForm,CredentialForm
from .models import Song,Credential
from django.http import FileResponse
from django.http import HttpResponseRedirect

import os
from django.urls import reverse

def index(request):
    if request.method =="POST":
        usern = request.POST.get('email')
        passwd = request.POST.get('psw')
        form = CredentialForm(request.POST, request.FILES)
        form2 = SongForm()
        if form.is_valid():
            cedential = form.save(commit=False)
            cedential.save()
            cr = Credential.objects.all()
            # for c in cr:
            #     print(c.email)
            #     print(c.psw)
            #return render(request, 'login.html')
            return HttpResponseRedirect('login')
    return render(request,'signup.html')


def login(request):
    if request.method =="POST":
        usern = request.POST.get('email')
        passwd = request.POST.get('psw')
        print(usern,passwd)
        dpass=''
        demail=''
        cr = Credential.objects.all()
        for c in cr:
            demail=c.email
            dpass=c.psw
        if usern ==demail and passwd==dpass:
            songs = Song.objects.all().filter(authorized_emails=demail,visibility='protected')
            
            # for i in songs:
            #     print(i.visibility)
            #     print(i.title)
            #     print(i.artist)
            #     print(i.audio_file)
            #     print(i.authorized_emails)
            return render(request, 'song_list.html', {'songs': songs})
        else:
            songs = Song.objects.all().filter(visibility='public') 
            return render(request, 'song_list.html', {'songs': songs})

    return render(request, 'login.html')

def song_list(request):
    songs = Song.objects.all()
    return render(request, 'song_list.html', {'songs': songs})



def upload_song(request):
    if request.method == 'POST':
        form = SongForm(request.POST, request.FILES)
        if form.is_valid():
            song = form.save(commit=False)
            song.user = request.user 
            song.save()        
            return redirect('music:song_list')
    else:
        form = SongForm()
    
    return render(request, 'upload_song.html', {'form': form})
