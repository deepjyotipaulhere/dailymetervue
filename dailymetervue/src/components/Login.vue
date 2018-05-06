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
                    <div class="col s8">
                        <ul class="tabs tabs-fixed-width z-depth-1">
                            <li class="tab col s3"><a href="#test1" class="active">Login</a></li>
                            <li class="tab col s3"><a href="#test4">Signup</a></li>
                        </ul>
                    </div>
                    <div id="test1" class="col s8" style="padding-top:20px;">
                        <form>
                            <div class="input-field col s12">
                                <input id="email" type="text" class="validate">
                                <label for="email">Email</label>
                            </div>
                        </form>
                    </div>
                    <div id="test4" class="col s12">Test 4</div>
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
