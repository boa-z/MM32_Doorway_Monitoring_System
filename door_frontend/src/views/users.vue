<script setup>
import axios from 'axios'
import { reactive, ref, onMounted } from "vue";
import { ElMessageBox } from 'element-plus'

const currentPath = ref(window.location.hash)

window.addEventListener('hashchange', () => {
    currentPath.value = window.location.hash
})

// 关于users的操作

const users = reactive([])
const getUsers = () => {
    axios.get("http://127.0.0.1:5000/users",).then(res => {
        users.splice(0, users.length)
        users.push(...res.data.results)
        console.log('更新数据')
    })
}

// 页面渲染之后添加数据
onMounted(() => {
    getUsers()
})

// 删除数据
const handleDelete = (index, scope) => {
    axios.delete(`http://127.0.0.1:5000/guests/${scope.id}`).then(() => {
        getUsers()
    })
}

/*表单添加*/
const add_dialog_visible = ref(false)
const ruleFormRef = ref()
const user_form = reactive({
    user_name: "",
    user_password: "",
    user_type: "",
    id: "",
})
// 表单提交事件
const submitForm = (formEl) => {
    axios.post('http://127.0.0.1:5000/users', user_form).then(() => {
        add_dialog_visible.value = false
        formEl.resetFields()
        getUsers()
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
            done()
        })
        .catch(() => { })
}

/*编辑表单*/
const editFormRef = ref()
const edit_dialog_visible = ref(false)
const handleEdit = (index, scope) => {
  for (let key in scope) {
    user_form[key] = scope[key]
  }
  edit_dialog_visible.value = true
}
// 编辑提交按钮
const submitEditForm = (formEl) => {
  axios.put(`http://127.0.0.1:5000/users/${user_form.id}`, user_form).then((res) => {
    formEl.resetFields()
    edit_dialog_visible.value = false
    getStudents()
  })
}

// 表单验证规则
const rules = reactive({
    user_name: [
        { required: true, message: '请输入用户名', trigger: 'blur' },
        { min: 2, max: 10, message: '长度在 2 到 10 个字符', trigger: 'blur' }
    ],
    user_password: [
        { required: true, message: '请输入密码', trigger: 'blur' },
        { min: 2, max: 10, message: '长度在 2 到 10 个字符', trigger: 'blur' }
    ],
    user_type: [
        { required: true, message: '请选择用户类型', trigger: 'blur' },
    ],
})

</script>

<template>
    <div style="margin: 0 auto; width: 100%;">
        <h1 style="text-align: center;">用户管理</h1>

        <!-- 添加用户按钮-->
        <el-button type="primary" @click="add_dialog_visible = true" size="small">添加用户</el-button>

        <!-- 数据表格 -->
        <el-table :data="users" style="margin: 20px auto;">
            <el-table-column label="用户id" prop="id" />
            <el-table-column label="门禁卡编号" prop="card_number" />
            <el-table-column label="用户姓名" prop="guest_name" />
            <el-table-column label="用户类型" prop="guest_type" />
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
        <el-dialog title="添加记录" v-model="add_dialog_visible" width="30%" :before-close="handleClose">
            <el-form ref="ruleFormRef" :model="user_form" status-icon label-width="120px" class="demo-ruleForm">
                <el-form-item label="门禁卡编号" prop="card_number">
                    <el-input v-model="user_form.card_number" autocomplete="off" />
                </el-form-item>
                <el-form-item label="用户姓名" prop="guest_name">
                    <el-input v-model="user_form.guest_name" autocomplete="off" />
                </el-form-item>
                <el-form-item label="用户类型" prop="guest_type">
                    <el-input v-model="user_form.guest_type" autocomplete="off" />
                </el-form-item>

                <el-form-item>
                    <el-button type="primary" @click="submitForm(ruleFormRef)">提交</el-button>
                    <el-button @click="resetForm(ruleFormRef)">重置</el-button>
                </el-form-item>
            </el-form>
        </el-dialog>

        <!-- 编辑图书页面 -->
        <el-dialog title="编辑访客记录" v-model="edit_dialog_visible" width="30%" :before-close="handleClose">
            <el-form ref="editFormRef" :model="user_form" status-icon label-width="120px" class="demo-ruleForm">
                <el-form-item label="门禁卡编号" prop="card_number">
                    <el-input v-model="user_form.card_number" autocomplete="off" />
                </el-form-item>
                <el-form-item label="用户姓名" prop="guest_name">
                    <el-input v-model="user_form.guest_name" autocomplete="off" />
                </el-form-item>
                <el-form-item label="用户类型" prop="guest_type">
                    <el-input v-model="user_form.guest_type" autocomplete="off" />
                </el-form-item>
                <el-form-item>
                    <el-button type="primary" @click="submitEditForm(editFormRef)">提交</el-button>
                    <el-button @click="resetForm(editFormRef)">重置</el-button>
                </el-form-item>
            </el-form>
        </el-dialog>
    </div>
</template>