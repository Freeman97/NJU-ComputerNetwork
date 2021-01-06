// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue';
//<link rel="stylesheet" href="https://unpkg.com/vxe-table/lib/index.css"></link>
import App from './App';//引入了一个组件
import router from './router';
import 'xe-utils';
import ElementUI from 'element-ui';
import 'element-ui/lib/theme-chalk/index.css';
import iView from 'iview';
import 'iview/dist/styles/iview.css';
import 'vue-easytable/libs/themes-base/index.css';
import {VTable,VPagination} from 'vue-easytable';
Vue.use(iView);
Vue.config.productionTip = false;
Vue.use(ElementUI); //注册使用element模块
Vue.component(VTable.name, VTable);
Vue.component(VPagination.name, VPagination);
//引入axios
import axios from 'axios';
Vue.prototype.$ajax = axios;
Vue.config.productionTip = false;
Vue.prototype.$http = axios;
// axios.defaults.baseURL = "https://www.liulongbin.top:8888/api/private/v1/";
// axios.defaults.withCredentials = true; // 允许携带cookie



Vue.config.productionTip = false;

//配置导航守卫
router.beforeEach((to, from, next) => {
  // ...
  // console.log('to',to);
  // console.log('from',from);

  next(true);
});
router.afterEach((to, from) => {
  // ...
  if(from.fullPath == '/loginRegister'){
    //alert('页面信息保存成功！');
  }
});
import store from './store/index';



Vue.config.productionTip = false

/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  store,
  components: { App },
  template: '<App/>'
})
