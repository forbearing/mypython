1:TXT 文本几乎兼容任何平台，但是不利于检索，如果对检索和数据结构要求不高，
  追求方便第一的话，可以采用 txt 文本存储



1:基本示例l
    import requests
    from pyquery import PyQuery as pq
    url = 'https://www.zhihu.com/explore'
    headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebkit/537.36 (KHTML, like Gecko) \
                Chrome/58.0.3029.110 Safar/537.36'
            }

    html = requests.get(url, headers=headers).text
    doc = pq(html)
    items = doc('.explore-tab .feed-item').items()
    for item in items:
        question = item.find('h2').text()
        print(question)
        author = item.find('.author-link-line').text()
        answer = pq(item.find('.content').html()).text()
        file = open('explore.txt', 'a', encoding='utf-8')
        file.write('\n'.join([question, author, answer]))
        file.write('\n'+'='*50+'\n')
        file.close()



2:打开方式
    r       以只读方式打开文件，文件的指针将会放在文件的开头，这是默认模式
    rb      以二进制只读模式打开一个文件，文件指针将会放在文件的开头
    r+      以读写方式打开一个文件，文件指针将会放在开头
    w       以写入方式打开一个文件，文件存在覆盖，不存在创建
    wb      以二进制写入方打开一个文件，文件存在覆盖，不存在创建
    w+      以读写方式打开一个文件，存在覆盖，不存在创建
    wb+     以二进制格式读写一个文件，存在覆盖，不存在创建
    a，ab，a+，ab+




3:简化写法
    1:文件写入还有一种简写方法，使用 with as 语法。在 with 控制块结束时，文建会自动关闭
      所以就不需要调用 close() 方法
    with open('explore.txt', 'a', encoding='utf-8') as file:
        file.write('\n', join([question, author, answer]))
        file.write('\n' + '='*50 + '\n')
