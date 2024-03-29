import requests
from requests import get
import json


class IP:

    # get IP info using https://ipinfo.io/
    def a_ip_check(self, a_record):
        error = None

        try:
            a = a_record[0]
            url = "https://ipinfo.io/{0}".format(a)
            result = requests.get(url)
            # return parsed data using built-in JSON
            dataObj = result.json()
            return dataObj

        except KeyError as err:
            error = "nice try. Please enter a valid ip address and try again."

    # get visitor's ip using https://www.ipify.org/
    #TODO: NEED to update visitor ip retrieval. currently, will provide ip associated with wherever api is being called. 
    def my_ip_check(self):
        my_ip = get('https://api.ipify.org').text
        return my_ip

