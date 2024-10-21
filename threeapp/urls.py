from django.urls import path
from django.views import View

from .import views


urlpatterns = [
        path('',views.index,name='index'),
        path('contact/', views.contact,name='contact'),
        path('ideagained/',views.ideagained,name='ideagained'),
        path('idea/',views.idea,name='idea'),
        path('ouridea/',views.ouridea,name='ouridea'),
        path('aboutpage/',views.aboutpage,name='aboutpage'),
        path('register/',views.register,name='register'),
        path('index/',views.index,name='index'),        
]

