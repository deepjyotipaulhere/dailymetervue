<template>
  <div>

    <ul id="dropdown1" class="dropdown-content">
        <li class="divider"></li>
        <li><router-link :to="{path:'/logout'}" class="red-text">Sign Out</router-link></li>
    </ul>
    <nav class="nav-extended" v-if="$session.exists()">
        <div class="nav-wrapper">
            <a href="#" class="brand-logo">Dailymeter</a>
            <a href="#" data-target="mobile-demo" class="sidenav-trigger"><i class="material-icons">menu</i></a>
            <ul id="nav-mobile" class="right hide-on-med-and-down">
                <li v-if="$session.exists()"><a class="dropdown-trigger" href="#!" data-target="dropdown1">{{ $session.get("name") }} <span class="fa fa-chevron-down"></span></a></li>
            </ul>
        </div>
        <!--
        <div class="nav-content">
            <ul class="tabs tabs-transparent">
                <li class="tab"><a href="#test1">Test 1</a></li>
                <li class="tab"><a class="active" href="#test2">Test 2</a></li>
                <li class="tab"><a href="#test4">Test 4</a></li>
            </ul>
        </div>
        -->
    </nav>
    <!--
    <ul class="sidenav" id="mobile-demo">
        <li><a href="sass.html">Sass</a></li>
        <li><a href="badges.html">Components</a></li>
        <li><a href="collapsible.html">JavaScript</a></li>
    </ul>

    <div id="test1" class="col s12">Test 1</div>
    <div id="test2" class="col s12">Test 2</div>
    <div id="test3" class="col s12">Test 3</div>
    <div id="test4" class="col s12">Test 4</div>
    -->
  </div>
</template>

<script>
export default {
    created:function(){
        $(document).ready(function(){
            $(".dropdown-trigger").dropdown({coverTrigger:false});
        });
    }
};
</script>

<style>

</style>
