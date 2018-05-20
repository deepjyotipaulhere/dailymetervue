<template>
  <div>
      <div class="container-fluid">
        <div class="row">
            <div class="col m3 s12 l3">
                <router-link :to="{path:'/new'}">
                    <div class="card-panel black">
                        <span class="white-text">
                            <h1 class="center" style="font-size:5em;margin:0"><span class="fa fa-plus"></span></h1>
                            <h5 class="center" style="margin:0">Add New</h5>
                        </span>
                    </div>
                </router-link>
                
            </div>
        </div>
        <hr>
        <h3 class="center">Your Days</h3>
        <div class="row">
            <div :key="post.postid" class="col m3 s12 l3" v-for="post in posts">
                <router-link :to="{path:'/post/'+ post.postid}">
                    <div class="card hoverable">
                        <div class="card-panel">
                            <span class="black-text">
                                <div style="min-height:150px">
                                    <h4 style="margin:0">{{ post.title }}</h4>
                                    <p style="margin:0">{{ post.post }}...</p>
                                </div>
                                <label class="text-muted right">{{ post.date }}</label>
                            </span>
                        </div>
                    </div>
                </router-link>
            </div>
        </div>
      </div>
  </div>
</template>

<script>
export default {
    data(){
        return {
            posts:[]
        }
    },
    created:function(){
        this.getposts()
    },
    methods:{
        getposts(){
            this.$http.get('http://149.56.14.83:5000/getposts/'+this.$session.get("userid")).then(response=>{
                var xposts=response.data
                const dataarr=[]
                for (var x in xposts){
                    dataarr.push(xposts[x])
                }

                this.posts=dataarr
            })
        }
    }
}
</script>

<style>

</style>
