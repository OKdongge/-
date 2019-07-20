import json
import requests



res = requests.get('https://m.weibo.cn/api/container/getIndex?uid=1191220232&ext=growth:0%7Cterminal:%7Creason:45.4%7Cuid:6814903818%7Cbuid:2145291155%7Cfollow:1191220232%7Cact:skip%7Cact_valu:scheme%7Cskiptype:profile%7Cagain:&featurecode=10000326&luicode=10000011&lfid=1076032145291155&type=uid&value=1191220232&containerid=1076031191220232&page=1')
res.encoding = 'utf-8'
print(res.text)