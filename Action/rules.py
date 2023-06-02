import requests

Reject_URL = "https://anti-ad.net/surge2.txt"

GFW_URL = "https://raw.githubusercontent.com/Loyalsoldier/clash-rules/release/gfw.txt"
TLD_URL = "https://raw.githubusercontent.com/Loyalsoldier/clash-rules/release/tld-not-cn.txt"
TELEGRAM_URL = "https://raw.githubusercontent.com/Loyalsoldier/clash-rules/release/telegramcidr.txt"

directRule = requests.get("https://raw.githubusercontent.com/Code-Dramatist/Rule_Actions/main/Direct_Rule/Direct_Rule.rule").text
proxyRule = requests.get("https://raw.githubusercontent.com/Code-Dramatist/Rule_Actions/main/Proxy_Rule/Proxy_Rule.rule").text
rejectRule = requests.get("https://raw.githubusercontent.com/Code-Dramatist/Rule_Actions/main/Reject_Rule/Reject_Rule.rule").text


directModule = requests.get("https://raw.githubusercontent.com/GMOogway/shadowrocket-rules/master/sr_direct_list.module").text
proxyModule = requests.get("https://raw.githubusercontent.com/GMOogway/shadowrocket-rules/master/sr_proxy_list.module").text
rejectModule = requests.get("https://raw.githubusercontent.com/GMOogway/shadowrocket-rules/master/sr_reject_list.module").text

with open("./Rules/Loon/direct.txt", "w") as f:
    f.write(directRule)
with open("./Rules/Loon/proxy.txt", "w") as f:
    f.write(proxyRule)
with open("./Rules/Loon/reject.txt", "w") as f:
    f.write(rejectRule)

with open("./Rules/Rocket/direct.module", "w") as f:
    f.write(directModule)
with open("./Rules/Rocket/proxy.module", "w") as f:
    f.write(proxyModule)
with open("./Rules/Rocket/reject.module", "w") as f:
    f.write(rejectModule)
