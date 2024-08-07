from django.shortcuts import render, get_object_or_404
from store.models import Product
from category.models import Category
from django.core.paginator import Paginator
from django.db.models import Q

# Create your views here.


def store(request, category_slug=None):
    categories = None
    products = None

    if category_slug is not None:
        categories = get_object_or_404(
            Category, slug=category_slug
        )  # Get an object if not exist it's will be raises 404
        products = Product.objects.filter(
            category=categories, is_available=True
        )  # Get object products that exist on database
        paginator = Paginator(products, 8)
        page = request.GET.get("page")
        paged_products = paginator.get_page(page)
        product_count = products.count()
    else:
        products = Product.objects.all().filter(is_available=True).order_by("id")
        paginator = Paginator(products, 8)
        page = request.GET.get("page")
        paged_products = paginator.get_page(page)
        product_count = products.count()
    context = {
        "products": paged_products,
        "product_count": product_count,
    }
    return render(request, "stores/store.html", context)


def product_detail(request, category_slug, product_slug):
    try:
        single_product = Product.objects.get(
            category__slug=category_slug, slug=product_slug
        )
    except Exception as e:
        raise e

    context = {
        "single_product": single_product,
    }
    return render(request, "stores/product_detail.html", context)


def search(request):
    # products = Product.objects.all().filter(is_available=True) #If doesn't type any words in search box this statement will take the user to all products
    if "keyword" in request.GET:
        keyword = request.GET["keyword"]
        if keyword:
            products = Product.objects.order_by("-created_date").filter(
                Q(description__icontains=keyword) | Q(product_name__icontains=keyword)
            )

    context = {
        "products": products,
    }
    return render(request, "stores/store.html", context)
