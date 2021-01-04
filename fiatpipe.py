import requests
from bottle import run, Bottle, response

root = Bottle()


@root.route('/')
def serve_index() -> str: return 'Fiat Pipe for Oxen'


@root.get('/api/price/:fiat/:crypto')
def serve_price(fiat: str, crypto: str) -> dict:
    fiat = fiat.lower()
    crypto = crypto.lower()
    if crypto == 'oxen':
        crypto = 'loki-network'

    pricing_url = 'https://api.coingecko.com/api/v3/simple/price?ids={}&vs_currencies={}'.format(crypto, fiat)
    result = requests.get(pricing_url).json()

    if crypto not in result.keys():
        response.status = 404
        return {}

    return result[crypto]


if __name__ == '__main__':
    run(root, port=8080)
