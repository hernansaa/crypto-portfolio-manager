from django.contrib import admin
from .models import Asset

# Register your models here.


class AssetAdmin(admin.ModelAdmin):
    list_display = ("symbol", "name", "price_usd", "market_cap_usd", "last_updated")
    list_filter = ("source", "last_updated")
    search_fields = ("symbol", "name")
    ordering = ("symbol",)
    readonly_fields = ("last_updated", "fetched_at")

    def save_model(self, request, obj, form, change):
        # Custom save logic, if any
        super().save_model(request, obj, form, change)


admin.site.register(Asset, AssetAdmin)
