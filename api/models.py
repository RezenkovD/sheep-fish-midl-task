from django.db import models


# Create your models here.

class Printer(models.Model):
    name = models.CharField(max_length=64, help_text="Printer name")
    api_key = models.CharField(max_length=128, help_text="API access key")
    KITCHEN = "KT"
    CLIENT = "CL"
    CHOICES = [
        (KITCHEN, "Kitchen"),
        (CLIENT, "Client"),
    ]
    check_type = models.CharField(
        max_length=2, choices=CHOICES, default=KITCHEN, help_text="The type of receipt printed by the printer"
    )
    point_id = models.IntegerField(help_text="The point to which the printer is bound")