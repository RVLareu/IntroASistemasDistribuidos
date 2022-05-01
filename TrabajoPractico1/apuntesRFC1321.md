<h1> Algoritmo de digestión de mensajes MD5 </h1>

<h2> RESUMEN </h2>

Toma por entrada un mensaje de largo arbitrario y produce como salida una "huella digital" de 128 bits. Computacionalmente es inviable producir 2 mensajes que tengan la misma huella digital ("mensaje digerido") o producir un mensaje dada una salida específica. El algoritma MD5 está pensado para aplicaciones con firma digital, donde un archivo debe ser comprimido de manera segura antes de ser encriptado con una llave privada (secreta) bajo un criptosistema de llave pública como RSA. Es rápido en arquitecturas de 32 bits. No requiere grandes tablas de sustitución. Se puede poner el código bastante compacto.
Es una extensión del MD4, más "conservador" en diseño. MD4 estuvo diseñado para ser muy rápido, al límite de poder ser vulnerado por un ataque criptoanalitico. MD5 es más lento, pero brinda más seguridad. Para aplicaciones OSI, el objeto identificador es:

```
md5 OBJECT IDENTIFIER ::= iso(1) member-body(2) US(840) rsadsi(113549) digestAlgorithm(2) 5}
```

<h4> NOTA: RSA </h4>
RSA es un sistema criptográfico de clave pública que utiliza factorización de números enteros. El algoritmos es válido tanto para cifrar como para firmar digitalmente. La seguridad radica en el problema de la factorización de números enteros. Como en todos los sistemas de clave pública, cada usuario posee dos claves de cifrado: una pública y otra privada. Cuando se quiere enviar un mensaje, el emisor busca la clave pública del receptor, cifra su mensaje con esa clave, y una vez que el mensaje cifrado llega al receptor, este lo descifra con su clave privada.

<h4> NOTA: APLICACIONES BASADAS EN OSI, IDENTIFICADOR DE OBJETO </h4>
<h4> NOTA: MD4 </h4>


<h2>TERMINOLOGIA Y NOTACIÓN </h2>

palabra será de 32 bits, byte de 8 bits. x_i es "x sub i". Las operaciones lógicas son "bit-wise"

<h2> DESCRIPCIÓN DEL ALGORITMO MD5 </h2>

Entrada de *b* bits, queremos hallar su mensaje digerido.

```

m_0 m_1 ... m_{b-1}

```

Se realizan los siguientes pasos para digerir el mensaje:

1. **Agregar bits de padding**: se extiende el mensaje (*padded*) para que el largo en bits sea congruente a 448, modulo 512. Esté a 64 bits de ser múltiplo de 512. Se hace agregando un bit en 1, y el resto en 0. Se agrega al menos 1 bit y como máximo 512.

2. **Agregar largo**: al paso previo se le agrega el largo *b* en representación de 64 bits. Si es mayor a 2^64, solo se ponen los 64 de menor orden de *b* (como 2 palabras de 32 bits). Ahora el mensaje es múltiplo de 512 bits y de 16 palabras o 32 bits. `M[0 ... N-1]` son las palabras del mensaje, con *N* múltiplo de 16

3. **Inicializar el Buffer de MD**: para computar el mensaje digerido se usa un buffer de 4 palabras: `(A,B,C,D)`. Cada uno es un registro de 32 bits. En *little endian*, se inicializan con los siguientes valores hexadecimales:

```

A: 01 23 45 67
B: 89 ab cd ef
C: fe dc ba 98
D: 76 54 32 10

```

4. **Procesar el mensaje en bloques de 16 palabras**: primero se definen 4 funciones auxiliares que toman 3 palabras de 32 bits y tienen una salida de 32 bits.

```

F(X,Y,Z) = XY v not(X) Z
G(X,Y,Z) = XZ v Y not(Z)
H(X,Y,Z) = X xor Y xor Z
I(X,Y,Z) = Y xor (X v not(Z))

```

