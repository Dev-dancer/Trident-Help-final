let p=document.querySelector(".p");
let r=document.querySelector(".r");
let t=document.querySelector(".t");
let check_returns=document.querySelector(".custom-btn");
let right_1=document.querySelector(".same-as-p");
let right_return=document.querySelector(".si");
let total=document.querySelector(".si-plus-p");
check_returns.addEventListener('click',()=>{
    if(p.value=='' || r.value=='' || t.value==''){
        alert("Kindly enter Required Data");
    }
    else{
        let si=(p.value*r.value*t.value)/100;
        right_1.value=p.value;
        let right_2=si;
        right_return.value=right_2;
        let tv=Number.parseInt(si)+Number.parseInt(p.value);
        total.value=tv;
    }
})