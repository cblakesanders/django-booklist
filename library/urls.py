"""library URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views

from django.conf import settings
from django.conf.urls.static import static

from booklist.views import *
from users.views import register_view, update_profile_view, profile_view, update_relationship_view

from rest_framework.routers import DefaultRouter

# router = DefaultRouter()
# router.register(r'update-relationship', update_relationship_view)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('add-book/', request_book_view, name='add-book'),
    path('register/', register_view, name='register'), 
    path('update-profile/', update_profile_view, name='update-profile'),
    path('profile/<str:username>/', profile_view.as_view(), name='profile'),
    path('book/<int:pk>/', BookDetailView.as_view(), name='book-detail'),
    path('', hopepage_view, name='home'), 
    path('api/', update_relationship_view)
] 

if settings.DEBUG: 
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
