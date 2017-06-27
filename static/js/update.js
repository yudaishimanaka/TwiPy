$(function (){
    $('#post_tweet').on('click', function() {
        var s = $('#status').val();
        $.ajax({
            type: 'POST',
            url: '/update_status',
            data: JSON.stringify({ "status": s }),
            contentType: 'application/json',
            success: function(response){
                console.log(response);
            }
        });
    });
});
$(function (){
    $('.like').click(function() {
        var status_id = $(this).parent('div').parent('div').attr("id");
        $.ajax({
            type: 'POST',
            url: '/action_favorite',
            data: JSON.stringify({ "status_id": status_id}),
            contentType: 'application/json',
            success: function(response){
                console.log(response)
            }
        })
    })
});
$('#clear').on('click', function() {
    $('#status').val("");
});

