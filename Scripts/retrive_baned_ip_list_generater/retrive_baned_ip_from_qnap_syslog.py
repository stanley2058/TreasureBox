# @Author d.f.
# @Date 2022.10.20
# This is a scipt banned ip list from my qnap syslog and others. So I can apply it to my router blacklist.


import csv
 
# final ip set
ips= []        


# --------------------
contents = []
with open("system-log.csv", "r", newline="", encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        # row 是 List 的型態，可以用 print(row[0], row[1], row[2]) 分別取得印出
        contents.append(row[7])

for msg in contents:
    if "ban list" in msg:
        ipstring = msg[msg.find('[',10) +1 : msg.find(']', 10)]
        ips.append(ipstring.strip())

     

yuderfile = open("yuder's-banned-list.txt", "r")
for ip in yuderfile:

    ips.append(ip.strip())
      
ipset = set(ips)  

f = open("ban-ip-list.txt", 'w')
for eachip in ipset:
    f.write(eachip + "\n")

print(ipset)
        
        
