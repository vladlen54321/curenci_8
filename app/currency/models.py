from django.db import models


class ContactUs(models.Model):
    email_from = models.EmailField(max_length=254)
    email_to = models.EmailField(max_length=254)
    subject = models.CharField(max_length=15)
    message = models.TextField()

# class Rate(models.Model):
#     base_currency_type = models.CharField(max_length=3)
#     currency_type = models.CharField(max_length=3)
#     sale = models.DecimalField(max_digits=10, decimal_places=4)
#     buy = models.DecimalField(max_digits=10, decimal_places=4)
#     source = models.CharField(max_length=64)
#     created = models.DateTimeField(auto_now_add=True)
