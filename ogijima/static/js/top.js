var screenHeight = window.screen.height;

var newsOffset = document.getElementById('news').offsetTop;
// var informationOffset = document.getElementById('information').offsetTop;
var work1Offset = document.getElementById('work-1').offsetTop;
var work2Offset = document.getElementById('work-2').offsetTop;
var desireOffset = document.getElementById('desire').offsetTop;
// スクロールバーで横スクロール発生する問題のため、少し小さくしている
var desireWidth = document.querySelector('header').clientWidth *0.68;
var flag = 0;

let mySwiper = new Swiper('.swiper', {
    autoplay: {
        delay: 5000,
    },
    effect: 'fade',
    speed: 1000,
    loop: true,
});
// var hidemaskTop = document.getElementById('information').offsetTop;
var hidemaskTop = document.getElementById('work').offsetTop;

window.addEventListener('scroll', () => {
    var scrollY = window.pageYOffset;
    // if(scrollY < screenHeight){
    //     document.getElementById('swiper-mask').style.opacity = (scrollY / screenHeight) * 0.7;
    //     document.getElementById('top').style.opacity = 1 - (scrollY / screenHeight) * 1.8;
    // }else{
    //     document.getElementById('swiper-mask').style.opacity = 0.7;
    //     document.getElementById('top').style.opacity = 0;
    // }

    if(scrollY < screenHeight*0.75){
        document.getElementById('top').style.opacity = (scrollY / screenHeight) * 4/3;
        document.getElementById('swiper-mask').style.opacity = 0;
    }
    else if(scrollY < screenHeight*1.5){
        document.getElementById('swiper-mask').style.opacity = 0;
        document.getElementById('top').style.opacity = 1 - ((scrollY-screenHeight*0.75) / screenHeight) * 4/3;
    }
    else if(scrollY < screenHeight*3){
        document.getElementById('swiper-mask').style.opacity = ((scrollY-screenHeight) / screenHeight) * 0.7;
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

    if(scrollY > desireOffset - screenHeight * 0.55 && flag == 0){
        flag = 1;
        document.querySelector('.desire__wrapper').style.width = desireWidth + "px";
        document.querySelector('.desire__wrapper').style.padding = "48px 15vw";
        window.setTimeout(() => {
            document.querySelector('.desire__wrapper').style.width = "auto";
            document.getElementById('desire__list-1').style.opacity = 1;
            document.getElementById('desire__list-1').style.transform = "translateY(0%)";
        }, 800);
        window.setTimeout(() => {
            document.querySelector('.desire__wrapper').style.width = "auto";
            document.getElementById('desire__list-2').style.opacity = 1;
            document.getElementById('desire__list-2').style.transform = "translateY(0%)";
        }, 1400);
        window.setTimeout(() => {
            document.querySelector('.desire__wrapper').style.width = "auto";
            document.getElementById('desire__list-3').style.opacity = 1;
            document.getElementById('desire__list-3').style.transform = "translateY(0%)";
        }, 2000);
    }
})

document.addEventListener("DOMContentLoaded", () => {
    // document.getElementById('top').style.opacity = 1;
    document.getElementById('swiper').style.opacity = 1;

    window.setTimeout(() => {
        document.getElementById('top').classList.remove('delay');
        document.getElementById('swiper').classList.remove('delay');
    }, 500);

    // var desireHeight = document.querySelector('.desire__wrapper').clientHeight;
    // document.querySelector('.desire__linktext').style.marginTop = desireHeight + 48 + "px";

    // var hidemaskTop = document.getElementById('information').offsetTop;
    var hidemaskTop = document.getElementById('work').offsetTop;
    var hidemaskBottom = document.getElementById('footer').offsetTop;
    document.getElementById('swiper-hide-mask').style.top = hidemaskTop - 60 + "px";
    document.getElementById('swiper-hide-mask').style.height = hidemaskBottom - hidemaskTop + 60 + "px";

    var separatorList = document.querySelectorAll('.separator');
    separatorList[separatorList.length - 1].style.display = "none";

    // document.querySelector('#popup_1_7 .popup__title').style.display = "none";
    // let aikienPopup = document.createElement('img');
    // aikienPopup.src = "https://aikien.s3.ap-northeast-3.amazonaws.com/image/logo/logo_HP_yoko_brown.svg";
    // aikienPopup.classList.add('aikienPopup');
    // document.getElementById('popup_1_7').insertAdjacentElement('afterbegin',aikienPopup);

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

// function popupActivate(elem) {
//     // elem.firstChild.style.color = "rgb(230,95,96)";
//     console.log(elem)
//     if(userAgent != "pc"){
//         var mapPopupList = document.querySelectorAll('.upblock');
//         for(let i = 0; i < mapPopupList.length; i++){
//             mapPopupList[i].style.display = "none";
//         }
//     }
//     elem.style.display = "flex";
// }

// function popupDeactivate(elem) {
//     if(userAgent == "pc"){elem.style.display = "none";}
// }

function popupActivate(id) {
    var markList = document.querySelectorAll('.mark');
    for(let i = 0; i < markList.length; i++){
        try{markList[i].querySelector('i').style.color = "rgb(104, 94, 96)";}catch{}
    }
    document.querySelector('#mark' + id + " i").style.color = "rgb(230,95,96)";
    if(userAgent != "pc"){
        var mapPopupList = document.querySelectorAll('.upblock');
        for(let i = 0; i < mapPopupList.length; i++){
            mapPopupList[i].style.display = "none";
        }
    }
    document.getElementById('popup' + id).style.display = "flex";
}

function popupDeactivate(id) {
    document.querySelector('#mark' + id + " i").style.color = "rgb(104, 94, 96)";
    if(userAgent == "pc"){document.getElementById('popup' + id).style.display = "none";}
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

// function aspectCheck(mapArea) {
//     // 地図の画像が変更された場合、ここの指数は変更する必要がある
//     // 画像のアスペクト比よりも横長の場合
//     if (mapArea[0] / mapArea[1] > 1.686) {
//         var imageWidth = mapArea[1] * 1.686 - 12;
//         // 12px小さくしているのは、計算誤差や思わぬヘッダーなどでスクロールが発生するのを防ぐため
//         var imageHeight = mapArea[1] - 12;
//     }
//     else {
//         var imageWidth = mapArea[0] - 12;
//         var imageHeight = mapArea[0] * 0.593 - 12;
//     }
//     document.querySelector('.map__image').style.width = imageWidth + "px";
//     document.querySelector('.map__image').style.height = imageHeight + "px";
//     document.querySelector('.map__wrapper').style.width = imageWidth + "px";
//     document.querySelector('.map__wrapper').style.height = imageHeight + "px";
//     return [imageHeight, imageWidth]
// }

document.addEventListener("DOMContentLoaded", () => {
    // let imageWidth = document.querySelector('.map__image').clientWidth;
    // let imageHeight = document.querySelector('.map__image').clientHeight;
    let screenWidth = window.screen.availWidth;
    // どっかのvhから逆算するのが堅い
    let screenHeight = document.querySelector('header').clientHeight * 10;

    // document.getElementById('zoom-mordal').style.height = screenHeight + 'px';

    // let mapArea = mapAreaSize(userAgent, screenWidth, screenHeight);
    // let imageSize = aspectCheck(mapArea)

    // if (userAgent == "pc") {
    //     $(function () {
    //         $(".mark").css({
    //             "height": imageSize[1] / 50 + "px",
    //             "width": imageSize[1] / 50 + "px",
    //         });
    //     });
    //     $(function () {
    //         $('#map__image').hover(function () {	//色領域にマウスカーソルがホバーしているとき開始
    //             function MouseMoveFunc(e) {	//マウスカーソルが移動するたびに実行する関数

    //                 // マウスカーソルの座標を取得
    //                 var mouse_x = e.clientX + 5;	//マウスカーソルのX座標 5px右へ調整
    //                 var mouse_y = $(window).scrollTop() + e.clientY + 5;	//マウスカーソルのY座標 現在のスクロール位置＋5px下へ調整

    //                 // 吹き出しの位置座標を取得したマウスカーソルの座標に変換
    //                 $("#popup").css({
    //                     "position": "absolute",
    //                     "left": mouse_x,
    //                     "top": mouse_y
    //                 });
    //             }

    //             if (document.addEventListener) {
    //                 document.addEventListener("mousemove", MouseMoveFunc);
    //             } else if (document.attachEvent) {
    //                 document.attachEvent("onmousemove", MouseMoveFunc);
    //             }
    //         });
    //     });
    // } else {
    //     $(function () {
    //         $(".mark").css({
    //             "height": imageSize[1] / 31 + "px",
    //             "width": imageSize[1] / 31 + "px",
    //         });
    //     });
    //     // window.addEventListener("DOMContentLoaded", () => {
    //     document.querySelector('.map__wrapper').style.height = imageSize[0] + "px";
    //     document.querySelector('.map__wrapper').style.width = imageSize[1] + "px";
    //     // })
    // };

    // if(userAgent == "sp"){
    //     var markList = document.querySelectorAll('.mark');
    //     for(let i = 0; i < markList.length; i++){
    //         markList[i].onmouseenter = "";
    //         markList[i].onmouseleave = "";
    //         markList[i].addEventListener('touchstart', () => {
    //             // popupActivate(document.getElementById('popup' + markList[i].id.replace('mark', "")))
    //             popupActivate(markList[i].id.replace('mark', ""))
    //         });
    //     }
    //     document.getElementById('mobile-text').innerText = "をタップすると";
    // }
})

// function modalDeactivate(){
//     document.getElementById('detail-modal').style.display = "none";
// }