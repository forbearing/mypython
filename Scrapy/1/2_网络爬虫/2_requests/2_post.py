1:
    import requests

    data = {'name':'hyb', 'age':22}
    r =requests.post('http://httpbin.org/post',data=data)
    print(r.text)
