function popupActivate(elem) {
    elem.style.display = "flex";
}

function popupDeactivate(elem) {
    elem.style.display = "none";
}

function modalDeactivate(){
    document.getElementById('detail-modal').style.display = "none";
}


function mapAreaSize(userAgent, screenWidth, screenHeight) {
    if (userAgent == "pc") {
        var mapArea = [
            // 横幅変更したらここも変えないといけない。点の座標ずれる
            screenWidth * 0.7 - 48, //横
            screenHeight * 0.92 - 48 //縦
        ]
    } else {
        var mapArea = [
            // 横幅変更したらここも変えないといけない。点の座標ずれる
            screenWidth - 48, //横
            screenHeight * 0.4 - 48 //縦
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
        var imageHeight = mapArea[0] * 0.593;
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

    document.querySelector('#popup_1_7 .popup__title').style.display = "none";
    let aikienPopup = document.createElement('img');
    aikienPopup.src = "https://aikien.s3.ap-northeast-3.amazonaws.com/image/logo/logo_HP_yoko_brown.svg";
    aikienPopup.classList.add('aikienPopup');
    document.getElementById('popup_1_7').insertAdjacentElement('afterbegin',aikienPopup);

})