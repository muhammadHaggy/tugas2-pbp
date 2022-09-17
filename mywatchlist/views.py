from django.shortcuts import render
from mywatchlist.models import MyWatchList
from django.http import HttpResponse
from django.core import serializers

# Create your views here.
def show_html(request):
    watchlist = MyWatchList.objects.all()
    number_of_watched = watchlist.filter(watched=True).count()
    number_of_not_watched = watchlist.count() - number_of_watched
    context = {
        'watchlist': watchlist,
        'nama': 'Muhammad Haggy',
        'student_id': '2106750370',
        'number_of_watched': number_of_watched,
        'not_watched_count': number_of_not_watched,
    }
    return render(request, 'watchlist.html', context)

def show_xml(request):
    watchlist = MyWatchList.objects.all()
    return HttpResponse(serializers.serialize("xml", watchlist), content_type="application/xml")

def show_json(request):
    watchlist = MyWatchList.objects.all()
    return HttpResponse(serializers.serialize("json", watchlist), content_type="application/json")
    