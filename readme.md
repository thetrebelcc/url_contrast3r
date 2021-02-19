# url_contrast3r

url_contrast3r is a python script that compares requested URLs against a list of domains to see if there are any matching elements. 

## Installation

```bash
pip install asyncio
pip install pyppeteer
```

## Usage

```python
Enter a FULL domain to scan: https://example.com/

This will scan https://example.com/ against the bad_actors list in the url_contrast.py app.

If a match is found an alert will show. 
```

## Next Steps
* Add a dynamic way to change urls to scan.
* Make terminal workflow easier to use. 
* Update bad actors list. 
* Save results as a txt file. 
## License
[MIT](https://choosealicense.com/licenses/mit/)
