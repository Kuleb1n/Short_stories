from django.shortcuts import render, redirect
from .models import Story, Category
from .forms import StoryForm


def index(request):
    content = {
        'stories': Story.objects.all(),
        'categories': Category.objects.all(),
    }
    return render(request, 'Stories/index.html', content)


def by_category(request, category_id):
    stories = Story.objects.filter(category=category_id)
    categories = Category.objects.all()
    current_category = Category.objects.get(pk=category_id)
    content = {
        'stories': stories,
        'categories': categories,
        'current_category': current_category,
    }
    return render(request, 'Stories/category.html', content)


def read_more(request, story_id):
    categories = Category.objects.all()
    current_story = Story.objects.get(pk=story_id)
    content = {
        'categories': categories,
        'current_story': current_story,
    }
    return render(request, 'Stories/story.html', content)


def add_story(request):
    if request.method == 'POST':
        form = StoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')

    else:
        form = StoryForm()
    return render(request, 'Stories/add_story.html', {'form': form, })
