$(function () {
    $('.select2').select2({
        theme: "bootstrap4",
        language: 'es'
    })
    var select_anios = $('select[name="anio"]');
    $('select[name="carrera"]').on('change', function () {
        var id = $(this).val();
        console.log(id);
        var options = '<option value="">---------</option>';
        if (id === '') {
            select_anios.html(options);
            return false;
        }
        $.ajax({
            url: window.location.pathname,
            type: 'POST',
            data: {
                'action': 'search_anios_id',
                'id': id
            },
            dataType: 'json',

        }).done(function (data) {
            if (!data.hasOwnProperty('error')) {
                select_anios.html('').select2({
                    theme: "bootstrap4",
                    language: 'es',
                    data: data
                });
                return false;
            }
            message_error(data.error);
        }).fail(function (jqXHR, textStatus, errorThrown) {
            //alert(textStatus + ': ' + errorThrown);
        }).always(function (data) {
        });
    });

    select_anios.on('change', function () {
        var value = $(this).val();
        console.log(value);
    });
});