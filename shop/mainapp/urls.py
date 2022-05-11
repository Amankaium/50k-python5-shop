from django.urls import path, include
from . import views
from .views import home
urlpatterns = [
    path('', home, name='home' ),
    # path('product/', views.product, name='product' ),
]
