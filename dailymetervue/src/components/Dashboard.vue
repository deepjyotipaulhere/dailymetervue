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
      </div>
  </div>
</template>

<script>
export default {

}
</script>

<style>

</style>
