function socketio() {
    var sock = io.connect('http://localhost:5000/timeline');
    var nickname = '';

    // receive message
    sock.on('response', function(msg) {
        if ($('.timeline-container .timeline-content').text() == 'No Contents') {
            $('.timeline-container .timeline-content').html('<ul><li>Socket_io Connected</li></ul>');
        };

        if (msg.stat == 'connect') {
            nickname = msg['nickname'];
            $('.timeline-container .timeline-content ul').append('<li>' + ' [Hello] ' + msg.data + ' (' + msg.nickname + ', ' + msg.time + ')' + '</li>');
            $('.timeline-container .timeline-title .tot-connection').text('현재 접속자 수: ' + msg.tot)
            console.log('Received Hello Message');
        } else if (msg.stat == 'timeline') {
            $('.timeline-container .timeline-content ul').append('<li>' + '   >> [' + msg.nickname + '] ' + msg.data + ' (' + msg.time + ')' + '</li>');
            $('.timeline-container .timeline-title .tot-connection').text('현재 접속자 수: ' + msg.tot)

            console.log('Received Message');
        }
    })

    // send message
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
        sock.emit('timeline', {data: timeline, nickname: nickname});
        $('.timeline-form #my-timeline').val('');
    });
}
