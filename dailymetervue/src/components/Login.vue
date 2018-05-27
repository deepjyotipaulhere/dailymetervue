<template>
    <div>
        <div style="background:url('/static/image/home.jpg');background-size:cover;min-height:80vh;background-position:center">
            <div class="container" style="padding-top:30px;">
                <h2 style="margin:0;color:white">Dailymeter</h2>
                <p style="margin:0;color:white">Forever Memories</p>
            </div>
        </div>
        <div style="padding-top:30px;">
            <div class="container">
                <div class="row">
                    <div class="col s6 m6 l6">
                        <div class="card">
                            <div class="card-tabs">
                                <ul class="tabs tabs-fixed-width">
                                    <li class="tab"><a href="#login">Log In</a></li>
                                    <li class="tab"><a href="#signup">Register</a></li>
                                </ul>
                            </div>
                            <div class="card-content white">
                                <div id="login">
                                    <form>
                                        <div class="input-field col s12">
                                            <input id="email" type="email" style="font-family:'Zilla'" v-model="logindata.email">
                                            <label for="email">Email</label>
                                        </div>
                                        <div class="input-field col s12">
                                            <input id="pwd" type="password" v-model="logindata.pwd">
                                            <label for="pwd">Password</label>
                                        </div>
                                        <span v-if="loginInvalid" class="right alert"><span class="fa fa-exclamation-triangle"></span> Username and Password did not match</span>
                                        <br>
                                        <button v-if="!isLoginClicked" class="btn btn-large black waves-effect waves-light" @click="login">Sign In</button>
                                        <div v-else class="preloader-wrapper small active">
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
                                    </form>
                                </div>
                                <div id="signup">
                                    <form>
                                        <div class="input-field col s12">
                                            <input id="semail" type="email" style="font-family:'Zilla'" v-model="registerdata.email">
                                            <label for="semail">Email</label>
                                        </div>
                                        <div class="input-field col s12">
                                            <input id="spwd" type="password" v-model="registerdata.pwd">
                                            <label for="spwd">Password</label>
                                        </div>
                                        <div class="input-field col s12">
                                            <input id="cpwd" type="password">
                                            <label for="cpwd">Confirm Password</label>
                                        </div>
                                        <div class="input-field col s12">
                                            <input id="cname" type="text" v-model="registerdata.name">
                                            <label for="cname">Your Full Name</label>
                                        </div>
                                        <br>
                                        <center>
                                        <button v-if="!isRegisterClicked" class="btn btn-large black waves-effect waves-light" style="width:100%" @click="register">Register</button>
                                        <div v-else class="preloader-wrapper small active">
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
                                    </form>
                                </div>
                            </div>
                        </div>
                    </div>
                    <div class="col s6 m6 l6">
                        <h3>Diary Writing. Simplified.</h3>
                        <p>Title</p>
                    </div>
                </div>
            </div>
        </div>

        <div style="background:url('/static/image/home1.jpg');background-size:cover">
            <div class="container">
                <div class="row">
                    <div class="col s6 m6 l6" style="color:white">
                        <h2>Your Story</h2>
                        <p style="font-size:1.1em">Write your daily stories and store it in the cloud. Dailymeter can be your personal diary where you can write about moments, attach photos, audio and videos. Recreate your day digitally.</p>
                        <h2>Share Moments</h2>
                        <p style="font-size:1.1em">Share your one memorable day or the entire diary with friends in the popular social networks.</p>
                        <h2>Get a print</h2>
                        <p style="font-size:1.1em">You can order a printed copy of your diary and in a quality package at a resonable cost. That includes a disc containing your digital media.</p>
                    </div>
                </div>
                <br>
            </div>
        </div>
    </div>
</template>

<script>
export default {
    data(){
        return {
            logindata:{
                email:'',
                pwd:''
            },
            registerdata:{
                email:'',
                pwd:'',
                name:''
            },
            isRegisterClicked: false,
            isLoginClicked: false,
            loginInvalid: false
        }
    },
    methods:{
        register(){
            this.isRegisterClicked=true
            this.$http.post('http://149.56.14.83:5000/register',this.registerdata).then(response=>{
                if (response.data=="Duplicate Key")
                {
                    M.toast({html: 'Duplicate Key found!'})
                    this.isRegisterClicked=false
                }
                else
                {
                    this.$session.start()
                    this.$session.set("email",this.registerdata.email)
                    this.$session.set("name",this.registerdata.name)
                    this.$session.set("userid",response.data)
                    this.$router.push("/dashboard")
                }
            })
        },
        login(){
            this.isLoginClicked=true
            this.loginInvalid=false
            this.$http.post('http://149.56.14.83:5000/login',this.logindata).then(response=>{
                if (response.data=="invalid")
                {
                    this.isLoginClicked=false
                    this.loginInvalid=true
                }
                else
                {
                    var x=response.data
                    this.$session.start()
                    this.$session.set("email",this.logindata.email)
                    this.$session.set("name",x["name"])
                    this.$session.set("userid",x["uid"])
                    location.reload()
                }
            })
        }
    },
    created(){
        $(document).ready(function(){
            $('.tabs').tabs();
        });
        if (this.$session.exists()){
            window.location.replace('/#/dashboard')
        }
    }
}
</script>

<style>
.alert{
    padding: 1em;
    border: 1px solid black;
    border-radius: 3px
}
</style>

