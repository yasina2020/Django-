from django.shortcuts import HttpResponse, render, redirect
from utils import sqlhelp
import json


def login(request):
    if request.method == "GET":
        return render(request, 'login.html')
    else:
        u = request.POST.get('user')
        p = request.POST.get('pwd')
        if u == 'root' and p == '123':
            obj = redirect('/class/')
            # max_age=10 cookies最多存在10s
            # import datetime
            # from datetime import timedelta
            # ct = datetime.datetime.utnow()
            # v = timedelta(seconds=10)
            # value = ct + 10
            # expires= value 设置到期时间 这里是十秒后到期
            # path='/url' 表明这个cookies只向该url写入
            # obj.set_cookie('tk', 'afdsfawefasf', max_age=5)
            # 签名COOKIE
            obj.set_signed_cookie('tk', 'afdsfawefasf', max_age=5,salt='askldma')
            return obj
        else:
            return render(request, 'login.html', {'msg': '账号或密码错误'})


def index(request):
    return render(request, 'index.html')


def classes(request):
    # tk = request.COOKIES.get('tk')
    tk = request.get_signed_cookie('tk', salt='askldma')
    if not tk:
        return render(request, 'login.html', {'msg': '请登录'})
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
        return redirect('/class')


def teacher(request):
    th_list = sqlhelp.get_list("select id,th_name from teacher", [])
    return render(request, 'teacher.html', {'th_list': th_list})


def add_teacher(request):
    if request.method == "GET":
        return render(request, 'add_teacher.html')
    else:
        v = request.POST.get('th_name')
        sqlhelp.modify("insert into teacher(th_name) value(%s)", [v, ])
        return redirect('/teacher')


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
        return redirect('/teacher')


def student(request):
    stu_list = sqlhelp.get_list(
        "SELECT s.id,stu_name,class_id,class_name FROM student  s,class WHERE s.class_id=class.id  order by s.id", [])
    #  id stu_name class_id class_name
    #  1   张三    4         初中二年级
    class_list = sqlhelp.get_list("select * from class", [])
    return render(request, 'student.html', {'stu_list': stu_list, 'class_list': class_list})


def add_student(request):
    if request.method == "GET":
        class_list = sqlhelp.get_list("SELECT * FROM class", [])
        return render(request, 'add_student.html', {'class_list': class_list})
    else:
        class_id = request.POST.get('class_id')
        stu_name = request.POST.get('stu_name')
        sqlhelp.modify("insert into student(stu_name,class_id) value(%s,%s)", [stu_name, class_id, ])
        return redirect('/student')


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
        return redirect('/student')


def add_class_m(request):
    ret = {'status': True, 'message': None}
    class_name = request.POST.get('class_name')
    if len(class_name) > 0:
        sqlhelp.modify("insert into class(class_name) value(%s)", [class_name, ])
    else:
        ret['status'] = False
        ret['message'] = '内容不能为空'
    return HttpResponse(json.dumps(ret))


def edit_class_m(request):
    ret = {'status': True, 'message': None}
    try:
        nid = request.POST.get('nid')
        class_name = request.POST.get('class_name')
        sqlhelp.modify('update class set class_name=%s where id=%s', [class_name, nid, ])
    except Exception as e:
        ret['status'] = False
        ret['message'] = e
        # 因为httpresponse只能传字符串，所以在后端用json.dumps()将其转化为字符串
    return HttpResponse(json.dumps(ret))


def add_teacher_m(request):
    ret = {'status': True, 'message': None}
    th_name = request.POST.get('th_name')
    if len(th_name) > 0:
        sqlhelp.modify("insert into teacher(th_name) value(%s)", [th_name, ])
    else:
        ret['status'] = False
        ret['message'] = '内容不能为空'
    return HttpResponse(json.dumps(ret))


def edit_teacher_m(request):
    ret = {'status': True, 'message': None}
    try:
        nid = request.POST.get('nid')
        th_name = request.POST.get('th_name')
        sqlhelp.modify('update teacher set th_name=%s where id=%s', [th_name, nid, ])
    except Exception as e:
        ret['status'] = False
        ret['message'] = e
        # 因为httpresponse只能传字符串，所以在后端用json.dumps()将其转化为字符串
    return HttpResponse(json.dumps(ret))


def add_student_m(request):
    ret = {'status': True, 'message': None}
    stu_name = request.POST.get('stu_name_add')
    class_id = request.POST.get('class_id_add')
    print(request.POST)
    if len(stu_name) > 0:
        sqlhelp.modify('insert into student(stu_name,class_id) value(%s,%s)', [stu_name, class_id])
    else:
        ret['status'] = False
        ret['message'] = '姓名不能为空'
    return HttpResponse(json.dumps(ret))


