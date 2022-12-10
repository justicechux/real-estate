from django.db import models

# Create your models here.

REASON = (
    ("rentage", "rentage"),
    ("sale", "sale"),
    ("mortgaage", "mortgage")
)

HOUSE_CHOICES = (
    ("Detached", "Detached"),
    ("Semi-detached", "semi-detached"),
    ("Duplex", "Duplex"), 
    ("Bungalow", "Bungalow")
)


class services(models.Model):
    services = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.services



class property(models.Model):
    name = models.CharField(max_length=50)
    type = models.CharField(choices = REASON, max_length=10)
    email = models.EmailField()
    choice = models.CharField(choices = HOUSE_CHOICES, max_length=20)
    date_of_viewing = models.DateField()
    messages = models.TextField(max_length=200)



    def __str__(self):
        return self.name