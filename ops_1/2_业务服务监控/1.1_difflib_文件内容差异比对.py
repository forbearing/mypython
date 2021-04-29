#!/usr/bin/env python3


'''
    * 业务服务监控是运维体系中最重要的环节，是保证业务服务质量的关键手段，需要根据不同的
      业务场景定制不同的监控策略。Python 在监控方面提供了大量的第三方工具，可以帮助我们
      快速、有效地开发企业级服务监控平台。
    * difflib 为标准库模块无需安装，实现文件内容差异比对，且支持输出可读性比较强的 HTML 文档
      与 Linux 的 diff 命令相似，可以使用 difflib 比对代码、配置文件的差别，在版本控制方面
      非常有用。

    '_'         包含在第一个序列行中，但不包含在第二个序列行中，
    '+'         包含在第二个序列行中，但不包含在第一个序列行中。
    ''          两个序列一致
    '?'         标志两个序列行存在增量差异
    '^'         标识出两个序列行存在的差异字符

'''


'''
    1. 字符串之间的差异
'''

import difflib
text1 = '''
The fast-spreading coronavirus variant is turning up in US sewers
8 Popular Types of Cloud Computing for Business and Individuals
 what the technology is. It’s understandable. The word “cloud” all by itself suggests something nebulous and ethereal. But the cloud
technology is. It’s understandable. The word “cloud” all by itself suggests something nebulous and ethereal. But the cloud
'''
text2 = '''
The fast-spreading coronavirus varian is turning up in US sewers
8 Popular Types of Cloud Computing for Business and individuals
what the technology is. It’s understandable. The word “cloud” all by itself suggests something nebulous and ethereal. But the cloud
technology is. It’s understandable. The word “cloud” all by itself suggests something nebulous and ethereal. But the cloud
'''
text1_line = text1.splitlines()
text2_line = text2.splitlines()

differ = difflib.Differ()
d = differ.compare(text1_line, text2_line)
print('\n'.join(list(d)))


'''
    2. 生成美观的对比 HTML 格式文档
'''
