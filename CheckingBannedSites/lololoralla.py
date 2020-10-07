from urllib.parse import urlparse
import socket


URLS = []
domains = []
IPs = []
with open("register.txt", encoding="utf-8") as f:
    while True:
        string = f.readline()[:-1]
        if string == " " or string == "":
            break
        buffer = list(string.split(";"))
        if "," in buffer[1]:
            URLS.append(list(buffer[1].split(",")))
        else:
            URLS.append(buffer[1])
        if "," in buffer[2]:
            domains.append(list(buffer[2].split(",")))
        else:
            domains.append(buffer[2])
        if "," in buffer[3]:
            IPs.append(list(buffer[3].split(",")))
        else:
            IPs.append(buffer[3])

strType = type("str")
listType = type(URLS)
URLFound = False
domainFound = False
IPFound = False
userURL = ""
while True:
    print("Enter your URL:", end=" ")
    userURL = input()
    userURL = userURL.strip(" ")
    protocol_index = userURL.index("://")
    protocol = userURL[:protocol_index + 3]
    if protocol_index != -1:
        if protocol == "http://" or protocol == "nttp://" or \
           protocol == "ftp://" or protocol == "file://" or \
           protocol == "about://" or protocol == "https://":
            break
userDomain = urlparse(userURL).netloc
userIP = ""
try:
    userIP = socket.gethostbyname(userDomain)
except BaseException:
    userIP = ""
for i in URLS:
    if type(i) == strType:
        if userURL == i:
            URLFound = True
            break
    elif type(i) == listType:
        for j in i:
            if userURL == j:
                URLFound = True
                break
for i in domains:
    if type(i) == strType:
        if userDomain == i:
            domainFound = True
            break
    elif type(i) == listType:
        for j in i:
            if userDomain == j:
                domainFound = True
for i in IPs:
    if type(i) == strType:
        if userIP == i:
            IPFound = True
            break
    elif type(i) == listType:
        for j in i:
            if userIP == j:
                IPFound = True
                break
print(userURL + " was found: " + str(URLFound))
print(userDomain + " was found: " + str(domainFound))
print(userIP + " was found: " + str(IPFound))