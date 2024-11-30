from django.shortcuts import render

# Create your views here.
from rest_framework.generics import get_object_or_404
from rest_framework.generics import  ListCreateAPIView, RetrieveAPIView, RetrieveUpdateAPIView
from rest_framework.generics import RetrieveUpdateDestroyAPIView
from rest_framework.mixins import ListModelMixin, CreateModelMixin
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Article, Author
from .serializers import ArticleSerializer
# class ArticleView(APIView):
#     def get(self, request):
#         articles = Article.objects.all()
#         serializer = ArticleSerializer(articles, many=True)
#         return Response({"articles": serializer.data})
#     def post(self, request):
#         article = request.data.get("articles")
#         # Create an article from the above data
#         serializer = ArticleSerializer(data=article)
#         if serializer.is_valid(raise_exception=True):
#             article_saved = serializer.save()
#         return Response({"success": "Article '{}' created successfully".format(article_saved.title)})
#     def put(self, request, pk):
#         saved_article = get_object_or_404(Article.objects.all(), pk=pk)
#         data = request.data.get('articles')
#         serializer = ArticleSerializer(instance=saved_article, data=data, partial=True)
#         if serializer.is_valid(raise_exception=True):
#             article_saved = serializer.save()
#         return Response({"success": "Article '{}' updated successfully".format(article_saved.title)})
#     def delete(self, request, pk):
#         # Get object with this pk
#         article = get_object_or_404(Article.objects.all(), pk=pk)
#         article.delete()
#         return Response({"message": "Article with id `{}` has been deleted.".format(pk) }, status=204)


# class ArticleView(ListCreateAPIView):
#     queryset = Article.objects.all()
#     serializer_class = ArticleSerializer
#     def perform_create(self, serializer):
#         author = get_object_or_404(Author, id=self.request.data.get('author'))
#         return serializer.save(author=author)
# class SingleArticleView(RetrieveUpdateDestroyAPIView):
#     queryset = Article.objects.all()
#     serializer_class = ArticleSerializer

from rest_framework import viewsets
from .models import Article
from .serializers import ArticleSerializer
class ArticleViewSet(viewsets.ModelViewSet):
    serializer_class = ArticleSerializer
    queryset = Article.objects.all()