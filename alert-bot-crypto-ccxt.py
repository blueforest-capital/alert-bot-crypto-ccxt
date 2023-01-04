import config
import ccxt
import time
import subprocess

# Set your API key and Secret and Address
api_key = config.apt_key
api_secret = config.api_secret
address = config.address

# Initialize the Waves exchange client
exchange = ccxt.wavesexchange({
    'apiKey': api_key,
    'secret': api_secret,
})  

# Load Markets
markets = exchange.load_markets()

# Check Balance
#balance = exchange.fetch_balance()
#print(balance)

def send_alert(message):
  subprocess.run(["telegram-send", message])

# Set the cryptocurrency and threshold values
symbol = 'WX/WAVES'
sell_threshold = 0.2369
buy_threshold = 0.05

while True:
  # Retrieve the current price of the cryptocurrency
  price = exchange.fetch_ticker(symbol)['last']

  # Check if the price is above the threshold
  if price > sell_threshold:
    # Send an alert
    print(f'The price of {symbol} has risen above {sell_threshold}! Current price: {price}')
    message = f'The price of {symbol} has risen above {sell_threshold}! Current price: {price}'
    send_alert(message)
  
  # Check if the price is below the threshold
  elif price < buy_threshold:
    # Send an alert
    print(f'The price of {symbol} has fallen below {buy_threshold}! Current price: {price}')
    message = f'The price of {symbol} has fallen below {buy_threshold}! Current price: {price}'
    send_alert(message)
    # 
  else:
    print(f'The price of {symbol} is {price}, which is above the buy threshold of {buy_threshold} and below the sell threshold of {sell_threshold}')
    message = f'The price of {symbol} is {price}, which is above the buy threshold of {buy_threshold} and below the sell threshold of {sell_threshold}'
    send_alert(message)



  # Sleep for a minute before checking again
  time.sleep(120)
