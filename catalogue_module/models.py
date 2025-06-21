from django.conf import settings
from django.core.validators import MaxValueValidator
from django.db import models


class Books(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название')
    author = models.ForeignKey('Authors', on_delete=models.CASCADE, verbose_name='Автор', related_name='books')
    categories = models.ManyToManyField('Categories', verbose_name='Категории', related_name='books')
    description = models.TextField(verbose_name='Описание')
    pages = models.IntegerField(verbose_name='Кол-во страниц')
    release_date = models.DateField(verbose_name='Дата выпуска')
    cover = models.ImageField(upload_to="book_covers/", verbose_name='Обложка')
    price = models.DecimalField(max_digits=6, decimal_places=2, verbose_name='Цена')
    stock = models.IntegerField(verbose_name='Количество')
    discount = models.DecimalField(max_digits=3, decimal_places=2, verbose_name='Скидка (0.0 - 1.0)',
                                   default=0, validators=[MaxValueValidator(1)],
                                   help_text='0 - скидка отсутствует, 1 - 100%')

    @property
    def total_price(self):
        if self.discount > 0:
            return round(self.price * (1 - self.discount), 2)
        return self.price

    def __str__(self):
        return self.title

class Authors(models.Model):
    image = models.ImageField(upload_to="authors/", verbose_name='Фотография')
    name = models.CharField(max_length=100, verbose_name='Имя автора')
    date_of_birth = models.DateField(verbose_name='Дата рождения', null=True, blank=True,
                                     help_text='Не оставлять пустым кроме случаев, когда дата рождения неизвестна')
    bio = models.TextField(verbose_name='Биография')

    def __str__(self):
        return self.name

class Categories(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название категории')

    def __str__(self):
        return self.title

class Cart(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    item = models.ForeignKey('catalogue_module.Books', on_delete=models.CASCADE)
    add_date = models.DateField(verbose_name='Дата добавления в корзину')

    def __str__(self):
        return f'{self.user} - {self.item.title} - {self.add_date}'

class History(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    item = models.ForeignKey('catalogue_module.Books', on_delete=models.CASCADE)
    add_date = models.DateField()
    price = models.DecimalField(max_digits=6, decimal_places=2, verbose_name='Цена на момент покупки')
