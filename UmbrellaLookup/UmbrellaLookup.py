import json
import requests
import argparse
from datetime import datetime

if __name__=='__main__':

	headers = {
		'Authorization': 'Basic <AUTHEN>',    #replace <AUTHEN> with your Authentication details
		'Content-Type': 'application/json',
	}
	
	parser = argparse.ArgumentParser()


	parser.add_argument("--var1", "-v1", help="variable to search")

	args = parser.parse_args()
	if args.var1:
		f = open("output.txt", "a")
		json_data=requests.get('https://management.api.umbrella.com/v1/organizations/<ORD-ID>/destinationlists', headers=headers).json()["data"]   #replace <ORG-ID> with your ORG ID. 
		f.write("Umbrella - Policy fetch and parse block lists for: "+args.var1+"\n")
		for node in json_data:
			status="passed"
			node_access=node["access"]
			node_id=node["id"]
			if node_access.lower()=="block":
				destinations = requests.get('https://management.api.umbrella.com/v1/organizations/<ORG-ID> /destinationlists/'+str(node_id)+'/destinations', headers=headers).json()["data"] #replace <ORG-ID>  with your ORG ID. 
				# print("ran 2nd get")
				for destination in destinations:
					if destination["destination"]==args.var1:
						status="blocked"
						print(args.var1+" has been blocked in destination list: "+str(node_id))
						break
				f.write("$Umb.Pol("+str(node_id)+") - "+status+"\n")                #                        ) " +status+" Dest.List ID: "+str(node_id)+"\n")
				#f.write(" "+args.var1+" "+status+" in block "+str(node_id)+"\n")	
		#time.sleep(2)
		f.close()  		
	else:
		print("Missing Variable.")
	
		
			 
