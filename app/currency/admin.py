from django.contrib import admin
from currency.models import Source
from rangefilter.filters import DateTimeRangeFilter


class SourceAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'source_url',
        'name',
    )

    readonly_fields = (
        'name',
        'source_url',
    )

    def has_delete_permission(self, request, obj=None):
        return False

    search_fields = (
        'name',
    )

    list_filter = (
        'name',
        ('created', DateTimeRangeFilter),
    )


admin.site.register(Source, SourceAdmin)
