from django.urls import path, include

from .views import*
# urlpatterns = [
#     path('', home, name='home' ),
#     path('product/', views.product, name='product' ),
# ]

urlpatterns = [
    path('', home, name='home'),
    path('<category_slug>', home, name='home_by_category'),
    path('product/', product, name='product'),
]