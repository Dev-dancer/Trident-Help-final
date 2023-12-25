let clicker=document.getElementsByClassName("vector-wrapper");
let green=document.getElementsByClassName("sel");
let proceed=document.getElementsByClassName("proceed");
clicker[0].addEventListener('click',()=>{
    console.log("hi");
    // if(clicker[0].style.display==='block'){
        clicker[0].style.display='none';
        // clicker[0].style.visibility='hidden';
        green[0].style.display='block';
        proceed[0].style.display='block';
    // }
})
green[0].addEventListener('click',()=>{
    if(clicker[0].style.display==='none'){
        clicker[0].style.display='block';
        green[0].style.display='none';
        proceed[0].style.display='none';
    }
})