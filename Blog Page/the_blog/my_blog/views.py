from django.shortcuts import render
from django.views.generic import ListView , DetailView
from my_blog.models import Post

# Create your views here.

# def index(request):
#     context = {}
#     return render(request, "index.html", context)

class HomeView(ListView):
    model = Post
    template_name = 'home.html'

class ArticleDetailsView(DetailView):
    model = Post
    template_name = 'article_details.html'