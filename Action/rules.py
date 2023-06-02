import requests

Reject_URL = "https://anti-ad.net/domains.txt"

Reject_Rules = requests.get(Reject_URL).text    
r_rules= set([item for item in Reject_Rules.strip().split("\n") if not item.startswith('#')])
reject_text = '\n'.join(r_rules)

with open("./Rules/reject.txt", "w") as f:
    f.write(reject_text)


GFW_URL = "https://raw.githubusercontent.com/Loyalsoldier/clash-rules/release/gfw.txt"
TLD_URL = "https://raw.githubusercontent.com/Loyalsoldier/clash-rules/release/tld-not-cn.txt"
TELEGRAM_URL = "https://raw.githubusercontent.com/Loyalsoldier/clash-rules/release/telegramcidr.txt"



directModule = requests.get("https://raw.githubusercontent.com/GMOogway/shadowrocket-rules/master/sr_direct_list.module").text
proxyModule = requests.get("https://raw.githubusercontent.com/GMOogway/shadowrocket-rules/master/sr_proxy_list.module").text
rejectModule = requests.get("https://raw.githubusercontent.com/GMOogway/shadowrocket-rules/master/sr_reject_list.module").text


with open("./Rules/direct.module", "w") as f:
    f.write(directModule)
with open("./Rules/proxy.module", "w") as f:
    f.write(proxyModule)
with open("./Rules/reject.module", "w") as f:
    f.write(rejectModule)
