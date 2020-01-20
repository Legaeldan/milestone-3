$(document).ready(function(){
    $(".dropdown-trigger").dropdown();
    $('select').formSelect();
    $('.modal').modal();
    $('.tooltipped').tooltip();
    $('.fixed-action-btn').floatingActionButton();
    if ($('.remove-valign').length > 0){
      $('.container').removeClass("valign-wrapper")
    };
    $(".discover-drink").on("error", function () {
      $(this).attr("src", "../static/images/no-image.png")
    });
    $(".drink-image").on("error", function () {
      $(this).attr("src", "../static/images/no-image.png")
    });
  });