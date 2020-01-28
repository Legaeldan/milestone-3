var toggledNavbar
const isToggled = window.localStorage.getItem('toggled');

$(document).ready(function(){
    $(".dropdown-trigger").dropdown();
    $('select').formSelect();
    $('.sidenav').sidenav();
    $('.modal').modal();
    $('.tooltipped').tooltip();
    $('.fixed-action-btn').floatingActionButton();
    if ($('.remove-valign').length > 0){
      $('.container').removeClass("valign-wrapper")
    };
    if (isToggled == 'enabled'){
      $('#nav-mobile').addClass("hide");
      $('.sidenav').addClass("hide");
      $('.sidenav-trigger').addClass("hide");
      $('.fixed-action-btn').removeClass("hide");
    };
});

$('#MainNavToggle').on("click", function(){
  $('.toggleNavbar').addClass("hide");
  $('.fixed-action-btn').removeClass("hide");
  window.localStorage.setItem('toggled', 'enabled')
});

$('#FabNavToggle').on("click", function(){
  $('.fixed-action-btn').addClass("hide");
  $('.toggleNavbar').removeClass("hide");
  window.localStorage.setItem('toggled', 'disabled');
});

$('#sideNavToggle').on("click", function(){
  $('.toggleNavbar').addClass("hide");
  $('.fixed-action-btn').removeClass("hide");
  window.localStorage.setItem('toggled', 'enabled');
});