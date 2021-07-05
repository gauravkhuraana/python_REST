import requests
from assertpy import assert_that
from lxml import etree
from config import BASE_URI_COVID
#from utils.print_helpers import pretty_print 


def test_xmlParsin():
   response = requests.get(f'{BASE_URI_COVID}/api/v1/summary/latest')
   print ("Response is \n",response)

   responseXml=response.text
   print ("ResponseXML is \n",responseXml)

   xmlTree = etree.fromstring(bytes(responseXml, encoding='utf8'))

   totalCases = xmlTree.xpath("//data/summary/total_cases")[0].text
   assert_that(int(totalCases)).is_greater_than(1000000)


def test_AnotherWayToParse():
    response = requests.get(f'{BASE_URI_COVID}/api/v1/summary/latest')

    responseXml = response.text

    xmlTree = etree.fromstring(bytes(responseXml,encoding='utf8'))

    overallCases = int(xmlTree.xpath("//data/summary/total_cases")[0].text)

    searchFor = etree.XPath("//data//regions//total_casse")
    casesByCountry=0

    for region in searchFor(xmlTree):
        casesByCountry += int(region.text)

    assert_that(overallCases).is_greater_than(casesByCountry)
