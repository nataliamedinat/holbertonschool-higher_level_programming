$.get( "https://swapi.co/api/people/5/?format=json", function( char ) {
    $( "DIV#character" ).text(char.name);
  });
