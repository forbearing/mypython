#!/usr/bin/env python3

---
    1:为了简化并更好地标识异步 IO，从 Python3.5 开始开始引入新的语法 async 和 await，
      可以让 coroutine 的代码更简洁易读
    2:async 和 await 是针对 coroutine 的新语法，要使用新的语法，只需要做两步简单的替换
        1:把 @asyncio.coroutine 替换为 async
        2:把 yield from 替换为 await

    async def hello():
        print("Hello Python")
        r = await asyncio.sleep(1)
        print('Hello Again!')

    loop = asyncio.get_event_loop()
    loop.run_until_complete(hello())
    loop.close()

