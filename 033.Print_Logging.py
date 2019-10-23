# -*-coding:utf-8-*-
# @auth ivan
# @time 20120604 --
# @goal test

def log_test01():
    import logging
    import logging.handlers
    LOG_FILE = "033.Print_Logging.log"
    handler = logging.handlers.RotatingFileHandler(LOG_FILE, maxBytes=20 * 1024 * 1024, backupCount=10) # 实例化handler
    fmt = "%(asctime)s - %(name)s - %(levelname)s - %(message)s - [%(filename)s:%(lineno)s]"
    formatter = logging.Formatter(fmt) # 实例化formatter
    handler.setFormatter(formatter) # 为handler添加formatter
    logger = logging.getLogger('xzs') # 获取名为xzs的logger
    logger.addHandler(handler) # 为logger添加handler
    logger.setLevel(logging.DEBUG)

    logger.debug("Hello boy, Debug")
    logger.info("Hello boy, Info")


if __name__ == "__main__":
    log_test01()

# 2019-10-23 20:16:36,248 - xzs - DEBUG - Hello boy, Debug - [033.Print_Logging.py:18]
# 2019-10-23 20:16:36,248 - xzs - INFO - Hello boy, Info - [033.Print_Logging.py:19]



