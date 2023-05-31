from django.urls import path
from .views import *

urlpatterns = [
    path('', home),
    path('news/<int:id>', blog),
    path('category/<int:id>', category_news),
    path('contact', contact),


]