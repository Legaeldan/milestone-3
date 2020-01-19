$(document).ready(function(){
    $(".dropdown-trigger").dropdown();
    $('select').formSelect();
    $('.modal').modal();
    $('.tooltipped').tooltip();
    $('.fixed-action-btn').floatingActionButton();
    if ($('#ingredient-form').length > 0){
      $('.container').removeClass("valign-wrapper")
    }
    if ($('#drinkResponse').length > 0){
      $('.container').removeClass("valign-wrapper")
    }
  });