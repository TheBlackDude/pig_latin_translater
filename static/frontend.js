
const send = document.getElementById('send');
send.onclick = function(e){
  const translate = document.getElementById('translate').value;
  // send the text to the api for translation
  fetch('http://localhost:8080/api/v1/translate', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ word: translate })
  })
  .then( response => response.json() )
  .then( data => {
    document.getElementById('result').innerHTML = data.word;
    document.getElementById('translate').value = '';
  } );
}
