from .models import Author, Book
from nastedSerializer_app.serializers import AuthorSerializer, BookSerializer
from rest_framework import generics
from rest_framework.authentication import BasicAuthentication

#this is only use for directly resticted view
from rest_framework.permissions import IsAuthenticated

#this model get the data from django model
#we make a user defined with rule
#by following the rules it will restices the views controlling
from rest_framework.permissions import DjangoModelPermissions


# Create your views here.
class AuthorListView(generics.ListCreateAPIView):
   queryset = Author.objects.all()
   serializer_class = AuthorSerializer

   #if the user is authenticated he can access this api
   authentication_classes = [BasicAuthentication]
   permission_classes = [IsAuthenticated,DjangoModelPermissions]


class AuthorDetailView(generics.RetrieveUpdateDestroyAPIView):
   queryset = Author.objects.all()
   serializer_class = AuthorSerializer


class BookListView(generics.ListCreateAPIView):
   queryset = Book.objects.all()
   serializer_class = BookSerializer


class BookDetailView(generics.RetrieveUpdateDestroyAPIView):
   queryset = Book.objects.all()
   serializer_class = BookSerializer

# Create your views here.
