from django.urls import path
from . import views

app_name = 'myshop'

urlpatterns = [
    path('products/',views.ProductListView.as_view(),name='product_list'),
    path('products/<pk>/',views.ProductDetailView.as_view(),name='product_detail'),
    path('feedbackshop/', views.feedbackshop_list),
]