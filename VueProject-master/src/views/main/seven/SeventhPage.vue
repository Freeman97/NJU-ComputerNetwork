<template>
    <div class="about">
        <h1>动态路由网络拓扑图显示：</h1> 
        <p v-for="course in course_list">{{course}}</p>
        <button @click="init">刷新</button>         
    </div>  
</template>

<script>
    export default {
        name: 'freecourse',
        data: function () {
            return {
                course_list: []             //这里设置为空就可以,数据驱动页面
            }
        },
        methods: {                          //这里就是axios 发送请求的实现
            'init': function () {
                var _this = this            //这里 吧this 赋值给_this
                this.$http.request({
                //向下面的地址发送get请求
                url:'http://127.0.0.1:8078/course/',        //url 指向的是后端发送请求的接口
                method:'get'                       //设置请求模式
            }).then(function (response) {
                //response.data才是真正的数据
                console.log(response.data)
                _this.course_list=response.data     //前面赋值给_this 拿到的数据给到course_list
            })
            }

        },
         mounted: function () {      //这段代码就是不需要点击事件了,当页面跳转到指定的,自动渲染页面了
            this.init()

        }
    }
</script>