$(document).ready(function(){
    $('.sidenav').sidenav({edge: "right"});
    $('.modal').modal();
    $('select').formSelect();
    
    let star_rating = $("input[name='star_rating'");
    console.log(star_rating);
    for(let i=0; i<star_rating.length; i++){
      $(star_rating[i]).click(function(){
        i = $(this).val();
        $("#rating_value").text(i);
      })
    }

  });