function aspectCheck(mapArea) {
    // 地図の画像が変更された場合、ここの指数は変更する必要がある
    // 画像のアスペクト比よりも横長の場合
    if (mapArea[0] / mapArea[1] > 1.686) {
        var imageWidth = mapArea[1] * 1.686 - 24;
        // 12px小さくしているのは、計算誤差や思わぬヘッダーなどでスクロールが発生するのを防ぐため
        var imageHeight = mapArea[1] - 24;
    }
    else {
        var imageWidth = mapArea[0] - 24;
        var imageHeight = mapArea[0] * 0.593 - 24;
    }
    document.querySelector('.map__image').style.width = imageWidth + "px";
    document.querySelector('.map__image').style.height = imageHeight + "px";
    document.querySelector('.map__wrapper').style.width = imageWidth + "px";
    document.querySelector('.map__wrapper').style.height = imageHeight + "px";
    return [imageHeight, imageWidth]
}