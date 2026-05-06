# from my_blog import views
from my_blog.views import HomeView, ArticleDetailsView
from django.urls import path

urlpatterns = [
    # path("", views.index, name="index")
    path("", HomeView.as_view(), name="home"),
    path("article/<int:pk>", ArticleDetailsView.as_view(), name="article_details")
]