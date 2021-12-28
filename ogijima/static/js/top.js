var screenHeight = window.screen.height;

var newsOffset = document.getElementById('news').offsetTop;
var informationOffset = document.getElementById('information').offsetTop;
var work1Offset = document.getElementById('work-1').offsetTop;
var work2Offset = document.getElementById('work-2').offsetTop;
var desireOffset = document.getElementById('desire').offsetTop;

let mySwiper = new Swiper('.swiper', {
    autoplay: {
        delay: 5000,
    },
    effect: 'fade',
    speed: 1000,
    loop: true,
});
var hidemaskTop = document.getElementById('information').offsetTop;

window.addEventListener('scroll', () => {
    var scrollY = window.pageYOffset;
    if(scrollY < screenHeight){
        document.getElementById('swiper-mask').style.opacity = (scrollY / screenHeight) * 0.7;
        document.getElementById('top').style.opacity = 1 - (scrollY / screenHeight) * 1.8;
    }else{
        document.getElementById('swiper-mask').style.opacity = 0.7;
        document.getElementById('top').style.opacity = 0;
    }

    if(scrollY > hidemaskTop){
        document.getElementById('swiper').style.opacity = 0;
    }else{
        document.getElementById('swiper').style.opacity = 1;
    }

    if(scrollY > desireOffset - screenHeight * 0.6){
        document.querySelector('#desire h2').classList.add('titlelinein');
    }
    else if(scrollY > work2Offset - screenHeight * 0.6){
        document.querySelector('#work-2 h2').classList.add('titlelinein');
    }
    else if(scrollY > work1Offset - screenHeight * 0.6){
        document.querySelector('#work-1 h2').classList.add('titlelinein');
    }
    else if(scrollY > informationOffset - screenHeight * 0.6){
        document.querySelector('#information .section-title h2').classList.add('titlelinein');
    }
    else if(scrollY > newsOffset - screenHeight * 0.6){
        document.querySelector('#news .section-title h2').classList.add('titlelinein');
    }

    // if(scrollY > desireOffset - screenHeight * 0.6){
    //     document.querySelector('#desire h2 span').style.transform = "translateX(0)";
    // }
    // else if(scrollY > workOffset - screenHeight * 0.6){
    //     document.querySelector('#work .section-title h2 span').style.transform = "translateX(0)";
    // }
    // else if(scrollY > informationOffset - screenHeight * 0.6){
    //     document.querySelector('#information .section-title h2 span').style.transform = "translateX(0)";
    // }
    // else if(scrollY > newsOffset - screenHeight * 0.6){
    //     document.querySelector('#news .section-title h2 span').style.transform = "translateX(0)";
    // }

    // if(scrollY > desireOffset - screenHeight * 0.6){
    //     document.querySelector('#desire h2 span').style.transform = "translateX(0)";
    // }
    // else if(scrollY > workOffset - screenHeight * 0.6){
    //     document.querySelector('#work .section-title h2 span').style.transform = "translateX(0)";
    // }
    // else if(scrollY > informationOffset - screenHeight * 0.6){
    //     document.querySelector('#information .section-title h2 span').style.transform = "translateX(0)";
    // }
    // else if(scrollY > newsOffset - screenHeight * 0.6){
    // if(scrollY > newsOffset - screenHeight * 0.6){
    //     document.querySelector('#news .section-title h2 span').style.transform = "translateY(0)";
    //     document.querySelector('#news .section-title h2 span').classList.add('h2mask');
    //     window.setTimeout(() => {
    //         document.querySelector('#news .section-title h2 span').classList.remove('h2mask');
    //     }, 300);    
    // }
})

document.addEventListener("DOMContentLoaded", () => {
    document.getElementById('top').style.opacity = 1;
    document.getElementById('swiper').style.opacity = 1;

    window.setTimeout(() => {
        document.getElementById('top').classList.remove('delay');
        document.getElementById('swiper').classList.remove('delay');
    }, 500);

    var desireHeight = document.querySelector('.desire__wrapper').clientHeight;
    document.querySelector('.desire__linktext').style.marginTop = desireHeight + 48 + "px";

    var hidemaskTop = document.getElementById('information').offsetTop;
    var hidemaskBottom = document.getElementById('footer').offsetTop;
    document.getElementById('swiper-hide-mask').style.top = hidemaskTop - 60 + "px";
    document.getElementById('swiper-hide-mask').style.height = hidemaskBottom - hidemaskTop + 60 + "px";

    var separatorList = document.querySelectorAll('.separator');
    separatorList[separatorList.length - 1].style.display = "none";
})

