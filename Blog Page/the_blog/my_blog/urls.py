from django.urls import path
from my_blog import views

urlpatterns = [
    path("", views.home , name= "home"),
    path("article_details/<int:pk>/", views.article_details, name="article_details"),
    path("add_post/", views.add_post, name = "add_post"),
    path("update_post/<int:pk>/", views.update_post, name="update_post"),
    path("delete_post/<int:pk>/", views.delete_post, name="delete_post"),
    path("category/<str:cats>/", views.category , name = "category"),
    # path("category_list", views.category_list, name="category_list")
]