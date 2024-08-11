from django.core.management.base import BaseCommand
import requests
from market_data.models import Asset

class Command(BaseCommand):
    """
    Populates de data base withe market data from Binance
    """
    help = 'Populate Asset data from Binance'

    def handle(self, *args, **kwargs):
        url = 'https://api.binance.com/api/v3/ticker/24hr'
        
        try:
            response = requests.get(url)
            response.raise_for_status()  # Raise an exception for HTTP errors
            data = response.json()

            for item in data:
                # Binance symbols are usually in uppercase with an optional suffix like 'BTC' or 'ETH'
                symbol = item['symbol']
                price_usd = float(item['lastPrice'])  # Convert the price to float
                market_cap_usd = None  # Binance API does not provide market cap directly
                volume_24h_usd = float(item['quoteVolume'])
                percent_change_24h = float(item['priceChangePercent'])

                # Create or update the asset
                asset, created = Asset.objects.update_or_create(
                    symbol=symbol,
                    defaults={
                        'name': symbol,  # Binance API does not provide names; using symbol as name
                        'slug': symbol.lower(),  # Use symbol as slug
                        'source': 'Binance',
                        'price_usd': price_usd,
                        'market_cap_usd': market_cap_usd,
                        'volume_24h_usd': volume_24h_usd,
                        'percent_change_24h': percent_change_24h,
                    }
                )
                if created:
                    self.stdout.write(self.style.SUCCESS(f'Created asset: {asset}'))
                else:
                    self.stdout.write(self.style.SUCCESS(f'Updated asset: {asset}'))

        except requests.RequestException as e:
            self.stdout.write(self.style.ERROR(f'Error fetching data from Binance: {e}'))



# class Command(BaseCommand):
#     """
#     Populates de data base withe market data from CoinGecko
#     """
#     help = 'Populate Asset data from CoinGecko'

#     def handle(self, *args, **kwargs):
#         url = 'https://api.coingecko.com/api/v3/coins/markets'
#         params = {
#             'vs_currency': 'usd',
#             'ids': 'bitcoin,ethereum,cardano',  # Add more coin IDs as needed
#         }
        
#         try:
#             response = requests.get(url, params=params)
#             response.raise_for_status()  # Raise an exception for HTTP errors
#             data = response.json()

#             for item in data:
#                 asset, created = Asset.objects.update_or_create(
#                     symbol=item['symbol'].upper(),
#                     defaults={
#                         'name': item['name'],
#                         'slug': item['id'],
#                         'source': 'CoinGecko',
#                         'price_usd': item['current_price'],
#                         'market_cap_usd': item['market_cap'],
#                         'volume_24h_usd': item['total_volume'],
#                         'percent_change_24h': item['price_change_percentage_24h'],
#                     }
#                 )
#                 if created:
#                     self.stdout.write(self.style.SUCCESS(f'Created asset: {asset}'))
#                 else:
#                     self.stdout.write(self.style.SUCCESS(f'Updated asset: {asset}'))
#         except requests.RequestException as e:
#             self.stdout.write(self.style.ERROR(f'Error fetching data from CoinGecko: {e}'))
