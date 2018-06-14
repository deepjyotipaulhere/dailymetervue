<template>
    <div>
        
        <div class="fixed-action-btn">
            <a class="btn-floating tooltipped btn-large waves-effect waves-light blue darken-4" data-position="left" data-tooltip="Share on Facebook" :href=shareLink target="_blank"><span class="fa fa-facebook"></span></a>
        </div>
      
          
        <div class="container">
            <br>
            <router-link :to="{path:'/dashboard'}">
                <b class="black-text"><span class="fa fa-chevron-left"></span> Back to My Diary</b>
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
            isLoaded: false,
            shareLink: "https://www.facebook.com/sharer/sharer.php?u=" + window.location
        }
    },
    created:function(){
        this.getpost()
        $(document).ready(function(){
            $('.tooltipped').tooltip();
        });
      
    },
    methods:{
        getpost(){
            this.$http.get(this.$store.state.url+'/post/'+this.$route.params.id).then(response=>{
                this.title=response.data.title
                this.post=response.data.post.replace(new RegExp("\\\\n", "g"), "<br />");
                this.date=response.data.date
                this.by=this.$session.get("name")
                
                document.title=this.title+" by "+this.by+" | Dailymeter"
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
