from django.urls import path,include
from Home import views
from django.contrib import admin


#django admin header customization

admin.site.site_header="Login to Devoloper Rajkumar"
admin.site.site_title="Welcome to Rk Dashboard"
admin.site.index_title="Welcome to this portal"
urlpatterns = [
  path('', views.home, name='home'),
  path('contact/', views.contact, name='contact'),
  path('aboutus/', views.aboutus, name='aboutus'),
  path('projects/', views.projects, name='projects'),
  
]
