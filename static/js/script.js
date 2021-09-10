$(document).ready(function(){
    $('.sidenav').sidenav();
    $('.modal').modal();
    $('select').formSelect();

    let star_rating = $("input[name='star_rating'")
    for(let i=0; i<star_rating.length; i++){
      star_rating[i].click(function(){
        i = this.val();
        console.log("test");
        $("#rating_value").text("your are best");
      })
    }

  });