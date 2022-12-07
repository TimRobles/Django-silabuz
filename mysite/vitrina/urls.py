from django.urls import path, include
from django.views.decorators.cache import cache_page

from vitrina.views import BooksListView, pagina1, pagina2, select_book, author

app_name = 'vitrina'

urlpatterns = [
    path("book-list/", cache_page(60*1)(BooksListView.as_view()), name="booklist"),
    # path("book-list/", BooksListView.as_view(), name="booklist"),
    path("book/<id>/", select_book, name='select_book'),
    path("autor/<id>/", author, name='onlyAuthor'),
    path("pagina1/", pagina1, name='pagina1'),
    path("pagina2/", pagina2, name='pagina2'),
]
