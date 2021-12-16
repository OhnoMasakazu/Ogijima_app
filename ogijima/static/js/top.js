document.addEventListener("DOMContentLoaded", () => {
    var screenHeight = window.screen.height;
    var fadein_1_1 = document.getElementById('fadein1-1').offsetTop
    var fadein_2_1 = document.getElementById('fadein2-1').offsetTop
    var fadein_3_1 = document.getElementById('fadein3-1').offsetTop
    var fadein_3_2 = document.getElementById('fadein3-2').offsetTop
    var fadein_3_3 = document.getElementById('fadein3-3').offsetTop
    var caption_1 = document.getElementById('caption-1').offsetTop
    var caption_2 = document.getElementById('caption-2').offsetTop
    var caption_3 = document.getElementById('caption-3').offsetTop
    window.addEventListener('scroll', () => {
        var scrollHeight = window.pageYOffset;
        if(scrollHeight + window.screen.height * 0.6 > fadein_1_1){document.getElementById('fadein1-1').style.opacity = 1;}
        if(scrollHeight + window.screen.height * 0.6 > fadein_2_1){document.getElementById('fadein2-1').style.opacity = 1;}
        if(scrollHeight + window.screen.height * 0.6 > fadein_3_1){document.getElementById('fadein3-1').style.opacity = 1;}
        if(scrollHeight + window.screen.height * 0.6 > fadein_3_2){document.getElementById('fadein3-2').style.opacity = 1;}
        if(scrollHeight + window.screen.height * 0.6 > fadein_3_3){document.getElementById('fadein3-3').style.opacity = 1;}
        if(scrollHeight + window.screen.height * 0.6 > caption_1){
            document.getElementById('caption-1').style.width = "90vw";
            document.getElementById('caption-1').style.opacity = 1;
        }
        if(scrollHeight + window.screen.height * 0.6 > caption_2){
            document.getElementById('caption-2').style.width = "90vw";
            document.getElementById('caption-2').style.opacity = 1;
        }
        if(scrollHeight + window.screen.height * 0.6 > caption_3){
            document.getElementById('caption-3').style.width = "90vw";
            document.getElementById('caption-3').style.opacity = 1;
        }
    })
})