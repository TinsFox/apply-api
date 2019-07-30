# -*- coding: utf8 -*-
class SocietyScope(object):
    # append_section: 添加部门信息
    # delete_section: 删除部门信息
    # file_download: 下载社团报名信息
    # user_info: 查看用户信息
    # section_info: 查看部门报名信息
    # society_info: 查看社团报名信息
    # admin_section_list: 查看部门列表
    society_permission = ['file_download']


class GeneralScope(SocietyScope):
    # 超级管理员
    general_permission = ['append_society', 'delete_society']
    general_forbbiden = ['append_section', 'delete_section', 'user_info', 'section_info', 'society_info',
                         'append_brief', 'admin_section_list', 'reset_society']


def scope(auth, endpoint):
    """ 权限控制 """
    endpoint = endpoint.split('.')[-1]
    if auth == 1:
        # 社团管理员
        if endpoint in SocietyScope.society_permission or endpoint in GeneralScope.general_forbbiden:
            return True
        else:
            return False
    elif auth == 2:
        # 超级管理员
        if endpoint in GeneralScope.general_forbbiden:
            return False
        else:
            return True
