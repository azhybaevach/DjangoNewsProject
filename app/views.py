from django.shortcuts import render, redirect
from .models import *
from .forms import *


def home(request):
    news = News.objects.all()
    categories = Category.objects.all()
    related_news = News.objects.all().order_by('?')[:3]
    return render(request, 'index.html', {'news': news, 'categories': categories, 'related_news': related_news})


def category_news(request, id):
    category = Category.objects.get(id=id)
    news = News.objects.filter(category=category)
    related_news = News.objects.all().order_by('?')[:3]
    categories = Category.objects.all()
    return render(request, 'index.html', {'news': news, 'categories': categories, 'category': category, 'related_news':related_news})


def blog(request, id):

    news = News.objects.get(id=id)
    categories = Category.objects.all()

    if request.method == 'POST':
        form = CommentForm(data=request.POST)
        data = form.save(commit=False)
        data.news = news
        data.save()

    related_news = News.objects.all().order_by('?')[:3]
    form = CommentForm()
    return render(request, 'blog.html', {'news': news, 'categories': categories,
                                         'related_news': related_news, 'form': form})


def contact(request):
    news = News.objects.all()
    categories = Category.objects.all()
    related_news = News.objects.all().order_by('?')[:3]
    form = NewsForm()
    if request.method =="POST":
        form = NewsForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/')

        else:
            print(form.errors)

    return render(request, 'contact.html', {'news': news, 'categories': categories,
                                            'related_news': related_news, 'form': form})




