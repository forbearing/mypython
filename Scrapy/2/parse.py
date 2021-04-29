#!/bin/env python3

# from urllib.parse import urlparse
# result = urlparse('https://www.google.com/search?tbm=isch&sxsrf=ALeKk01MQem16rBYM2McEVdOxU-Hq5D2FQ%3A1584192369171&source=hp&biw=1486&bih=758&ei=cdtsXuq8CJXe9QP9oqe4Dw&q=%E6%B8%85%E6%96%B0&oq=%E6%B8%85%E6%96%B0&gs_l=img.3..35i39j0l9.1182.5075..5577...4.0..0.184.1446.0j11......0....1..gws-wiz-img.....10..0i131j35i362i39j0i5i30j0i7i30j0i24j0i10i24.t4wLDSjxnvY&ved=0ahUKEwiquay7iJroAhUVb30KHX3RCfcQ4dUDCAY&uact=5')
# print(result)

# from urllib.parse import urlunparse
# data = ['http', 'www.baidu.com', 'index.html', 'user', 'a=6', 'comment']
# print(urlunparse(data))

from urllib.parse import urlencode
params = {
        'name': 'hybfkuf',
        'age': 23
        }
base_url = 'https://hybfkuf.com'
url = base_url + urlencode(params)
print(url)
