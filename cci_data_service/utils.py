# pylint: disable=W0311
import requests



def create_query(queryObj):
   queryObj.coords['coverage'] = queryObj.coverage
   _q = queryObj.template.format(**queryObj.coords)
   return _q


def web_post(url, payload):
   return requests.post(url, data=payload).text

def web_post_file(url, payload):
   return requests.post(url, data=payload).content

