from common import LOGIN_TITLE


def get_site_info(request):
    """
    根据登录的用户获取网站标题
    :param request:
    :return:
    """
    return {'site_web': LOGIN_TITLE}
