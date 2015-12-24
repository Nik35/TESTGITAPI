from django.shortcuts import render
from .models import *

# Create your views here.
def paintings_data(request):
    painting_data = Paintings.objects.all()
    return render(request,'index.html',{'painting_data': painting_data})
