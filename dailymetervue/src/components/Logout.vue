<template>
    
</template>

<script>
export default {
    created:function(){
        this.$session.destroy();
        window.location.replace('/')
    }
}
</script>

<style>

</style>
