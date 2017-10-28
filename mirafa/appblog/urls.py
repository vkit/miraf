from django.conf.urls import url
from .import views

urlpatterns = [
    url(r'^book_list/$', views.BookList.as_view(), name="book_list"),
]