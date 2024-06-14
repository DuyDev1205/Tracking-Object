let isCameraOn = false;
const videoElement = document.getElementById('video');
const toggleButton = document.getElementById('toggleButton');

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