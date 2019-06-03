function convertPage(target) {
    // $('.masthead-nav > li').removeClass();
    target.addClass('active');
}

function funcAutocomplete(e) {
    if (e.keyCode == '40'){
        $('.cover-contents .autocomplete-container button').on('focus', function(){
            $(this).css({'background-color': 'black'});
            $(this).on('click', function() {
                $('#custom-search-bar').val($(this).html().split(', ')[1]);
            });
        });
        $('.cover-contents .autocomplete-container button').on('focusout', function(){
            $(this).css({'background-color': 'grey'});
        });
        $('.cover-contents .autocomplete-container button:first-child').focus();

        $('.cover-contents .autocomplete-container button').keyup(function(e) {
            if (e.keyCode == '38') {
                if ($(event.target).is(':first-child')) {
                    //alert('this is first child!');
                } else {
                    $(this).prev().focus();
                }
            } else if (e.keyCode == '40') {
                if ($(event.target).is(':last-child')) {
                    //alert('this is last child!');
                } else {
                    $(this).next().focus();
                }
            }
        });
    } else {
        var val = $(event.target).val();
        if (val.length > 1) {
            $.ajax({
                type: 'post',
                url: '/autocomplete',
                data: {query: val},
                dataType: 'json',
                success: function(jsonData) {
                    var result = jsonData.suggestions; // type of tuple
                    $('.cover-contents .autocomplete-container ul').html('');
                    for (var i = 0; i < result.length; i++) {
                        $('.cover-contents .autocomplete-container ul').append('<button value="' + result[i][0] + '">' +
                            result[i][1] + ', ' + result[i][2] + '</button>');
                    }
                }
            });
        }
    }
}