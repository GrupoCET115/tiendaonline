from django.shortcuts import render, get_object_or_404
from cart.forms import CartAddProductForm
from .models import Category, Product, FeedbackShop


def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    return render(request,
                  'shop/product/list.html',
                  {'category': category,
                   'categories': categories,
                   'products': products})


def product_detail(request, id, slug):
    product = get_object_or_404(Product,
                                id=id,
                                slug=slug,
                                available=True)
    cart_product_form = CartAddProductForm()
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    return render(request,
                  'shop/product/detail.html',
                  {'product': product,
                   'cart_product_form': cart_product_form
                   ,'categories': categories, 'products': products})


def QuestionFrecuentAsk(request):
    return render(request, 'shop/help/FQA.html')

def SaleTerms(request):
    return render(request,'shop/help/termsSale.html')

def DisTerms(request):
    return render(request,'shop/help/disterms.html')

def Inicio(request):
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    feedbackshop = FeedbackShop.objects.all()
    return render(request,'shop/inicio.html', {'categories': categories, 'products': products, 'feedbackshop': feedbackshop})
