$(document).ready(function() {
    $('#createInfoFile').click(function() {
        $.post('/create_info_file', function(data) {
            $('#result').text(data.message);
        });
    });

    $('#updateStudio').click(function() {
        $.post('/update_studio', function(data) {
            $('#result').text(data.message);
        });
    });

    $('#getJavaInfo').click(function() {
        $.post('/get_java_info', function(data) {
            $('#result').text(data.message);
        });
    });
});