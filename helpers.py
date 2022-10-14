from urllib.request import urlopen
import json

def get_categories():
	url = "https://2wf0rg.deta.dev/api/categories/"
	response = urlopen(url)
	data_json = json.loads(response.read())
	return data_json

def get_cards(skip=0, top=9):
	url = "https://2wf0rg.deta.dev/api/cards/?skip="+str(skip)+"&top="+str(top)
	response = urlopen(url)
	data_json = json.loads(response.read())
	return data_json

def get_next(to_skip=0):
	url = "https://2wf0rg.deta.dev/api/cards/?skip="+str(to_skip)+"&top=1"
	response = urlopen(url)
	data_json = json.loads(response.read())
	if len(data_json) > 0:
		return True
	return False