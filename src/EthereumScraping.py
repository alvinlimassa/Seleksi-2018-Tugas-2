# import library
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
import json
import time

# variabel global
url_mainpage = "https://etherscan.io/blocks?ps=100&p="
# url file json yang dibuat
url_json = "D:/Kuliah/Tugas CaKru Basdat/Tugas 2/Data/EtheriumData.json"
data = []
# fungsi untuk mendapatkan data pada satu page tertentu

def scrape_item(url):
	try:
		req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
		page = urlopen(req).read()
	except:
		print("MaskExp ERROR!!!")
		return {}
	mainsoup = BeautifulSoup(page,'html.parser')
	table = mainsoup.find('table', attrs={'class':''})
	tableBody = table.find('tbody')
	rows = tableBody.findAll('tr')
	counter = 0
	for row in rows:
		cols = row.findAll('td')
		cols = [ele.text.strip() for ele in cols]
		item = {
			"Miner" : cols[4],
			"Avg.GasPrice" : cols[7],
			"Reward" : cols[8],
			"Time" : cols[1]
		}
		data.append(item)

#program utama
if __name__ == "__main__":
	total = input('Number of page: ')
	pageCount = 0
	while pageCount < int(total):
		pageCount += 1
		scrape_item(url_mainpage + str(pageCount))
		print("Progress = " + str(pageCount) + "/" + total)
		time.sleep(1)
	print("Done")
	# penulisan kedalam json
	with open(url_json,"w") as f:
		json.dump(data,f,indent=4)