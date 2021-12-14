document.addEventListener("DOMContentLoaded", () => {
    document.getElementById("privacypolicy-check").addEventListener('change', () => {
        if(document.getElementById("privacypolicy-check").checked){
            document.getElementById("submit-button").style.opacity = 1;
            document.getElementById("submit-button").disabled = false;
            document.getElementById("button-cover").style.display = "none";
        }else{
            document.getElementById("submit-button").style.opacity = 0.3;
            document.getElementById("submit-button").disabled = true;
            document.getElementById("button-cover").style.display = "block";
       }
    })
    document.getElementById("button-cover").addEventListener('click', () => {
        swal('プライバシーポリシーに同意して、チェックボックスをチェックしてください。');
    })
})
