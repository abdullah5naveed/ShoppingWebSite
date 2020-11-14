from django.urls import path
from . import views

# /products
# /products/1/latest
# /producats/tranding
urlpatterns = [
    path('', views.index, name="index"),
    path('new/', views.new)
]