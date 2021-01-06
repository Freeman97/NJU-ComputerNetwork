import Vue from 'vue'
import Router from 'vue-router'

//page
//const Main = r => require.ensure([], () => r(require('../views/main/Main')))
import Main from '../views/main/Main';
//const Main = () => import(/* webpackChunkName: "Main-page" */ '../views/main/Main');

import FirstPage from '../views/main/first/FirstPage'
//import Classify from '../views/main/goShoping/classify/Classify'
import SecondPage from '../views/main/second/SecondPage'
import ThirdPage from '../views/main/third/ThirdPage'
//import ShopName from '../views/main/myShop/shopName/ShopName'
//import ShopSet from '../views/main/myShop/shopSet/ShopSet'
import ForthPage from '../views/main/forth/ForthPage'
import SeventhPage from '../views/main/seven/SeventhPage'
import SixthPage from '../views/main/sixth/SixthPage'
import FifthPage from '../views/main/fifth/FifthPage'
//import MyOrder from '../views/main/userCenter/myOrder/MyOrder'
//import SetPage from '../views/main/userCenter/setPage/SetPage'
import LoginRegister from '../views/loginRegister/LoginRegister'
import Start from '../views/startPage/StartPage'
import ChangePassword from '../views/changePassword/ChangePassword'
import SetPassWord from '../views/changePassword/setPassWord/SetPassWord'
import GetCode from '../views/changePassword/getCode/GetCode'

//other
Vue.use(Router)

const routes = [
  {
    path: '/',
    name: 'Main',
    component: Main,
    children: [
      { path: '/',component: FirstPage },
      { path: '/firstPage',component: FirstPage },
      { path: '/secondPage',component: SecondPage },
      { path: '/thirdPage',component: ThirdPage },
      { path: '/forthPage',component: ForthPage },
      { path: '/sixthPage',component: SixthPage },
      { path: '/fifthPage',component: FifthPage },
      { path: '/seventhPage',component: SeventhPage }
    ]
  }
  ,{
    path: '/loginRegister',
    component:LoginRegister
  },{
    path: '/start',
    component: Start
  },{
    path: '/changePassword',
    component: ChangePassword
  },{
    path: '/setpassword',
    component: SetPassWord
  },{
    path: '/getcode',
    component: GetCode
  },{
    path: '*',
    redirect: '/loginRegister'
  }
]
export default new Router({
  routes: routes,
  scrollBehavior (to, from, savedPosition) {
    return { x: 0, y: 0 }
  }
})
