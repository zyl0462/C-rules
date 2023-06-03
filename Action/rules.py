import requests

######reject_text
Reject1_Rules = requests.get("https://anti-ad.net/domains.txt").text
Reject2_Rules = requests.get("https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Loon/EasyPrivacy/EasyPrivacy_Domain.list").text

r_rules= set([item for item in Reject1_Rules.strip().split("\n") if not item.startswith('#')])
r_rules.update([item for item in Reject2_Rules.strip().split("\n") if not item.startswith('#')])

reject_text = '\n'.join(sorted(r_rules))
del(r_rules)

with open("./Rules/reject.txt", "w") as f:
    f.write(reject_text)
    
######proxy_text
Proxy_Rules = requests.get("https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Loon/Proxy/Proxy_Domain.list").text
Proxy_Rules1 = requests.get("https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Loon/GlobalMedia/GlobalMedia_Domain.list").text
Proxy_Rules2 = requests.get("https://raw.githubusercontent.com/Loyalsoldier/surge-rules/release/gfw.txt").text
Proxy_Rules3 = requests.get("https://raw.githubusercontent.com/Loyalsoldier/surge-rules/release/tld-not-cn.txt").text
p_rules= set([item for item in Proxy_Rules.strip().split("\n") if not item.startswith('#')])
p_rules.update([item for item in Proxy_Rules1.strip().split("\n") if not item.startswith('#')])
p_rules.update([item for item in Proxy_Rules2.strip().split("\n") if not item.startswith('#')])
p_rules.update([item for item in Proxy_Rules3.strip().split("\n") if not item.startswith('#')])
proxy_text = '\n'.join(sorted(p_rules))
del(p_rules)
with open("./Rules/proxy.txt", "w") as f:
    f.write(proxy_text)

######social
Social_Rules = requests.get("https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Loon/Telegram/Telegram_Resolve.list").text
Social_Rules1 = requests.get("https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Loon/OpenAI/OpenAI.list").text
Social_Rules2 = requests.get("https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Loon/Google/Google_Resolve.list").text
s_rules= set([item for item in Social_Rules.strip().split("\n") if not item.startswith('#')])
s_rules.update([item for item in Social_Rules1.strip().split("\n") if not item.startswith('#')])
s_rules.update([item for item in Social_Rules2.strip().split("\n") if not item.startswith('#')])
social_text = '\n'.join(sorted(s_rules))
del(s_rules)
with open("./Rules/social.txt", "w") as f:
    f.write(social_text)
TELEGRAM_rules = requests.get("https://raw.githubusercontent.com/Loyalsoldier/clash-rules/release/telegramcidr.txt").text
with open("./Rules/telegramcidr.yaml", "w") as f:
    f.write(TELEGRAM_rules)

######video
Video_Rules = requests.get("https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Loon/TikTok/TikTok.list").text
Video_Rules1 = requests.get("https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Loon/YouTube/YouTube_Resolve.list").text
v_rules= set([item for item in Video_Rules.strip().split("\n") if not item.startswith('#')])
v_rules.update([item for item in Video_Rules1.strip().split("\n") if not item.startswith('#')])
video_text = '\n'.join(sorted(v_rules))
del(v_rules)
with open("./Rules/video.txt", "w") as f:
    f.write(video_text)

######shadowrocket-rules
proxyModule = requests.get("https://raw.githubusercontent.com/GMOogway/shadowrocket-rules/master/sr_proxy_list.module").text
rejectModule = requests.get("https://raw.githubusercontent.com/GMOogway/shadowrocket-rules/master/sr_reject_list.module").text

with open("./Rules/proxy.module", "w") as f:
    f.write(proxyModule)
with open("./Rules/reject.module", "w") as f:
    f.write(rejectModule)
