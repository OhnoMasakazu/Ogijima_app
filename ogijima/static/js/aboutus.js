var screenHeight = window.screen.height;
var sourceOffset = document.getElementById('source').offsetTop;
var willOffset = document.getElementById('will').offsetTop;
var missionOffset = document.getElementById('mission').offsetTop;
var beliefOffset = document.getElementById('belief').offsetTop;

window.addEventListener('scroll', () => {
    var scrollY = window.pageYOffset;
    if(scrollY > beliefOffset - screenHeight * 0.4){
        document.getElementById('bgimage-1').style.opacity = 0;
        document.getElementById('bgimage-2').style.opacity = 0;
        document.getElementById('bgimage-3').style.opacity = 0;
        document.getElementById('bgimage-4').style.opacity = 1;
    }else if(scrollY > missionOffset - screenHeight * 0.4){
        document.getElementById('bgimage-1').style.opacity = 0;
        document.getElementById('bgimage-2').style.opacity = 0;
        document.getElementById('bgimage-3').style.opacity = 1;
        document.getElementById('bgimage-4').style.opacity = 0;
    }else if(scrollY > willOffset - screenHeight * 0.4){
        document.getElementById('bgimage-1').style.opacity = 0;
        document.getElementById('bgimage-2').style.opacity = 1;
        document.getElementById('bgimage-3').style.opacity = 0;
        document.getElementById('bgimage-4').style.opacity = 0;
    }else{
        document.getElementById('bgimage-1').style.opacity = 1;
        document.getElementById('bgimage-2').style.opacity = 0;
        document.getElementById('bgimage-3').style.opacity = 0;
        document.getElementById('bgimage-4').style.opacity = 0;
    }
})

document.addEventListener("DOMContentLoaded", () => {

})