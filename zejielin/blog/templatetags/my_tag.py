from django import template

register = template.Library()

# @register.filter
# def add1(item):
#     return int(item) + 1

#自定义标签要注册
@register.inclusion_tag('my_tag/headers.html')
# 用于接收菜单的名字
def banner(menu_name):
    img_list = [
        "https://images.cnblogs.com/cnblogs_com/blogs/771696/galleries/2304611/o_230607074913_6.jpg",
        "https://images.cnblogs.com/cnblogs_com/blogs/771696/galleries/2304611/o_230607074926_7.png",
        "https://images.cnblogs.com/cnblogs_com/blogs/771696/galleries/2304611/o_230607074946_9.jpg",
    ]
    # 以对象的形式返回数据
    return {"img_list": img_list}