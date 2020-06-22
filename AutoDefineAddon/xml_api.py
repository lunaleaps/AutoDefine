

from xml.etree import ElementTree as ET
from .utils import ParseError


def xml_entries(api_response):
    # can I use non-decoded?
    try:
        etree = ET.fromstring(api_response)
        return etree.findall("entry")
    except(ET.ParseError):
        raise ParseError()
