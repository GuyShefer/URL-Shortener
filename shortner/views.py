from django.conf.urls import url
from django.shortcuts import redirect, render
from django.http import HttpResponse
import uuid
from .models import Url


def index(request):
    return render(request, 'index.html')


def create(request):
    if request.method == 'POST':
        link = request.POST['link']
        uid = str(uuid.uuid4())[:5]
        new_url = Url(link=link, uuid=uid)
        new_url.save()
        return HttpResponse(uid)


def go(request, pk):
    url_details = Url.objects.get(uuid=pk)
    print('@', url_details.link)
    return redirect(url_details.link)
