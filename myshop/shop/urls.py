from django.urls import path
from . import views

app_name = 'shop'

urlpatterns = [
    path('preguntasFrecuentes/',views.QuestionFrecuentAsk, name='QuestionFrecuentAsk'),
    path('terminosDeVenta/',views.SaleTerms, name="SaleTerms"),
    path('terminosDeDistriucion',views.DisTerms,name="DisTerms"),
    path('', views.Inicio, name='inicio'),
    path('categoria/', views.product_list, name='product_list'),
    path('categoria/<slug:category_slug>/', views.product_list,
         name='product_list_by_category'),
    path('<int:id>/<slug:slug>/', views.product_detail,
         name='product_detail'),
]
