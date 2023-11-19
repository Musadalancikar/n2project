# myapp/urls.py
from django.shortcuts import render
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import GeoViewSet, AddressViewSet, CompanyViewSet, UsersViewSet, PostsViewSet, CommentsViewSet, AlbumsViewSet, PhotosViewSet, TodoViewSet

router = DefaultRouter()
router.register(r'geo', GeoViewSet)
router.register(r'address', AddressViewSet)
router.register(r'company', CompanyViewSet)
router.register(r'users', UsersViewSet)
router.register(r'posts', PostsViewSet)
router.register(r'comments', CommentsViewSet)
router.register(r'albums', AlbumsViewSet)
router.register(r'photos', PhotosViewSet)
router.register(r'todo', TodoViewSet)

# def home(request):
#     return render(request, 'home.html', {'message': 'Hoş geldiniz!'})

urlpatterns = [
    # path('', home, name='home'),
    path('', include(router.urls)),
]
