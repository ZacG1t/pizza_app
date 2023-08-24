from django.db import models

class Pizza(models.Model):
    """Pizza model."""
    name = models.TextField(max_length=50)

    def __str__(self):
        return self.name
    
class Topping(models.Model):
    """Pizza toppings."""
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)
    name = models.TextField(max_length=50)

    def __str__(self):
        return self.name
    