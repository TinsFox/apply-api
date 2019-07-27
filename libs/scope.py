class SocietyScope(object):
    # append_section: 添加部门信息
    # delete_section: 删除部门信息
    # file_download: 下载社团报名信息
    # user_info: 查看用户信息
    # section_info: 查看部门报名信息
    # society_info: 查看社团报名信息
    # admin_section_list: 查看部门列表
    society_permission = ['append_section', 'delete_section', 'file_download', 'user_info', 'section_info',
                          'society_info', 'admin_section_list', 'append_society_brief', 'append_section_brief',
                          'delete_society']


class GeneralScope(SocietyScope):
    # 超级管理员
    general_permission = ['append_society', 'file_download']


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
        if endpoint in GeneralScope.forbbiden:
            return False
        return True
