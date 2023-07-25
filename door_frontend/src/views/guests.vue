<script setup>
import axios from 'axios'
import { reactive, ref, onMounted } from "vue";
import { ElMessageBox } from 'element-plus'

const currentPath = ref(window.location.hash)

window.addEventListener('hashchange', () => {
  currentPath.value = window.location.hash
})

// 关于guests的操作

const guests = reactive([])
const getStudents = () => {
  axios.get("http://127.0.0.1:5000/guests",).then(res => {
    guests.splice(0, guests.length)
    guests.push(...res.data.results)
    console.log('更新数据')
  })
}
// 页面渲染之后添加数据
onMounted(() => {
  getStudents()
})

// 删除数据
const handleDelete = (index, scope) => {
  axios.delete(`http://127.0.0.1:5000/guests/${scope.id}`).then(() => {
    getStudents()
  })
}

/*表单添加*/
const add_dialog_visible = ref(false)
const ruleFormRef = ref()
const guest_form = reactive({
  card_number: "",
  guest_name: "",
  guest_type: "",
  guest_time: "", // 不需要填写
  guest_login_type: "",
  id: "", // 不需要填写
})
// 表单提交事件
const submitForm = (formEl) => {
  axios.post('http://127.0.0.1:5000/guests', guest_form).then(() => {
    add_dialog_visible.value = false
    formEl.resetFields()
    getStudents()
  })
}
// 重置表单
const resetForm = (formEl) => {
  formEl.resetFields()
}

// 关闭弹窗前确认
const handleClose = (done) => {
  ElMessageBox.confirm('确认关闭？')
    .then(() => {
      done();
    })
    .catch(() => {
    });
}

/*编辑表单*/
const editFormRef = ref()
const edit_dialog_visible = ref(false)
const handleEdit = (index, scope) => {
  for (let key in scope) {
    guest_form[key] = scope[key]
  }
  edit_dialog_visible.value = true
}
// 编辑提交按钮
const submitEditForm = (formEl) => {
  axios.put(`http://127.0.0.1:5000/guests/${guest_form.id}`, guest_form).then((res) => {
    formEl.resetFields()
    edit_dialog_visible.value = false
    getStudents()
  })
}

</script>

<template>
  <div style="margin: 0 auto;width: 100%;">

    <h1 style="text-align: center">访客管理</h1>
    <!--  添加记录按钮 -->
    <el-button type="primary" @click="add_dialog_visible = true" size="small">添加记录</el-button>

    <!-- 数据表格 -->
    <el-table :data="guests" style="margin: 20px auto;">
      <el-table-column label="门禁卡编号" prop="card_number" />
      <el-table-column label="名称" prop="guest_name" />
      <el-table-column label="访客类型" prop="guest_type" />
      <el-table-column label="登陆类型" prop="guest_login_type" />
      <el-table-column label="时间" prop="guest_time" />
      <el-table-column align="right" label="操作" width="200px">
        <template #default="scope">
          <el-button size="small" @click="handleEdit(scope.$index, scope.row)">
            编辑
          </el-button>
          <el-button size="small" type="danger" @click="handleDelete(scope.$index, scope.row)">
            删除
          </el-button>
        </template>
      </el-table-column>
    </el-table>
    <!-- 添加图书页面 -->
    <el-dialog title="添加记录" v-model="add_dialog_visible" width="30%" :before-close="handleClose">
      <el-form ref="ruleFormRef" :model="guest_form" status-icon label-width="120px" class="demo-ruleForm">
        <el-form-item label="门禁卡编号" prop="card_number">
          <el-input v-model="guest_form.card_number" autocomplete="off" />
        </el-form-item>
        <el-form-item label="名称" prop="guest_name">
          <el-input v-model="guest_form.guest_name" autocomplete="off" />
        </el-form-item>
        <el-form-item label="访客类型" prop="guest_type">
          <el-radio-group v-model="guest_form.guest_type" @change="handleChange" autocomplete="off">
            <el-radio-button :label="1">vip_1</el-radio-button>
            <el-radio-button :label="2">temp_2</el-radio-button>
          </el-radio-group>
        </el-form-item>
        <el-form-item label="登陆类型" prop="guest_login_type">
          <el-radio-group v-model="guest_form.guest_login_type" @change="handleChange" autocomplete="off">
            <el-radio-button :label="1">密码_1</el-radio-button>
            <el-radio-button :label="2">NFC_2</el-radio-button>
            <el-radio-button :label="3">人脸_3</el-radio-button>
          </el-radio-group>
        </el-form-item>
        <el-form-item>
          <el-button type="primary" @click="submitForm(ruleFormRef)">提交</el-button>
          <el-button @click="resetForm(ruleFormRef)">重置</el-button>
        </el-form-item>
      </el-form>
    </el-dialog>

    <!-- 编辑图书页面 -->
    <el-dialog title="编辑访客记录" v-model="edit_dialog_visible" width="30%" :before-close="handleClose">
      <el-form ref="editFormRef" :model="guest_form" status-icon label-width="120px" class="demo-ruleForm">
        <el-form-item label="门禁卡编号" prop="card_number">
          <el-input v-model="guest_form.card_number" autocomplete="off" />
        </el-form-item>
        <el-form-item label="名称" prop="guest_name">
          <el-input v-model="guest_form.guest_name" autocomplete="off" />
        </el-form-item>
        <el-form-item label="访客类型" prop="guest_type">
          <el-radio-group v-model="guest_form.guest_type" @change="handleChange" autocomplete="off">
            <el-radio-button :label="1">vip_1</el-radio-button>
            <el-radio-button :label="2">temp_2</el-radio-button>
          </el-radio-group>
        </el-form-item>
        <el-form-item label="登陆类型" prop="guest_login_type">
          <el-radio-group v-model="guest_form.guest_login_type" @change="handleChange" autocomplete="off">
            <el-radio-button :label="1">密码_1</el-radio-button>
            <el-radio-button :label="2">NFC_2</el-radio-button>
            <el-radio-button :label="3">人脸_3</el-radio-button>
          </el-radio-group>
        </el-form-item>
        <el-form-item label="时间" prop="guest_time">
          <el-input v-model="guest_form.guest_time" autocomplete="off" />
        </el-form-item>
        <el-form-item>
          <el-button type="primary" @click="submitEditForm(editFormRef)">提交</el-button>
          <el-button @click="resetForm(editFormRef)">重置</el-button>
        </el-form-item>
      </el-form>
    </el-dialog>
  </div>
</template>

<style scoped></style>
