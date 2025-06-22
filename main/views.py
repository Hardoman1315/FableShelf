from django.contrib.auth.decorators import login_required
from django.template.response import TemplateResponse

from catalogue_module.models import Books, Categories, History
from main.models import IndexBanners

from django.urls import reverse_lazy


def index_page(request):
    random_categories_id = Categories.objects.order_by('?')[:3]
    chosen_categories = []

    for category in random_categories_id:
        books = Books.objects.filter(categories=category, stock__gt=0)[:10]

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
    user = request.user
    history = History.objects.filter(user=user).order_by('-id')

    context = {
        "user": user,
        "history": history
    }

    return TemplateResponse(request, "profile.html", context)
