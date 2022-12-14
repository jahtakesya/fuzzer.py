import requests,argparse, concurrent, builtwith, sys
import simple_colors as c
from concurrent.futures import ThreadPoolExecutor

parser = argparse.ArgumentParser()
parser.add_argument('--url', type=str, required=True)
parser.add_argument('-w', '--wordlist', default=None, required=False)
parser.add_argument('-t', '--threads', default=20, type=int, required=False)
parser.add_argument('-hc', '--hide404', action='store_true')
parser.add_argument('-rh', '--headers', action='store_false')
parser.add_argument('--enum', action='store_false')
args = parser.parse_args()

url = args.url
filename = args.wordlist
threads = args.threads
hideStatusCode = args.hide404
rHeaders = args.headers
techID = args.enum
	
if rHeaders == True and filename == None:
	r = requests.get(url)
	print(c.magenta(r.headers))
	sys.exit(0)
if techID == True and filename == None:
	print(c.magenta(builtwith.parse(url)))
	sys.exit(0)
else:
	pass

f = open(filename)
def request(f):
	r = requests.get(f'{url}/{f}/')
	sc = r.status_code
	if hideStatusCode == True:
		if sc == 200:
			print(c.green("[*] " + str(sc) + " " + url + "/" +  f, ['underlined', 'bright', 'italic']))
		else:
			pass
	else:
		if sc == 200:
			print(c.green("[*] " + str(sc) + " " + url + "/" +  f, ['underlined', 'bright', 'italic']))
		else:
			print(c.red("[*] " + str(sc) + " " + url + "/" + f, ['italic', 'dim']))

with ThreadPoolExecutor(max_workers=threads) as executor:
	future_to_url = {executor.submit(request, i)
	for i in f}