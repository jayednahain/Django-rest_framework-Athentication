from django.contrib import admin
from django.urls import path
from nastedSerializer_app import views


urlpatterns = [
   path('author/',views.AuthorListView.as_view()),
   path('authormodeification/<int:pk>',views.AuthorDetailView.as_view()),

   path('book/',views.BookListView.as_view()),
   path('bookmodification/<int:pk>',views.BookDetailView.as_view())
]
