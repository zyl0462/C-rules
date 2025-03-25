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

############################################################  
############################################################
REJECT_URL = ("https://raw.githubusercontent.com/privacy-protection-tools/anti-AD/master/anti-ad-domains.txt",
             "https://adguardteam.github.io/AdGuardSDNSFilter/Filters/filter.txt")
PROXY_URL = (('https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/refs/heads/master/rule/Clash/Proxy/Proxy_Domain.txt',
             'https://raw.githubusercontent.com/Loyalsoldier/surge-rules/release/gfw.txt'),
             ('https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/refs/heads/master/rule/Clash/Proxy/Proxy.yaml',
              'https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/refs/heads/master/rule/Clash/Netflix/Netflix_Classical.yaml',
             'https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/refs/heads/master/rule/Clash/AppleTV/AppleTV.yaml',
             'https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/refs/heads/master/rule/Clash/GitHub/GitHub.yaml',
             'https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/refs/heads/master/rule/Clash/Google/Google.yaml',
             'https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/refs/heads/master/rule/Clash/YouTube/YouTube.yaml',
             'https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/refs/heads/master/rule/Clash/Telegram/Telegram.yaml',
             'https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/refs/heads/master/rule/Clash/TikTok/TikTok.yaml',
             'https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/refs/heads/master/rule/Clash/Twitter/Twitter.yaml',
             'https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/refs/heads/master/rule/Clash/Facebook/Facebook.yaml',
             'https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/refs/heads/master/rule/Clash/Discord/Discord.yaml',
             'https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/refs/heads/master/rule/Clash/Instagram/Instagram.yaml',
             'https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/refs/heads/master/rule/Clash/GitLab/GitLab.yaml',
             'https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/refs/heads/master/rule/Clash/Pinterest/Pinterest.yaml',
             'https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/refs/heads/master/rule/Clash/OpenAI/OpenAI.yaml')
            )
DIRECT_URL = ('https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/refs/heads/master/rule/Clash/AliPay/AliPay.yaml',
              'https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/refs/heads/master/rule/Clash/Apple/Apple_Classical.yaml',
              'https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/refs/heads/master/rule/Clash/JingDong/JingDong.yaml',
              ‘https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/refs/heads/master/rule/Clash/Alibaba/Alibaba_Classical.yaml’，
              'https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/refs/heads/master/rule/Clash/WeChat/WeChat.yaml',
              'https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/refs/heads/master/rule/Clash/DouYin/DouYin.yaml'，
              ’https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/refs/heads/master/rule/Clash/ByteDance/ByteDance.yaml‘
             )


