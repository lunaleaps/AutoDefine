import urllib.error
import urllib.parse
import urllib.request


class InvalidAPIKeyError(Exception):
    pass


class ResultsNotFoundError(Exception):
    pass


def fetch(url):
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:62.0)'
                                               ' Gecko/20100101 Firefox/62.0'})
    response = urllib.request.urlopen(req).read()
    decoded_response = returned.decode("UTF-8")
    if "Invalid API key" in decoded_response:
        raise InvalidAPIKeyError()
    if "Results not found" in decoded_response:
        raise ResultsNotFoundError()
    return response
