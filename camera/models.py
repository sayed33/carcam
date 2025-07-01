from django.db import models

# Create your models here.


class CarCapture(models.Model):
    image = models.ImageField(upload_to='car_images/')
    timestamp = models.DateTimeField(auto_now_add=True)
    car_type = models.CharField(max_length=100)
    car_number = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.car_type} - {self.car_number} - {self.timestamp}"
