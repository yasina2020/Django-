import pymysql


def get_list(sql, args):
    conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='wu', db='django_test')
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
    cursor.execute(sql, args)
    result = cursor.fetchall()
    cursor.close()
    conn.close()
    return result


def modify(sql, args):
    conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='wu', db='django_test')
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
    cursor.execute(sql, args)
    conn.commit()
    cursor.close()
    conn.close()


def get_one(sql, args):
    conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='wu', db='django_test')
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
    cursor.execute(sql, args)
    result = cursor.fetchone()
    cursor.close()
    conn.close()
    return result


class SqlHelp(object):
    def __init__(self):
        self.conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='wu', db='django_test')
        self.cursor = self.conn.cursor(cursor=pymysql.cursors.DictCursor)

    def get_list(self, sql, args):
        self.cursor.execute(sql, args)
        result = self.cursor.fetchall()
        return result

    def get_one(self, sql, args):
        self.cursor.execute(sql, args)
        result = self.cursor.fetchone()
        return result

    def modify(self, sql, args):
        self.cursor.execute(sql, args)
        self.conn.commit()

    # 添加一条数据并且返回该数据的ID
    def creat(self, sql, args):
        self.cursor.execute(sql, args)
        self.conn.commit()
        return self.cursor.lastrowid

    # 使用executemany对数据进行批量插入
    # args是[(1,'小明'),(2,'zeke'),(3,'琦琦')]
    # 可以将args[i]作为参数依次执行sql语句 速度比循环execute快得多
    def multiple_modify(self, sql, args):
        self.cursor.executemany(sql, args)
        self.conn.commit()

    def close(self):
        self.cursor.close()
        self.conn.close()
