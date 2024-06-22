from django.contrib.auth.base_user import BaseUserManager
from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    name = models.CharField(max_length=120)
    email = models.EmailField(unique=True)
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]
    ROLE_CHOICES = (
        ("A", "Admin"),
        ("AU", "Author"),
        ("B", "Buyer"),
        ("U", "User"),
    )

    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default="U")

    def is_author(self):
        return self.role == "AU"


class AuthorManager(BaseUserManager):
    def get_queryset(self):
        results = super().get_queryset()
        return results.filter(is_author=True)

    def create_user(self, email, name, password=None):
        if not email and password:
            raise ValueError("Email and password are required.")
        create_user = self.model(email=self.normalize_email(email), name=name)
        create_user.set_password(password)
        create_user.save(using=self._db)
        return create_user


class AuthorUser(User):
    def __str__(self):
        return self.name

    objects = AuthorManager()


class Author(models.Model):
    name = models.CharField(max_length=120)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Book(models.Model)

    title = models.CharField(max_length=100)
    author = models.ForeignKey(Author, on_delete=models.SET_DEFAULT, default=2)
    other_author = models.CharField(max_length=100, blank=True, null=True)

    price = models.DecimalField(max_digits=5, decimal_places=2)
    category = models.ManyToManyField(Category)

    def __str__(self):
        return self.title


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Cart #{self.pk} for {self.user.username}"


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.quantity} x {self.book.title} in Cart #{self.cart.pk}"
