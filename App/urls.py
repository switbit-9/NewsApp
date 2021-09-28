
from django.urls import path
from django.contrib import admin
from . import views

urlpatterns = [
   path('newsfeed/', views.newsfeed, name='newsfeed'),
   path('toparticles/', views.top, name='topheadlines'),
   path('toparticles/', views.top, name='topheadlines'),
   path('newsfeed/<str:category>', views.fcategory, name='fcategory'),
   path('admin/', admin.site.urls),
   path('sources/', views.sources, name='sources'),
   path('article/<str:title>/', views.article, name='article'),
   path('get/search/', views.search, name='search'),
   path('osources/<str:id>', views.osources, name='osources')

]