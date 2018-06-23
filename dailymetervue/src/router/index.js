import Vue from 'vue'
import Router from 'vue-router'
import Login from '@/components/Login'
import Dashboard from '@/components/Dashboard'
import New from '@/components/New'
import Post from '@/components/Post'
import Logout from '@/components/Logout'

Vue.use(Router)

export default new Router({
  mode: 'history',
  routes: [
    {
      path: '/',
      name: 'Login',
      component: Login
    },
    {
      path: '/dashboard',
      name: 'Dashboard',
      component: Dashboard
    },
    {
      path: '/new',
      name: 'NewDoc',
      component: New
    },
    {
      path: '/post/:id',
      name: 'Post',
      component: Post
    },
    {
      path: '/logout',
      name: 'LogOut',
      component: Logout
    }
  ]
})
