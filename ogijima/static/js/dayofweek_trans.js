// Djangoの組み込みの曜日を日本語に変える
// １，組み込みでは、「{{ work.work_start_date | date:"Y年m月d日（w）" }}」のように全角カッコに「w」を挿入
// ２，それを「<span class="dayofweek-trans">」で囲う
document.addEventListener("DOMContentLoaded", () => {
    var dayOfWeekList = document.querySelectorAll('.dayofweek-trans');
    for(let i = 0;i < dayOfWeekList.length; i++){
        dayOfWeekList[i].innerText = dayOfWeekList[i].innerText.replace("（0）","（日）");
        dayOfWeekList[i].innerText = dayOfWeekList[i].innerText.replace("（1）","（月）");
        dayOfWeekList[i].innerText = dayOfWeekList[i].innerText.replace("（2）","（火）");
        dayOfWeekList[i].innerText = dayOfWeekList[i].innerText.replace("（3）","（水）");
        dayOfWeekList[i].innerText = dayOfWeekList[i].innerText.replace("（4）","（木）");
        dayOfWeekList[i].innerText = dayOfWeekList[i].innerText.replace("（5）","（金）");
        dayOfWeekList[i].innerText = dayOfWeekList[i].innerText.replace("（6）","（土）");
    }
})