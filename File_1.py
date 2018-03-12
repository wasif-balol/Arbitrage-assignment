import requests
import matplotlib as plt

def Exchange_rates(Base, Destination):
    data =requests.get('https://api.cryptonator.com/api/full/{}-{}'.format(Base, Destination))
    Data = (data.json()['ticker']['markets'])

    market = []
    price = []
    volume = []

    for A in range(len(Data)):
        market.append(Data[A]['market'])
        price.append(Data[A]['price'])
        volume.append(Data[A]['volume'])
    Difference = float(max(price))-float(min(price))
    print("Minimum Price is \t",max(price)," \tat ", market[price.index(max(price))],
          " \nMaximum Price is \t",min(price)+" \tat ", market[price.index(min(price))],
          "\ndifference \t  is\t", Difference,Destination)

    numbers = (0, len(market))

    plt.scatter(numbers, market, color='red')

    for i, txt in enumerate(price):
        plt.annotate(txt, (numbers[i], market[i]))

    plt.title('ARBITRAGE')
    plt.ylabel('#PRICE')
    plt.show()

print("Basic Currency in BTC")
Dest_Currency = input('Enter the currency in which you want rates')
Exchange_rates('BTC', Dest_Currency)