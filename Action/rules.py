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
with open("./Rules/reject.txt", "w") as f:
    f.write(reject_text)
del Reject1_Rules,Reject2_Rules,Reject3_Rules,r_rules,reject_text

Proxy_Rules = requests.get("https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Loon/Proxy/Proxy_Domain.list").text
Proxy_Rules1 = requests.get("https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Loon/GlobalMedia/GlobalMedia_Domain.list").text
Proxy_Rules2 = requests.get("https://raw.githubusercontent.com/Loyalsoldier/surge-rules/release/gfw.txt").text
Proxy_Rules3 = requests.get("https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Loon/Global/Global_Domain.list").text
p_rules= set([item for item in Proxy_Rules.strip().split("\n") if not item.startswith('#')])
p_rules.update([item for item in Proxy_Rules1.strip().split("\n") if not item.startswith('#')])
p_rules.update([item for item in Proxy_Rules2.strip().split("\n") if not item.startswith('#')])
p_rules.update([item for item in Proxy_Rules3.strip().split("\n") if not item.startswith('#')])
LEN_proxy = len(p_rules)
proxy_text = '\n'.join(sorted(p_rules))
with open("./Rules/proxy.txt", "w") as f:
    f.write(proxy_text)
del Proxy_Rules,Proxy_Rules1,Proxy_Rules2,Proxy_Rules3,p_rules

p_rules= [item for item in proxy_text.strip().split("\n") if not item.startswith('.')]
p_rules1= [item[1:] for item in proxy_text.strip().split("\n") if  item.startswith('.')]
p_text = ',PROXY\n'.join(p_rules)
p_text1 = ',PROXY\n'.join(p_rules1)
del p_rules,p_rules1
p_rules= [item for item in p_text.strip().split("\n")]
p_rules1= [item for item in p_text1.strip().split("\n")]
p_text = '\nDOMAIN,'.join(sorted(p_rules))
p_text1 = '\nDOMAIN-SUFFIX,'.join(sorted(p_rules1))
del p_rules,p_rules1
p_rules= [item for item in p_text.split("\n")]
p_rules1= [item for item in p_text1.split("\n")]
p_rules.insert(0,'DOMAIN,'+p_rules.pop(0))
p_rules.insert(-1,p_rules.pop()+',PROXY')
p_rules1.insert(0,'DOMAIN-SUFFIX,'+p_rules1.pop(0))
p_rules1.insert(-1,p_rules1.pop()+',PROXY')
p_text ='\n'.join(sorted(p_rules))
p_text1 ='\n'.join(sorted(p_rules1))
with open("./Rules/rproxy.text", "w") as f:
    f.write(p_text + '\n' + p_text1)
del p_rules,p_rules1,p_text,p_text1

Social_Rules = requests.get("https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Loon/Telegram/Telegram_Resolve.list").text
Social_Rules1 = requests.get("https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Loon/OpenAI/OpenAI.list").text
Social_Rules2 = requests.get("https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Loon/Google/Google_Resolve.list").text
s_rules= set([item for item in Social_Rules.strip().split("\n") if not item.startswith('#')])
s_rules.update([item for item in Social_Rules1.strip().split("\n") if not item.startswith('#')])
s_rules.update([item for item in Social_Rules2.strip().split("\n") if not item.startswith('#')])
LEN_social= len(s_rules)
social_text = '\n'.join(sorted(s_rules))
with open("./Rules/social.txt", "w") as f:
    f.write(social_text)
del s_rules,Social_Rules,Social_Rules1,Social_Rules2,social_text

Video_Rules = requests.get("https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Loon/TikTok/TikTok.list").text
Video_Rules1 = requests.get("https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Loon/YouTube/YouTube_Resolve.list").text
v_rules= set([item for item in Video_Rules.strip().split("\n") if not item.startswith('#')])
v_rules.update([item for item in Video_Rules1.strip().split("\n") if not item.startswith('#')])
LEN_video= len(v_rules)
video_text = '\n'.join(sorted(v_rules))
with open("./Rules/video.txt", "w") as f:
    f.write(video_text)
del Video_Rules,Video_Rules1,v_rules,video_text

current_time = '#UTC time: ' + datetime.now().strftime("%Y/%m/%d %H:%M:%S") + '\n'
STR_stat = "reject rules: {}\nproxy rules: {}\nsocial rules: {}\nvideo rules: {}\ntotal rules: {}".format(LEN_reject, LEN_proxy, LEN_social,LEN_video,LEN_reject+LEN_proxy+LEN_social+LEN_video)
with open("./stat.dat", "w") as f:
    f.write(current_time + STR_stat)

Social_Rules = requests.get("https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Clash/Telegram/Telegram.yaml").text
Social_Rules1 = requests.get("https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Clash/OpenAI/OpenAI.yaml").text
Social_Rules2 = requests.get("https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Clash/Google/Google.yaml").text
s_rules= set([item for item in Social_Rules.strip().split("\n") if not (item.startswith('#') or item.startswith('payload:'))])
s_rules.update([item for item in Social_Rules1.strip().split("\n") if not (item.startswith('#') or item.startswith('payload:'))])
s_rules.update([item for item in Social_Rules2.strip().split("\n") if not (item.startswith('#') or item.startswith('payload:'))])
social_text = '\n'.join(sorted(s_rules))
with open("./Rules/social.yaml", "w") as f:
    f.write('payload:\n'+social_text)
del Social_Rules,Social_Rules1,Social_Rules2,s_rules,social_text

Video_Rules = requests.get("https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Clash/YouTube/YouTube.yaml").text
Video_Rules1 = requests.get("https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Clash/TikTok/TikTok.yaml").text
v_rules= set([item for item in Video_Rules.strip().split("\n") if not (item.startswith('#') or item.startswith('payload:'))])
v_rules.update([item for item in Video_Rules.strip().split("\n") if not (item.startswith('#') or item.startswith('payload:'))])
video_text = '\n'.join(sorted(v_rules))
with open("./Rules/video.yaml", "w") as f:
    f.write('payload:\n'+video_text)
del Video_Rules,Video_Rules1,v_rules,video_text
