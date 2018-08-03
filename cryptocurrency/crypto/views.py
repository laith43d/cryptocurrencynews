from django.shortcuts import render


# Create your views here.
def home(request):
    import requests
    import json

    # grap crypto news
    api_request = requests.get('https://min-api.cryptocompare.com/data/v2/news/?lang=EN')
    api = json.loads(api_request.content)

    # grap crypto price data
    price_request = requests.get(
        'https://min-api.cryptocompare.com/data/pricemultifull?fsyms=BTC,ETH,XRP,BCH,EOS,LTC,XLM,ADA,USDT,TRX&tsyms=USD')
    price = json.loads(price_request.content)

    return render(request, 'home.html', {'api': api, 'price': price})


def prices(request):
    import requests
    import json

    if request.method == 'POST':
        quote = request.POST['quote'].upper()
        crypto_request = requests.get(f'https://min-api.cryptocompare.com/data/pricemultifull?fsyms={quote}&tsyms=USD')
        crypto = json.loads(crypto_request.content)
        return render(request, 'prices.html', {'quote': quote, 'crypto': crypto})

    else:
        notfound = 'Please type a crypto currency symbol in the search field above ...'
        return render(request, 'prices.html', {'notfound': notfound})
