from django.contrib import admin
from .models import Portfolio, PortfolioTransaction


class PortfolioTransactionAdmin(admin.ModelAdmin):
    list_display = ('portfolio', 'asset', 'transaction_type', 'quantity', 'price_at_transaction', 'transaction_date', 'total_value')
    search_fields = ('portfolio__name', 'asset__symbol', 'transaction_type')
    list_filter = ('transaction_type', 'transaction_date', 'portfolio')
    ordering = ('-transaction_date',)
    readonly_fields = ('portfolio', 'asset', 'transaction_type', 'quantity', 'price_at_transaction', 'transaction_date', 'fees', 'total_value',)
    autocomplete_fields = ['portfolio', 'asset']
    list_per_page = 50
    # list_editable = ('quantity', 'price_at_transaction', 'transaction_date')

    class PortfolioTransactionInline(admin.TabularInline):
        model = PortfolioTransaction
        extra = 1
        autocomplete_fields = ['asset']
        ordering = ('-transaction_date',)  # Orders inline transactions from newest to oldest


admin.site.register(PortfolioTransaction, PortfolioTransactionAdmin)


class PortfolioAdmin(admin.ModelAdmin):
    list_display = ('name','total_value')
    search_fields = ('name',)
    ordering = ('name',)
    inlines = [PortfolioTransactionAdmin.PortfolioTransactionInline]

    def total_value(self, obj):
        return obj.total_value
    
    total_value.short_description = 'Total Portfolio Value'

admin.site.register(Portfolio, PortfolioAdmin)

