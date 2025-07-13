from django.db import models

class Accommodation(models.Model):
    TYPE_CHOICES = [
        ('PG', 'PG'),
        ('Hostel', 'Hostel'),
        ('Apartment', 'Apartment'),
        ('Shared Flat', 'Shared Flat'),
    ]

    name = models.CharField(max_length=200)
    location = models.CharField(max_length=300)
    accommodation_type = models.CharField(max_length=20, choices=TYPE_CHOICES, default='PG')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    features = models.TextField()  # Comma-separated features
    rating = models.FloatField(default=0.0)  # Default rating to 0.0
    review_count = models.IntegerField(default=0.0)
    image_url = models.CharField(max_length=500, blank=True, null=True)

    def __str__(self):
        return self.name