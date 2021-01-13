from django.shortcuts import render
from .models import categories
# Create your views here.


def index(request):

    categos = categories.objects.all()

    return render(request,'index.html', {'categos': categos})