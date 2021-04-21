
import Vue from 'vue'
import Router from 'vue-router'
import Home from '../views/Home.vue'
import About from '../views/About.vue'
import Login from '../views/Login.vue'
import Details from '../views/Details.vue'
import EditArticle from '../views/EditArticle.vue'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/', // path 设置为 “/” ，默认显示该页面
      component: Home,
      name: 'Home'
    },
    {
      path: '/about', // path 设置为 “/” ，默认显示该页面
      component: About,
      name: 'about'
    },
    {
      path: '/login',
      component: Login,
      name: 'login'
    },

    {
      path: '/details',
      component: Details,
      name: 'Details'
    },

    {
      path: '/edit',
      component: EditArticle,
      name: 'edit'
    }

  ],
  mode: 'history' // mode 设置为history ，去掉地址栏上的 # 号
})