def edit_student_m(request):
    ret = {'status': True, 'message': None}
    try:
        stu_id = request.POST.get('stu_id')
        stu_name = request.POST.get('stu_name')
        class_id = request.POST.get('class_id')
        sqlhelp.modify("update student set stu_name=%s,class_id=%s where id=%s", [stu_name, class_id, stu_id, ])
    except Exception as e:
        ret['status'] = False
        ret['message'] = str(e)
        # 因为httpresponse只能传字符串，所以在后端用json.dumps()将其转化为字符串
    return HttpResponse(json.dumps(ret))


def teacherinfo(request):
    tf = sqlhelp.get_list("""
        SELECT r.id,t.th_name,t_id,c_id,c.class_name
        FROM teacher t,class c,relationship r 
        WHERE t.id=r.t_id AND c.id=r.c_id order by r.id
    """, [])

    tn = {}

    for row in tf:
        tid = row['t_id']
        if tid in tn:
            tn[tid]['c_name'].append(row['class_name'])
        else:
            tn[tid] = {'tid': row['t_id'], 'th_name': row['th_name'], 'c_name': [row['class_name'], ]}
    class_list = sqlhelp.get_list('select * from class', [])

    return render(request, 'teacherinfo.html', {'th_to_c_list': tn.values(), 'class_list': class_list})


def add_teacherinfo(request):
    if request.method == 'GET':
        class_list = sqlhelp.get_list('select * from class', [])
        print(class_list)
        return render(request, 'add_teacherinfo.html', {'class_list': class_list})
    else:
        class_ids = request.POST.getlist('class_id')
        th_name = request.POST.get('th_name')

        obj = sqlhelp.SqlHelp()
        th_id = obj.creat('insert into teacher(th_name) values(%s)', [th_name, ])
        data_list = []
        for class_id in class_ids:
            temp = (th_id, class_id)
            data_list.append(temp)
        obj.multiple_modify('insert into relationship(t_id,c_id) values(%s,%s)', data_list)
        obj.close()
        print(data_list)
        return redirect('/teacherinfo')


def edit_teacherinfo(request):
    if request.method == 'GET':
        t_id = request.GET.get('t_id')
        obj = sqlhelp.SqlHelp()
        th_name = obj.get_one('select * from teacher where id=%s', [t_id, ])
        class_list = obj.get_list('select * from class', [])
        th_class_list = obj.get_list('select c_id from relationship where t_id=%s', [t_id, ])
        obj.close()
        tc_list = []
        for row in th_class_list:
            tc_list.append(row['c_id'])
        return render(request, 'edit_teacherinfo.html',
                      {'th_name': th_name, 'tc_list': tc_list, 'class_list': class_list})

    else:
        th_id = request.GET.get('tid')
        th_name = request.POST.get('th_name')
        class_ids = request.POST.getlist('class_id')
        obj = sqlhelp.SqlHelp()
        obj.modify('update teacher set th_name=%s where id=%s', [th_name, th_id, ])

        # 更新relationship表，把之前tid数据全删掉 把新数据添加
        obj.modify('delete from relationship where t_id=%s', [th_id, ])
        data_list = []
        for row in class_ids:
            temp = (th_id, row)
            data_list.append(temp)
        obj.multiple_modify('insert into relationship(t_id,c_id) values(%s,%s)', data_list)
        obj.close()
        return redirect('/teacherinfo/')

def del_teacherinfo(request):
    t_id = request.GET.get('t_id')
    obj = sqlhelp.SqlHelp()
    obj.modify('delete from teacher where id=%s', [t_id, ])
    obj.modify('delete from relationship where t_id=%s', [t_id, ])
    obj.close()
    return redirect('/teacherinfo/')

def get_class_list(request):
    class_list = sqlhelp.get_list('select * from class', [])
    return HttpResponse(json.dumps(class_list))

def add_teacherinfo_m(request):
    ret = {'status': True, 'message': None}
    th_name = request.POST.get('th_name')
    class_ids = request.POST.getlist('class_ids')
    if len(th_name) > 0:
        obj = sqlhelp.SqlHelp()
        th_id = obj.creat('insert into teacher(th_name) values(%s)', [th_name, ])
        data = []
        for row in class_ids:
            temp = (th_id, row)
            data.append(temp)
        obj.multiple_modify('insert into relationship(t_id,c_id) values(%s,%s)', data)
    else:
        ret['status'] = False
        ret['message'] = '姓名不能为空'
    return HttpResponse(json.dumps(ret))


def edit_teacherinfo_m(request):
    if request.method == "GET":
        th_id = request.GET.get('th_id')
        ced_list = sqlhelp.get_list('select c_id from relationship where t_id=%s', [th_id, ])
        class_list = sqlhelp.get_list('select * from class', [])
        c_list = []
        for row in class_list:
            c_list.append(row['c_id'])
        print(c_list)
        return HttpResponse(json.dumps(c_list))
