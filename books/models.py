from django.db import models

class Book(models.Model):
    book_serial_number = models.AutoField(primary_key=True)
    book_name = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField()
    publisher = models.CharField(max_length=255)
    discount = models.DecimalField(max_digits=5, decimal_places=2)
    book_description = models.TextField()
    photo_url = models.CharField(max_length=255)

    def __str__(self):
        return self.book_name
