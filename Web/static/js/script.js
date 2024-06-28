let isCameraOn = false;
const videoElement = document.getElementById('video');
const toggleButton = document.getElementById('toggleButton');
const arrowright = document.getElementById('arrowright');
const arrowleft = document.getElementById('arrowleft');
const btn = document.getElementById('btn_test');
toggleButton.addEventListener('click', () => {
    isCameraOn = !isCameraOn;
    if (isCameraOn) {
        videoElement.src = "/video_feed"; // Bật video feed
        toggleButton.innerText = 'Turn Off Camera';
    } else {
        videoElement.src = ''; // Tắt video feed
        toggleButton.innerText = 'Turn On Camera';
    }
});
arrowright.addEventListener('click', () => {
    videoElement.src = "/prevpage";
    setTimeout(function() {
        // Sau 5 giây, yêu cầu reload trang
        window.location.reload();
    }, 50); 
    
});

btn.addEventListener('click', () => {
    console.log("eheh")
    videoElement.src = "/editAttend";

})
arrowleft.addEventListener('click', () => {
    videoElement.src = "/nextpage";
    setTimeout(function() {
        // Sau 5 giây, yêu cầu reload trang
        window.location.reload();
    }, 50); 
})