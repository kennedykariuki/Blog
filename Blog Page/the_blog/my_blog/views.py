from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from my_blog.models import Article, Category
from members.models import Member
from my_blog.forms import PostForm, UpdateForm

# Create your views here.

def home(request):
    articles = Article.objects.all().order_by("-publication_date")
    members = Member.objects.all()
    cat_menu = Category.objects.all()
    context = {
        "articles":articles,
        "members":members,
        "cat_menu":cat_menu
    }
    return render(request, "home.html", context)

# cat_menu view
def get_context_data(self, *args , **kwargs):
    cat_menu = Category.objects.all()
    context = super(home, self).get_context_data( *args , **kwargs)
    context["cat_menu"] = cat_menu
    return context

def article_details(request, pk):
    article_details = Article.objects.get( id = pk)
    members = Member.objects.all()
    cat_menu = Category.objects.all()
    context = {
        "article_details":article_details,
        "members":members,
        "cat_menu":cat_menu
    }
    return render(request, "article_details.html", context)

@login_required
def add_post(request):
    cat_menu = Category.objects.all()
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            article = form.save()
            return redirect("article_details", pk = article.id)
    else:
        form = PostForm()
    context = {
        "form":form,
        "cat_menu":cat_menu
    }
    return render(request, "add_post.html", context)

@login_required
def update_post(request, pk):
    cat_menu = Category.objects.all()
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
        "article": article,
        "cat_menu":cat_menu
    }
    return render(request, "update_post.html", context)

@login_required
def delete_post(request , pk):
    cat_menu = Category.objects.all()
    articles = get_object_or_404(Article , id = pk)
    if request.method == "POST":
        articles.delete()
        return redirect("home")
    context = {
        "articles":articles,
        "cat_menu":cat_menu
    }
    return render(request, "delete_post.html", context)

def category(request , cats):
    cat_menu = Category.objects.all()
    category_posts = Article.objects.filter(category__name = cats)
    members = Member.objects.all()
    context = {
        "category_posts":category_posts,
        "cats":cats,
        "members":members,
        "cat_menu":cat_menu
    }
    return render(request, "categories.html", context)

# def category_list(request):
#     cat_menu_list = Category.objects.all()
#     context = {
#         "cat_menu_list":cat_menu_list
#     }
#     return render(request, "category_list.html", context)

