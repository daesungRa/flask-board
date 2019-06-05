function convertPage(target) {
    // $('.masthead-nav > li').removeClass();
    target.addClass('active');
}

function funcAutocomplete(e) {
    if (e.keyCode == '40'){
        $('.cover-contents .autocomplete-container button:first-child').focus();

        $('.cover-contents .autocomplete-container button').on('focus', function(){
            $(this).css({'background-color': '#efcece'});
            $('#custom-search-bar').val($(this).html().split(' / ')[1]);
            $(this).on('click', function() {
                var searchResult = funcSearch($('#custom-search-bar').val());
            });
        });

        $('.cover-contents .autocomplete-container button').on('focusout', function(){
            $(this).css({'background-color': '#fff'});
        });

        $('.cover-contents .autocomplete-container button').keyup(function(e) {
            if (e.keyCode == '38') {
                if ($(event.target).is(':first-child')) {
                    // alert('this is first child!');
                    $('#custom-search-bar').focus();
                    $('#custom-search-bar').select();
                } else {
                    $(this).prev().focus();
                }
            } else if (e.keyCode == '40') {
                if ($(event.target).is(':last-child')) {
                    // alert('this is last child!');
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
                    var result = jsonData.suggestions; // type of tuple (or other collections)
                    $('.cover-contents .autocomplete-container').html('');
                    if (result.length == 0) {
                        $('.cover-contents .autocomplete-container').append('<div>There is no result</div>');
                    } else {
                        for (var i = 0; i < result.length; i++) {
                            // mariadb
                            // $('.cover-contents .autocomplete-container').append('<button value="' + result[i][0] + '">' +
                            //     result[i][1] + ', ' + result[i][2] + '</button>');

                            // mongodb
                            $('.cover-contents .autocomplete-container').append('<button value="' + result[i]['Code'] + '">' +
                                result[i]['Code'] + ' / ' + result[i]['Name'] + '</button>');
                        }
                    }
                }
            });
        } else {
            $('.cover-contents .autocomplete-container').html('');
        }
    }
}

function funcSearch(word) {
    $.ajax({
        type: 'post',
        url: '/search',
        data: {word: word},
        dataType: 'json',
        success: function(data) {
            alert('[' + data.result._id + '] ' + data.result.Code + ' / ' + data.result.Name);
        }
    })
}