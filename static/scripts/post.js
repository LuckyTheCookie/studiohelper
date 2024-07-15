$(function() {
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

    $('#goToSolver').click(function() {
        window.location.href = '/solver';
    });

    $('#solverAccept').click(function() {
        $.post('/solver_accept', function(data) {
            $('#result').text(data.message);
            if (data.status === 'success') {
                $('#solverWaitingStep').hide();
                $('#solverSuccessStep').show();
            } else if (data.status === 'error') {
                $('#solverWaitingStep').hide();
                $('#solverErrorStep').show();
            } else if (data.status === 'reload') {
                $('#solverWaitingStep').hide();
                $('#solverReloadStep').show();
            } else if (data.status === 'java') {
                $('#solverWaitingStep').hide();
                $('#solverJavaStep').show();
            }
        });
        $('#solverFirstStep').hide();
        $('#solverWaitingStep').show();
        
    });

    $('#mainMenuButton').click(function() {
        window.location.href = '/';
    });

    $('#solverClose').click(function() {
        $('#solverCloseCategory').hide();
        $('#solverClosed').show();
        $.post('/solver_close', function(data) {
            $('#result').text(data.message);
        });
    });

    $('#solverRetry').click(function() {
        // Recharger la page
        window.location.reload();
    }
    );
});