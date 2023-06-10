import requests
from datetime import datetime

Reject1_Rules = requests.get("https://anti-ad.net/domains.txt").text
Reject2_Rules = requests.get("https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Loon/EasyPrivacy/EasyPrivacy_Domain.list").text
Reject3_Rules = requests.get("https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Loon/AdGuardSDNSFilter/AdGuardSDNSFilter_Domain.list").text
r_rules= set([item for item in Reject1_Rules.strip().split("\n") if not item.startswith('#')])
r_rules.update([item for item in Reject2_Rules.strip().split("\n") if not item.startswith('#')])
r_rules.update([item for item in Reject3_Rules.strip().split("\n") if not item.startswith('#')])
LEN_reject = len(r_rules)

reject_text = '\n'.join(sorted(r_rules))
del(r_rules)
with open("./Rules/reject.txt", "w") as f:
    f.write(reject_text)

Social_Rules = requests.get("https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Loon/Telegram/Telegram_Resolve.list").text
Social_Rules1 = requests.get("https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Loon/OpenAI/OpenAI.list").text
Social_Rules2 = requests.get("https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Loon/Google/Google_Resolve.list").text
s_rules= set([item for item in Social_Rules.strip().split("\n") if not item.startswith('#')])
s_rules.update([item for item in Social_Rules1.strip().split("\n") if not item.startswith('#')])
s_rules.update([item for item in Social_Rules2.strip().split("\n") if not item.startswith('#')])
LEN_social= len(s_rules)

social_text = '\n'.join(sorted(s_rules))
#del(s_rules)
with open("./Rules/social.txt", "w") as f:
    f.write(social_text)
TELEGRAM_rules = requests.get("https://raw.githubusercontent.com/Loyalsoldier/clash-rules/release/telegramcidr.txt").text
with open("./Rules/telegramcidr.yaml", "w") as f:
    f.write(TELEGRAM_rules)

Video_Rules = requests.get("https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Loon/TikTok/TikTok.list").text
Video_Rules1 = requests.get("https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Loon/YouTube/YouTube_Resolve.list").text
v_rules= set([item for item in Video_Rules.strip().split("\n") if not item.startswith('#')])
v_rules.update([item for item in Video_Rules1.strip().split("\n") if not item.startswith('#')])
LEN_video= len(v_rules)

video_text = '\n'.join(sorted(v_rules))
#del(v_rules)
with open("./Rules/video.txt", "w") as f:
    f.write(video_text)

Proxy_Rules = requests.get("https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Loon/Proxy/Proxy_Domain.list").text
Proxy_Rules1 = requests.get("https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Loon/GlobalMedia/GlobalMedia_Domain.list").text
Proxy_Rules2 = requests.get("https://raw.githubusercontent.com/Loyalsoldier/surge-rules/release/gfw.txt").text
Proxy_Rules3 = requests.get("https://raw.githubusercontent.com/Loyalsoldier/surge-rules/release/tld-not-cn.txt").text
p_rules= set([item for item in Proxy_Rules.strip().split("\n") if not item.startswith('#')])
p_rules.update([item for item in Proxy_Rules1.strip().split("\n") if not item.startswith('#')])
p_rules.update([item for item in Proxy_Rules2.strip().split("\n") if not item.startswith('#')])
p_rules.update([item for item in Proxy_Rules3.strip().split("\n") if not item.startswith('#')])
p_rules.__isub__(s_rules)
p_rules.__isub__(v_rules)
LEN_proxy = len(p_rules)

proxy_text = '\n'.join(sorted(p_rules))
del(p_rules)
del(s_rules)
del(v_rules)
with open("./Rules/proxy.txt", "w") as f:
    f.write(proxy_text)

p_rules= [item for item in proxy_text.strip().split("\n") if not item.startswith('.')]
p_rules1= [item[1:] for item in proxy_text.strip().split("\n") if  item.startswith('.')]
p_text = ',PROXY\n'.join(p_rules)
p_text1 = ',PROXY\n'.join(p_rules1)
del(p_rules)
del(p_rules1)
p_rules= [item for item in p_text.strip().split("\n")]
p_rules1= [item for item in p_text1.strip().split("\n")]
p_text = '\nDOMAIN,'.join(sorted(p_rules))
p_text1 = '\nDOMAIN-SUFFIX,'.join(sorted(p_rules1))
del(p_rules)
del(p_rules1)
p_rules= [item for item in p_text.split("\n")]
p_rules1= [item for item in p_text1.split("\n")]
p_rules.insert(0,'DOMAIN,'+p_rules.pop(0))
p_rules.insert(-1,p_rules.pop()+',PROXY')
p_rules1.insert(0,'DOMAIN-SUFFIX,'+p_rules1.pop(0))
p_rules1.insert(-1,p_rules1.pop()+',PROXY')

p_text ='\n'.join(sorted(p_rules))
p_text1 ='\n'.join(sorted(p_rules1))
del(p_rules)
del(p_rules1)

with open("./Rules/rproxy.text", "w") as f:
    f.write(p_text + '\n' + p_text1)

current_time = '#UTC time: ' + datetime.now().strftime("%Y/%m/%d %H:%M:%S") + '\n'
STR_stat = "reject rules: {}\nproxy rules: {}\nsocial rules: {}\nvideo rules: {}\ntotal rules: {}".format(LEN_reject, LEN_proxy, LEN_social,LEN_video,LEN_reject+LEN_proxy+LEN_social+LEN_video)
with open("./Rules/stat.dat", "w") as f:
    f.write(current_time + STR_stat)
