// let clicker = document.querySelector(".sel-plain");
// let green_box=document.querySelector(".sel")
// let green = document.querySelector(".selected");
// let proceed = document.querySelector(".proceed1");
// clicker.addEventListener('click', () => {
//     clicker.style.display = 'none';
//     green.style.display = 'block';
//     green_box.style.display = 'block';
//     proceed.style.display = 'block';
//     proceed.style.cursor = 'pointer';
// })
// green.addEventListener('click', () => {
//     if (clicker.style.display === 'none') {
//         clicker.style.display = 'block';
//         green.style.display = 'none';
//         green_box.style.display = 'none';
//         proceed.style.display = 'none';
//     }
// })

let investors=document.querySelectorAll(".investor");
investors.forEach(investor=>{
    let clicker = investor.querySelector(".sel-plain");
    let green_box=investor.querySelector(".sel")
    let green = investor.querySelector(".selected");
    let proceed = investor.querySelector(".proceed1");
    clicker.addEventListener('click', () => {
            clicker.style.display = 'none';
            green.style.display = 'block';
            green_box.style.display = 'block';
            proceed.style.display = 'block';
            proceed.style.cursor = 'pointer';
        })
        green.addEventListener('click', () => {
            if (clicker.style.display === 'none') {
                clicker.style.display = 'block';
                green.style.display = 'none';
                green_box.style.display = 'none';
                proceed.style.display = 'none';
            }
        })
})
