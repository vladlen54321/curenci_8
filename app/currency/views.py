# from django.shortcuts import render
from django.http import HttpResponse
# from currency.utils import get_password
from currency.models import ContactUs


# def rate_list(request):

#     rate_list = []
#     for rate in Rate.objects.all():
#         html_string = f'ID: {rate.id}, sale: {rate.sale}, buy: {rate.buy}, <br> '
#         rate_list.append(html_string)
#     return HttpResponse(str(rate_list))

def email_ms(request):
    email = []
    for ms in ContactUs.objects.all():
        html_str = f'ID: {ms.id}, email_from: {ms.email_from}, email_to: {ms.email_to}, message: {ms.message}, <br>'
        email.append(html_str)
    return HttpResponse(str(email))
