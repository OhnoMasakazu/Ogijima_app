function sectionChange(id){
    if(id == 1){var sectionname = "blog"}
    else if(id == 2){var sectionname = "crowdfunding"}
    // else if(id == 3){var sectionname = "donation"}
    else if(id == 4){var sectionname = "shop"}
    // for(let i = 0; i < 4; i++){
    for(let i = 0; i < 3; i++){
        document.querySelectorAll('.reports-list-button')[i].classList.remove('reports-list-button-active');
    }
    // for(let i = 0; i < 4; i++){
    for(let i = 0; i < 3; i++){
        document.querySelectorAll('.section')[i].style.display = "none";
    }
    document.getElementById('button-' + sectionname).classList.add('reports-list-button-active');
    document.getElementById('section-' + sectionname).style.display = "block";
}

document.addEventListener("DOMContentLoaded", () => {
    if(window.location.search == "?1"){sectionChange(1)}
    else if(window.location.search == "?2"){sectionChange(2)}
    // else if(window.location.search == "?3"){sectionChange(3)}
    else if(window.location.search == "?4"){sectionChange(4)}
    // NullでもクエリがPageでもブログを表示することになる
    else{sectionChange(1)}

    var separatorList = document.querySelectorAll('.separator');
    separatorList[separatorList.length - 1].style.display = "none";
})