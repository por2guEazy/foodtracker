// Calendar day and time picker for input
$('.datepicker').datetimepicker({
    format:'Y-m-d H:m'
});

// Show edit profile field
$('.show-edit-profile').on('click', function(){
    $('.edit-profile').removeClass('d-none');
})

// Hide edit profile fields
$('.edit-profile-submit').on('click', function() {
    $('.edit-profile').addClass('d-none');
});


// Add current datetime to input field
$('.add-time-now').on('click', function() {
    $('#id_date_added').val(moment().format('Y-MM-DD HH:mm'));
});

// Display remove btn and done button 
$('.edit-list').on('click', function() {
    $('.rmv-item').removeClass('d-none');
    $('.edit-list-done').removeClass('d-none');
});

// Hide rmv buttons 
$('.edit-list-done').on('click', function() {
    $('.rmv-item').addClass('d-none');
});
   
