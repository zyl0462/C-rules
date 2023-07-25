import requests,sys,time
from datetime import datetime

def get_text(url):
    r = requests.get(url, stream= True)
    if r.status_code == 200:
        with open("./Rules/tmp", "wb") as f:
            for chunk in r.iter_content(chunk_size=1024):
                if chunk:
                    f.write(chunk)
        time.sleep(0.25)
        with open("./Rules/tmp", "r",encoding='utf-8') as f:
            return f.read().strip()
    else:
        sys.exit(0)

REJECT_URL = ("https://anti-ad.net/domains.txt",
         "https://raw.githubusercontent.com/Cats-Team/AdRules/main/ad-domains.txt",
         "https://adguardteam.github.io/AdGuardSDNSFilter/Filters/filter.txt")
PROXY_URL = ("https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Loon/Proxy/Proxy_Domain.list",
             "https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Loon/GlobalMedia/GlobalMedia_Domain.list",
             "https://raw.githubusercontent.com/Loyalsoldier/surge-rules/release/gfw.txt")
SOCIAL_URL = ("https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Loon/Telegram/Telegram.list",
              "https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Loon/OpenAI/OpenAI.list",
              "https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Loon/Google/Google.list")
VIDEO_URL = ("https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Loon/TikTok/TikTok.list",
             "https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Loon/YouTube/YouTube.list")
SOCIAL_YMAL = ("https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Clash/Telegram/Telegram_No_Resolve.yaml",
               "https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Clash/OpenAI/OpenAI.yaml",
              "https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Clash/Google/Google_No_Resolve.yaml")
VIDEO_YMAL = ("https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Clash/YouTube/YouTube_No_Resolve.yaml",
              "https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Clash/TikTok/TikTok_No_Resolve.yaml")

reject_set = set([i for i in get_text(REJECT_URL[0]).split("\n") if not (i.startswith('#') or i.startswith('!'))])
reject_set .update([i for i in get_text(REJECT_URL[1]).lower().split("\n") if not (i.startswith('#') or i.startswith('!'))])
reject_set .update([i[2:-1] for i in get_text(REJECT_URL[2]).split("\n") if (i.startswith('||') and i.endswith('^'))])
LEN_reject = len(reject_set)
reject_text = '\n'.join(sorted(reject_set))
with open("./Rules/reject.txt", "w",encoding='utf-8') as f:
    f.write(reject_text)
del reject_set,reject_text,REJECT_URL

proxy_set =set()
for item in PROXY_URL:
    proxy_set.update([i for i in get_text(item).split("\n") if not i.startswith('#')])
LEN_proxy = len(proxy_set)
proxy_text = '\n'.join(sorted(proxy_set))
with open("./Rules/proxy.txt", "w",encoding='utf-8') as f:
    f.write(proxy_text)
p_rules= [('DOMAIN,' + i + ',PROXY') for i in proxy_text.strip().split("\n") if not i.startswith('.')]
p_rules.extend([('DOMAIN-SUFFIX,'+ i[1:] + ',PROXY') for i in proxy_text.strip().split("\n") if i.startswith('.')])
p_text ='\n'.join(sorted(p_rules))
with open("./Rules/rproxy.txt", "w",encoding='utf-8') as f:
    f.write(p_text)
del p_rules, proxy_text, p_text,proxy_set,PROXY_URL

social_set = set()
for item in SOCIAL_URL:
    social_set.update([i for i in get_text(item).split("\n") if not i.startswith('#')])
LEN_social= len(social_set)
social_text = '\n'.join(sorted(social_set))
with open("./Rules/social.txt", "w",encoding='utf-8') as f:
    f.write(social_text)
video_set = set()
for item in VIDEO_URL:
    video_set.update([i for i in get_text(item).split("\n") if not i.startswith('#')])
LEN_video= len(video_set)
video_text = '\n'.join(sorted(video_set))
with open("./Rules/video.txt", "w",encoding='utf-8') as f:
    f.write(video_text)
del video_set,video_text,VIDEO_URL,social_set,social_text,SOCIAL_URL

STR_stat = f'#UTC time: {datetime.now().strftime("%Y/%m/%d %H:%M:%S")}\n\
reject rules: {LEN_reject}\nproxy rules: {LEN_proxy}\n\
social rules: {LEN_social}\nvideo rules: {LEN_video}\n\
total rules: {LEN_reject+LEN_proxy+LEN_social+LEN_video}'
with open("./stat", "w",encoding='utf-8') as f:
    f.write(STR_stat)
del STR_stat,LEN_reject,LEN_proxy,LEN_social,LEN_video

social_ymal_set = set()
for item in SOCIAL_YMAL:
    social_ymal_set.update([i for i in get_text(item).split("\n") if not (i.startswith('#') or i.startswith('payload:'))])
social_ymal = '\n'.join(sorted(social_ymal_set))
with open("./Rules/social.yaml", "w",encoding='utf-8') as f:
    f.write('payload:\n'+social_ymal)
video_ymal_set = set()
for item in VIDEO_YMAL:
    video_ymal_set.update([i for i in get_text(item).split("\n") if not (i.startswith('#') or i.startswith('payload:'))])
video_ymal = '\n'.join(sorted(video_ymal_set))
with open("./Rules/video.yaml", "w",encoding='utf-8') as f:
    f.write('payload:\n'+video_ymal)
del video_ymal_set,video_ymal,VIDEO_YMAL,social_ymal_set,social_ymal,SOCIAL_YMAL
