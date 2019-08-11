from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from kkbox_search.models import KkboxSong, UserlikeRecord
from django.db import models
from django.contrib import messages
import time
# Create your views here.
def index(request):
    message = ''
    title = 'KKBOX Search Web'
    return render(request, 'kkbox_search/index.html', locals())

def search(request):
    mess = ''
    song_name = ''
    id = []
    song = []
    artist = []
    url = []
    img = []
    '''if('delete' in request.POST):
        id = request.POST['delete']
        song_name = KkboxSong.objects.filter(id = int(id))[0].song_name
        KkboxSong.objects.filter(id = int(id)).delete()
    else:'''
    song_name = request.GET['song_name']
    songs = KkboxSong.objects.filter(song_name__contains = song_name)
    for s in songs:
        id.append(s.id)
        song.append(s.song_name)
        artist.append(s.artist)
        url.append(s.url)
        img.append(s.image)
    if not songs :
        mess = '歌曲不存在'
    #return render(request, 'kkbox_search/search.html', locals())
    print("hii")
    return JsonResponse({'id':id,'song':song, 'artist':artist, 'url':url, 'image':img})
    
def insert(request):
    print("insert")
    song_name = request.POST['song_name']
    artist = request.POST['artist']
    songs = KkboxSong.objects.filter(song_name = song_name)
    for song in (songs):
        if(song.artist == artist):
            return JsonResponse({'response' : "歌曲已存在"})
    new_song = KkboxSong.objects.create(song_name = song_name, artist = artist,
                                                    url = request.POST['url'], image = request.POST['image'],
                                                    length = request.POST['length'],is_deleted = 0,
                                                    created_at = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()),
                                                    updated_at = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()))
    new_song.save()
    #messages.add_message(request, messages.INFO, '歌曲新增成功')
    return JsonResponse({"response" : "新增歌曲成功"})
    #return render(request, 'kkbox_search/index.html', locals())
def edit(request):
    '''message = ''
    if request.method == 'POST':
        id = request.POST['done']
        song = KkboxSong.objects.get(id = id)
        
        song.artist = request.POST['artist']
        song.song_name = request.POST['song_name']
        song.url = request.POST['url']
        song.save()
        #messages.info(request, '修改成功!')
        messages.add_message(request, messages.INFO, '修改成功')
        return HttpResponseRedirect('/')
    else:
        id = request.GET['edit']
        songs = KkboxSong.objects.filter(id = id)
    return render(request, 'kkbox_search/edit.html', locals())'''
    song = KkboxSong.objects.get(id = request.GET["id"])
    return JsonResponse({"id":song.id,"song":song.song_name,"artist":song.artist,"url":song.url,"image":song.image})
def done(request):
    id = request.POST["id"]
    song = KkboxSong.objects.get(id = id)
    song.song_name = request.POST["song_name"]
    song.artist = request.POST["artist"]
    song.url = request.POST["url"]
    song.save()
    return JsonResponse({"response":"修改成功"})
def delete(request):
    id = request.POST['id']
    song_name = KkboxSong.objects.filter(id = int(id))[0].song_name
    KkboxSong.objects.filter(id = int(id)).delete()
    return JsonResponse({"response":"刪除成功"})

def like(request):
    
    print("Some one linkin")
    items = UserlikeRecord.objects.filter(user_like = 'like')
    id_list = []
    songs = []
    artists = []
    for item in items:
        if(not item.item_id in id_list):
            id_list.append(item.item_id)
    for id in id_list:
        songs.append(KkboxSong.objects.get(id = id).song_name)
        artists.append(KkboxSong.objects.get(id = id).artist)
    return JsonResponse({"songs":songs,"artists":artists})
    #return render(request, 'kkbox_search/like.html', locals())

def unlike(request):
    items = UserlikeRecord.objects.filter(user_like = 'unlike')
    id_list = []
    songs = []
    artists = []
    for item in items:
        if(not item.item_id in id_list):
            id_list.append(item.item_id)
    for id in id_list:
        songs.append(KkboxSong.objects.get(id = id).song_name)
        artists.append(KkboxSong.objects.get(id = id).artist)
    return JsonResponse({"songs":songs,"artists":artists})
'''def insert(request):
    title = "KKbox Search Web"
    mess = ''
    if request.method == 'POST':
        song_name = request.POST['song_name']
        songs = kkbox_song.objects.all()
        songs = kkbox_song.objects.filter(song_name = song_name)
        if not songs:
            new_song = kkbox_song.objects.create(song_name = song_name,artist = request.POST['artist'],
                                                url = request.POST['url'], is_deleted = False)
            new_song.save()
            mess = '新增歌曲成功'
        else :
            mess = '此歌曲已存在'
    return render(request, 'kkbox_search/index.html', locals())
def modify(request):
    mess = ''
    if request.method == 'POST':
        song_name = request.POST['song_name']
        songs = kkbox_song.objects.all()
        songs = kkbox_song.objects.filter(song_name = song_name)
        if songs:
            new_song = kkbox_song.objects.update(song_name = song_name,artist = request.POST['artist'],
                                                url = request.POST['url'], is_deleted = False)
            new_song.save()
            mess = '歌曲修改成功'
        else :
            mess = '此歌曲不存在'
    return render(request, 'kkbox_search/index.html',locals())

def action(request):
    title = "KKbox Search Web"
    if request.POST:
        if search in request.POST:
            Search()



def Search(request):
    mess=''
    song = ''
    artist = ''
    image = None
    url = ''
    length = ''
    if 'search' in request.POST:
        if request.POST:
            song_name = request.POST['song_name']
            songs = KkboxSong.objects.filter(song_name = song_name)
            if not songs :
                mess = '此歌曲不存在'
            else:
                artist = songs.values('artist')[0]['artist']
                url = songs.values('url')[0]['url']
                image = songs.values('image')[0]['image']
                length = songs.values('length')[0]['length']
    return render(request, 'kkbox_search/index.html', locals())


def insert(request):
    mess = ''
    if 'insert' in request.POST:
        if request.POST:
            song = KkboxSong.objects.filter(song_name = request.POST['song_name'])
            if not song :
                new_song = KkboxSong.objects.create(song_name = request.POST['song_name'], artist = request.POST['artist'],
                                                    url = request.POST['url'], image = request.POST['image'],
                                                    length = request.POST['length'],is_deleted = 0,
                                                    created_at = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()),
                                                    updated_at = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()))
                new_song.save()
                mess = '歌曲新增成功'
            else:
                mess = '歌曲已存在'
    return render(request, 'kkbox_search/index.html', locals())
    '''
