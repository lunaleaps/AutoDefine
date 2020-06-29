import json
from itertools import chain
import re


WAV_AUDIO_LINK = "https://media.merriam-webster.com/audio/prons/en/us/wav/{subdir}/{audio}.wave"


def json_entries(api_response):
    return json.loads(api_response)


def valid_entries(entries):
    return filter(lambda entry: get_word_from_id(entry['meta']['id']) == WORD, data)


def subdirectory(audio):
    if audio.startswith('bix'):
        return 'bix'
    if audio.startswith('gg'):
        return 'gg'

    first_letter = audio[0]
    if not first_letter.isalpha():
        return 'number'
    return first_letter


def wav_audio_link_for_entry(entry):
    try:
        audio = entry['hwi']['prs']['sound']
    except KeyError:
        return None

    subdir = subdirectory(audio)
    return WAV_AUDIO_LINK.format(subdir=subdir, audio=audio)


def get_word_from_id(id):
    return id.split(':')[0]


def phonetic_transcription(entry):
    try:
        transcription = entry['prs']['mw']
        part_of_speech = entry['fl']
    except KeyError:
        return None
    return f'<b>{part_of_speech}</b> \\{transcription}\\'


def get_functional_label(entry):
    return entry['fl']


DEFINITION_KEY = 'dt'


def get_definitions_array(value):
    if value is None or (isinstance(value, dict) is False and isinstance(value, list) is False):
        return []

    if isinstance(value, list):
        dt = []
        for item in value:
            dt.extend(get_definitions_array(item))
        return dt
    if isinstance(value, dict):
        dt = []
        if DEFINITION_KEY in value:
            dt = (list(map(lambda text_df: text_df[1], filter(lambda dt: dt[0] == 'text', value[DEFINITION_KEY]))))

        rest = []
        for (_key, _value) in value.items():
            if _key != DEFINITION_KEY:
                rest.extend(get_definitions_array(_value))
        return dt + rest


def get_definition(entry):
    entry_def = entry['def']
    definitions = get_definitions_array(entry_def)
    definition = '\n'.join(definitions)
    definition = handle_formatting(definition)
    # definition = handle_cross_ref(definition)
    return definition


def handle_formatting(definition_str):
    def_str = re.sub(r'\{b\}([^{]+)\{\\\/b\}', r'<b>\1</b>', definition_str)
    def_str = re.sub(r'\{sup\}([^{]+)\{\\\/sup\}', r'<sup>\1</sup>', def_str)
    def_str = re.sub(r'\{inf\}([^{]+)\{\\\/inf\}', r'<sub>\1</sub>', def_str)
    def_str = def_str.replace('{bc}', ': ')
    return def_str
