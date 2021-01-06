<!--<template>
  <div id="app">
    <h1>请输入您希望配置的IP地址信息：</h1>
    <p>路由器A的IP地址 : <input type="text" v-model="msg1"></p>
    <p></p>
    <p>路由器B的IP地址 : <input type="text" v-model="msg2"></p>
    <p></p>
    <p>路由器C的IP地址 : <input type="text" v-model="msg3"></p>
    <p></p>
    <p>交换机D的IP地址 : <input type="text" v-model="msg4"></p>
    <p></p>
    <p>你的输入信息如下所示：</p>
    <p>IP1 : {{msg1}}</p>
    <p>IP2 : {{msg2}}</p>
    <p>IP3 : {{msg3}}</p>
    <p>IP4 : {{msg4}}</p>
    <p>如果正确，请点击确定，将信息发送到服务器</p>
    <p>然后进入命令区跟随指示执行相应命令</p>
    <button @click="init">确定✅</button>  
  </div>
</template>

<script>
export default {
  name: 'app',
  data () {
    return {
      msg1: '',
      msg2: '',
      msg3: '',
      msg4: '',

    }
  },
   methods:{
      'init': function () {
                var _this = this            //这里 吧this 赋值给_this
                this.$http.request({
                //向下面的地址发送get请求
                url:'http://127.0.0.1:80/router/',        //url 指向的是后端发送请求的接口
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
-->
<template>
    <div class="goShopping">
        <div class="main">
            <el-card class="box-card">
                <div slot="header" class="clearfix">
                    <div v-for="(item,index) in cmdArr" :key="index" class="text item">
                        <el-button
                            type="success"
                            style="width:100%; height:40px; margin:5px 0 "
                            @click="setActiveItem(item)"
                        >{{item.title}}</el-button>
                    </div>

                    <!-- <el-input type="textarea" :rows="6" placeholder="请输入IP地址" v-model="textarea"></el-input> -->
                </div>

                <el-form v-show="activeItem!==''" ref="form" :model="form" label-width="100px">
                    <el-form-item v-show="activeItem.id!=6" label="路由器名称">
                        <el-radio-group label="12131" v-model="url[0]">
                            <el-radio label="A" name="router">A</el-radio>
                            <el-radio label="B" name="router">B</el-radio>
                            <el-radio label="C" name="router">C</el-radio>
                        </el-radio-group>
                    </el-form-item>
                    <el-form-item v-show="activeItem.id==1||activeItem.id==2" label="接口类型">
                        <el-radio-group v-model="url[1]">
                            <el-radio label="f" name="interfaceType">快速以太网</el-radio>
                            <el-radio label="s" name="interfaceType">串行接口</el-radio>
                        </el-radio-group>
                    </el-form-item>
                    <el-form-item v-show="activeItem.id==1||activeItem.id==2" label="第几个接口">
                        <el-radio-group v-model="url[2]">
                            <el-radio label="0" name="interfaceId">0</el-radio>
                            <el-radio label="1" name="interfaceId">1</el-radio>
                        </el-radio-group>
                    </el-form-item>
                    <el-form-item v-show="activeItem.id==1||activeItem.id==6" label="ipAddress">
                        <el-input v-model="form.ipAddress" placeholder="请输入ipAddress"></el-input>
                    </el-form-item>
                    <el-form-item v-show="activeItem.id==1" label="subnetMask">
                        <el-input v-model="form.subnetMask" placeholder="请输入subnetMask"></el-input>
                    </el-form-item>
                    <el-button type="primary" style="width:100%; height:40px;" @click="onSubmit">提交</el-button>
                </el-form>
                <div v-show="resData.length>0">
                    <div v-for="(item,index) in resData" :key="index">{{item}}</div>
                </div>
            </el-card>
        </div>
    </div>
</template>

<script>
import "../../home.css";
export default {
    name: "GoShopping",
    data() {
        return {
            // 表单实例
            form: {
                ipAddress: "",
                subnetMask: ""
            },
            // 路由选择
            url: [""+""+""],
            // 命令数组
            cmdArr: [
                {
                    id: 1,
                    title: "配置单个路由器上指定接口的IP地址和子网掩码",
                    key: "router"
                },
            ],
            // 选中命令
            activeItem: "",
            // 返回数据
            resData: ""
        };
    },
    methods: {
        onSubmit() {
            let params = this.url.join("");
            switch (this.activeItem.id) {
                case 1:
                    params +=`-${this.form.ipAddress}-${this.form.subnetMask}`;
                    break;
                case 6:
                    params = `${this.form.ipAddress}`;
                    break;
            }
            console.log(params);
            this.$http
                .get("http://127.0.0.1:80/api/", {
                    params: {
                        //opr: this.activeItem.key,
                        params
                    }
                })
                .then(res => {
                    this.resData = JSON.stringify(res.data).split(",");
                    console.log(this.resData);
                });
        },
        setActiveItem(item) {
            this.activeItem = item;
            this.url = [];
            this.resData = "";
            this.form = {
                ipAddress: "",
                subnetMask: ""
            };
        }
    }
};
</script>
<style >
</style>

