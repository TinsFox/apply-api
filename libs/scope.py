class SocietyScope(object):
    society_permission = ['apply_user', 'section_apply_user', 'single_society_apply_user']


class GeneralScope(SocietyScope):
    general_permission = ['all_society_apply_user', 'apply_count'] + SocietyScope.society_permission


def scope(auth, endpoint):
    """ 权限控制 """
    if auth == 1:
        # 社团管理员
        endpoint = endpoint.split('.')[-1]
        if endpoint in SocietyScope.society_permission:
            return True
        return False
    elif auth == 2:
        # 超级管理员
        return True
