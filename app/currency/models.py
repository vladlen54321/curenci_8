from django.db import models
from currency.model_choices import CurrencyType


class Source(models.Model):
    source_url = models.CharField(
        max_length=255,
        choices=CurrencyType.choices,
        default=CurrencyType.CURRENCY_TYPE_GIT
    )
    name = models.CharField(max_length=64)
    created = models.DateTimeField(auto_now_add=True)


class ContactUs(models.Model):
    email_from = models.EmailField(max_length=254)
    email_to = models.EmailField(max_length=254)
    subject = models.CharField(max_length=15)
    message = models.TextField()


class ResponseLog(models.Model):
    response_time = models.FloatField()
    request_method = models.CharField(max_length=10)
    query_params = models.CharField(max_length=20)
    ip = models.CharField(max_length=60)
    path = models.CharField(max_length=168)

# class Rate(models.Model):
#     base_currency_type = models.CharField(max_length=3)
#     currency_type = models.CharField(max_length=3)
#     sale = models.DecimalField(max_digits=10, decimal_places=4)
#     buy = models.DecimalField(max_digits=10, decimal_places=4)
#     source = models.CharField(max_length=64)
#     created = models.DateTimeField(auto_now_add=True)
