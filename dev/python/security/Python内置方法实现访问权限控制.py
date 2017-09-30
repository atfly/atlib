
#!/usr/bin/env python
#-*- coding:utf-8 -*-

import rbac.acl
import rbac.context

import myapp


#: 建立访问规则注册表和用户标识上下文
acl = rbac.acl.Registry()
identity = rbac.context.IdentityContext(acl)

#: 注册角色
acl.add_role("everyone")
acl.add_role("editor", ["everyone"])
acl.add_role("admin", ["everyone"])

#: 注册资源
acl.add_resource("post")
acl.add_resource("blog-post", ["post"])
acl.add_resource("blog-post:10001", ["blog-post"])


#: 规则断言www.iplaypy.com
def assert_is_author(acl, role, op, res):
    """检查 blog-post 类型的资源是否属于当前用户所有.

    若一个规则的断言返回 False, 权限检查时视为这条规则不存在.
    """
    #: 对资源标识不属于 blog-post 的, 断言无效
    if not isinstance(res, basestring):
        return False
    #: 分割形如 "blog-post:10001" 的资源标识
    splited = res.split(":", 1)
    #: 对资源标识不属于 blog-post 的, 断言无效
    if len(splited) != 2 or splited[0] != "blog-post":
        return False
    #: 取出资源对应的模型
    blog_post = myapp.get_blog_post_by_id(splited[1])
    #: 断言是否生效取决于博文的作者是否是当前用户
    return blog_post.author == myapp.get_current_user()


#: 注册规则
acl.allow("everyone", "view", "post")
acl.allow("editor", "edit", "post", assertion=assert_is_author)
acl.allow("admin", "edit", "post")


#: 角色加载回调函数
@identity.set_roles_loader
def load_roles():
    """加载当前上下文拥有的角色"""
    yield "everyone"
    user = myapp.get_current_user()

    if myapp.user_is_admin(user):
        yield "admin"
    for role in myapp.get_roles(user):
        yield str(role)


#: 使用权限检查（装饰器语法）
@identity.check_permission("view", "blog-post", message="can't view")
def view_blog_post(id):
    blog_post = myapp.get_blog_post_by_id(id)
    if blog_post:
        return blog_post.title
    else:
        return "not found"


#: 使用权限检查（with-context 语法）
def edit_blog_post(id, new_title):
    blog_post = myapp.get_blog_post_by_id(id)
    resource = "blog-post:%s" % id

    with identity.check_permission("edit", resource, message="can't edit"):
        if blog_post:
            blog_post.title = new_title
        else:
            return "not found"


if __name__ == "__main__":
    #: 因为默认拥有 everyone 角色而可行
    print view_blog_post("10001")

    #: 执行下面这句则会抛出 rbac.context.PermissionDenied: can't edit 异常
    # edit_blog_post("10001", "It's a bad day.")

    #: 修改当前用户为 tom
    myapp.current_user = "tom"
    #: 仍然会抛出异常，因为既不是 admin 又不是 author
    #: author 只是普通 editor 角色，但 assert_is_author 调用返回 True
    # edit_blog_post("10001", "It's a bad day.")

    #: 修改当前用户为 tony
    myapp.current_user = "tony"
    #: 因为 editor 角色的授权生效, 可以执行
    edit_blog_post("10001", "It's a bad day.")
    #: 可以看到标题已修改
    print view_blog_post("10001")

    #: 修改当前用户为 admin
    myapp.current_user = "admin"
    print "%s is not author:" % myapp.current_user.capitalize(),
    print myapp.get_blog_post_by_id("10001").author != "admin"
    #: 因为 admin 角色的授权生效, 可以执行
    edit_blog_post("10001", "It's a wonderful day.")
    #: 可以看到标题已修改
    print view_blog_post("10001")

#!/usr/bin/env python
#-*- coding:utf-8 -*-

class BlogPost(object):
    """博文模型"""

    def __init__(self, title, author):
        self.title = title
        self.author = author


current_user = "nobody"
blog_posts = {'10001': BlogPost("It's a sunny day", "tony")}


def get_current_user():
    return current_user


def get_blog_post_by_id(id):
    return blog_posts.get(id)


def user_is_admin(user):
    return user == "admin"


def get_roles(user):
    if user in ("tony", "tom"):
        return ["editor"]
    else:
        return []
