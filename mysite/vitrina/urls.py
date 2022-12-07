from django.urls import path, include
from django.views.decorators.cache import cache_page

from vitrina.views import BooksListView, select_book, author

app_name = 'vitrina'

urlpatterns = [
    path("book-list/", cache_page(60*1)(BooksListView.as_view()), name="booklist"),
    # path("book-list/", BooksListView.as_view(), name="booklist"),
    path("book/<id>/", select_book, name='select_book'),
    path("autor/<id>/", author, name='onlyAuthor'),
]
