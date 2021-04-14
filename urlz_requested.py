import asyncio
from pprint import pprint
from pyppeteer import launch
from pyppeteer.network_manager import NetworkManager
import sys



url_name = input("Enter a FULL domain to scan: ")
print("scanning:" + str(url_name))

input_url_list = ["https://"+url_name]

url_list = input_url_list

refactored_url_list = []

for i in url_list:
    refactored_url_list.append(i.rstrip("\n"))

for url in refactored_url_list:

    request_listing = []

    def logging(event):
        req = event._request
        request_listing.append(req.url)


    async def main():
        browser = await launch({"headless": True})
        page = await browser.newPage()
        page._networkManager.on(NetworkManager.Events.Response, logging)
        await page.goto(url, {'waitUntil': 'networkidle0'})

        await browser.close()


    asyncio.get_event_loop().run_until_complete(main())


from urllib.parse import urlparse


def url_extract(link):
    return urlparse(link).netloc


parsed_urls = []

for url in request_listing:
    parsed_urls.append(url_extract(url))


def pause():
    programPause = input("Press the <ENTER> key to see list of domains that were parsed")
    pprint(parsed_urls)

    sys.stdout = open("test.txt", "w")
    pprint(parsed_urls)
    sys.stdout.close()


pause()

