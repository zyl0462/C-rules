import requests

Reject1_Rules = requests.get("https://anti-ad.net/domains.txt").text
Reject2_Rules = requests.get("https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Loon/EasyPrivacy/EasyPrivacy_Domain.list").text

r_rules1= set([item for item in Reject1_Rules.strip().split("\n") if not item.startswith('#')])
r_rules2= set([item for item in Reject2_Rules.strip().split("\n") if not item.startswith('#')])

r_rules = r_rules1.union(r_rules2)
del(r_rules1)
del(r_rules2)
reject_text = '\n'.join(sorted(r_rules))
with open("./Rules/reject.txt", "w") as f:
    f.write(reject_text)

del(r_rules)


GFW_rules = requests.get("https://raw.githubusercontent.com/Loyalsoldier/surge-rules/release/ruleset/gfw.txt").text  
TLD_rules = requests.get("https://raw.githubusercontent.com/Loyalsoldier/surge-rules/release/ruleset/tld-not-cn.txt").text  
TELEGRAM_rules = requests.get("https://raw.githubusercontent.com/Loyalsoldier/surge-rules/release/ruleset/telegramcidr.txt").text  



directModule = requests.get("https://raw.githubusercontent.com/GMOogway/shadowrocket-rules/master/sr_direct_list.module").text
proxyModule = requests.get("https://raw.githubusercontent.com/GMOogway/shadowrocket-rules/master/sr_proxy_list.module").text
rejectModule = requests.get("https://raw.githubusercontent.com/GMOogway/shadowrocket-rules/master/sr_reject_list.module").text


with open("./Rules/direct.module", "w") as f:
    f.write(directModule)
with open("./Rules/proxy.module", "w") as f:
    f.write(proxyModule)
with open("./Rules/reject.module", "w") as f:
    f.write(rejectModule)
