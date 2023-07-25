<script setup>
import { reactive, ref, onMounted, computed } from "vue";
import Home from './views/Home.vue'
import About from './views/About.vue'
import NotFound from './views/NotFound.vue'
import Guests from './views/guests.vue'
import Users from './views/users.vue'
import Alarms from './views/alarms.vue'
import { ElMessageBox } from 'element-plus'

const routes = {
  '/': Home,
  '/about': About,
  '/guests': Guests,
  '/users': Users,
  '/alarms': Alarms
}
const currentPath = ref(window.location.hash)

window.addEventListener('hashchange', () => {
  currentPath.value = window.location.hash
})

const currentView = computed(() => {
  return routes[currentPath.value.slice(1) || '/'] || NotFound
})
</script>

<template>
  <div style="margin: 0 auto;width: 75%;">
    <el-container>
      <el-header>
        <el-menu
          mode="horizontal"
          router
          
          @select="handleSelect"
        >
          <el-menu-item><el-link href="#/">Home</el-link></el-menu-item>
          <el-menu-item><el-link href="#/about">About</el-link></el-menu-item>
          <el-menu-item><el-link href="#/guests">Guests</el-link></el-menu-item>
          <el-menu-item><el-link href="#/users">Users</el-link></el-menu-item>
          <el-menu-item><el-link href="#/alarms">Alarms</el-link></el-menu-item>
        </el-menu>
      </el-header>
      <el-main>
        <router-view></router-view>
      </el-main>
    </el-container>
    <component :is="currentView" />
  </div>
</template>

<style scoped>
.el-header {
  background-color: #b3c0d1;
  color: #333;
  line-height: 60px;
}
</style>
