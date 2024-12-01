from rest_framework.routers import DefaultRouter
from django.urls import path
from . import views

from .views import ArticleViewSet
# router = DefaultRouter()
# router.register(r'articles', ArticleViewSet, basename='user')
# urlpatterns = router.urls

urlpatterns = [
    path('api/capitals/', views.GetCapitalInfoView.as_view()),
    path('', views.main_page, name='main_page'),
]