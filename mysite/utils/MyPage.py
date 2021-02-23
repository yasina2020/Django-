class PageInfo(object):

    def __init__(self, cur_page, per_page, all_count, url, show_page=11):
        """

        :param cur_page: 当前页
        :param per_page: 每页几条数据
        :param all_count: 总行数
        :param show_page: 显示多少个页码
        :param url: 显示页码的网址
        """
        try:
            self.cur_page = int(cur_page)
        except Exception as e:
            self.cur_page = 1
        self.per_page = per_page
        self.all_page, b = divmod(all_count, per_page)
        if b:
            self.all_page += 1
        self.show_page = show_page
        self.url = url

    def start(self):
        return (self.cur_page - 1) * self.per_page

    def end(self):
        return self.cur_page * self.per_page

    def pager(self):
        page_list = []
        # 注释1 比如页面一共有100页，太多了，下面可以保证页码显示的始终是当前页的附近几页
        # 注释1.1 下面两行来保证当总页面比要展示的页码少时，不会溢出
        if self.all_page < self.show_page:
            self.show_page = self.all_page

        half_p = int(self.show_page / 2)
        begin = self.cur_page - half_p
        stop = self.cur_page + half_p

        # 注释1.2 下面这个if，当self.cur_page过小时，stop会变大，当其过大时，begin会变小，
        # 来保证始终有self.show_page个页码。
        if self.cur_page <= half_p:
            stop = self.show_page
        elif self.cur_page > self.all_page - half_p:
            begin = self.all_page - self.show_page

        # 注释1.3 下面这两个if来保证页码不会越界
        if begin < 1:
            begin = 1
        if stop > self.all_page:
            stop = self.all_page

        # 注释2 下面来做上一页和下一页
        if self.cur_page > 1:
            prve = "<li><a href='%s?p=%s'>上一页</a></li>" % (self.url, self.cur_page - 1)
            page_list.append(prve)
        else:
            page_list.append("<li><span>到头了</span></li>")

        for i in range(begin, stop + 1):
            if i == self.cur_page:
                temp = "<li class='active'><a href='%s?p=%s'>%s</a></li>" % (self.url, i, i)
            else:
                temp = "<li><a href='%s?p=%s'>%s</a></li>" % (self.url, i, i)
            page_list.append(temp)

        if self.cur_page < self.all_page:
            end = "<li><a href='%s?p=%s'>下一页</a></li>" % (self.url, self.cur_page + 1)
            page_list.append(end)
        else:
            page_list.append("<li><span>没有啦</span></li>")

        return ''.join(page_list)
