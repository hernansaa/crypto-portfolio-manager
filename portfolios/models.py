from django.db import models
from django.db.models import Sum, Case, When, F

from market_data.models import Asset


class Portfolio(models.Model):
    name = models.CharField(max_length=100)
    initial_value = models.DecimalField(
        max_digits=30, decimal_places=2, null=True, blank=True
    )

    def __str__(self):
        return self.name

    @property
    def total_value(self):
        return (
            self.transactions.aggregate(
                total=Sum(
                    Case(
                        When(transaction_type="SELL", then=-F("total_value")),
                        When(transaction_type="BUY", then=F("total_value")),
                        default=F("total_value"),
                    )
                )
            )["total"]
            or 0
        )

    class Meta:
        verbose_name = "Portfolio"
        verbose_name_plural = "Portfolios"


class PortfolioTransaction(models.Model):
    """
    Represents a transaction within a portfolio, such as buying or selling an asset.
    """

    TRANSACTION_TYPES = [
        ("BUY", "Buy"),
        ("SELL", "Sell"),
        ("TRANSFER_IN", "Transfer In"),
        ("TRANSFER_OUT", "Transfer Out"),
    ]

    portfolio = models.ForeignKey(
        Portfolio, related_name="transactions", on_delete=models.CASCADE
    )
    asset = models.ForeignKey(Asset, on_delete=models.CASCADE)
    transaction_type = models.CharField(max_length=20, choices=TRANSACTION_TYPES)
    quantity = models.DecimalField(max_digits=20, decimal_places=10)
    transaction_date = models.DateTimeField()
    price_at_transaction = models.DecimalField(max_digits=20, decimal_places=10)
    fees = models.DecimalField(max_digits=20, decimal_places=10, null=True, blank=True)
    total_value = models.DecimalField(
        max_digits=30, decimal_places=2, null=True, blank=True
    )

    def save(self, *args, **kwargs):
        # Calculate total value: (quantity * price_at_transaction) - fees
        self.total_value = (self.quantity * self.price_at_transaction) - (
            self.fees or 0
        )
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.transaction_type} {self.quantity} {self.asset.symbol} on {self.transaction_date}"

    class Meta:
        verbose_name = "Portfolio Transaction"
        verbose_name_plural = "Portfolio Transactions"
        indexes = [
            models.Index(fields=["portfolio", "asset", "transaction_date"]),
        ]
