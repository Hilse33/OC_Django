# from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from .models import Album, Artist, Contact, Booking


def index(request):
    albums = Album.objects.filter(available=True).order_by('-created_at')[:12]
    formated_albums = ["<li>{}<li/>".format(album.title) for album in albums]
    template = loader.get_template('store/index.html')
    context = {'albums': albums}
    return HttpResponse(template.render(context, request=request))


def listing(request):
    albums = Album.objects.filter(available=True)
    formated_albums = ["<li>{}<li/>".format(album.title) for album in albums]
    message = """<ul>{]<ul/>""".format("\n".join(formated_albums))
    return HttpResponse(message)
