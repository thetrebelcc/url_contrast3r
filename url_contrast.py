import asyncio
from pprint import pprint

from pyppeteer import launch
from pyppeteer.network_manager import NetworkManager


name = input("Enter a FULL domain to scan: ")
print("scanning:"+ str(name))

list = [name]

url_list = list

clean_url_list = []

for i in url_list:
    clean_url_list.append(i.rstrip("\n"))

for url in clean_url_list:

    request_listing = []
    request_clean = []


    def logit(event):
        req = event._request
        request_listing.append(req.url)


    async def main():
        browser = await launch({"headless": True})
        page = await browser.newPage()
        page._networkManager.on(NetworkManager.Events.Response, logit)
        await page.goto(url, {'waitUntil': 'networkidle0'})

        await browser.close()


    asyncio.get_event_loop().run_until_complete(main())


from urllib.parse import urlparse


def url_extract(link):
    return urlparse(link).netloc


parsed_urls = []

for url in request_listing:
    parsed_urls.append(url_extract(url))



bad_actors = [
		"payment-mastercard.com",
		"google-query.com",
		"google-analytics.top",
		"google-smart.com",
		"google-payment.com",
		"jquery-assets.com",
		"sagepay-live.com",
		"google-query.com",
		"payment-sagepay.com",
		"payment-worldpay.com",
		"124.156.34.157",
		"47.245.55.198",
		"5.53.124.235",
		"jsboxcontents.com",
		"ms-akadns.com",
		"survey-microsoft.net",
		"cnzz.work",
		"45.76.97.191",
		"54.215.230.114",
		"cnzz.space",
		"45.76.97.191",
		"139.180.207.51",
		"202.181.24.14",
		"103.230.122.162",
		"sdsyxwx.com",
        "pixel.quantserve.com"
	]



matches =(set(parsed_urls).intersection(bad_actors))
if_matches = ("**********Mage bad actor detected**************" + str(matches))

if not matches:
    print('No bad actors found')
else:
    print(if_matches)




def pause():
    programPause = input("Press the <ENTER> key to see list of domains that were parsed")
    pprint(parsed_urls)

pause()
