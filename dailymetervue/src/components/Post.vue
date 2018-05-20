<template>
  <div>
      <div class="container">
        <label class="right">{{date}}</label>
        <h2>{{title}}</h2>
        <h6>By <b>{{by}}</b></h6>
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
            by:''
        }
    },
    created:function(){
        this.getpost()
    },
    methods:{
        getpost(){
            this.$http.get('http://localhost:5000/post/'+this.$route.params.id).then(response=>{
                this.title=response.data.title
                this.post=response.data.post.replace(new RegExp("\\\\n", "g"), "<br />");
                this.date=response.data.date
                this.by=this.$session.get("name")
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
