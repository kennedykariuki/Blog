from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from my_blog.models import Article
from my_blog.forms import PostForm, UpdateForm

# Create your views here.

def home(request):
    articles = Article.objects.all().order_by("-publication_date")
    context = {
        "articles":articles,
    }
    return render(request, "home.html", context)

def article_details(request, pk):
    article_details = Article.objects.get( id = pk)
    context = {
        "article_details":article_details
    }
    return render(request, "article_details.html", context)

@login_required
def add_post(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            article = form.save()
            return redirect("article_details", pk = article.id)
    else:
        form = PostForm()
    context = {
        "form":form
    }
    return render(request, "add_post.html", context)

@login_required
def update_post(request, pk):
    # Get the article to edit
    article = get_object_or_404(Article, id = pk)
    if request.method == "POST":
        form = UpdateForm(request.POST, instance=article)
        if form.is_valid():
            form.save()
            return redirect("article_details", pk=article.id)
    else:
        form = PostForm(instance=article)
    context = {
        "form": form,
        "article": article
    }
    return render(request, "update_post.html", context)

@login_required
def delete_post(request , pk):
    articles = get_object_or_404(Article , id = pk)
    if request.method == "POST":
        articles.delete()
        return redirect("home")
    context = {
        "articles":articles
    }
    return render(request, "delete_post.html", context)