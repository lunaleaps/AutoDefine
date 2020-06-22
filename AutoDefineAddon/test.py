import urllib.error
import urllib.parse
import urllib.request
# from xml.etree import ElementTree as ET
import json

XML_COLLEGIATE_API_BASE = "http://www.dictionaryapi.com/api/v1/references/collegiate/xml/{word}?key={key}"
JSON_API = "https://www.dictionaryapi.com/api/v3/references/collegiate/json/{word}?key={key}"
KEY = "99ca71e6-f544-4f2e-8b88-fdbbc301c013"
WORD = "volume"

WAV_AUDIO_LINK = "https://media.merriam-webster.com/audio/prons/en/us/wav/{subdir}/{audio}.wave"
# if audio begins with "bix", the subdirectory should be "bix",
# if audio begins with "gg", the subdirectory should be "gg",
# if audio begins with a number or punctuation (eg, "_"), the subdirectory should be "number",
# otherwise, the subdirectory is equal to the first letter of audio.


def subdirectory(audio):
    if audio.startswith('bix'):
        return 'bix'
    if audio.startswith('gg'):
        return 'gg'

    first_letter = audio[0]
    if not first_letter.isalpha():
        return 'number'
    return first_letter


def audio_link(audio):
    subdir = subdirectory(audio)
    return WAV_AUDIO_LINK.format(subdir=subdir, audio=audio)


def get_word_from_id(id):
    return id.split(':')[0]


if __name__ == "__main__":
    url = JSON_API.format(key=KEY, word=WORD)
    # url = XML_COLLEGIATE_API_BASE.format(word="voluminous", key=KEY)
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:62.0)'
                                               ' Gecko/20100101 Firefox/62.0'})
    response = urllib.request.urlopen(req).read().decode('UTF-8')
    entries = json.loads(response)
    # print(data)

    valid_entries = filter(lambda entry: get_word_from_id(entry['meta']['id']) == WORD, data)

    # print(valid_entries)
    # etree = ET.fromstring(response)
    # print(etree.findall("entry"))
    # decoded_response = response.decode("UTF-8")
    # if "Invalid API key" in decoded_response:
    #     raise InvalidAPIKeyError()
    # if "Results not found" in decoded_response:
    #     raise ResultsNotFoundError()

    # return response
