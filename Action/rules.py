import requests

Reject1_Rules = requests.get("https://anti-ad.net/domains.txt").text
Reject2_Rules = requests.get("https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Loon/EasyPrivacy/EasyPrivacy_Domain.list").text

r_rules= set([item for item in Reject1_Rules.strip().split("\n") if not item.startswith('#')])
r_rules.update([item for item in Reject2_Rules.strip().split("\n") if not item.startswith('#')])

reject_text = '\n'.join(sorted(r_rules))
del(r_rules)

with open("./Rules/reject.txt", "w") as f:
    f.write(reject_text)

Proxy_Rules = requests.get("https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Loon/Proxy/Proxy_Domain.list").text
#Proxy_Rules1 = requests.get("https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Loon/Global/Global_Domain.list").text
Proxy_Rules3 = requests.get("https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Loon/GlobalMedia/GlobalMedia_Domain.list").text
Proxy_Rules1 = requests.get("https://raw.githubusercontent.com/Loyalsoldier/surge-rules/release/gfw.txt").text
#Proxy_Rules1 = requests.get("https://raw.githubusercontent.com/Loyalsoldier/surge-rules/release/proxy.txt").text
Proxy_Rules2 = requests.get("https://raw.githubusercontent.com/Loyalsoldier/surge-rules/release/tld-not-cn.txt").text

p_rules= set([item for item in Proxy_Rules.strip().split("\n") if not item.startswith('#')])
p_rules.update([item for item in Proxy_Rules1.strip().split("\n") if not item.startswith('#')])
p_rules.update([item for item in Proxy_Rules2.strip().split("\n") if not item.startswith('#')])
p_rules.update([item for item in Proxy_Rules3.strip().split("\n") if not item.startswith('#')])
#p_rules.update([item for item in Proxy_Rules4.strip().split("\n") if not item.startswith('#')])
#p_rules.update([item for item in Proxy_Rules5.strip().split("\n") if not item.startswith('#')])

proxy_text = '\n'.join(sorted(p_rules))
del(p_rules)

with open("./Rules/proxy.txt", "w") as f:
    f.write(proxy_text)

GFW_rules = requests.get("https://raw.githubusercontent.com/Loyalsoldier/clash-rules/release/gfw.txt").text  
TLD_rules = requests.get("https://raw.githubusercontent.com/Loyalsoldier/clash-rules/release/tld-not-cn.txt").text  
TELEGRAM_rules = requests.get("https://raw.githubusercontent.com/Loyalsoldier/clash-rules/release/telegramcidr.txt").text

c_rules= set([item for item in GFW_rules.split("\n") if not (item.startswith('#') or item.startswith('payload:'))])
c_rules.update([item for item in TLD_rules.split("\n") if not (item.startswith('#') or item.startswith('payload:'))])
lists = sorted(c_rules)
lists.insert(0,'payload:')
c_text = '\n'.join(lists)

del(c_rules)
lists.clear()

with open("./Rules/proxy.yaml", "w") as f:
    f.write(c_text)
with open("./Rules/telegramcidr.yaml", "w") as f:
    f.write(TELEGRAM_rules)

directModule = requests.get("https://raw.githubusercontent.com/GMOogway/shadowrocket-rules/master/sr_direct_list.module").text
proxyModule = requests.get("https://raw.githubusercontent.com/GMOogway/shadowrocket-rules/master/sr_proxy_list.module").text
rejectModule = requests.get("https://raw.githubusercontent.com/GMOogway/shadowrocket-rules/master/sr_reject_list.module").text


with open("./Rules/direct.module", "w") as f:
    f.write(directModule)
with open("./Rules/proxy.module", "w") as f:
    f.write(proxyModule)
with open("./Rules/reject.module", "w") as f:
    f.write(rejectModule)
