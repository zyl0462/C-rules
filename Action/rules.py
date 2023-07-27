import requests,sys,time
from datetime import datetime,timezone,timedelta

def get_text(url):
    with requests.get(url, stream= True) as r:
        if r.status_code == 200:
            with open("./Rules/tmp", "wb") as f:
                for chunk in r.iter_content(chunk_size=4096):
                    if chunk:
                        f.write(chunk)
            time.sleep(0.1)
            with open("./Rules/tmp", "r",encoding='utf-8') as f:
                return f.read().strip()
        else:
            sys.exit(0)

RULES_URL =(("https://anti-ad.net/domains.txt",
                "https://raw.githubusercontent.com/Cats-Team/AdRules/main/ad-domains.txt",
                "https://adguardteam.github.io/AdGuardSDNSFilter/Filters/filter.txt"),
            ("https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Loon/Proxy/Proxy_Domain.list",
                "https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Loon/GlobalMedia/GlobalMedia_Domain.list",
                "https://raw.githubusercontent.com/Loyalsoldier/surge-rules/release/gfw.txt"),
            ("https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Loon/Telegram/Telegram.list",
                 "https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Loon/OpenAI/OpenAI.list",
                "https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Loon/Google/Google.list"),
            ("https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Loon/TikTok/TikTok.list",
                "https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Loon/YouTube/YouTube.list"),
            ("https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Clash/Telegram/Telegram_No_Resolve.yaml",
                "https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Clash/OpenAI/OpenAI.yaml",
                "https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Clash/Google/Google_No_Resolve.yaml"),
            ("https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Clash/YouTube/YouTube_No_Resolve.yaml",
                "https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Clash/TikTok/TikTok_No_Resolve.yaml")
)

reject_set = set([i for i in get_text(RULES_URL[0][0]).split("\n") if not (i.startswith('#') or i.startswith('!'))])
reject_set .update([i for i in get_text(RULES_URL[0][1]).lower().split("\n") if not (i.startswith('#') or i.startswith('!'))])
reject_set .update([i[2:-1] for i in get_text(RULES_URL[0][2]).split("\n") if (i.startswith('||') and i.endswith('^'))])
LEN_reject = len(reject_set)
reject_text = '\n'.join(sorted(reject_set))
with open("./Rules/reject.txt", "w",encoding='utf-8') as f:
    f.write(reject_text)
del reject_set,reject_text

proxy_set =set()
for item in RULES_URL[1]:
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
del p_rules, proxy_text, p_text,proxy_set

social_set = set()
for item in RULES_URL[2]:
    social_set.update([i for i in get_text(item).split("\n") if not i.startswith('#')])
LEN_social= len(social_set)
social_text = '\n'.join(sorted(social_set))
with open("./Rules/social.txt", "w",encoding='utf-8') as f:
    f.write(social_text)
video_set = set()
for item in RULES_URL[3]:
    video_set.update([i for i in get_text(item).split("\n") if not i.startswith('#')])
LEN_video= len(video_set)
video_text = '\n'.join(sorted(video_set))
with open("./Rules/video.txt", "w",encoding='utf-8') as f:
    f.write(video_text)
del video_set,video_text,social_set,social_text

my_stat = []
with open("./stat", "r",encoding='utf-8') as f:
    my_stat.extend([i[i.rindex(' ')+1:] for i in f.read().strip().split("\n") if not i.startswith('#')])
LEN_reject0,LEN_proxy0,LEN_social0,LEN_video0,LEN_total= int(my_stat[0]),int(my_stat[1]),int(my_stat[2]),int(my_stat[3]),int(my_stat[4])
STR_stat = f'#{(datetime.utcnow().astimezone(timezone(timedelta(hours=8)))).strftime("%Y/%m/%d %H:%M:%S")}\n\
reject rules({"+" if LEN_reject-LEN_reject0 >= 0 else "-"}{abs(LEN_reject-LEN_reject0)}): {LEN_reject}\n\
proxy rules({"+" if LEN_proxy-LEN_proxy0 >= 0 else "-"}{abs(LEN_proxy-LEN_proxy0)}): {LEN_proxy}\n\
social rules({"+" if LEN_social-LEN_social0 >= 0 else "-"}{abs(LEN_social-LEN_social0)}): {LEN_social}\n\
video rules({"+" if LEN_video-LEN_video0 >= 0 else "-"}{abs(LEN_video-LEN_video0)}): {LEN_video}\n\
total rules({"+" if LEN_reject+LEN_proxy+LEN_social+LEN_video-LEN_total >= 0 else "-"}{abs(LEN_reject+LEN_proxy+LEN_social+LEN_video-LEN_total)}): {LEN_reject+LEN_proxy+LEN_social+LEN_video}'
with open("./stat", "w",encoding='utf-8') as f:
    f.write(STR_stat)
del my_stat,STR_stat,LEN_reject,LEN_proxy,LEN_social,LEN_video,LEN_reject0,LEN_proxy0,LEN_social0,LEN_video0,LEN_total

social_ymal_set = set()
for item in RULES_URL[4]:
    social_ymal_set.update([i for i in get_text(item).split("\n") if not (i.startswith('#') or i.startswith('payload:'))])
social_ymal = '\n'.join(sorted(social_ymal_set))
with open("./Rules/social.yaml", "w",encoding='utf-8') as f:
    f.write('payload:\n'+social_ymal)
video_ymal_set = set()
for item in RULES_URL[5]:
    video_ymal_set.update([i for i in get_text(item).split("\n") if not (i.startswith('#') or i.startswith('payload:'))])
video_ymal = '\n'.join(sorted(video_ymal_set))
with open("./Rules/video.yaml", "w",encoding='utf-8') as f:
    f.write('payload:\n'+video_ymal)
del video_ymal_set,video_ymal,social_ymal_set,social_ymal,RULES_URL
