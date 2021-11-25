document.addEventListener("DOMContentLoaded", () => {
    for(let i = 0; i < photoUrlList.length; i++){
        document.getElementById('photo-' + (i + 1)).addEventListener('click', () => {
            document.getElementById('popup-image').src = 'media/' + photoUrlList[i];
            document.getElementById('photo__popup').style.display = 'block';
        })
    }

    document.getElementById('popup-close-button').addEventListener('click', () => {
        document.getElementById('photo__popup').style.display = 'none';
    })
})