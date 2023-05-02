from django.contrib import admin
# from currency.views import email_ms, index, http_response, rate_update, rate_delete, rate_create
from currency import views
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('__debug__/', include('debug_toolbar.urls')),

    path('currency/', include('currency.urls')),

    path('', views.IndexView.as_view()),


]
