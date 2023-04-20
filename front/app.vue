<script>
export default {
    // 组件选项
    // 此处声明一些响应式状态
    data(){
        return{
            message:'Hello World!'
        }
    }
}
</script>

<template>
    <h1>Make me dynamic! {{message}}</h1>
</template>