from django.db import models
# Create your models here.

class School(models.Model):
    id = models.AutoField(primary_key=True)
    school = models.CharField(max_length=200)
    email = models.CharField(max_length=200)	
    principal = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)	
    address2 = models.CharField(max_length=200)

    def __str__(self):
        return f'School: {self.school}'

class Book(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    author_name = models.CharField(max_length=200)
    date_of_publication = models.CharField(max_length=200, null=True, blank=True)
    number_of_pages = models.CharField(max_length=200)

    def __str__(self):
        return f'Book: {self.title}'


class Student(models.Model):
    id = models.AutoField(primary_key=True)
    first_name	= models.CharField(max_length=200)
    last_name	= models.CharField(max_length=200, null=True, blank=True)	
    email	= models.CharField(max_length=200)	
    gender	= models.CharField(max_length=200, null=True, blank=True)	
    school	=  models.ForeignKey(School, null=True, blank=True, on_delete=models.SET_NULL)
    books	= models.ManyToManyField(Book, blank=True)

    def __str__(self):
        return f'Student: {self.first_name} {self.last_name}'

    @property
    def student_full_name(self):
        return f'{self.first_name} {self.last_name}'

    @property
    def school_name(self):
        return self.school.school 

    @property
    def school_phone(self):
        return self.school.phone

    @property
    def books_read(self):
        books = self.books.all()
        books_read = [book.title for book in books]
        return books_read

    @property
    def book_pages_read(self):
        books = self.books.all()
        book_pages_read = 0
        for book in books:
            book_pages_read += int(book.number_of_pages)
        return book_pages_read


