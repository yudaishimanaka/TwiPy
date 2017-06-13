$(function(){
    $.ajax({
        type: 'GET',
        url: 'http://localhost:5000/stream',
        contentType: 'application/json',
        success: function(data) {
            console.log(data);
            $('#tweet').val(data);
        }
    })
    return false;
});