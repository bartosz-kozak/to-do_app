from django.urls import path
from . import views
urlpatterns = [
    path('', views.home,name='home'),
    path('about/', views.about,name='about'),
    path('delete/<list_id>', views.delete, name='delete'),
    path('wykonanie/<list_id>', views.wykonanie, name='wykonanie'),
    path('do_wykonania/<list_id>', views.do_wykonania, name='do_wykonania'),
    path('edycja/<list_id>', views.edycja,  name='edycja'),
]
