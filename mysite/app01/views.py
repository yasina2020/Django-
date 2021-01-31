from django.shortcuts import HttpResponse, render, redirect
import pymysql
from utils import sqlhelp

def login(request):
    """
    处理用户请求，并返回内容
    :param request:用户请求相关（对象-django已做好分割）
    :return:
    """
    # return HttpResponse('login') # 只能返回字符串'
    if request.method == "GET":
        return render(request, 'login.html')
    else:
        u = request.POST.get('user')
        p = request.POST.get('pwd')
        if u == 'root' and p == '123':
            # 登陆成功 跳转
            # return redirect('http://www.baidu.com')
            return redirect('/index/')
            # 执行这一行会重新到路由系统中匹配yul，
            # 然后匹配成功 进入index函数，再由index函数加载index页面
        else:
            # 登录失败
            return render(request, 'login.html', {'msg': '登陆失败'})


def index(request):
    return render(request, 'index.html', {
        'user_list_dict': [
            {'id': 1, 'name': 'user_1', 'email': 'user_1@qq.com'},
            {'id': 2, 'name': 'user_2', 'email': 'user_2@qq.com'},
            {'id': 3, 'name': 'user_3', 'email': 'user_3@qq.com'},
        ]
    })


def classes(request):
    class_list = sqlhelp.get_list("select id,class_name from class", [])
    return render(request, 'class.html', {'class_list': class_list})


def add_class(request):
    if request.method == "GET":
        return render(request, 'add_class.html')
    else:
        v = request.POST.get('class_name')
        sqlhelp.modify("insert into class(class_name) value(%s)", [v, ])
        return redirect('/class/')


def del_class(request):
    nid = request.GET.get('nid')
    sqlhelp.modify("delete from class where id=%s", [nid, ])
    return redirect('/class/')


def edit_class(request):
    if request.method == "GET":
        nid = request.GET.get('nid')
        result = sqlhelp.get_one("select id,class_name from class where id=%s", [nid, ])
        return render(request, 'edit_class.html', {'result': result})
    else:
        nid = request.GET.get('nid')
        class_name = request.POST.get('class_name')
        sqlhelp.modify("update class set class_name=%s where id=%s", [class_name, nid, ])
        return redirect('/class/')


def teacher(request):
    th_list = sqlhelp.get_list("select id,th_name from teacher", [])
    return render(request, 'teacher.html', {'th_list': th_list})


def add_teacher(request):
    if request.method == "GET":
        return render(request, 'add_teacher.html')
    else:
        v = request.POST.get('th_name')
        sqlhelp.modify("insert into teacher(th_name) value(%s)", [v, ])
        return redirect('/teacher/')


def del_teacher(request):
    nid = request.GET.get('nid')
    sqlhelp.modify("delete from teacher where id=%s", [nid, ])
    return redirect('/teacher')


def edit_teacher(request):
    if request.method == "GET":
        nid = request.GET.get('nid')
        th_name = request.GET.get('th_name')
        result = {'id': nid, 'th_name': th_name}
        return render(request, 'edit_teacher.html', {'result': result})
    else:
        nid = request.GET.get('nid')
        th_name = request.POST.get('th_name')
        sqlhelp.modify("update teacher set th_name=%s where id=%s", [th_name, nid, ])
        return redirect('/teacher/')


def student(request):
    stu_list = sqlhelp.get_list("SELECT s.id,stu_name,class_id,class_name FROM student  s,class WHERE s.class_id=class.id", [])
    #  id stu_name class_id class_name
    #  1   张三    4         初中二年级
    return render(request, 'student.html', {'stu_list': stu_list})


def add_student(request):
    if request.method == "GET":
        class_list = sqlhelp.get_list("SELECT * FROM class", [])
        return render(request, 'add_student.html', {'class_list': class_list})
    else:
        class_id = request.POST.get('class_id')
        stu_name = request.POST.get('stu_name')
        sqlhelp.modify("insert into student(stu_name,class_id) value(%s,%s)", [stu_name, class_id, ])
        return redirect('/student/')


def del_student(request):
    nid = request.GET.get('nid')
    sqlhelp.modify("delete from student where id=%s", [nid, ])
    return redirect('/student')


def edit_student(request):
    if request.method == "GET":
        nid = request.GET.get('nid')
        result = sqlhelp.get_one("SELECT * FROM student where id=%s", [nid, ])
        class_list = sqlhelp.get_list("SELECT * FROM class", [])
        return render(request, 'edit_student.html', {'result': result, 'class_list': class_list})
    else:
        nid = request.GET.get('nid')
        stu_name = request.POST.get('stu_name')
        class_id = request.POST.get('class_id')
        sqlhelp.modify("update student set stu_name=%s,class_id=%s where id=%s", [stu_name, class_id, nid, ])
        return redirect('/student/')
