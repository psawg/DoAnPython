document.addEventListener("DOMContentLoaded", () => {

    const cards = document.querySelectorAll(".stat-card");

    cards.forEach((card,index)=>{

        setTimeout(()=>{
            card.classList.add("show");
        }, index * 150);

    });

});