"""settings URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from currency import views
from django.urls import path

app_name = 'currency'

urlpatterns = [
    path('', views.IndexView.as_view()),
    path('email_ms/', views.SourceListView.as_view(), name='email_ms'),
    path('rate/create/', views.SourceCreateView.as_view(), name='rate_create'),
    path('rate/update/<int:pk>/', views.SourceUpdateView.as_view(), name='rate_updata'),
    path('rate/delete/<int:pk>/', views.SourceDeleteView.as_view(), name='rate_delete'),
    path('rate/details/<int:pk>/', views.SourceDetailsView.as_view(), name='rate_details'),
    path('contactus/create/', views.ContactUsCreateView.as_view(), name='contactus_create'),
    path('response/create/', views.ResponseCreateView.as_view(), name='response_create'),
]
