import uuid

from django.db import models
from django.urls import reverse


class Genre(models.Model):

    name = models.CharField(max_length=200, help_text="Enter a book genre")

    def __str__(self):
        return self.name


class Language(models.Model):

    name = models.CharField(max_length=50, help_text="Enter a book language")

    def __str__(self):
        return self.name


class Book(models.Model):

    title = models.CharField(max_length=150, help_text="Enter a book title")
    author = models.ForeignKey('Author', models.SET_NULL, null=True)
    summary = models.TextField(max_length=1000, help_text="Enter a book summary")
    isbn = models.CharField('ISBN', max_length=13, help_text='13 Character <a href="https://www.isbn-international.org/content/what-isbn">ISBN number</a>')
    genre = models.ManyToManyField(Genre, help_text="Select a book genre")
    language = models.ForeignKey(Language, models.SET_NULL, null=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('book-detail', args=[str(self.id)])


class Author(models.Model):

    first_name = models.CharField(max_length=100)
    second_name = models.CharField(max_length=100)
    date_of_birth = models.DateField(null=True, blank=True)
    date_of_death = models.DateField(null=True, blank=True)

    def __str__(self):
        return f'{self.first_name} {self.second_name}'

    def get_absolute_url(self):
        return reverse('author-detail', args=[str(self.id)])


class BookInstance(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text="Unique key of a book")
    book = models.ForeignKey(Book, on_delete=models.SET_NULL, null=True)
    due_back = models.DateField(null=True, blank=True)

    LOAN_STATUS = (
        ('m', 'Maintenance'),
        ('o', 'On loan'),
        ('a', 'Available'),
        ('r', 'Reserved')
    )


    status = models.CharField(max_length=1, choices=LOAN_STATUS, default='m')

    def __str__(self):
        return f"{self.book.title} {self.id}"






