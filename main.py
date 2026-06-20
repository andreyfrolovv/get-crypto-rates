import requests
from fastapi import FastAPI

app = FastAPI()


@app.get("/get-crypto-rates")
def get_crypto_rates(crypto_currency: str = "bitcoin,ethereum", vs_currencies: str = "usd"):
    # Эндпоинт для получения простых цен
    url = "https://api.coingecko.com/api/v3/simple/price"

    # Параметры: id монет в системе CoinGecko и валюты для перевода
    params = {
        "ids": crypto_currency,
        "vs_currencies": vs_currencies
    }

    try:
        response = requests.get(url, params=params)
        data = response.json()

        return {
            "results": True,
            "data": data
        }
    except Exception as e:
        return {
            "results": False,
            "data": e
        }