En cada bit, F actúa como un condicional: si X entoces Y sino Z. Si los bits de X,Y y Z son independientes y *unbiased* entonces también lo serán los de F(X,Y,Z). Esto último también ocurre para G, H e I. En este paso se usa una tabla de 64 elementos `T[1 ... 64]` contruida a partir de la función seno. `T[i]` es igual a la parte entera de `4294967296 * abs(sin(i))` con i en radianes. El procesamiento es el siguiente:

```c

/* Process each 16-word block. */
   For i = 0 to N/16-1 do

     /* Copy block i into X. */
     For j = 0 to 15 do
       Set X[j] to M[i*16+j].
     end /* of loop on j */

     /* Save A as AA, B as BB, C as CC, and D as DD. */
     AA = A
     BB = B
     CC = C
     DD = D

     /* Round 1. */
     /* Let [abcd k s i] denote the operation
          a = b + ((a + F(b,c,d) + X[k] + T[i]) <<< s). */
     /* Do the following 16 operations. */
     [ABCD  0  7  1]  [DABC  1 12  2]  [CDAB  2 17  3]  [BCDA  3 22  4]
     [ABCD  4  7  5]  [DABC  5 12  6]  [CDAB  6 17  7]  [BCDA  7 22  8]
     [ABCD  8  7  9]  [DABC  9 12 10]  [CDAB 10 17 11]  [BCDA 11 22 12]
     [ABCD 12  7 13]  [DABC 13 12 14]  [CDAB 14 17 15]  [BCDA 15 22 16]

     /* Round 2. */
     /* Let [abcd k s i] denote the operation
          a = b + ((a + G(b,c,d) + X[k] + T[i]) <<< s). */
     /* Do the following 16 operations. */
     [ABCD  1  5 17]  [DABC  6  9 18]  [CDAB 11 14 19]  [BCDA  0 20 20]
     [ABCD  5  5 21]  [DABC 10  9 22]  [CDAB 15 14 23]  [BCDA  4 20 24]
     [ABCD  9  5 25]  [DABC 14  9 26]  [CDAB  3 14 27]  [BCDA  8 20 28]
     [ABCD 13  5 29]  [DABC  2  9 30]  [CDAB  7 14 31]  [BCDA 12 20 32]

     /* Round 3. */
     /* Let [abcd k s t] denote the operation
          a = b + ((a + H(b,c,d) + X[k] + T[i]) <<< s). */
     /* Do the following 16 operations. */
     [ABCD  5  4 33]  [DABC  8 11 34]  [CDAB 11 16 35]  [BCDA 14 23 36]
     [ABCD  1  4 37]  [DABC  4 11 38]  [CDAB  7 16 39]  [BCDA 10 23 40]
     [ABCD 13  4 41]  [DABC  0 11 42]  [CDAB  3 16 43]  [BCDA  6 23 44]
     [ABCD  9  4 45]  [DABC 12 11 46]  [CDAB 15 16 47]  [BCDA  2 23 48]

     /* Round 4. */
     /* Let [abcd k s t] denote the operation
          a = b + ((a + I(b,c,d) + X[k] + T[i]) <<< s). */
     /* Do the following 16 operations. */
     [ABCD  0  6 49]  [DABC  7 10 50]  [CDAB 14 15 51]  [BCDA  5 21 52]
     [ABCD 12  6 53]  [DABC  3 10 54]  [CDAB 10 15 55]  [BCDA  1 21 56]
     [ABCD  8  6 57]  [DABC 15 10 58]  [CDAB  6 15 59]  [BCDA 13 21 60]
     [ABCD  4  6 61]  [DABC 11 10 62]  [CDAB  2 15 63]  [BCDA  9 21 64]

     /* Then perform the following additions. (That is increment each
        of the four registers by the value it had before this block
        was started.) */
     A = A + AA
     B = B + BB
     C = C + CC
     D = D + DD

   end /* of loop on i */


```

*Falta analizar este bloque de codigo infame, masomenos 1 hs de dedicacion - fin pagina 5*
