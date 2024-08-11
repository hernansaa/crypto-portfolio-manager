from django.contrib import admin
from .models import Portfolio, PortfolioHolding


class PortfolioHoldingInline(admin.TabularInline):
    model = PortfolioHolding
    extra = 1
    readonly_fields = ('cost_basis',)
    fields = ('asset', 'quantity', 'purchase_price', 'cost_basis')
    can_delete = True
    verbose_name = "Holding"
    verbose_name_plural = "Holdings"

class PortfolioAdmin(admin.ModelAdmin):
    list_display = ('name', 'total_value')  # Add a method for total value calculation if needed
    search_fields = ('name',)
    inlines = [PortfolioHoldingInline]

    def total_value(self, obj):
        # Example method to calculate the total value of the portfolio
        total = sum(
            holding.quantity * holding.asset.price_usd for holding in obj.portfolioholding_set.all()
        )
        return f"${total:,.2f}"
    total_value.short_description = 'Total Value'


class PortfolioHoldingAdmin(admin.ModelAdmin):
    list_display = ('portfolio', 'asset', 'quantity', 'purchase_price', 'cost_basis')
    list_filter = ('portfolio', 'asset')
    search_fields = ('portfolio__name', 'asset__symbol')
    readonly_fields = ('cost_basis',)

admin.site.register(Portfolio, PortfolioAdmin)
admin.site.register(PortfolioHolding, PortfolioHoldingAdmin)

