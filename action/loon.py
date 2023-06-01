import requests

rawDirect = requests.get("https://raw.githubusercontent.com/Code-Dramatist/Rule_Actions/main/Direct_Rule/Direct_Rule.rule").text
rawProxy = requests.get("https://raw.githubusercontent.com/Code-Dramatist/Rule_Actions/main/Proxy_Rule/Proxy_Rule.rule").text
rawReject = requests.get("https://raw.githubusercontent.com/Code-Dramatist/Rule_Actions/main/Reject_Rule/Reject_Rule.rule").text

result = list()
for rawresult in rawDirect:
    result.extend([item for item in rawresult.split("\n") if not item.startswith('#')])
result_text = '\n'.join(result)

with open("./direct.txt", "w") as f:
    f.write("\n".join(result))
 
result.clear()

for rawresult in rawProxy:
    result.extend([item for item in rawresult.split("\n") if not item.startswith('#')])
result_text = '\n'.join(result)

with open("./proxy.txt", "w") as f:
    f.write("\n".join(result))
 
result.clear()

for rawresult in rawReject:
    result.extend([item for item in rawresult.split("\n") if not item.startswith('#')])
result_text = '\n'.join(result)

with open("./reject.txt", "w") as f:
    f.write("\n".join(result))
 
result.clear()

