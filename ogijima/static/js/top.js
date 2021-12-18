let mySwiper = new Swiper('.swiper', {
  autoplay: {
    delay: 5000,
  },
  effect: 'fade',
  speed: 1000,
});

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

document.getElementById('map-expansor').addEventListener('input',() => {
    let ratio = document.getElementById('map-expansor').value;
    // document.querySelector('.map__image').style.transform = "scale(" + ratio + ", " + ratio + ")";
    document.querySelector('.map').style.transform = "scale(" + ratio + ", " + ratio + ")";
    let marginRatio = (ratio - 1) / 0.02;
    document.querySelector('.map').style.margin = marginRatio + "%";
    // console.log(document.querySelector('.map__image'));
    // console.log(ratio);
})

function popupActivate(elem){
  elem.style.display = "flex";
}

function popupDeactivate(elem){
  elem.style.display = "none";
}

function mapAreaSize(userAgent, screenWidth, screenHeight){
  if(userAgent == "pc"){
    var mapArea = [
      // 横幅変更したらここも変えないといけない。点の座標ずれる
      screenWidth * 0.7 - 48, //横
      screenHeight * 0.92 - 48 //縦
    ]
  }else{
    var mapArea = [
      // 横幅変更したらここも変えないといけない。点の座標ずれる
      screenWidth - 48, //横
      screenHeight * 0.65 - 48 //縦
    ]
  }
  return mapArea
}

function aspectCheck(mapArea){
  // 地図の画像が変更された場合、ここの指数は変更する必要がある
  // 画像のアスペクト比よりも横長の場合
  if(mapArea[0] / mapArea[1] > 1.098){
    var imageWidth = mapArea[1] * 1.097;
    // 12px小さくしているのは、計算誤差や思わぬヘッダーなどでスクロールが発生するのを防ぐため
    var imageHeight = mapArea[1] - 12;
  }
  else{
    var imageWidth = mapArea[0] - 12;
    var imageHeight = mapArea[0] * 0.91;
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
  let screenHeight = document.querySelector('header').clientHeight * 12.5;

  document.getElementById('zoom-mordal').style.height = screenHeight + 'px';

  let mapArea =  mapAreaSize(userAgent, screenWidth, screenHeight);
  let imageSize = aspectCheck(mapArea)

  if(userAgent == "pc"){
    $(function() {
      $(".mark").css({
          "height": imageSize[1] / 50 + "px",
          "width": imageSize[1] / 50 + "px",
      });
    });
    $(function(){
      $('#map__image').hover(function(){	//色領域にマウスカーソルがホバーしているとき開始
        function MouseMoveFunc(e){	//マウスカーソルが移動するたびに実行する関数
    
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
    
        if(document.addEventListener){
          document.addEventListener("mousemove" , MouseMoveFunc);
        }else if(document.attachEvent){
          document.attachEvent("onmousemove" , MouseMoveFunc);
        }
      });
    });
  }else{
    $(function() {
      $(".mark").css({
          "height": imageSize[1] / 20 + "px",
          "width": imageSize[1] / 20 + "px",
      });
    });
    // window.addEventListener("DOMContentLoaded", () => {
    document.querySelector('.map__wrapper').style.height = imageSize[0] + "px";
    document.querySelector('.map__wrapper').style.width = imageSize[1] + "px";
    // })
  };
})

document.body.addEventListener("touchstart", function(e){
  if (e.touches && e.touches.length > 1) {
    e.preventDefault();
  }
}, {passive: false});
document.body.addEventListener("touchmove", function(e){
  if (e.touches && e.touches.length > 1) {
    e.preventDefault();
    document.getElementById('zoom-mordal').style.display = "block";
  }
}, {passive: false});

document.getElementById('zoom-mordal__button').addEventListener('click', ()=>{
  document.getElementById('zoom-mordal').style.display = "none";
})