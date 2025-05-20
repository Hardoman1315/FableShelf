from random import randint

from django.contrib.auth.decorators import login_required
from django.template.response import TemplateResponse

from catalogue_module.models import Books, Categories
from main.models import IndexBanners

from django.urls import reverse_lazy


def index_page(request):
    random_categories_id = Categories.objects.order_by('?')[:3]
    chosen_categories = []

    for category in random_categories_id:
        books = Books.objects.filter(categories=category)[:10]

        chosen_categories.append({
            "category": category,
            "books": books,
        })

    context = {
        "banner": IndexBanners.objects.filter(is_active = True),
        "categories": chosen_categories,
    }
    return TemplateResponse(request, "index.html", context)

@login_required(login_url=reverse_lazy("auth_module:login_page"))
def profile_page(request):
    return TemplateResponse(request, "profile.html")
