# a commandline utility script that uses urllib to consume an api that returns
# xml dataset. The dataset is iterated through and all <pt> tags are printed.
import sys
import urllib.request as url
from xml.etree.ElementTree import XML

if len(sys.argv) != 3:
    SystemExit('Usage: Nextbus route stopid')
route = sys.argv[2]
stopid = sys.argv[1]

u = url.urlopen('http://ctabustracker.com/bustime/map/getStopPredictions.jsp?stop={}&route={}'.format(stopid, route))

# reading the returned dataset from the api
data = u.read()

doc = XML(data)
#iterating through all <pt> tags in the returned dataset and printing their values.
for pt in doc.findall('.//pt'):
    print(pt.text)