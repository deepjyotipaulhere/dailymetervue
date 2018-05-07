<template>
    <div>
        <div style="background:url('/static/image/home.jpg');background-size:cover;min-height:80vh;background-position:center">
            <div class="container" style="padding-top:30px;">
                <h2 style="margin:0;color:white">Welcome to Dailymeter</h2>
                <p style="margin:0;color:white">Forever Memories</p>
            </div>
        </div>
        <div style="padding-top:30px;">
            <div class="container">
                <div class="row">
                <div class="card black">
                    <div class="card-tabs">
                        <ul class="tabs tabs-fixed-width">
                            <li class="tab"><a href="#test4">Log In</a></li>
                            <li class="tab"><a href="#test6">Sign Up</a></li>
                        </ul>
                    </div>
                    <div class="card-content grey lighten-4">
                        <div id="test4">
                            <form>
                                <div class="input-field col s12">
                                    <input id="email" type="email" style="font-family:'Zilla'">
                                    <label for="email">Email</label>
                                </div>
                                <div class="input-field col s12">
                                    <input id="pwd" type="password">
                                    <label for="pwd">Password</label>
                                </div>
                                <br>
                                <button class="btn btn-large black waves-effect waves-light">Sign In</button>
                            </form>
                        </div>
                        <div id="test6">Test 3</div>
                    </div>
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

        }
    },
    methods:{
        create(){
            $(document).ready(function(){
                $('.tabs').tabs();
            });
        }
    },
    created(){
            this.create();
    }
}
</script>

<style>

</style>
