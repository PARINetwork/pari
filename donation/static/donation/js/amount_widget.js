$(function () {
    $('.other-amount').focus(function () {
        $(this).prev().prop('checked', true);
    });

    $('input[type=radio][name=amount_0]').change(function() {
        if ($(this).val().toLowerCase() !== 'other')
            $('.other-amount').val('');
    });
});
