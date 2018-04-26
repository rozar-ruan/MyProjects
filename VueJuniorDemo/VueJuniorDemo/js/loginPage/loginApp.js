///<reference path="../lib/vue.js"/>
var loginFormApp = new Vue({
    el: "#loginApp",
    data: {
        name: "",
        pwd:""
    },
    methods: {
        doLogin: function () {
            alert("name:" + this.name + ";pwd:" + this.pwd);
            // 在此处提交给后台
        }
    }
});