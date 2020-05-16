from apikeys import CC_API_KEY
"""
Documentation:
https://min-api.cryptocompare.com/documentation?key=Historical&cat=dataHistohour
"""
# https://min-api.cryptocompare.com/data/v4/all/exchanges
# https://min-api.cryptocompare.com/data/v2/cccagg/pairs
# daily and hourly
# http://www.cryptodatadownload.com/data/northamerican/

# TODO we have to page through 2000 at a time
url = "https://min-api.cryptocompare.com/data/v2/histohour?fsym=BTC&tsym=USD&limit=2000"
url += "&api_key=" + CC_API_KEY