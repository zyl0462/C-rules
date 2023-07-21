import requests
from datetime import datetime

def get_text(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.text.strip().split("\n")
    except requests.exceptions.RequestException as he:
        print("Error fetching content:", he)
    except Exception as e
        print("Error content:", e)
    finally:
        return None

Reject_Rules = get_text("https://anti-ad.net/domains.txt")
Reject_Rules1 = get_text("https://raw.githubusercontent.com/Cats-Team/AdRules/main/ad-domains.txt").lower()
Reject_Rules2 = get_text("https://adguardteam.github.io/AdGuardSDNSFilter/Filters/filter.txt")
r_rules= set([item for item in Reject_Rules if not (item.startswith('#') or item.startswith('!'))])
r_rules.update([item for item in Reject_Rules1 if not (item.startswith('#') or item.startswith('!'))])
r_rules.update([item[2:-1] for item in Reject_Rules2 if (item.startswith('||') and item.endswith('^'))])
LEN_reject = len(r_rules)
reject_text = '\n'.join(sorted(r_rules))
with open("./Rules/reject.txt", "w",encoding='utf-8') as f:
    f.write(reject_text)
del Reject_Rules,Reject_Rules1,Reject_Rules2,r_rules,reject_text

Proxy_Rules = get_text("https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Loon/Proxy/Proxy_Domain.list")
Proxy_Rules1 = get_text("https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Loon/GlobalMedia/GlobalMedia_Domain.list")
Proxy_Rules2 = get_text("https://raw.githubusercontent.com/Loyalsoldier/surge-rules/release/gfw.txt")
p_rules= set([item for item in Proxy_Rules if not item.startswith('#')])
p_rules.update([item for item in Proxy_Rules1 if not item.startswith('#')])
p_rules.update([item for item in Proxy_Rules2 if not item.startswith('#')])
LEN_proxy = len(p_rules)
proxy_text = '\n'.join(sorted(p_rules))
with open("./Rules/proxy.txt", "w",encoding='utf-8') as f:
    f.write(proxy_text)
del Proxy_Rules,Proxy_Rules1,Proxy_Rules2,p_rules

p_rules= [('DOMAIN,' + item + ',PROXY') for item in proxy_text.strip().split("\n") if not item.startswith('.')]
p_rules.extend([('DOMAIN-SUFFIX,'+ item[1:] + ',PROXY') for item in proxy_text.strip().split("\n") if item.startswith('.')])
p_text ='\n'.join(sorted(p_rules))
with open("./Rules/rproxy.txt", "w",encoding='utf-8') as f:
    f.write(p_text)
del p_rules, proxy_text, p_text

Social_Rules = get_text("https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Loon/Telegram/Telegram.list")
Social_Rules1 = get_text("https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Loon/OpenAI/OpenAI.list")
Social_Rules2 = get_text("https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Loon/Google/Google.list")
s_rules= set([item for item in Social_Rules if not item.startswith('#')])
s_rules.update([item for item in Social_Rules1 if not item.startswith('#')])
s_rules.update([item for item in Social_Rules2 if not item.startswith('#')])
LEN_social= len(s_rules)
social_text = '\n'.join(sorted(s_rules))
with open("./Rules/social.txt", "w",encoding='utf-8') as f:
    f.write(social_text)
del s_rules,Social_Rules,Social_Rules1,Social_Rules2,social_text

Video_Rules = get_text("https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Loon/TikTok/TikTok.list")
Video_Rules1 = get_text("https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Loon/YouTube/YouTube.list")
v_rules= set([item for item in Video_Rules if not item.startswith('#')])
v_rules.update([item for item in Video_Rules1 if not item.startswith('#')])
LEN_video= len(v_rules)
video_text = '\n'.join(sorted(v_rules))
with open("./Rules/video.txt", "w",encoding='utf-8') as f:
    f.write(video_text)
del Video_Rules,Video_Rules1,v_rules,video_text

STR_stat = f'#UTC time: {datetime.now().strftime("%Y/%m/%d %H:%M:%S")}\nreject rules: {LEN_reject}\nproxy rules: {LEN_proxy}\nsocial rules: {LEN_social}\nvideo rules: {LEN_video}\ntotal rules: {LEN_reject+LEN_proxy+LEN_social+LEN_video}'
with open("./stat", "w",encoding='utf-8') as f:
    f.write(STR_stat)
del STR_stat

Social_Rules = get_text("https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Clash/Telegram/Telegram_No_Resolve.yaml")
Social_Rules1 = get_text("https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Clash/OpenAI/OpenAI.yaml")
Social_Rules2 = get_text("https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Clash/Google/Google_No_Resolve.yaml")
s_rules= set([item for item in Social_Rules if not (item.startswith('#') or item.startswith('payload:'))])
s_rules.update([item for item in Social_Rules1 if not (item.startswith('#') or item.startswith('payload:'))])
s_rules.update([item for item in Social_Rules2 if not (item.startswith('#') or item.startswith('payload:'))])
social_text = '\n'.join(sorted(s_rules))
with open("./Rules/social.yaml", "w",encoding='utf-8') as f:
    f.write('payload:\n'+social_text)
del Social_Rules,Social_Rules1,Social_Rules2,s_rules,social_text

Video_Rules = get_text("https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Clash/YouTube/YouTube_No_Resolve.yaml")
Video_Rules1 = get_text("https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Clash/TikTok/TikTok_No_Resolve.yaml")
v_rules= set([item for item in Video_Rules if not (item.startswith('#') or item.startswith('payload:'))])
v_rules.update([item for item in Video_Rules1 if not (item.startswith('#') or item.startswith('payload:'))])
video_text = '\n'.join(sorted(v_rules))
with open("./Rules/video.yaml", "w",encoding='utf-8') as f:
    f.write('payload:\n'+video_text)
del Video_Rules,Video_Rules1,v_rules,video_text
