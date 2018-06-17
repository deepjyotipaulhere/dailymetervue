<template>
    <div class="container">
        <form>
            
                <div class="card" style="position:fixed;width:20%;float:right;bottom:0;right:0;z-index:5000">
                    <div class="card-image">
                        
                        <div class="collection" style="max-height:30vh;overflow-y:auto">
                            <a href="#!" class="collection-item">Alvin</a>
                            <a href="#!" class="collection-item active">Alvin</a>
                            <a href="#!" class="collection-item">Alvin</a>
                            <a href="#!" class="collection-item">Alvin</a>
                            <a href="#!" class="collection-item">Alvin</a>
                            <a href="#!" class="collection-item">Alvin</a>
                            <a href="#!" class="collection-item">Alvin</a>
                            <a href="#!" class="collection-item">Alvin</a>
                            <a href="#!" class="collection-item">Alvin</a>
                            <a href="#!" class="collection-item">Alvin</a>
                            <a href="#!" class="collection-item">Alvin</a>
                            <a href="#!" class="collection-item">Alvin</a>
                            <a href="#!" class="collection-item">Alvin</a>
                        </div>
                        <input class="btn-floating halfway-fab waves-effect waves-light black" type="file" multiple name="mediafile" @change="filesChange($event.target.name, $event.target.files)">
                        <!-- <a class="btn-floating halfway-fab waves-effect waves-light black"><i class="material-icons">add</i></a> -->
                    </div>
                    <div class="card-content">
                        <h5>Media Pallete</h5>
                    </div>
                </div>
            
            <br>
            <div class="row">
                <div class="col m9 s9">
                    
                </div>
                <div class="col l3 m3 s12">
                    <input id="dateselect" type="text" class="datepicker col s1 m1 l1" style="border:none;font-size:2em;font-family:'Bebas';height:auto;width:100%;text-align:center" @select="check" placeholder="Date of this story">
                </div>
            </div>
            <div class="row">
                <input type="text" placeholder="Enter Title" style="border:none;font-size:4em;font-family:'Bebas';height:auto" class="col s12 m12 l12" v-model="postdata.title" />
            </div>
            <textarea placeholder="Start typing your story..." style="border:none;font-family:'ZillaRegular';font-size:larger;height:auto !important;outline:none" rows="30" v-model="postdata.post"></textarea>
            <div class="row">
                <div class="col l4 m4"></div>
                <div class="col l4 m4 s12">
                    <button class="btn btn-large black waves-effect waves-light" style="width:100%" @click.prevent="createPost">Post</button>
                    <button class="btn btn-large black-text grey waves-effect waves-light" style="width:100%" @click.prevent="cancelpost">Cancel</button>
                </div>
                <div class="col l4 m4"></div>
            </div>
            
        </form>
    </div>
</template>

<script>
import axios from 'axios'
export default {
    created(){
        autosize($('textarea'));
        $(document).ready(function(){
            $('.datepicker').datepicker({
                format: 'ddd, mmm dd, yyyy'
            });
            $('#lbldate').click(function(){
                $('#dateselect').click();
            });
        });
    },
    methods:{
        check(){
            alert('sdgs')
        },
        createPost(){
            this.$http.post(this.$store.state.url+'/createpost', this.postdata).then(response=>{
                console.log("Ok")
            })
        },
        cancelpost(){
            if (confirm("Do you want to discard your post?"))
                this.$router.push('/dashboard')
        },
        filesChange(fieldName, fileList) {
            alert("Hello")
            const formData = new FormData();

            if (!fileList.length) return;

            Array
            .from(Array(fileList.length).keys())
            .map(x => {
                formData.append(fieldName, fileList[x], fileList[x].name);
            });

            // save it
            this.save(formData);
        },
        save(formData) {
            axios.post(this.$store.state.url+'/insertdoc', formData).then(response=>{
                console.log(response.data)
            })
        },
    },
    data(){
        return {
            postdata:{
                date:'',
                title:'',
                post:'',
                user: this.$session.get("userid")
            }
        }
    },
    computed:{
        getDate(){
            if ($('#dateselect').val()!='')
                this.date=$('#dateselect').val()
            else 
                this.date="Date"
        }
    }
}
</script>

<style>
</style>
