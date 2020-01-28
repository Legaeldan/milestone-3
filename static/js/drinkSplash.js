var toggledNavbar
const isToggled = window.localStorage.getItem('toggled');

if (isToggled == null){
  console.log('null');
  window.localStorage.setItem('toggled', 'disabled');
  toggledNavbar = 'disabled';
  console.log('state set to disabled');
} else if (isToggled == 'disabled'){
  toggledNavbar = 'disabled';
  console.log('navbar disabled');
} else if (isToggled == 'enabled'){
  toggledNavbar = 'enabled';
  console.log('Navbar is enabled');
} ;

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
    if (toggledNavbar == 'enabled'){
      $('#nav-mobile').addClass("hide");
      $('.sidenav').addClass("hide");
      $('.sidenav-trigger').addClass("hide");
      $('.fixed-action-btn').removeClass("hide");
    };
});

$('#MainNavToggle').on("click", function(){
  $('#nav-mobile').addClass("hide");
  $('.sidenav').addClass("hide");
  $('.sidenav-trigger').addClass("hide");
  $('.fixed-action-btn').removeClass("hide");
  window.localStorage.setItem('toggled', 'enabled')
});

$('#FabNavToggle').on("click", function(){
  $('.fixed-action-btn').addClass("hide");
  $('#nav-mobile').removeClass("hide");
  $('.sidenav').removeClass("hide");
  $('.sidenav-trigger').removeClass("hide");
  window.localStorage.setItem('toggled', 'disabled');
});

$('#sideNavToggle').on("click", function(){
  $('.sidenav').addClass("hide");
  $('.sidenav-trigger').addClass("hide");
  $('#nav-mobile').addClass("hide");
  $('.fixed-action-btn').removeClass("hide");
  window.localStorage.setItem('toggled', 'enabled');
});