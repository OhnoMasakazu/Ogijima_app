document.addEventListener("DOMContentLoaded", () => {
    for(let i = 0; i < photoUrlList.length; i++){
        document.getElementById('photo-' + photoUrlList[i][0]).addEventListener('click', () => {
            document.getElementById('popup-image').src = 'media/' + photoUrlList[i][1];
            document.getElementById('photo__popup').style.display = 'block';
        })
    }

    document.getElementById('popup-close-button').addEventListener('click', () => {
        document.getElementById('photo__popup').style.display = 'none';
    })
})