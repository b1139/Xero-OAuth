"""
Description: Common function are available here for the application
"""

import requests
import xmltodict
import json


def send_get_request(url, params=None, headers=None):
    """
    Process the Get Request throughout the application
    :param url: URL
    :param params: Data to bind
    :param headers: Header
    :return: response object
    """

    return requests.get(url=url, params=params, headers=headers)


def send_post_request(url, data=None, headers=None):
    """
    Process the POST Request throughout the application
    :param url: URL
    :param data: Data to bind
    :param headers: Header
    :return: response object
    """

    return requests.post(url=url, data=data, headers=headers)


def send_put_request(url, data=None, headers=None):
    """
    Process the PUT Request throughout the application
    :param url: URL
    :param data: Data to bind
    :param headers: Header
    :return: response object
    """

    return requests.put(url=url, data=data, headers=headers)


def parse_xml(xml_string):
    """
    Parses xml string ot Dict
    :param xml_string:
    :return: Dictonary
    """
    data_dict = json.loads(json.dumps(xmltodict.parse(xml_string)))
    return data_dict