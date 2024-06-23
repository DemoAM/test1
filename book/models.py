from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Category(models.Model):
    category_name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.category_name


class Book(models.Model):
    title = models.CharField(max_length=50, unique=True)
    categories = models.ManyToManyField(Category)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=6,decimal_places=2)

    def __str__(self):
        return f"Book is {self.title} Author is {self.author} "


class Cart(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    price = models.IntegerField(null=True,blank=True)

    def save(self, *args, **kwargs):
        self.price = self.book.price * self.quantity
        return super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.quantity} book's {self.book.title} in Cart"
