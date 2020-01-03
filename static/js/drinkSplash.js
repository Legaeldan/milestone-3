fetch('https://www.thecocktaildb.com/api/json/v1/1/random.php')
  .then(response => response.text())  
.then(html => {
  // console.log(html);
  document.getElementById('drinkResponse').innerHTML = html;
})