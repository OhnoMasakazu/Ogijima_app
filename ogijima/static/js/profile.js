var screenWidth = window.screen.availWidth;
document.addEventListener("DOMContentLoaded", () => {
    for(let i = 0; i < profileList.length; i++){
        document.getElementById('image-' + (i + 1)).addEventListener('click', () => {
            document.getElementById('popup-image').src = 'media/' + profileList[i][0];
            document.getElementById('popup-name').innerText = profileList[i][1];
            document.getElementById('popup-roll').innerText = profileList[i][2];
            document.getElementById('popup-intro').innerText = profileList[i][3];
            // DBでNullFalseになっていたので、この判定にした
            if(profileList[i][4].length < 10){
                document.getElementById('popup-link').style.display = "none";
                document.getElementById('popup-intro').style.marginBottom = "48px";
            }else{
                document.getElementById('popup-link').href = profileList[i][4];
                document.getElementById('popup-link').style.display = "block";
                document.getElementById('popup-link').style.marginBottom = "48px";
                document.getElementById('popup-intro').style.marginBottom = "12px";
            }
            document.getElementById('popup').style.display = 'flex';
        })
    }

    document.getElementById('popup-close-button').addEventListener('click', () => {
        document.getElementById('popup').style.display = 'none';
    })
})