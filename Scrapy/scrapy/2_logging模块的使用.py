#!/usr/bin/env python3

- scrapy
  - settings 中设置 LOG_LEVEL="WARNING"
  - settings 中设置 LOG_FILE="/tmp/file.log"    
    # 设置日志保存位置, 设置后，终端不会保显示日志内容
  - import logging，实例化 logger 的方式在任何文件中使用 logger 输出内容

- 普通项目
  - import logging
  - logging.basicConfig(...)        # 设置日志输出格式
  - 实例化一个 'logger=logging.getLogger(__name__)'
  - 在任何 py 文件中调用 logger 即可



--- vi log_a.py
import logging
# 设置日志输出样式
logging.basicConfig(level=logging.WARNING,
                    filename='./log/log.txt',
                    filemode='w',
                    format='%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s')
logger = logging.getLogger(__name__)
if __name__ == '__main__':
    logger.info("this is a info log")
    logger.info("this is a info log 1")

--- vi log_b.py
from log_a import logger
if __name__ == '__main__':
    logger.warning('this is log b 1')
    logger.warning('this is log b 2')
