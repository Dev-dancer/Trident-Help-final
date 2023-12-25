let team_member_photo=document.getElementsByClassName("i");
// team_member_photo.forEach(tmp=>{
    let ins=document.querySelector(".insta-logo");
    let li=document.querySelector(".li");
    let gm=document.querySelector(".gm");
    //     tmp.addEventListener('click',()=>{
        //         ins.styles.display='block';
        //         li.styles.display='block';
        //         gm.styles.display='block';
        //     })
        // })
        let c=0;
team_member_photo[0].addEventListener('click',()=>{
    c=c+1;
    if(c%2!=0){
        ins.style.display='block';
        li.style.display='block';
        gm.style.display='block';
    }
    else{
        ins.style.display='none';
        li.style.display='none';
        gm.style.display='none';
    }
})
let d=0;
let ins2=document.querySelector(".insta-logo2");
let li2=document.querySelector(".li2");
let gm2=document.querySelector(".gm2");
team_member_photo[1].addEventListener('click',()=>{
    d=d+1;
    if(d%2!=0){
        ins2.style.display='block';
        li2.style.display='block';
        gm2.style.display='block';
    }
    else{
        ins2.style.display='none';
        li2.style.display='none';
        gm2.style.display='none';
    }
})

let e=0;
let ins3=document.querySelector(".insta-logo3");
let li3=document.querySelector(".li3");
let gm3=document.querySelector(".gm3");
team_member_photo[2].addEventListener('click',()=>{
    e=e+1;
    if(e%2!=0){
        ins3.style.display='block';
        li3.style.display='block';
        gm3.style.display='block';
    }
    else{
        ins3.style.display='none';
        li3.style.display='none';
        gm3.style.display='none';
    }
})
let f=0;
let ins4=document.querySelector(".insta-logo4");
let li4=document.querySelector(".li4");
let gm4=document.querySelector(".gm4");
team_member_photo[3].addEventListener('click',()=>{
    f=f+1;
    if(f%2!=0){
        ins4.style.display='block';
        li4.style.display='block';
        gm4.style.display='block';
    }
    else{
        ins4.style.display='none';
        li4.style.display='none';
        gm4.style.display='none';
    }
})
let g=0;
let ins5=document.querySelector(".insta-logo5");
let li5=document.querySelector(".li5");
let gm5=document.querySelector(".gm5");
team_member_photo[4].addEventListener('click',()=>{
    g=g+1;
    if(g%2!=0){
        ins5.style.display='block';
        li5.style.display='block';
        gm5.style.display='block';
    }
    else{
        ins5.style.display='none';
        li5.style.display='none';
        gm5.style.display='none';
    }
})