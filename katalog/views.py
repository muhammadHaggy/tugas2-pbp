from multiprocessing import context
from django.shortcuts import render
from katalog.models import CatalogItem
# TODO: Create your views here.
def show_katalog(request):
    data_catalog = CatalogItem.objects.all()
    context = {
        'list_katalog': data_catalog,
        'student_id': '2106750370',
        'nama': 'Muhammad Haggy'
    }
    return render(request, 'katalog.html', context)