from datetime import date

from django.core.mail import send_mail
from django.db.models import Q
from django.shortcuts import redirect, get_object_or_404
from django.template.response import TemplateResponse

from catalogue_module.models import Books, Authors, Categories, Cart, History
from review_module.models import Reviews


def redirect_to_index(request):
    return redirect("/")

def book_page(request, book_id):
    book = get_object_or_404(Books, id=book_id)
    reviews = Reviews.objects.filter(book=book)

    context = {
        'book': book,
        'reviews': reviews,
    }

    return TemplateResponse(request, "book.html", context)

def add_review(request, book_id):
    book = get_object_or_404(Books, id=book_id)

    entry = Reviews(
        user=request.user,
        book=book,
        review=request.POST.get('new_review'),
        date=date.today()
    )
    entry.save()

    return redirect("catalogue_module:book_page", book_id)

def author_page(request, author_id):
    author = get_object_or_404(Authors, id=author_id)

    context = {
        'author': author,
        'books': author.books.all()
    }
    return TemplateResponse(request, "author.html", context)

def authors_page(request):
    authors = Authors.objects.all()

    context = {
        'authors': authors,
    }

    return TemplateResponse(request, 'authors-list.html', context)

def catalogue_page(request, category_id):
    categories = Categories.objects.all()
    selected_category = get_object_or_404(Categories, id=category_id)
    items = Books.objects.filter(categories=selected_category)

    context = {
        'categories': categories,
        'items': items,
    }

    return TemplateResponse(request, "catalogue.html", context)

def discounts_page(request):
    books = Books.objects.filter(discount__gt=0)
    context = {
        'books': books,
    }
    return TemplateResponse(request, "discounts.html", context)

def search(request):
    if request.method == "POST":
        search_request = request.POST.get('search')

        books = Books.objects.filter(
            Q(title__icontains=search_request) | Q(author__name__icontains=search_request)
        )
        authors = Authors.objects.filter(name__icontains=search_request)

        context = {
            'request': search_request,
            'books': books,
            'authors': authors,
        }

        return TemplateResponse(request, "search.html", context)
    return redirect("/")

def cart_page(request):
    if not request.user.is_authenticated:
        return redirect('auth_module:login_page')

    items = Cart.objects.filter(user=request.user)
    total_price = sum(item.item.total_price for item in items)

    context = {
        'items': items,
        'total_price': total_price,
    }

    return TemplateResponse(request, "cart.html", context)

def add_to_cart(request, book_id):
    if not request.user.is_authenticated:
        return redirect('login')

    book = get_object_or_404(Books, id=book_id)

    if book.stock <= 0:
        return redirect("catalogue_module:book_page", book_id)

    Cart.objects.create(
        user=request.user,
        item=book,
        add_date=date.today()
    )

    book.stock -= 1
    book.save()

    return redirect('catalogue_module:cart_page')

def remove_from_cart(request, cart_id, book_id):
    book = get_object_or_404(Books, id=book_id)

    book.stock += 1
    book.save()

    Cart.objects.filter(id=cart_id).delete()

    return redirect('catalogue_module:cart_page')

def clear_cart(request):
    cart_entries = Cart.objects.filter(user=request.user)

    for cart_entry in cart_entries:
        book = cart_entry.item
        book.stock += 1
        book.save()
        cart_entry.delete()

    return redirect('catalogue_module:cart_page')

def confirm_payment(request, cart_id):
    entry = Cart.objects.get(id=cart_id)

    send_mail(
        subject='Покупка подтверждена',
        message=f'Вы успешно приобрели "{entry.item.title}" на сумму {entry.item.total_price} рублей. Спасибо за покупку',
        from_email=None,
        recipient_list=[request.user.email],
        fail_silently=False,
    )

    entry.delete()

    return redirect('catalogue_module:cart_page')

def confirm_all_payments(request):
    cart_entries = Cart.objects.filter(user=request.user)
    message = 'Вы успешно приобрели следующие предметы:'
    total = 0

    for cart_entry in cart_entries:
        book = cart_entry.item

        total += book.total_price
        message += f'\n{book.title} - {book.total_price};'

    message += f'\nЧто в сумме будет {total} рублей. Спасибо за покупку'

    send_mail(
        subject='Покупка подтверждена',
        message=message,
        from_email=None,
        recipient_list=[request.user.email],
        fail_silently=False,
    )

    for cart_entry in cart_entries:
        History.objects.create(
            user=request.user,
            item=cart_entry.item,
            add_date=date.today(),
            price=cart_entry.item.total_price
        )
        cart_entry.delete()

    return redirect('catalogue_module:cart_page')
