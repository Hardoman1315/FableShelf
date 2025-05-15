from django.contrib.auth.decorators import login_required
from django.template.response import TemplateResponse

from catalogue_module.models import Books
from main.models import IndexBanners


def index_page(request):
    context = {
        "banner": IndexBanners.objects.filter(is_active = True),
        "fantasy": Books.objects.filter(categories__title__iexact='Фэнтези').order_by('-id')[:10],
    }
    return TemplateResponse(request, "index.html", context)

@login_required
def profile_page(request):
    return TemplateResponse(request, "profile.html")
