from django.shortcuts import render
from .models import Story, Category


def index(request):
    content = {
        'stories': Story.objects.all(),
        'categories': Category.objects.all(),
    }
    return render(request, 'Stories/index.html', content)
