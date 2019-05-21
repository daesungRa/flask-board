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

// get view, modify page
function getDocument(uri, id) {
    location.href = 'http://localhost:5000/' + uri + id;
}

function modifyAction(form) {
    var formData = form.serialize();
    $.ajax({
        type: 'post',
        url: 'http://localhost:5000/board/modify/',
        data: formData,
        dataType: 'text',
        success: function(data) {
            if (data != null && data.length > 0) {
                location.href = 'http://localhost:5000/board/view/' + data;
            } else if (data == null) {
                alert('글 수정에 실패했습니다. 다시 시도하세요.');
                $('.write-form .title').focus();
                $('.write-form .title').select();
            } else {
                alert('글 수정에 실패했습니다. 관리자에게 문의하세요.');
            }
        }
    });
}