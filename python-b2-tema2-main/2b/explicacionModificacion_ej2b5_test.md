"He modificado el test porque Wikipedia bloquea peticiones automáticas sin identificación. 
El test original no incluía un User-Agent (identificador de navegador), por lo que Wikipedia devuelve un error 403. 
Para solucionarlo he añadido headers con un User-Agent que simule dos posible navegadores o Firefox o Chorme, 
permitiendo así que Wikipedia acepte la petición. 
Como lo he puesto en una lista he importado la libreria ramdom para que reconozca indistintamente cualquiera de las dos simulaciones Chorem o FireFox.

Pedro Rios.

