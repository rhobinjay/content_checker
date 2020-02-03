$(document).ready(function($) {
    // $(".clickable-row").click(function() {
        // $(this)[0].cells[0].innerText
    // });
});

function check(username) {
    $.ajax({
        url: 'http://127.0.0.1:5000/content/check/' + username,
        type: 'post',
        dataType: 'json',
        contentType: 'application/json',
        success: function (data) {
            console.log(data)
        }
    });
}
