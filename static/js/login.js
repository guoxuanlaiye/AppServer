$(document).ready(function(){
    //  登录/注册按钮点击
    $("#commit-btn").click(function(){
        var data = {}
        var params = $("#login-form").serializeArray();
        $.each(params,function(){
            data[this.name] = this.value;
        });

        var url = "http://127.0.0.1:8998/users/";
        if ($(this).text() == "登录") {
            url = url+"login";
        } else {
            url = url+"regist";
        }
        console.log("请求参数 = "+JSON.stringify(data));
        $.post(url, JSON.stringify(data), function(data, status){
            alert("status = "+status+", data = "+data);
        });
    });
    // 注册按钮点击
    $(".regist-span").click(function(){
        if ($(this).text() == "注册") {
            $("#commit-btn").text("注册");
            var name = document.createElement("input");
            name.placeholder = "用户名";
            name.type = "text";
            name.name = "name";
            name.id = "user-name";
            $("#login-form").prepend(name);
            $(".title-span").text("");
            $(this).text("已有账号登录");
        } else {
            $("#user-name").remove();
            $("#commit-btn").text("登录");
            $(".title-span").text("没有账号?");
            $(this).text("注册");
        }
    });
});

