<template>
  <div>
      <div class="container-fluid">
        <div class="row">
            <div class="col m2 s12 l2">
                <router-link :to="{path:'/new'}">
                    <div class="card-panel black">
                        <span class="white-text">
                            <h1 class="center" style="font-size:4em;margin:0"><span class="fa fa-plus"></span></h1>
                            <h5 class="center" style="margin:0">Add New</h5>
                        </span>
                    </div>
                </router-link>
                
            </div>
        </div>
        <hr>
        <h3 class="center" style="margin:0;padding:0">My Diary</h3>
        <p class="center" style="margin:0;padding:0">{{ posts.length>0?posts.length+" pages":"" }}</p>
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


        <div v-else class="container">
            <div class="row">
                <div class="collection z-depth-1">
                    <router-link :to="{path:'/post/'+ post.postid}" href="#!" class="collection-item" :key="post.postid" v-for="(post,i) in posts">
                        <h4 style="margin:0">{{ post.title }}<span class="right">{{(i+1)}}</span></h4>
                        <p style="margin:0">{{ post.post }}...</p>
                        
                    </router-link>
                </div>
            </div>
        </div>
      </div>
  </div>
</template>

<script>
export default {
    data(){
        return {
            posts:[],
            isLoaded: false
        }
    },
    created:function(){
        this.getposts()
    },
    methods:{
        getposts(){
            this.$http.get(this.$store.state.url+'/getposts/'+this.$session.get("userid")).then(response=>{
                var xposts=response.data
                const dataarr=[]
                for (var x in xposts){
                    dataarr.push(xposts[x])
                }

                this.posts=dataarr
                this.isLoaded=true
            })
        }
    }
}
</script>

<style scoped>
.collection-item{
    border-left: 5px solid white;
}
.collection-item:hover{
    border-left: 5px solid black;
}
</style>