// ブラウザバックしたときにもともと表示されていたポップアップが出たままになるエラーを修正
window.onpageshow = function(event) {
    if (event.persisted) {
        let popupwindow = document.querySelectorAll('.upblock');
        for(let i = 0; i < popupwindow.length; i++){
            popupwindow[i].style.display = "none";
        }
    }
};

function popupActivate(elem) {
    if(userAgent != "pc"){
        var mapPopupList = document.querySelectorAll('.upblock');
        for(let i = 0; i < mapPopupList.length; i++){
            mapPopupList[i].style.display = "none";
        }
    }
    elem.style.display = "flex";
}

function popupDeactivate(elem) {
    if(userAgent == "pc"){elem.style.display = "none";}
}

function mapAreaSize(userAgent, screenWidth, screenHeight) {
    if (userAgent == "pc") {
        var mapArea = [
            // 横幅変更したらここも変えないといけない。点の座標ずれる
            screenWidth * 0.7 - 48, //横
            screenHeight * 0.80 - 48 //縦
        ]
    } else {
        var mapArea = [
            // 横幅変更したらここも変えないといけない。点の座標ずれる
            screenWidth - 48, //横
            screenHeight * 0.40 - 48 //縦
        ]
    }
    return mapArea
}

function aspectCheck(mapArea) {
    // 地図の画像が変更された場合、ここの指数は変更する必要がある
    // 画像のアスペクト比よりも横長の場合
    if (mapArea[0] / mapArea[1] > 1.686) {
        var imageWidth = mapArea[1] * 1.686 - 12;
        // 12px小さくしているのは、計算誤差や思わぬヘッダーなどでスクロールが発生するのを防ぐため
        var imageHeight = mapArea[1] - 12;
    }
    else {
        var imageWidth = mapArea[0] - 12;
        var imageHeight = mapArea[0] * 0.593 - 12;
    }
    document.querySelector('.map__image').style.width = imageWidth + "px";
    document.querySelector('.map__image').style.height = imageHeight + "px";
    document.querySelector('.map__wrapper').style.width = imageWidth + "px";
    document.querySelector('.map__wrapper').style.height = imageHeight + "px";
    return [imageHeight, imageWidth]
}

document.addEventListener("DOMContentLoaded", () => {
    // let imageWidth = document.querySelector('.map__image').clientWidth;
    // let imageHeight = document.querySelector('.map__image').clientHeight;
    let screenWidth = window.screen.availWidth;
    // どっかのvhから逆算するのが堅い
    let screenHeight = document.querySelector('header').clientHeight * 10;

    // document.getElementById('zoom-mordal').style.height = screenHeight + 'px';

    let mapArea = mapAreaSize(userAgent, screenWidth, screenHeight);
    let imageSize = aspectCheck(mapArea)

    if (userAgent == "pc") {
        $(function () {
            $(".mark").css({
                "height": imageSize[1] / 50 + "px",
                "width": imageSize[1] / 50 + "px",
            });
        });
        $(function () {
            $('#map__image').hover(function () {	//色領域にマウスカーソルがホバーしているとき開始
                function MouseMoveFunc(e) {	//マウスカーソルが移動するたびに実行する関数

                    // マウスカーソルの座標を取得
                    var mouse_x = e.clientX + 5;	//マウスカーソルのX座標 5px右へ調整
                    var mouse_y = $(window).scrollTop() + e.clientY + 5;	//マウスカーソルのY座標 現在のスクロール位置＋5px下へ調整

                    // 吹き出しの位置座標を取得したマウスカーソルの座標に変換
                    $("#popup").css({
                        "position": "absolute",
                        "left": mouse_x,
                        "top": mouse_y
                    });
                }

                if (document.addEventListener) {
                    document.addEventListener("mousemove", MouseMoveFunc);
                } else if (document.attachEvent) {
                    document.attachEvent("onmousemove", MouseMoveFunc);
                }
            });
        });
    } else {
        $(function () {
            $(".mark").css({
                "height": imageSize[1] / 31 + "px",
                "width": imageSize[1] / 31 + "px",
            });
        });
        // window.addEventListener("DOMContentLoaded", () => {
        document.querySelector('.map__wrapper').style.height = imageSize[0] + "px";
        document.querySelector('.map__wrapper').style.width = imageSize[1] + "px";
        // })
    };
})

function modalDeactivate(){
    document.getElementById('detail-modal').style.display = "none";
}