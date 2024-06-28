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

// btn.addEventListener('click', () => {
//     videoElement.src = "/editAttend";
//     // setTimeout(function() {
//     //     // Sau 5 giây, yêu cầu reload trang
//     //     window.location.reload();
//     // }, 50); 
// })
arrowleft.addEventListener('click', () => {
    videoElement.src = "/nextpage";
    setTimeout(function() {
        // Sau 5 giây, yêu cầu reload trang
        window.location.reload();
    }, 50); 
})

$(document).ready(function() {
    // Định nghĩa hàm để gửi yêu cầu AJAX và cập nhật dữ liệu
    function updateData() {
        $.ajax({
            url: '/editAttend',
            type: 'POST',
            contentType: 'application/json',
            success: function(response) {
                // Nếu thành công, cập nhật lại dữ liệu trên trang web
                var updatedData = response;
                var html = '';
                var tbody = $('#table_data');
                console.log(updatedData);
                // Xóa toàn bộ nội dung của tbody cũ
                tbody.empty();

                // Tạo HTML mới cho các dòng dữ liệu
                for (var i = 0; i < updatedData.length; i++) {
                    html += '<tr>';
                    html += '<td>' + updatedData[i][0] + '</td>';
                    html += '<td>' + updatedData[i][1] + '</td>';
                    html += '<td>' + updatedData[i][2] + '</td>';
                    html += '</tr>';
                }

                // Thêm dòng tiêu đề vào tbody
                html = '<tr>' +
                       '<th>ID</th>' +
                       '<th>Name</th>' +
                       '<th>State</th>' +
                       '</tr>' + html;

                // Thêm HTML mới vào tbody
                tbody.append(html);
            },
            error: function() {
                alert('Update failed. Please try again later.');
            }
        });
    }

    // Cập nhật dữ liệu ban đầu khi trang được tải
    updateData();

    // Thiết lập để cập nhật dữ liệu mỗi 5 giây
    setInterval(updateData, 5000); // 5000 milliseconds = 5 seconds
});
