<script setup>
import axios from 'axios'
import { reactive, ref, onMounted } from "vue";
import { UploadFilled } from '@element-plus/icons-vue'
import { ElMessageBox } from 'element-plus'

const currentPath = ref(window.location.hash)

const tableLayout = ref('fixed')

window.addEventListener('hashchange', () => {
    currentPath.value = window.location.hash
})

// 关于alarm的操作

const alarms = reactive([])
const getStudents = () => {
    axios.get("http://127.0.0.1:5000/alarms",).then(res => {
        alarms.splice(0, alarms.length)
        alarms.push(...res.data.results)
        console.log('更新数据')
    })
}
// 页面渲染之后添加数据
onMounted(() => {
    getStudents()
})

// 删除数据
const handleDelete = (index, scope) => {
    axios.delete(`http://127.0.0.1:5000/alarms/${scope.id}`).then(() => {
        getStudents()
    })
}

/*表单添加*/
const add_dialog_visible = ref(false)
const ruleFormRef = ref()
const alarm_form = reactive({
    alarm_photo: "",
    alarm_time: "",
    id: "",
})
// 表单提交事件
const submitForm = (formEl) => {
    axios.post('http://127.0.0.1:5000/alarms', alarm_form).then(() => {
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
        alarm_form[key] = scope[key]
    }
    edit_dialog_visible.value = true
}
// 编辑提交按钮
const submitEditForm = (formEl) => {
    axios.put(`http://127.0.0.1:5000/alarms/${alarm_form.id}`, alarm_form).then((res) => {
        formEl.resetFields()
        edit_dialog_visible.value = false
        getStudents()
    })
}

</script>

<template>
    <div style="margin: 0 auto;width: 100%;">
        <h1 style="text-align: center">警报管理</h1>
        <!--  添加记录按钮 -->
        <el-button type="primary" @click="add_dialog_visible = true" size="small">添加记录</el-button>

        <!-- 数据表格 -->
        <el-table :data="alarms" style="margin: 20px auto; " table-layout="fixed">
            <el-table-column label="警报时间" prop="alarm_time" />
            <el-table-column label="警报照片" prop="alarm_photo">
                <template #default="scope">
                    <el-image style="max-width: 100%; max-height: 100%" :src="scope.row.alarm_photo" alt="警报照片" />
                </template>
            </el-table-column>

            <el-table-column align="right" label="操作">
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
            <el-form ref="ruleFormRef" :model="alarm_form" status-icon label-width="120px" class="demo-ruleForm">
                <el-form-item label="警报时间" prop="alarm_time">
                    <el-input v-model="alarm_form.alarm_time" autocomplete="off" />
                </el-form-item>
                <el-form-item>
                    <el-button type="primary" @click="submitForm(ruleFormRef)">提交</el-button>
                    <el-button @click="resetForm(ruleFormRef)">重置</el-button>
                </el-form-item>
            </el-form>
        </el-dialog>

        <!-- 编辑图书页面 -->
        <el-dialog title="编辑记录" v-model="edit_dialog_visible" width="30%" :before-close="handleClose">
            <el-form ref="editFormRef" :model="alarm_form" status-icon label-width="120px" class="demo-ruleForm">
                <el-form-item label="警报时间" prop="alarm_time">
                    <el-input v-model="alarm_form.alarm_time" autocomplete="off" />
                </el-form-item>
                <el-form-item>
                    <el-button type="primary" @click="submitEditForm(editFormRef)">提交</el-button>
                    <el-button @click="resetForm(editFormRef)">重置</el-button>
                </el-form-item>
            </el-form>
        </el-dialog>
    </div>
</template>

<style scoped>
.demo-image .block {
    padding: 30px 0;
    text-align: center;
    border-right: solid 1px var(--el-border-color);
    display: inline-block;
    width: 20%;
    box-sizing: border-box;
    vertical-align: top;
}

.demo-image .block:last-child {
    border-right: none;
}

.demo-image .demonstration {
    display: block;
    color: var(--el-text-color-secondary);
    font-size: 14px;
    margin-bottom: 20px;
}
</style>
