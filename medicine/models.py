from django.db import models
from django.db.models import Model
import datetime


class Medicine(Model):

    title = models.CharField(max_length=30)
    company = models.CharField(max_length=30)
    country = models.CharField(max_length=30)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    definition = models.TextField(help_text='Enter biological and chemical composition')
    expiration_date = models.DateField(default=datetime.date(2025, 3, 4))
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='medicine_image/% Y/% m/% d/', default='default.png', blank=True, null=True)

    def __str__(self):
        return f"{self.title} ({self.company}) "


