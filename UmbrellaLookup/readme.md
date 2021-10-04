# Description

Python script that does a recursive lookup through the Cisco Umbrella policies to test for any blocks. 

## Usage

In order to use this script you will need Python3 and you must edit the script with your Authorization Token and your ORG ID as

headers = {
		'Authorization': 'Basic <your authen header',
		'Content-Type': 'application/json',
	}
  
And your ORG ID here

json_data=requests.get('https://management.api.umbrella.com/v1/organizations/<ORG ID> /destinationlists', headers=headers).json()["data"]
and here
destinations = requests.get('https://management.api.umbrella.com/v1/organizations/<ORG ID>/destinationlists/'+str(node_id)+'/destinations', headers=headers).json()["data"]

There are also comments in the code as to where these are
  
### Help

(Burgundy)-(jobs:0)-(/Other - 23 files)
(11:57:33) -> python Umbrella-Policy-Lookup.py -h
usage: Umbrella-Policy-Lookup.py [-h] [--var1 VAR1]

optional arguments:
  -h, --help            show this help message and exit
  --var1 VAR1, -v1 VAR1
                        variable to search
                        
                        
### Example

(Burgundy)-(jobs:0)-(/Other - 23 files)
(11:57:35) -> python Umbrella-Policy-Lookup.py --var1 facebook.com
facebook.com has been blocked in destination list: 9060424
