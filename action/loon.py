import requests

rawDirect = requests.get("https://raw.githubusercontent.com/Code-Dramatist/Rule_Actions/main/Direct_Rule/Direct_Rule.rule").text
rawProxy = requests.get("https://raw.githubusercontent.com/Code-Dramatist/Rule_Actions/main/Proxy_Rule/Proxy_Rule.rule").text
rawReject = requests.get("https://raw.githubusercontent.com/Code-Dramatist/Rule_Actions/main/Reject_Rule/Reject_Rule.rule").text

with open("./Loon/direct.txt", "w") as f:
    f.write(rawDirect)

with open("./Loon/proxy.txt", "w") as f:
    f.write(rawProxy)

with open("./Loon/reject.txt", "w") as f:
    f.write(rawReject)
