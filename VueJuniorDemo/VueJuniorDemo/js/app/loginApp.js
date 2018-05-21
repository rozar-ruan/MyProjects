///<reference path="../lib/vue.js"/>
///<reference path="../lib/jquery-1.9.0.min.js"/>
var loginApp = new Vue({
    el: "#loginApp",
    data: {
        name: "",
        pwd: "",
        dataFrameSrc:"",
        canLogin: false,
        bookList: {
            "book1": "中国通史",
            "book2": "走近科学",
            "book4": "再读周树人",
            "book3":"听风煮雨"
        },
        userStatus: 0,
        hour: 0,
        minute: 0
    },
    computed: {
        WelcomeMsg: function () {
            return "欢迎您，" + this.name;
        },
        LoginStatus: {
            set: function (value) {
                this.userStatus = value;
            },
            get: function () {
                switch (this.userStatus) {
                    case 0: return "读者";
                    case 1: return "职工";
                    case 2: return "管理员";
                    default: return "用户状态异常";
                }
            }
        },
        Hour: {
            set: function (value) {
                this.hour = value;
                this.minute = value * 60;
            },
            get: function () {
                return this.hour;
            }
        },
        Minute: {
            set: function (value) {
                this.minute = value;
                this.hour = value / 60;
            },
            get: function () {
                return this.minute;
            }
        }
    },
    methods: {
        doLogin: function () {
            $.post("../Handler/HandlerDemo.ashx?type=login", { name: this.name, pwd: this.pwd }, function (data) {
                debugger;
                if (data == "success") {
                    alert("登陆成功！");
                    this.canLogin = true;
                    // 回掉方法中，this 不再指向到 vue 自己，改用app名字访问才行
                    loginApp.showFrame();
                    return true;
                } else {
                    alert("验证失败！");
                    this.canLogin = false;
                }
            });
            //if (this.name.length==this.pwd.length) {
            //    alert("登陆成功！");
            //    window.location = "https://www.baidu.com"; // 不能通过这种方式跳转，那要咋办？
            //    this.canLogin = true;
            //    this.showFrame();
            //    return true;
            //}
            //alert("验证失败！");
            //this.canLogin = false;
            //return false;
             //在此处提交给后台
        },
        showFrame: function () {
            this.dataFrameSrc = "DataShow.html";
        }
    },
    watch: {
        kilos: function (value) {

        }
    }
});