from django.urls import path
from .views import show_all, one_book

urlpatterns = [
    path('showbooks',show_all),
    path('book/<id>', one_book, name='book'),
]
