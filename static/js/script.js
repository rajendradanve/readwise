$(document).ready(function(){
    $('.sidenav').sidenav({edge: "right"});
    $('.modal').modal();
    $('select').formSelect();
    $('#delete-modal').modal();

    $('#delete-btn').click(function(){

      $("#delete-confirmation-text").text($('#book-name').text());
    });
  });