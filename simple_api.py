from pycoingecko import CoinGeckoAPI
import pandas as pd

cg = CoinGeckoAPI()
bitcoin_data = cg.get_coin_market_chart_by_id(id="bitcoin", vs_currency="usd", days=30)
bitcoin_price_data = bitcoin_data['prices']

data = pd.DataFrame(bitcoin_price_data, columns=['Timestamp', 'Price'])