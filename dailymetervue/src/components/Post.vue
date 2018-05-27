<template>
    <div>
        <div class="container">
            <br>
            <router-link :to="{path:'/dashboard'}">
                <b class="black-text"><span class="fa fa-chevron-left"></span> Back to posts</b>
            </router-link>
        </div>
    <center v-if="!isLoaded">
        <div class="preloader-wrapper small active">
            <div class="spinner-layer spinner-green-only" style="border-color:#000">
                <div class="circle-clipper left">
                    <div class="circle"></div>
                </div><div class="gap-patch">
                    <div class="circle"></div>
                </div><div class="circle-clipper right">
                    <div class="circle"></div>
                </div>
            </div>
        </div>
    </center>
    <div class="container" v-else>
        <h2>{{title}}</h2>
        <h6>By <b>{{by}}</b></h6>
        <label>{{date}}</label>
        <p v-html="post"></p>
    </div>
  </div>
</template>

<script>
export default {
    data(){
        return {
            title:'',
            date:'',
            post:'',
            by:'',
            isLoaded: false
        }
    },
    created:function(){
        this.getpost()
    },
    methods:{
        getpost(){
            this.$http.get('http://149.56.14.83:5000/post/'+this.$route.params.id).then(response=>{
                this.title=response.data.title
                this.post=response.data.post.replace(new RegExp("\\\\n", "g"), "<br />");
                this.date=response.data.date
                this.by=this.$session.get("name")
            }).then(()=>{
                this.isLoaded=true
            })
        }
    },
    computed:{
        getthispost(){
            return this.post.replace('\\n','<br>')
        }
    }
}
</script>

<style>

</style>
