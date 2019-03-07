<template>
  <div id="app">
    <div id="nav">
      <router-link to="/LinearModel">线性模型。</router-link> |
      <router-link to="/PosenetModel">海底小鱼根据人物动作跟随移动</router-link>
    </div>
    <router-view/>
  </div>
</template>

<style>
  #app {
    font-family: 'Avenir', Helvetica, Arial, sans-serif;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
    color: #2c3e50;
  }

  ul,
  ol,
  li {
    list-style: none;
  }
</style>