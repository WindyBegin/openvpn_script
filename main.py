import sys
import os

import logging

logger = logging.getLogger(__name__)
logger.setLevel(level=logging.INFO)
handler = logging.FileHandler("vpn_log.txt")  # 添加个日志文件调试一下
handler.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)


def checkpsw(username, password):
    """
    检查文本中账号密码是否存在
    :param username:
    :param password:
    :return:
    """
    # 暂无,懒得写了,有空补上吧,多账号才用得上
    pass


def run():
    """
        账号密码 是通过参数传递返回的, 不是通过命令参数

    //验证通过应该返回0
    //错误应该返回1
    //异常返回-1
    :return:
    """
    # print(sys.argv)
    # 初始化相关参数
    argv_user = ""
    argv_pass = ""
    USERNAME = os.getenv('USERNAME')
    PASSWORD = os.getenv('PASSWORD')

    # logger.info(sys.argv) #输出起动参数
    # if len(sys.argv) > 1:  # 根据返回参数列表的数量,判断是否代参数
    #     argv_user = sys.argv[-2]
    #     argv_pass = sys.argv[-1]
    # else:
    #     sys.exit(-1)  # 未指定账号密码,返回异常码

    logger.info(f"输入: {USERNAME} {PASSWORD}  检验: {argv_user} {argv_pass}")
    if USERNAME == 'meta1' and PASSWORD == 'meta111':
        logger.info(f"登陆成功OK")
        # return 0 #验证通过应该返回0
        sys.exit(0)
    elif USERNAME == 'meta2' and PASSWORD == 'meta222':
        logger.info(f"登陆成功OK")
        # return 0 #验证通过应该返回0
        sys.exit(0)
    elif USERNAME == 'meta3' and PASSWORD == 'meta333':
        logger.info(f"登陆成功OK")
        # return 0 #验证通过应该返回0
        sys.exit(0)
    elif USERNAME == 'meta4' and PASSWORD == 'meta444':
        logger.info(f"登陆成功OK")
        # return 0 #验证通过应该返回0
        sys.exit(0)
    elif USERNAME == 'meta5' and PASSWORD == 'meta555':
        logger.info(f"登陆成功OK")
        # return 0 #验证通过应该返回0
        sys.exit(0)
    elif USERNAME == 'meta6' and PASSWORD == 'meta666':
        logger.info(f"登陆成功OK")
        # return 0 #验证通过应该返回0
        sys.exit(0)
    elif USERNAME == 'meta7' and PASSWORD == 'meta777':
        logger.info(f"登陆成功OK")
        # return 0 #验证通过应该返回0
        sys.exit(0)
    else:
        logger.info(f"登陆失败NO{USERNAME} {PASSWORD}")
        # return 1 #错误应该返回1
        sys.exit(-1)


if __name__ == "__main__":
    run()

