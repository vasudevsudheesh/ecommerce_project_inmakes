from django.shortcuts import render
from shop.models import Product
from django.db.models import Q


def searchresults(request):
    products = None
    query = None
    if "q" in request.GET:
        query = request.GET.get("q")
        products = Product.objects.all().filter(
            Q(name__contains=query) | Q(description__contains=query)
        )
    return render(
        request, "search_core/search.html", {"query": query, "products": products}
    )
