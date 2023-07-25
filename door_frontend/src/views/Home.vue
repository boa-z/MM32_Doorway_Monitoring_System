<template>
  <div style="margin: 0 auto;width: 50%;">
    <h1 style="text-align: center">admin 登陆</h1>
    <el-form>
      <el-form-item label="账号">
        <el-input v-model="username" />
      </el-form-item>

      <el-form-item label="密码">
        <el-input v-model="password" type="password" />
      </el-form-item>
    </el-form>
    <div class="login-btn">
      <el-button type="primary" @click="onSubmit">确认</el-button>
      <el-button @click="onReset">重置</el-button>
    </div>
    <p class="login-tips">Tips : 默认账号密码为 admin</p>
  </div>
</template>
  
<script>

import { ElForm, ElFormItem, ElInput, ElButton } from 'element-plus'

export default {
  components: {
    ElForm, ElFormItem, ElInput, ElButton
  },
  data() {
    return {
      username: '',
      password: ''
    }
  },
  methods: {
    onSubmit() {
      // 登录逻辑
      this.$message.success('登录成功')
      // this.$router.push('#/guests')
    },
    onReset() {
      this.username = ''
      this.password = ''
    }
  }
}
</script>

<style scoped>
.login-btn {
  text-align: center;
}

.login-btn button {
  width: 25%;
  height: 36px;
  margin-bottom: 10px;
}

.login-tips {
  line-height: 30px;
  color: #0077ff;
}
</style>
