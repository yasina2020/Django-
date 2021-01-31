import socket


def f1(request):
    """
    处理用户请求并返回内容
    :param request:用户请求的所有信息
    :return:
    """
    f = open('index.html', 'rb')
    data = f.read()
    f.close()
    return data


def f2():
    f = open('article.html', 'rb')
    data = f.read()
    f.close()
    return data


def f3(request):
    # https://www.cnblogs.com/wupeiqi/articles/5713330.html
    import pymysql

    conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='wu', db='django_test')
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
    cursor.execute("select id,username,password from userinfo")
    user_list = cursor.fetchall()
    cursor.close()
    conn.close()

    print(user_list)

    conten_list = []
    for row in user_list:
        tp = "<tr><td>%s</td><td>%s</td><td>%s</td></tr>" % (row["id"], row["username"], row["password"])
        conten_list.append(tp)
    content = "".join(conten_list)  # join() 方法用于将序列中的元素以指定的字符连接生成一个新的字符串。

    f = open('userlist.html', 'r', encoding='utf-8')
    data_temp = f.read()
    f.close()

    data = data_temp.replace('@@userlist@@', content)
    return bytes(data, encoding='utf-8')


def f4(request):
    # https://www.cnblogs.com/wupeiqi/articles/5713330.html
    import pymysql

    conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='wu', db='django_test')
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
    cursor.execute("select id,username,password from userinfo")
    user_list = cursor.fetchall()
    cursor.close()
    conn.close()

    f = open('host.html', 'r', encoding='utf-8')
    data = f.read()
    f.close()

    from jinja2 import Template
    template = Template(data)
    data = template.render(user_list_h=user_list)

    return data.encode('utf-8')


routers = [
    ('/xxx', f1),
    ('/ooo', f2),
    ('/userlist.html', f3),  # 动态网页：从数据库读数据
    ('/host.html', f4),  # 使用jinjia2渲染

]


def run():
    sock = socket.socket()
    sock.bind(('127.0.0.1', 8080))
    sock.listen(5)

    while True:
        conn, addr = sock.accept()
        data = conn.recv(8096)  # 8096是接受的套接字大小
        data = str(data, encoding='utf-8')
        headers, bodys = data.split('\r\n\r\n')
        temp_list = headers.split('\r\n')
        method, url, protocal = temp_list[0].split(' ')
        conn.send(b'HTTP\1.1 200 OK\r\n\r\n')

        func_name = None
        for item in routers:
            if item[0] == url:
                func_name = item[1]
                break
        if func_name:
            response = func_name(bodys)
        else:
            response = b'404'

        conn.send(response)
        conn.close()


if __name__ == '__main__':
    run()
