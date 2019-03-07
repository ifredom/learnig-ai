import Router from 'vue-router';
import Vue from 'vue';

Vue.use(Router);

const routes = [
  {
    path: '/LinearModel',
    name: 'LinearModel',
    component: r => require.ensure([], () => r(require('@/pages/LinearModel')), 'LinearModel')
  },
  {
    path: '/PosenetModel',
    name: 'PosenetModel',
    component: r => require.ensure([], () => r(require('@/pages/PosenetModel')), 'PosenetModel')
  }
];

export default new Router({
  base: '/',
  mode: 'hash',
  routes
});
