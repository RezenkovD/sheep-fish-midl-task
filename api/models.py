import os

from django.db import models


# Create your models here.

class Printer(models.Model):
    name = models.CharField(max_length=64, help_text="Printer name")
    api_key = models.CharField(max_length=128, help_text="API access key", unique=True)
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

    def __str__(self):
        return self.name


def user_directory_path(instance, filename):
    return "{0}_{1}.pdf".format(instance.printer_id, instance.type)


class Check(models.Model):
    printer_id = models.ForeignKey(Printer, on_delete=models.CASCADE, help_text="printer")
    KITCHEN = "KT"
    CLIENT = "CL"
    CHOICES = [
        (KITCHEN, "Kitchen"),
        (CLIENT, "Client"),
    ]
    type = models.CharField(
        max_length=2, choices=CHOICES, default=KITCHEN, help_text="Type check"
    )
    order = models.JSONField(help_text="order information")
    NEW = "NW"
    RENDERED = "RD"
    PRINTED = "PD"
    CHOICES_STATUS = [
        (NEW, "New"),
        (RENDERED, "Rendered"),
        (PRINTED, "Printed"),
    ]
    status = models.CharField(
        max_length=2, choices=CHOICES_STATUS, default=NEW, help_text="Check status"
    )
    pdf_file = models.FileField(upload_to=user_directory_path, max_length=1024,
                                help_text="link to created PDF file")

    def __str__(self):
        return self.printer_id
