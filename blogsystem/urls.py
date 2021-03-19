from django.urls import path
from . import views
from .views import CommentCreateView, PostListView, AboutView, PortfolioView, ContactView, RandomPostByHeader, post_detail
urlpatterns = [
    path('', views.index, name='index'),
    path("json/csharp", views.RandomPostByHeader().Csharp, name="Csharp_json"),
    path("json/javascript", views.RandomPostByHeader().Javascript,
         name="Javascript_json"),
    path("json/css", views.RandomPostByHeader().Css, name="css_json"),
    path("json/html", views.RandomPostByHeader().Html, name="html_json"),
    path("json/Python", views.RandomPostByHeader().Python, name="python_json"),
    path("posts/<slug:slug>/", post_detail, name='post-detail'),
    path("posts/", PostListView.as_view(), name='post-list'),
    path("about/", AboutView.as_view(), name="about"),
    path("cv/", PortfolioView.as_view(), name="cv"),
    path("contact/", ContactView.as_view(), name="contact"),
    path("posts/<slug:slug>/comment/",
         CommentCreateView.as_view(), name='post_comment'),
]
