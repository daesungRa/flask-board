function writeAction(form) {
    var formData = form.serialize();
    $.ajax({
        type: 'post',
        url: 'http://localhost:5000/board/write/',
        data: formData,
        dataType: 'text',
        success: function(data) {
            if (data == '1') {
                location.href = 'http://localhost:5000/boards/';
            } else if (data == '0') {
                alert('글쓰기에 실패했습니다. 다시 시도하세요.');
                $('.write-form .title').focus();
                $('.write-form .title').select();
            } else {
                alert('글쓰기에 실패했습니다. 관리자에게 문의하세요.');
            }
        }
    });
}