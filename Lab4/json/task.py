import json
f = open("sample.json")#opening the sample json file
print("Interface Status")
print("================================================================================")
print("DN                                                 Description           Speed    MTU  ")
print("-------------------------------------------------- --------------------  ------  ------")
link = json.load(f)#loading the data
cnt = 0 #creating a counter to output the data
for i in link["imdata"]: #running a cycle in imdata dict
    if cnt == 18:
        break
    print(i["l1PhysIf"]["attributes"]["dn"] + '                               ' + i["l1PhysIf"]["attributes"]["fecMode"] + '   ' + i["l1PhysIf"]["attributes"]["mtu"])
    cnt+=1