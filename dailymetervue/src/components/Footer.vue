<template>
  <div>
            <footer class="page-footer">
                <div class="container" v-if="!$session.exists()">
                    <div class="row">
                    <div class="col l6 s12">
                        <h5 class="white-text">Follow Us</h5>
                        <p class="grey-text text-lighten-4">Follow us in Twitter</p>
                    </div>
                    <div class="col l4 offset-l2 s12">
                        <h5 class="white-text">Links</h5>
                        <ul>
                        <li><a class="grey-text text-lighten-3" href="#!">Link 1</a></li>
                        <li><a class="grey-text text-lighten-3" href="#!">Link 2</a></li>
                        <li><a class="grey-text text-lighten-3" href="#!">Link 3</a></li>
                        <li><a class="grey-text text-lighten-3" href="#!">Link 4</a></li>
                        </ul>
                    </div>
                    </div>
                </div>
                <div class="footer-copyright">
                    <div class="container">
                        <h6 class="grey-text text-darken-3 center" href="#!">&copy; Dailymeter</h6>
                    </div>
                </div>
            </footer>
        </div>
</template>

<script>
export default {

}
</script>

<style>
footer {
    position: relative;;
   bottom:0;
   width:100%;
}
</style>
