function socketio() {
    var sock = io.connect('http://localhost:5000/timeline');
    var nickname = '';

    sock.on('response', function(msg) {
        if ($('.timeline-container .timeline-content').text() == 'No Contents') {
            $('.timeline-container .timeline-content').html('<ul><li>Socket_io Connected</li></ul>');
        }

        if (msg.stat == 'connect') {
            nickname = msg.nickname;
            $('.timeline-container .timeline-content ul').append('<li>' + ' [Hello] ' + msg.data + ' (' + msg.nickname + ', ' + msg.time + ')' + '</li>');
            console.log('Received Hello Message');
        } else {
            if (nickname != msg.nickname) {
                $('.timeline-container .timeline-content ul').append('<li>' + '   >> [' + msg.nickname + '] ' + msg.data + ' (' + msg.time + ')' + '</li>');
            }
            console.log('Received Message : ' + msg.data);
        }

    });

    // message send
    $('.timeline-form #my-timeline').keyup(function(e) {
        if (e.keyCode == '13') {
            $('.timeline-form #btn-send').trigger('click');
        }
    });
    $('.timeline-form #btn-send').on('click', function() {
        if ($('.timeline-form #my-timeline').val() == '') {
            return false;
        }
        var timeline = $('.timeline-form #my-timeline').val();
        var date = new Date();
        var now = date.getHours() + ':' + date.getMinutes();

        $('.timeline-container .timeline-content ul').append('<li style="text-align: right;">(' + now + ') ' + timeline + '</li>');
        sock.emit('request', {data: timeline});
        $('.timeline-form #my-timeline').val('');
    });
}