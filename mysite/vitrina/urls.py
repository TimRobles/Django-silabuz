from django.urls import path, include

from vitrina.views import BooksListView

urlpatterns = [
    path("booklist/", BooksListView.as_view(), name="booklist"),
]
