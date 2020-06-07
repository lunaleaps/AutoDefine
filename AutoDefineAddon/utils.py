import urllib.error
import urllib.parse
import urllib.request

XML_COLLEGIATE_API_BASE = "http://www.dictionaryapi.com/api/v1/references/collegiate/xml/{word}?key={key}"
XML_MEDICAL_API_BASE = "https://www.dictionaryapi.com/api/references/medical/v2/xml/{word}?key={key}"


class InvalidAPIKeyError(Exception):
    pass


class ResultsNotFoundError(Exception):
    pass


def fetch(url):
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:62.0)'
                                               ' Gecko/20100101 Firefox/62.0'})
    response = urllib.request.urlopen(req).read()
    decoded_response = response.decode("UTF-8")
    if "Invalid API key" in decoded_response:
        raise InvalidAPIKeyError()
    if "Results not found" in decoded_response:
        raise ResultsNotFoundError()
    return response


def create_api(word, key, is_collegiate):
    urlsafe_word = urllib.parse.quote_plus(word)
    if is_collegiate:
        return XML_COLLEGIATE_API_BASE.format(urlsafe_word, key)
    return XML_MEDICAL_API_BASE.format(urlsafe_word, key)
