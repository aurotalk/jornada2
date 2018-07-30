from django.shortcuts import render
from django.http import HttpResponse
from tuites.models import Tuite
from datetime import datetime





def index(request):
    context = {
        'now': datetime.now(),
        'tuites': Tuite.objects.all(),
    }
    return render(request, 'template.html', context)
    

