import json
import requests

class RequestError(Exception): ...
class UserError(Exception): ...
class WrongFormat(UserError): ...
class WrongSym(UserError): ...

class Convertion():
    @staticmethod
    def get_price(base, quote, num):
        r = requests.get(f"https://min-api.cryptocompare.com/data/price?fsym={base}&tsyms={quote}")
        if r.status_code >= 400:
            raise RequestError(f"HTTPError: {r.status_code}")
        else:
            data = json.loads(r.content)
            converted = float(data[quote])*float(num)
            return converted