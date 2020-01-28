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
    $('.modal').modal();
    $('.tooltipped').tooltip();
    $('.fixed-action-btn').floatingActionButton();
    if ($('.remove-valign').length > 0){
      $('.container').removeClass("valign-wrapper")
    };

  });