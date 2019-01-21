# import Modules
import urllib3
from bs4 import BeautifulSoup as Bs

#Disable warnings for certificates
urllib3.disable_warnings()

# Variables
yourl = "http://apod.nasa.gov/apod/astropix.html"


# Connect()
def connect(yourl):
    http = urllib3.PoolManager()
    resp = http.request('GET', yourl)
    soup = Bs(resp.data, 'html.parser')
    return http, resp, soup


# Identify
def identify_image(soup):
    durl = "http://apod.nasa.gov/apod/" + soup.find("img").parent.get("href")
    image_name = durl.split("/")[-1]
    return image_name, durl


# Save
def save_image(image_name, durl, resp, http):
    os_loc = 'C:/Users/brian/Pictures/Nasa' + '/' + image_name
    image = open(os_loc, 'wb')
    resp = http.request('GET', durl)
    image.write(resp.data)


# Close
def close_conn(resp):
    resp.close()
    resp.release_conn()


http, resp, soup = connect(yourl)
image_name, durl = identify_image(soup)
save_image(image_name, durl, resp, http)
close_conn(resp)


