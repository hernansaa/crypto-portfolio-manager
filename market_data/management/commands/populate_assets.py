from django.core.management.base import BaseCommand
import requests
from market_data.models import Asset

class Command(BaseCommand):
    help = 'Populate Asset data from CoinGecko'

    def handle(self, *args, **kwargs):
        url = 'https://api.coingecko.com/api/v3/coins/markets'
        params = {
            'vs_currency': 'usd',
            'ids': 'bitcoin,ethereum,cardano',  # Add more coin IDs as needed
        }
        
        try:
            response = requests.get(url, params=params)
            response.raise_for_status()  # Raise an exception for HTTP errors
            data = response.json()

            for item in data:
                asset, created = Asset.objects.update_or_create(
                    symbol=item['symbol'].upper(),
                    defaults={
                        'name': item['name'],
                        'slug': item['id'],
                        'source': 'CoinGecko',
                        'price_usd': item['current_price'],
                        'market_cap_usd': item['market_cap'],
                        'volume_24h_usd': item['total_volume'],
                        'percent_change_24h': item['price_change_percentage_24h'],
                    }
                )
                if created:
                    self.stdout.write(self.style.SUCCESS(f'Created asset: {asset}'))
                else:
                    self.stdout.write(self.style.SUCCESS(f'Updated asset: {asset}'))
        except requests.RequestException as e:
            self.stdout.write(self.style.ERROR(f'Error fetching data from CoinGecko: {e}'))
