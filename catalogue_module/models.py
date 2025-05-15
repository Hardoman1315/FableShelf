from django.db import models


class Books(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название')
    author = models.ForeignKey('Authors', on_delete=models.CASCADE, verbose_name='Автор', related_name='books')
    categories = models.ManyToManyField('Categories', verbose_name='Категории', related_name='books')
    pages = models.IntegerField(verbose_name='Кол-во страниц')
    release_date = models.DateField(verbose_name='Дата выпуска')
    cover = models.ImageField(upload_to="book_covers/", verbose_name='Обложка')
    price = models.DecimalField(max_digits=6, decimal_places=2, verbose_name='Цена')

    def __str__(self):
        return self.title

class Authors(models.Model):
    name = models.CharField(max_length=100, verbose_name='Имя автора')
    date_of_birth = models.DateField(verbose_name='Дата рождения')
    bio = models.TextField(verbose_name='Биография')

    def __str__(self):
        return self.name

class Categories(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название категории')

    def __str__(self):
        return self.title
