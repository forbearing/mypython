#!/usr/bin/env python3

---
    1:asyncio 可以实现单线程并发 IO 操作，如果仅用在客户端，发挥的威力不大。如果把
      asyncio 用在服务器端，例如 Web 服务器，由于 HTTP 连接就是 IO 操作，因此可以用
      单线程 + coroutine 实现多用户的高并发操作。
    2:asyncio 实现了 TCP、UDP、SSL 等协议，aiohttp 则是基于 HTTP 框架
    3:pip install aiohttp

    import asyncio
    from aiohttp import web

    async def index(request):
        await asyncio.sleep(0.5)
        return web.Response(body=b'<h1>Index</h1>')

    async def hello(request):
        await asyncio.sleep(0.5)
        text = '<h1>hello, %s!</h1>' % request.match_info['name']
        return web.Response(body=text.encode('utf-8'))

    async def init(loop):
        app = web.Application(loop=loop)
        app.router.add_route('GET', '/', index)
        app.router.add_route('GET', '/hello/{name}', hello)
        srv = await loop.create_server(app.make_handler(), '127.0.0.1', 8000)
        print('Server started at http://127.0.0.1:8000...')
        return srv

    loop = asyncio.get_event_loop()
    loop.run_until_complete(init(loop))
    loop.run_forever()
