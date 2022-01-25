var screenHeight = window.screen.height;
var sec1Offset = document.getElementById('will').offsetTop;
var sec2Offset = document.getElementById('mission').offsetTop;
var sec3Offset = document.getElementById('belief').offsetTop;
var sec4Offset = document.getElementById('business').offsetTop;
var sec5Offset = document.getElementById('source').offsetTop;
var sec6Offset = document.getElementById('footer').offsetTop;

if(userAgent == "pc"){
    window.addEventListener('scroll', () => {
        var scrollY = window.pageYOffset;
        if(scrollY > sec3Offset - screenHeight * 0.1){
            document.getElementById('bgimage-1').style.opacity = 0;
            document.getElementById('bgimage-2').style.opacity = 0;
            document.getElementById('bgimage-3').style.opacity = 1;
        }else if(scrollY > sec2Offset - screenHeight * 0.4){
            document.getElementById('bgimage-1').style.opacity = 0;
            document.getElementById('bgimage-2').style.opacity = 1;
            document.getElementById('bgimage-3').style.opacity = 0;
        }else{
            document.getElementById('bgimage-1').style.opacity = 1;
            document.getElementById('bgimage-2').style.opacity = 0;
            document.getElementById('bgimage-3').style.opacity = 0;
        }
    })
}else{
    window.addEventListener('scroll', () => {
        var scrollY = window.pageYOffset;
        if(scrollY > sec3Offset - screenHeight * 0.1){
            document.getElementById('bgimage-1').style.opacity = 0;
            document.getElementById('bgimage-2').style.opacity = 0;
            document.getElementById('bgimage-3').style.opacity = 1;
        }else if(scrollY > sec2Offset - screenHeight * 0.7){
            document.getElementById('bgimage-1').style.opacity = 0;
            document.getElementById('bgimage-2').style.opacity = 1;
            document.getElementById('bgimage-3').style.opacity = 0;
        }else{
            document.getElementById('bgimage-1').style.opacity = 1;
            document.getElementById('bgimage-2').style.opacity = 0;
            document.getElementById('bgimage-3').style.opacity = 0;
        }
    })
   
}

if(userAgent == "pc"){
    document.getElementById('bgimage-1').src = "https://lh3.googleusercontent.com/pw/AM-JKLU6I9G5GIj73WKm90o95kxQR0LKorlDlHvcXtp44blZi1wBIbrN661i09sxu1kj7_pOTiNNIFW1kPVbY-ro9c31pMvCvp1pD_DOzhzu6utrvOl15CwFRK6HUdF1iL_f0V4R7uEK4-K33K_gHCzn4guz=s0";
    document.getElementById('bgimage-2').src = "https://lh3.googleusercontent.com/pw/AM-JKLX50AORMVprK90icuaff48h55PW0dxnwJQg9qX2jtxG6W1mUpbXb-kndFNbltGzry3sL_vCHMMZKw8tn1Vb9pvWAJbcD1nbTDCWcHL4ZMQOvU1mohFPfrZSW7X74jSZGkWtPzodf_RqP7GLQzddqT2m=s0";
    document.getElementById('bgimage-3').src = "https://lh3.googleusercontent.com/pw/AM-JKLXg7MI5rv7UzUKmnX59n51LIFdikUAD3EWU4qIUQvOgqoX1kgLMVPOn14DTSMGSjDxVaGEDkO-0mewUeQZKMWd2FmfaNprNyDM477lapgmZJqwp8Tc-eien-wNQe1_lTKPWUZARXOtLifTqsVK3TDQ-=s0"; 
}else{
    document.getElementById('bgimage-1').src = "https://lh3.googleusercontent.com/pw/AM-JKLVEkFQ1TKRDrwt-dVs89SCHBQEth83lFzyEwl8nrpvGopMtwmET92XFzGp7SFEe9QyLKM4WwNfi01HM5_TaBo0rUmhaij9I6OwMCYep8Ymn23T4oWpIbqcU6e4bCKrOdzLCo07dxbu3zoHt5rOVUd_5=s0";
    document.getElementById('bgimage-2').src = "https://lh3.googleusercontent.com/pw/AM-JKLXXKuZlumnTBAPMyKLdGO8o5HJN4IGNSwc7l1J5J-jGzbiZwCtz9OUUqMK8QP4j7PomKLzmr3sw-Xb_3I_NFlGh204qsfdWKNOGMgu1SMVGV0vmrdOzaVJZU-QVtj6AZpFjJiXwvF1QP5ZTK6Qz3DmN=s0";
    document.getElementById('bgimage-3').src = "https://lh3.googleusercontent.com/pw/AM-JKLXg7MI5rv7UzUKmnX59n51LIFdikUAD3EWU4qIUQvOgqoX1kgLMVPOn14DTSMGSjDxVaGEDkO-0mewUeQZKMWd2FmfaNprNyDM477lapgmZJqwp8Tc-eien-wNQe1_lTKPWUZARXOtLifTqsVK3TDQ-=s0";
}
