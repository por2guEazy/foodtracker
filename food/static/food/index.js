// Calendar day and time picker for input
$('.datepicker').datetimepicker({
    format:'Y-m-d H:m'
});

$('.show-edit-profile').on('click', function(){
    $('.edit-profile').removeClass('d-none')
})

$('.edit-profile-submit').on('click', function() {
    $('.edit-profile').addClass('d-none')
});
