// get view, modify page
function getDocument(uri, id) {
    location.href = 'http://localhost:5000/' + uri + id;
}

function writeAction(form, highlight) {
    highlight = highlight.toLowerCase();
    var formData = form.serialize();
    $.ajax({
        type: 'post',
        url: 'http://localhost:5000/' + highlight + '/write/',
        data: formData,
        cache: false,
        dataType: 'text',
        success: function(data) {
            if (data == '1') {
                location.href = 'http://localhost:5000/' + highlight + 's/';
            } else if (data == '0') {
                alert('글 쓰기에 실패했습니다. 다시 시도하세요.');
                $('.write-form .title').focus();
                $('.write-form .title').select();
            } else {
                alert('글 쓰기에 실패했습니다. 관리자에게 문의하세요.');
            }
        }
    });
}

function modifyAction(form, highlight) {
    highlight = highlight.toLowerCase();
    var formData = form.serialize();
    $.ajax({
        type: 'post',
        url: 'http://localhost:5000/' + highlight + '/modify/',
        data: formData,
        cache: false,
        dataType: 'text',
        success: function(data) {
            if (data != null && data.length > 0) {
                location.href = 'http://localhost:5000/' + highlight + '/view/' + data;
            } else if (data == null) {
                alert('글 수정에 실패했습니다. 다시 시도하세요.');
                $('.modify-form .title').focus();
                $('.modify-form .title').select();
            } else {
                alert('글 수정에 실패했습니다. 관리자에게 문의하세요.');
            }
        }
    });
}

function deleteAction(id, highlight) {
    highlight = highlight.toLowerCase();
    $.ajax({
        type: 'post',
        url: 'http://localhost:5000/' + highlight + '/delete/',
        data: {_id: id},
        cache: false,
        dataType: 'json',
        success: function(data) {
            if (data == '1') {
                location.href = 'http://localhost:5000/' + highlight + 's/';
            } else if (data == '0') {
                alert('글 삭제에 실패했습니다. 다시 시도하세요.');
            }
        }
    });
}