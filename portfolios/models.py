from django.db import models

from market_data.models import Asset


class Portfolio(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Portfolio"
        verbose_name_plural = "Portfolios"


class PortfolioHolding(models.Model):
    """
    Asociative Entity between Porfolio and Asset models.
    Represents an asset within a portfolio, along with additional details like quantity.
    """
    portfolio = models.ForeignKey(Portfolio, on_delete=models.CASCADE)
    asset = models.ForeignKey(Asset, on_delete=models.CASCADE)
    quantity = models.DecimalField(max_digits=20, decimal_places=10, default=0)
    date_acquired = models.DateField(null=True, blank=True)
    purchase_price = models.DecimalField(max_digits=20, decimal_places=10, null=True, blank=True)
    cost_basis = models.DecimalField(max_digits=30, decimal_places=2, null=True, blank=True)

    def __str__(self):
        return f"{self.portfolio.name} - {self.asset.symbol} ({self.quantity})"

    class Meta:
        verbose_name = "Portfolio Holding"
        verbose_name_plural = "Portfolio Holdings"
        unique_together = ('portfolio', 'asset')
        indexes = [
            models.Index(fields=['portfolio', 'asset']),
        ]
