# do not import from project
from django.db import models


class CurrencyType(models.TextChoices):
    CURRENCY_TYPE_GAME = 'URL_Game', 'https://itorrents-igruha.org/11739-1-the-last-of-us-part-1.html'
    CURRENCY_TYPE_GPT = 'URL_gpt', 'https://chat.openai.com/'
    CURRENCY_TYPE_DJANGO = 'URL_django', 'https://jeffkit.gitbooks.io/django-girls-tutorial/content/ru/django_templates/index.html'
    CURRENCY_TYPE_GIT = 'URL_git', 'https://github.com/vladlen54321/curenci_8'
