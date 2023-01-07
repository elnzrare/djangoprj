from django.db import models

class book(models.Model):
    name = models.CharField(max_length=20)
    is_about = models.TextField(max_length=1000)
    is_free = models.BooleanField()
    updated_time = models.DateTimeField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Book"
        verbose_name_plural = "Books"

class comment(models.Model):
    book = models.ForeignKey(book, on_delete=models.CASCADE)
    text = models.TextField()
    created_time = models.DateField()


