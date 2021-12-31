document.addEventListener("DOMContentLoaded", () => {
    var ua = navigator.userAgent;
    try{
        if (ua.indexOf("iPhone") > 0 || ua.indexOf("iPod") > 0 || ua.indexOf("iPad") > 0) {
            document.querySelector('.map-link-apple').style.display = "inline";
            document.querySelector('.map-link-google').style.display = "inline";
            document.querySelector('.map-link-pc').style.display = "none";
        } else if (ua.indexOf("Android") > 0) {
            document.querySelector('.map-link-apple').style.display = "none";
            document.querySelector('.map-link-google').style.display = "inline";
            document.querySelector('.map-link-pc').style.display = "none";
        } else {
            document.querySelector('.map-link-apple').style.display = "none";
            document.querySelector('.map-link-google').style.display = "none";
            document.querySelector('.map-link-pc').style.display = "inline";
        }
    }catch(e){}

    let screenWidth = window.screen.availWidth;
    let screenHeight = document.querySelector('header').clientHeight * 10;
    let mapArea = mapAreaSize(userAgent, screenWidth, screenHeight);
    let imageSize = aspectCheck(mapArea);
    if (userAgent == "pc") {
        document.getElementById('mark').style.height = imageSize[1] / 30 + "px";
        document.getElementById('mark').style.width = imageSize[1] / 30 + "px";
    } else {
        document.getElementById('mark').style.height = imageSize[1] / 31 + "px";
        document.getElementById('mark').style.width = imageSize[1] / 31 + "px";
    };
})

function mapAreaSize(userAgent, screenWidth, screenHeight) {
    if (userAgent == "pc") {
        var mapArea = [
            // 横幅変更したらここも変えないといけない。点の座標ずれる
            screenWidth * 0.5, //横
            screenHeight * 0.6 //縦
        ]
    } else {
        var mapArea = [
            // 横幅変更したらここも変えないといけない。点の座標ずれる
            screenWidth - 48, //横
            screenHeight * 0.65 - 48 //縦
        ]
    }
    return mapArea
}