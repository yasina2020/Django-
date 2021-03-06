<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>教师任教信息表</title>
    <link rel="stylesheet" href="/static/plug/bootstrap-3/css/bootstrap.css" />
    <link rel="stylesheet" href="/static/plug/bootstrap-3/js/bootstrap.js" />
    <link rel="stylesheet" href="/static/common.css" />
</head>
<body>
<div style="margin: 0 auto;width: 700px">
    <h3>教师任教信息表</h3>
    <div style="margin: 10px 0">
        <a href="/add_teacherinfo" class="btn btn-primary">添加任教信息</a>
        <a id="ShowModal" class="btn btn-info">对话框添加</a>
    </div>
    <table border="1" class="table table-hover">
        <thead>
        <tr>
            <th>ID</th>
            <th>任教老师</th>
            <th>任教班级</th>
            <th>操作</th>
            <th>对话框操作(未实现)</th>
        </tr>
        </thead>
        <tbody>
        {%for row in th_to_c_list%}
        <tr>
            <th>{{row.tid}}</th>
            <th>{{row.th_name}}</th>
            <th>
                {%for item in row.c_name%}
                <span>{{item}}</span>
                {%endfor%}
            </th>
            <th>
                <a href="/edit_teacherinfo/?t_id={{row.tid}}">编辑</a>
                |
                <a href="/del_teacherinfo/?t_id={{row.tid}}">删除</a>
            </th>
            <th>
                <a onclick="th_edit(this);">对话框编辑</a>
            </th>
        </tr>
        {%endfor%}
        </tbody>
    </table>
</div>
<div id="shadow" class="f_shadow f_hide"></div>
<div id="loading" class="loading2 f_hide"></div>
<div id="modal" class="f_modal f_hide">
    <span id="errormsg" class="f_hide"></span>
    <p>教师姓名：
        <input id="th_name_add" type="text" required="required">
    </p>
    <p>任课班级(多选):</p>
    <p>
        <select id="class_ids_add" multiple="multiple" size="5">
<!--            这里用动态js加载的方法添加option-->
        </select>
    </p>
    <input type="button" value="提交" id="AjaxSend">
    <input type="button" value="取消" id="CanelModal">
</div>

<!--    编辑教师任教信息-->
<div id="editmodal" class="f_modal f_hide">
    <span id="errormsg" class="f_hide"></span>
    <p>教师姓名：
        <input id="th_name_edit" type="text" required="required">
    </p>
    <p>任课班级(多选):</p>
    <p>
        <select id="class_ids_edit" multiple="multiple" size="5">
<!--            这里用动态js加载的方法添加option-->
        </select>
    </p>
    <input type="button" value="提交" id="AjaxSend">
    <input type="button" value="取消" id="CanelModal">
</div>

<script src="https://apps.bdimg.com/libs/jquery/2.1.4/jquery.min.js"></script>
<!--    addModalTeacherInfo-->
<script>
    $(function () {
        showmodal();
        cleanmodal();
        ajaxsend();
    })

    function cleanmodal(){
        $('#CanelModal,#shadow').click(function () {
            $('#shadow,#modal,#editmodal').addClass('f_hide');
        });
    }

    function showmodal(){
        $('#ShowModal').click(function () {
            $('#shadow,#loading').removeClass('f_hide');
            $.ajax({
                url:'/get_class_list/',
                type:'GET',
                dataType:'JSON',
                success:function (arg) {
                    // 上面的datatype已经声明了数据是json，所以就不再转换了
                    // arg = JSON.parse(arg);
                    $.each(arg,function (i,row) { //i 是索引  row 是内容
                        let tag = document.createElement('option');//生成标签
                        tag.innerHTML = row.class_name; //设置值
                        tag.setAttribute('value',row.id);   //设置属性
                        $('#class_ids_add').append(tag); //将标签添加到网页
                    });
                    $('#loading').addClass('f_hide');
                    $('#modal').removeClass('f_hide');

                }
            });
        });
    }

    function ajaxsend(){
        $('#AjaxSend').click(function () {
            let th_name = $('#th_name_add').val();
            let class_ids = $('#class_ids_add').val();
            console.log(class_ids)
            $.ajax({
                url:'/add_teacherinfo_m/',
                type:'POST',
                data:{'th_name':th_name,'class_ids': class_ids},
                traditional:true,//不对data做特殊处理，否则class_ids列表会被当作字符串
                success:function (arg) {
                    arg = JSON.parse(arg);
                    if (arg.status)
                        location.reload();
                    else {
                        $('#errormsg').removeClass('f_hide');
                        $('#errormsg').text(arg.message);
                    }
                }
            })
        });
    }
<!--    editModalTeacherInfo-->
    function th_edit(ths) {
            $('#shadow,#editmodal').removeClass('f_hide');
            let v = $(ths).parent().prevAll();
            let th_id = $(v[3]).text();
            $('#th_name_edit').val($(v[2]).text());
            $.ajax({
                url:'/edit_teacherinfo_m/',
                type:'GET',
                data:{'th_id':th_id},
                success:function (arg) {
                    arg = JSON.parse(arg);
                    console.log(arg[0]);

                }
            })



    }

</script>

</body>
</html>