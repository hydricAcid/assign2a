import sys
import re

print('Number of arguments:', len(sys.argv), 'arguments.')
print('Argument List:', str(sys.argv))
filename = sys.argv[1]

country_map = {}

with open(filename) as f:
    for line in f:
        content = line.strip()
        if content == "Nodes:":
            reading = "nodes"
        if content == "Edges:":
            reading = "edges"
        if reading == "nodes":
   #         contentStart = re.search("^.:\s", content)
            nodex = re.search("\(.,", content)
            cleanx = nodex.group
            if nodex: 
                print("node x: " + nodex.group())
            nodey = re.search(",.$", content)
        
            if nodey: 
                print("node y: " + nodey.group())
    #        if contentStart:
  #              print(contentStart.string)

        

    
        
            
        
#print(country_map)
        
