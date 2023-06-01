import requests

directModule = requests.get("https://raw.githubusercontent.com/GMOogway/shadowrocket-rules/master/sr_direct_list.module").text
proxyModule = requests.get("https://raw.githubusercontent.com/GMOogway/shadowrocket-rules/master/sr_proxy_list.module").text
rejectModule = requests.get("https://raw.githubusercontent.com/GMOogway/shadowrocket-rules/master/sr_reject_list.module").text

with open("./Rules/direct.txt", "w") as f:
    f.write(rawDirect)
with open("./Rules/proxy.txt", "w") as f:
    f.write(rawProxy)
with open("./Rules/reject.txt", "w") as f:
    f.write(rawReject)
