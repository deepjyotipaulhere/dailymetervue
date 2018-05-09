<template>
    <div class="container">
        <form>
            <br>
            <div class="row">
                <div class="col m9 s9">
                    
                </div>
                <div class="col l3 m3 s12">
                    <input id="dateselect" type="text" class="datepicker col s1 m1 l1" style="border:none;font-size:2em;font-family:'Bebas';height:auto;width:100%;text-align:center" @select="check" placeholder="Date of this story">
                </div>
            </div>
            <div class="row">
                <input type="text" placeholder="Enter Title" style="border:none;font-size:4em;font-family:'Bebas';height:auto" class="col s12 m12 l12" />
            </div>
            <textarea placeholder="Start typing your story..." style="border:none;font-family:'ZillaRegular';font-size:larger;height:auto !important;outline:none" rows="30"></textarea>
            <div class="row">
                <div class="col l4 m4"></div>
                <div class="col l4 m4 s12">
                    <button class="btn btn-large black waves-effect waves-light" style="width:100%">Post</button>
                </div>
                <div class="col l4 m4"></div>
            </div>
            
        </form>
    </div>
</template>

<script>
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
        }
    },
    data(){
        return {
            date:''
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
