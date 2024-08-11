from django.db import models

# Create your models here.

class Asset(models.Model):
    symbol = models.CharField(max_length=10, unique=True)  # e.g., 'BTC', 'ETH', 'ADA'
    name = models.CharField(max_length=100)  # e.g., 'Bitcoin', 'Ethereum'
    slug = models.SlugField(max_length=100, unique=True)  # URL-friendly identifier
    source = models.CharField(max_length=50)
    price_usd = models.DecimalField(max_digits=20, decimal_places=10)
    market_cap_usd = models.DecimalField(max_digits=30, decimal_places=2, null=True, blank=True)
    volume_24h_usd = models.DecimalField(max_digits=30, decimal_places=2, null=True, blank=True)
    percent_change_24h = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    last_updated = models.DateTimeField(auto_now=True)
    fetched_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.symbol} ({self.name}) ({self.source})"

    class Meta:
        verbose_name = "Asset"
        verbose_name_plural = "Assets"
        indexes = [
            models.Index(fields=['symbol']),
            models.Index(fields=['source']),
            models.Index(fields=['last_updated']),
        ]
