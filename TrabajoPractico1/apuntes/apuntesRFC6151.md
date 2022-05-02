<h1> Update de consideraciones de seguridad para el MD5 y el HMAC-MD5 </h1>

<h2> Introducción </h2>

Los ataques publicados contra el MD5 muestran que no es prudente usar MD5 cuando la resistencia de colisión es requerida (**QUÉ SERÁ ESTO, INVESTIGAR**). HMAC define un mecanismo para autenticacion de mensajes usando funciones criptográficas de hash. Cualquier algoritmo de digestion de mensajes puede ser usado, pero la fuerza criptografica del HMAC reside en las propiedades de la funcion de hash. 
