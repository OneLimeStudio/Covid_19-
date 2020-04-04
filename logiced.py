import json


data = {}
data['main_data'] = []
doto = []




def logic(sp):
	for i in sp.select("#maincounter-wrap"):
		data['main_data'].append(i.text)



	with open('data.txt', 'w') as outfile:
	    json.dump(data, outfile)
	    #time.sleep(15)

	with open('data.txt') as inFile:
	    load_data = json.load(inFile)
	    for n in load_data['main_data']:
	    	#print(n)
	    	doto.append(n)

	    #time.sleep(15)		


