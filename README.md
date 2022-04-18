# Introducción A Sistemas Distribuidos - 75.43

<h3> Resumen del Libro </h3>

<details>
 <summary>  <h3>Capitulo 1 red de computadoras e Internet</h3> 🍾 </summary> 
 
 </br>

*host* o *end systems*: dispositivos conectados a la red (lapotot, tablet, reloj, etc).

Estos ultimos conectados por una red de *communication links* y *packet switches*.

![image](https://user-images.githubusercontent.com/71232328/160488180-daf2192f-ce6a-45b4-ac0f-9b4b0ba07cc0.png)

Los *links*  transmiten de acuerda a una *transmission rate* medida en bits/segundo.

*Packet*: paquete de informacion a ser enviado a través de la red.

El *packet switch* toma el *packet* que viene de su *comunication link* de entrada y lo redirecciona a uno de salida. Un *packet switch* puede ser un *router* (en *network core*) o un *link-layer switch*(en *acces network*).

El camino recorrido por el *packet* es el *route* o *path*.

 <h4> Analogia </h4>

*packets* = camiones.
*comunication links* = rutas.
*packet switches* = intersecciones.

*end systems* accedent a internet a traves de *Internet Service Providers (ISPs)*. Cada *ISP* es en si mismo una red aparte. Los *ISPs* o *lower tier ISPs* estan interconectados por *upper tier ISP* (fibra optica).

Las piezas que componen internet corren protocolos para controlar envio y recepcion de datos. El *Transmission Control Protocol (TCP)* y *Internet Protocol (IP)* son los mas importantes. 

*internet standards* son desarrollados por la *IETF*. Estos documentos son llamados *request for comments (RFCs* y definen los protocolos

El internet tambíen puede ser descripto como una infraestructura que provee servicios a aplicaciones (*distributed applications*). Corren en *end systems*.
Los *end systems* proveen interfaces para *sockets* que especifican como solicitar y enviar informacion a otro *end system*

<h4> Protocolo </h4>

![image](https://user-images.githubusercontent.com/71232328/160490600-228c2304-3668-4ec8-883f-a11a39c9c6a2.png)

</br>

Un protocolo define el formato y orden de los mensajes a intercambiar entre dos o mas entidades en comunicacion, al igual que las acciones a tomar luego de enviar/recibir los mensajes
Ambos que se esten comunicando deben estar utilizando el mismo protocolo


*end systems* son también conocidos como *hosts*. Estos ultimos se dividen en clientes y servidores. La mayoria de los servidores residen en *data centers*

*access network*: la red que conecta fisicamente un *host* al primer *router* en su camino a otro *end system*

El acceso a internet residencial mas comun es por *digital suscriber line (DSL)* (en general lo provee la compañia de telefono, el modem usa la linea telefonica en este caso) y por cable.

![image](https://user-images.githubusercontent.com/71232328/160491855-2dd767ac-9f61-494a-b1af-6c0cfa0d3f2b.png)


</br>

Existen estándares para DSL que definen multiples *transmission rates*.

Por otra parte, los cables de acceso a internet hacen uso del cable del proveedor de television.

</br>

![image](https://user-images.githubusercontent.com/71232328/160492070-cf203c45-c8c1-4129-936f-73eaa410c91a.png)


</br>

requiere modems especiales para cable, en general conectados a la PC por un puertp *ethernet*. En estos casos los *packets* llegan a todos. Los *channel* de subida y bajada son compartidos.


Más veloz que los ultimos dos pero menos común en *fiber to home (FTTH)*.

*LAN (local area network)* es usada para conectar un *end system* al primer *router (edge)*. En general se hace via *ethernet switch*.

![image](https://user-images.githubusercontent.com/71232328/160492621-8adc1fa6-4871-415c-a273-36bc2eca2d63.png)


</br>

Tambien es posbile tener una *wireless LAN* basada en IEEE (*WIFI*)

![image](https://user-images.githubusercontent.com/71232328/160492779-54c7125b-1417-4739-84e9-0909ae515057.png)

*Wide-Area Wirelles acces: 3g and LTE*, mayor alcance que el wifi.

Los bits se propagan a través de un medio físico: par trenzado, coaxial, fibra optica, espectro radial, etc. Puede ser un medio guiado o no. En el primer caso las ondas son guiadas a traves de un medio fisico (cable). En el caso de no ser guiado, las ondas se propagan por la atmosfera y espacio (*wireless LAN*). Un par trenzado conocido es el *Unshielded twisted pair (UTP)*. El cable coaxial puede ser usado como un medio compartido. La fibra optica traslada pulsos de luz, pero los dispositivos opticos son muy costosos. Canales de transmision radial sufren mayor interferencia y tienen tres categorias: distancia corta, locales y largo alcance (kilometros). Canales de transmision satelital transmiten/reciben microondas en bandas de frecuencia determinadas, los satelites pueden ser geoestacionarios u orbitar más cerca de la tierra.

 <h4> Core  </h4>

*end systems* intercambian mensajes. Estos mensajes se dividen en *packets* para ser enviados. Cada *packet* viaja a través de *communication links* y *packet switches (routers or link-layer switches)*. Se transmite al *rate* del *communication link*. Entonces si el *rate* es R y el largo del *link* es L, el tiempo de transmisión es `L/R segundos`.

Los *packet switches* usan *store-and-forward transmission*. Debe recibir el *packet* entero antes de empezar a transmitirlo.

![image](https://user-images.githubusercontent.com/71232328/160494400-f1327cb7-36ba-471f-8a29-270b3957f523.png)

Por cada *link* que tiene el *packet switch*, va a tener un *output buffer* o *output queue* donde guarda *packets* que está a punto de enviar. Puede ocurrir que llegue un *packet* y deba esperar en el *output buffer* a que termine otro: *queuing delay*. Este delay depende de que tan congestionada esté la red.


![image](https://user-images.githubusercontent.com/71232328/160518735-493aef40-248d-4d2a-9d3c-3bcb698e71a6.png)

Si el *packet* llega y la cola está llena entonces ocurre una *packet loss*. O el que llega es dropeado o uno que ya está en la cola.

¿Cómo determina el *router* a donde enviar el *packet*?

Cada sistema tiene su direccion IP. En el header del *packet* va a figurar la ip de destino. Cada *router* examina esta porcion y se basa en una *forwarding table* para direccionar el *packet*. La tabla está creada en base a un *routing protocol*, por ejemplo el del camino más corto para determinar el próximo *router*.

También puede moverse data de otra manera que no es *packet switching*, sino *circuit switching*. En estos casos el *path* entre *end systems* se encuentra reservado por el tiempo que dure la comunicación, no ocurre esto en el caso previamente visto. Cuando dos *host* se quieren comunicar se establece una *end-to-end connection*, reservando el circuito que los une. Limita la cantidad de conexiones en simultaneo que se pueden tener.

En el caso de *packet switching* no se garantiza la llegada a destino del mismo, si que se dará el mayor esfuerzo.

Un circuito es implementado con una *frequency-division multiplexing (FDM)* o con una *time-division multiplexing (TDM)*. En la primera se le dedica una frecuencia a cada conexion. En el caso de *TDM* se le otorga a cada conexion una cantidad fija de tiempo.

![image](https://user-images.githubusercontent.com/71232328/160519904-75316e99-12f6-4652-b128-7928d8b5e7ab.png)

Circuitos dedicados tienen periodos silenciosos en los que se desperdician.

*Packet switching* es superior en eficiencia. Mientras que *circuit switching* reserva en el *link* desconociendo la demanda (desperdiciando espacio), *packet switching* reserva el *link* en base a la demanda.


Para conectar *ISPs* se hace una red de redes. El *access ISP* es *customer*, mientras que el *global transit ISP* es un proveedor.
Cada *access ISP* paga al *regional ISP* al que se conecta, quien a su vez paga al *tier-1 ISP* al cual se conecta. Este ultimo no paga a nadie ya que no se conecta a nadie.

Admemás en la red hay *PoP* (grupo de *routers* en la red del proveedor donde *customer ISPs* se pueden conectar a un *provider ISP*.
Para reducir costos, *customer ISPs* que sean vecinos pueden unirse (*peer*) siendo beneficioso para ambos. También existen *Internet Exchange Points (IXP)* donde multiples *ISPs* pueden unirse (*peer*).
Finalmente tenemos en la ultima capa los *content-provider netwroks*, por ejemplo google.

![image](https://user-images.githubusercontent.com/71232328/160521215-521f2157-3565-4bee-88c0-ef64db322dae.png)



*processing delay*: tiempo requerido para examinar el *packet* y ver a qué *link* dirigirlo.

*queuing delay*: tiempo que espera en la cola a ser transferido **(???????????? no era cuando recibia)**. Depende de la congestion.

*transmission delay*: `L/R`, siendo L el largo del *packet* y R la tasa de transimsion. Tiempo requerido en transmitir todos los bits por el *link*. No tiene nada que ver con la distancia entre *routers*.

*propagation delay*: una vez en el *link*, los bits deben llegar al proximo router. Depende de la distancia entre *routers* y el material. `d/s` siendo d la distancia y s la velocidad de propagación del *link*.

![image](https://user-images.githubusercontent.com/71232328/160522042-38efadca-e33d-4f32-99be-823be10f9dcd.png)

Sumados generan un *total nodal delay*

Si R es la tasa de transmision en bits/sec, **a** es la tasa de arribo de *packets*, L el largo de los packets entonces la tasa de arribo de bits es `L * a`. `L*a/R` es la intensidad del tráfico. Si `L*a/R > 1` entonces aumentará el *queuing delay*

![image](https://user-images.githubusercontent.com/71232328/160522582-09cc2afa-dc2b-4597-b1cd-4fff2c8ff5c5.png)

Una cola tiene capacidad finita. Si una *packet* llega a un *router* con la cola llena, va a ser un *drop*. En resumen, ese *packet* se pierde.

El delay entre *end systems* con N-1 *routers* entre ellos es `dend-end = N(dproc+dtrans+dprop+dqueuing)`.

*end-to-end throughput*: el instantaneo es la tasa en bits/sec a la que un host recibe un mensaje. Si envio de servidor a cliente: si la tasa de recepcion es más rapida que la de transmision entonces no va a poder transmitirlos igual de rápido que los recibe. En este caso Rc<Rs y el *end-to-end throughput* es Rc. Idealmente Rc>Rs y el *end-to-end throughput* es Rs.

![image](https://user-images.githubusercontent.com/71232328/160523899-188591c9-c409-4030-8e76-1d3522770391.png)

 <h3> Protocol Layering  </h3>

cada protocolo se corresponde con una capa.

Protocolos de la capa de aplicacion siempre estan implementadas en software. La capa fisica y de linkeo son las encargadas de manejar la comunicacion en un link (en general Ethernet o WIFI asociadas con un *link*). La cpa de red es un mix entre fisica y hardware

![image](https://user-images.githubusercontent.com/71232328/160524387-999652a6-db64-4d99-9ed4-cc0fc7e4193f.png)

 <h4> Capa de aplicaciones  </h4>

donde residen las aplicaciones de red y sus protocolos como HTTP, SMTP, FTP, DNS. Se distribuye sobre muchos *end systems*. La aplicacion en uno intercambiendo *packets* con la aplicación en otro *host* siguiendo un protocolo. En esta capa la data son mensajes.

 <h4> Capa de transporte  </h4>

transporta los mensajes de la capa de aplicacion entre *end points*. Protocolos: TCP y UDP

 <h4> Capa de red </h4>

Mueve los *packets* de la capa de red llamados *datagrams* de un *host* a otro. Protocolo IP, que define los campos en el *datagram*. También hay *routing protocols* para determinar las rutas que toman los *datagrams*.

 <h4> Capa de linkeo </h4>

Para mover un *packet* entre un nodo y tro (*host* o *router*), la capa de red acude a la capa de linkeo. Aquí se pasa el *datagram* a la capa de linkeo, que lo lleva al proximo nodo, donde vuelve a la capa de red. Como ejemplo son Ethernet, Wifi. Un *datagram* puede ser manejado por distintos protocolos en la capa de linkeo.

 <h4> Capa de física </h4>

Su trabajo es mover bits entre un nodo y el siguiente. Los protocolos dependen del medio (fibra, par trenzado, etc). Ethernet tiene varias protocolos en esta capa: una para par trenzado, otro para coaxial, fibnra, etc.

![image](https://user-images.githubusercontent.com/71232328/160525485-3d8082b6-c118-4180-8700-5750eb3e8fae.png)

Notar que routers y switches de la capa de linkeo no implementan todas las capas. En cada capa un *packet* tiene dos campos: *header* y *payload*. El ultimo es un *packet* de la capa anterior y *header* sirve para que la capa actual actue. A esto se llama encapsulacion.

<h3> OSI </h3>

Otra forma de ver los protocolos distinta al *stack*.

![image](https://user-images.githubusercontent.com/71232328/160525375-169cb37b-6664-40fa-9a2a-4b125961864e.png)

Malware (?)



</details>


<details>
 
<summary> <h2>Capitulo 2 Capa de aplicación</h2> 🍾</summary>
 
</br>
 
Al desarrollar una aplicación, hay que escribir software de tal manera que pueda correr en multiples sistemas (no es necesario en *routers* o *link-layer switches*, estos no funcionan en la capa de aplicación). La arquitectura de la aplicación está diseñada por el desarrollador, a diferencia de la arquitectura de la red. Esta puede ser cliente-servidor o *peer-to-peer*.

En la arquitectura cliente-servidor , siempre hay un *host* llamado servidor que recibe peticiones de otros *host* llamados clientes. En esta arquitectura los clientes no se comunican directamente entre si. El servidor tiene una dirección IP fija. Para aplicaciones con muchos clientes, se tiene un *data center* con varios *host* creando un servidor virtual grande.
 
En la arquitectura P2P no hay servidores dedicados, se basa en la comunicacion entre usuarios (ej: Torrent). Esta arquitectura es auto escalable.
 
<h3> Comunicacion </h3>
 
Los que se comunican no son los programas, sino los procesos en diferentes (o el mismo) *end systes*. Lo hacen mediante mensajes. En general en una comunicacion, uno es el cliente y el otro el servidor. El que inicia la conexion es el cliente, el que espera a ser conectado, el servidor. Los mensajes se envian y reciben a través de una interfaz de software llamada *socket*. El *socket* es la interfaz entre la capa de aplicacion y la de transporte. También llamada *application programming interface (API)* entre la aplicacion y la red.
 
Para identificar al proceso que recibe mensajes debe tenerse la direccion del host (IP) y un algo que identifique al proceso receptor en el host de destino. Al host lo define la dirección IP (32 bits). Para identificar al proceso, su utiliza el número de puerto.
 
La aplicacion envia mensajes por el socket, la capa de transporte debe llevarlos al socket de destino. Un protocolo de la capa de transporte puede ofrecer varios servicios:

* *Reliable Data Transfer*: asegura que no habrá pérdida de paquetes. Si no lo asegura, esto puede ser tolerable para ciertas aplicaciones (*loss-tolerant applications*) pero no para otras como son las aplicaciones multimedia
* *Throughput*: asegura una tasa mínima de **r** bits/sec. Las aplicaciones que requieren una tasa especifica son *bandwidth-sensitive applications*. Las que no so *elastic applications*.
* *Timing*: un tiempo máximo de arribo del paquete desde que sale hasta que llega al socket receptor (delay).
* *Security*: puede proveer mas de un servicio de seguridad. Puede encriptar los datos al salir y desencriptarlos al llegar.
 
<h3> Servicios de transporte provistos por internet </h3>
 
Las redes TCP/IP tienen 2 protocolos de transporte: UDP y TCP.
 
Servicios de TCP:

* *Connection-oriented servide*: cliente y servidor intercambian informacion antes de que empiezen a fluir los mensajes de la aplicacion (*handshake*). Luego de esto se dice que existe la conexion TCP. Pueden enviarse mensajes al mismo tiempo. Una vez finalizada, debe destruirse la conexion.
* *Reliable data transfer*: se va a enviar toda la data sin errores y en orden.
* *congestion-control mechanism*
 
*TCP-enhanced-with-SSL (Secure Sockets Layer)* agrega seguridad (encripta, autenticacion de *end point*, etc).
 
Servicios de UDP:
 
* *connectionless*: no hay *handshake*
* *unreliable data transfer*: no garantiza que llege el mensaje. Pueden llegar en desorden
* No tiene mecanismo de control de congestion
* El lado que envia, puede hacerlo al *rate* que quiera.
 
En ambos casos, no se proveen servicios para *throughput* y *timing*.
 
<h3> Protocolos de capa de aplicación </h3>
 
Definen como los procesos de aplicaciones se envian mensajes entre ellas:
* tipo (request o respuesta)
* Sintaxis (campos)
* Semantica (qué contienen los campos)
* Reglas para cuándo enviar y recibir mensajes

## Web y HTTP
 
*HyperText Transfer Protocol (HTTP)* se implementa en el cliente y en el servidor. Web browsers implementan el lado del cliente y Web Servers el lado del servidor. HTTP usa TCP como protocolo de transporte.
 
![image](https://user-images.githubusercontent.com/71232328/160632290-47bcc71e-05ac-40d4-b088-564287af5e29.png)

El servidor no guarda informacion del cliente, por lo que se dice que HTTP es *stateless protocol*.
 
### Tipos de conexiones
 
Cuando hay interacciones cliente-servidor debe definirse si las request/respuesta van en la misma conexion TCP (*persistent connections*) o en distintas (*non-persistent connections*). Por default HTTP usa *persistent connections*. En *non-persistent connections* puede ocurrir cierto paralelismo.

*Round-trip-time (RTT)*: tiempo que le toma a un paquete viajar desde el cliente al servidor y volver. Incluye delay de propagacion, delay de cola y de procesamiento.
 
![image](https://user-images.githubusercontent.com/71232328/160634079-c4d20bf4-45b9-46e4-9f0a-c5f635d36eb8.png)
 
Se observa que cada conexion tiene un delay de 2 RTT, gran contra en *non-persistent connections*.
 
## Formato del mensjae HTTP
 
Hay dos tipos de mensaje: request y respuesta
 
* Request: primer linea es la *request line*, tiene 3 campos: metodo (GET, POST, HEAD, PUT, DELETE), URL y version de HTTP. Las lineas que siguen son *header lines*. La de Host especifica el host donde reside el objeto, en connection va el tipo de conexion, en *user-agent* va el browser y en *accept-language* va el lenguaje que prefiere el usuario (varios headers mas como este)
 
 ![image](https://user-images.githubusercontent.com/71232328/160635494-45571e96-5f4a-4a81-9fa3-ad910fec6afd.png)

El campo *entity* va lleno cuando se usa el método POST enviando info. También puede ir en la URL con un método GET. El HEAD se utiliza para debugging. PUT es para subir objetos a servidores web
 
* Respuesta: tiene una *status line* (3 campos: version del protocolo, codigo de status y el mensaje de status), seis *header lines* y un *entity body* (contiene lo que se pidió en el request). Las *header lines*: *date* tiene hora y dia en que el servidor envia data, *Server* indica que servidor generó el mensaje, *Last modified* indica el momento de creacion o última modificacion del objeto, *Content-Lenght* indica el largo del *body* y *Content-type* el tipo del body (HTML por ej). El status code puede ser varios: 200 es OK, 301 es que el objecto fue removido, 400 es bad request, 404 no encontrado, etc. Visitar https://http.cat/.
 
 ![image](https://user-images.githubusercontent.com/71232328/160636893-f80a5076-f769-44e2-9875-012d6659b7b6.png)
 
 ### Interacción Usuario-Servidor
 
##### Cookies
 
HTTP es *sateless* pero usa cookies para trackear a los usuarios. Esta tecnologia tiene 4 componentes:
 
* Cookie Header line en respuesta de HTTP (Set-Cookie: <identificador>)
* Cookie Header line en request de HTTP (Cookie: <identificador>)
* archivo cookie guardado en el *end system* y manejado por el browser
* base de datos en la pagina de internet.
 
 ![image](https://user-images.githubusercontent.com/71232328/160638156-1558a839-3a47-47ca-92df-29930aaef2c7.png)

 
 ##### Web Caching
 
 El cache de la web (*proxy server*) guarda copias de objetos recientemente *requested*. Antes de establecer TCP con servidor, se establece con el *Web Cache* y se ve si tiene el objeto deseado. si lo tiene, se envia en una respuesta HTTP. Sino, la *Web Cache* establece una conexion TCP con el servidor, envia una request y al recibir una respuesta la envia al usuario, previamente almacenando una copia.

![image](https://user-images.githubusercontent.com/71232328/160639015-5b6e00be-4d9d-43b2-88e4-59e4e807aeec.png)
 
 El *Web cache* hace la conexion más rapida y reduce el trafico hacia el servidor. *Content Distribution Networks (CDNs)*. Una compañia CDN instala caches a lo largo de todo internet.
Aparece un problema, el objecto en la cache puede estar desactualizado. Aparece el GET condicional, que agrega campo *If-Modified-Since*. El cache envia al server un request con este campo, indicando al servidor que envie un nuevo objecto si la fecha en que fue modificado es distinta a la del request de la cache (304 not modified status code)
 
 ![image](https://user-images.githubusercontent.com/71232328/160639460-651fe762-7f7a-4664-93d1-b25894394221.png)

## Mail en Internet
 
3 componentes:
* *User agents*: permite a los usuarios leer, responder, enviar, guardar y escribir mensajes (Outlook)
* *mail servers*: Aqui se envian los mensajes, donde son colocados en una cola de salida. Cuando un usuario quiere leer, el agente lo recupera de este servidor. Aqui estan las *mailbox*.
* *Simple Mail Transfer Protocol (SMTP)*
 
![image](https://user-images.githubusercontent.com/71232328/160641013-5ab15568-4fc0-4502-be9c-1893ca8a87f6.png)

 Si un servidor no puede enviar un mensaje, lo guarda en una cola de mensajes y lo intenta un tiempo despues.
 
SMTP es el principal protocolo de la capa de aplicaciones para mails. Usa *reliable data transfer* de TCP. Tiene un lado cliente (envia) y otro servidor(mail server). Ambos lados residen en todos los *mail servers*. SMTP restringe a ASCII de  7 bits.

![image](https://user-images.githubusercontent.com/71232328/160644403-b1b54b24-6979-48d4-816b-91c74f01f175.png)

SMTP tiene *handshake* donde se indica las direcciones de email de ambos.
Comandos del cliente: HELO, MAIL FROM, RCPT TO, DATA, QUIT, CRLF.CRLF (linea vacia). *telnet* sirve para establecer conexion TCP entre localhost y *mail server*.
 
En comparación, HTTP es un *pull protocol*, alguien sube data a la web para que varios *pulleen* del server cuando quieran. Por el contrario, SMTP es mas bién *push protocol*, donde el que envia el mensaje lo *pushea* al *mail server* del receptor. Otra es que SMTP restringe a ASCIIs de 7 bits, HTTP no. HTTP encapsula cada objeto en su mensaje de respuesta, SMTP envia todos en un mensaje.

En el header de SMTP van a aparecer: FROM, TO, SUBJECT. SMTP es un *push protocol*, entonces cómo obtiene el receptor sus mails del servidor? hay varios protocolos para esto: *Post Office Protocol version 3(POP3)*, *Internet Mail Acces Protocol (IMAP)* y HTTP:

* POP3: una vez establecida la conexion TCP tiene 3 fases. En *authorization*, envia contraseña y usuario (user <uuario> pass <contraseña>). En *transaction*, recupera el mensaje y otros comandos (list, retr, dele, quit). En *update*, termina la sesión POP3 y el servidor elimina los mails marcados para este fin. Posibles respuestas del servidor a todos los comandos: OK, ERR. POP3 no guarda información entre sesiones.
* IMAP: POP3 no permite al usuario crear carpetas remotas y asignarle mensajes. IMAP asocia cada mensaje con una carpeta (INBOX cuando llega el mensaje, luego puede moverse a otra). IMAP mantiene informacion del usaurio entre sesiones. También permite obtener porciones de mensajes (solo el header por ej).
* HTTP: Hotmail, donde el *user agent* es un web browser. Se usa para enviar y recibir a los servidores un mensaje HTTP.
 
## DNS: Directory Service
 
Para identificar un *host* se usan *hostnames*, pero estos nombres no permiten conocer su locacion en el internet. Entonces se los identifica con las direcciones IP (4 bytes), separados por "." donde cada byte en decimal va de 0 a 255. Es jerárquica. El DNS traduce de *hostname* a IP. DNS es una base de datos distribuida implementada en una jerarquoia de servidores DNS y un protocolo de la capa de aplicacion que permite a los *hosts* realizar consultas a la base de datos. DNS corre sobre UDP.DNS es usada por otro protocolos como HTTP y SMTP. La maquina del usuario hace de cliente. Luego de obtener la IP, el browser inicia la conexion TCP. DNS agrega delay.
Servicios que provee DNS:
 
* *Host aliasing*: mas de un nombre o alias. El mas completo es el canonico
* *mail server aliasing*: por ej yahoo.com
* *load distribution*: permite asociar varias IPs a un nombre canónico para distribuir la carga en varios servidores que repliquen lo mismo

No conviene un servidor DNS centralizado:
 * Falla y se cae todo
 * Volumen de tráfico
 * Distancia al servidor centralizado
 * Mantenimiento, actualizando constantemente para un host nuevo
 
Entonces se usa una base de datos descentralizada y jerárquica:
 * servidores DNS raiz: dan IP de los TLD DNS servers
 * *top-level domain (TLD) DNS servers*: devuelven IP de los *authorative DNS servers*
 * *authoritative DNS servers*: mapea el nombre de los hosts a su IP.
 
![image](https://user-images.githubusercontent.com/71232328/160653358-023c279d-bd3f-4376-8e43-265c05137b90.png)

 El cliente contacta a un servidor raiz, que devuelve direcciones IP para serividores TLD con cierto dominio (com). El cliente luego contacta uno de estos, que devuelve direccion IP de un servidor *authorative* para cierta direccion (amazon.com). finalmente el cliente contacta un servidor *authorative* de la pagina (amazon.com) que devuelve la IP del host requerido (www. amazon. com). 
 
 Además, cada ISP tien un servidor DNS local. Actúa como un proxy y forwardea la consulta a un servidor raiz.
 
 ![image](https://user-images.githubusercontent.com/71232328/160654734-f7f1413a-8d7a-4f8e-bed7-735d4c79a665.png)

 Las *querys* son recursivas e iterativas. Recursivas por piden que se obtenga el mapeo en su nombre, iterativas porque responden inmediatamente. *querys* de DNS pueden ser recursivas o iterativas.
 
 ![image](https://user-images.githubusercontent.com/71232328/160655196-18c555d5-a09d-4e82-8355-98b000ddccc0.png)

 
 #### DNS Caching
 
 Para mejorar el delay del sistema DNS y disminuir los mensajes DNS. Se *cachea* el par *hostname*/IP. Esta tarea la realiza el servidor local DNS
 
 #### Mensjaes DNS
 
 Los servidores DNS almacenan *resource records (RRs)*. Cada respuesta DNS lleva uno o mas de estos: (Name, Value, Type, TTL).
 
 * TTL: *time to live*, cuando borrarlo de la cache.
 * Tipo: si es A, name es hostname y value es IP. Si es NS, name es domain y value es hostname de *authorative DNS server*. Si es CNAME, value es el *hostname* canonico y name el alias. Si es MX, vale es nombre canonico del servidor de mail con alias en name
 
 Formato del mensaje:
 
 ![image](https://user-images.githubusercontent.com/71232328/160656495-d382134f-d730-4af3-bb31-9714f60c48a8.png)

 * Primeros 12 bytes son el header
 * Question: información acerca de la *query* realizada. name, type.
 * Answer: contiene RRs. Cada uno con Type, value y TTL
 * Authority Section: tiene RRs de *authorative servers*
 * Additional section: otros RRs que sirven de ayuda
 
 #### Poner RRs en una base de datos
 
 Se registra el dominio en una empresa *registrar* que lo pone en la base de datos DNS. Se registran en los TLD un tipo NS y otra A. Suponiendo se pasan 2 hostnames y dos IPs. También podria ser MX para un mail.
 
 ## Peer-to-Peer File Distribution
 
 
 ![image](https://user-images.githubusercontent.com/71232328/160658320-70011a61-7c83-45cd-8deb-a4f5fca36604.png)
 
 Cada *peer* puede redistribuir una parte de un archivo grande. El tiempo de distribuicion es el tiempo que le lleva al archivo llegar a todos. En una cliente servidor va a ser el que le lleve al cliente con la menor tasa de descarga o lo que le lleve al servidor si tiene menor tasa de envio. Sube linealmente con la cantidad de clientes. En P2P, es mas complicado de calcular. Primero el servidor debe enviar aunque sea 1 vez todos los bits del archivo. La tasa de subida es la del servidor mas la de los peers

 ![image](https://user-images.githubusercontent.com/71232328/160659048-1ec3206f-f611-43bf-80c5-f773ce7d8b6c.png)

 #### BitTorrent
 
 Todos los *peers* participando de la distribucion de un archivo son el *torrent*. El tamaño estandar de las porciones a distribuir es 256kb. Una vez que un *peer* obtiene todo el archivo puede irse o quedarse en el torrent ayudando a la subida del archivo
 
 ![image](https://user-images.githubusercontent.com/71232328/160659398-eb886069-994b-4a1b-a4b7-151d62fc72b6.png)
Cada torrent tiene un nodo llamado *tracker*. Cuando un *peer* se suma al *torrent*, se registra con el *tracker*, informando periodicamente si sigue en el torrent o no. Al sumarse a un torrent, se le envian los IPs de los *peers* (no todos) al recien llegado. Se intentan generar conexiones TCP con todos. De estos *peers* es de quien se obtienen las porciones del archivo. Primero va a pedir de los que no tiene, los que menos se repitan entre los vecinos (*rarest first*). Para enviar porciones de archivo, se prioriza a los que esten suministrando data a la tasa más alta. Se elige a los 4 *peers* (*Unchoked*) que mas rapido esten suministrando data y se les envia. Esto se calcula cada 10 segundos. Además cada 30 segundos se elige un *peer* al azar (*optmistically unchoked*).
 
 Otra aplicacion de P2P es *Distributed Hash Table (DHT)*. Es una base de datos distribuida entre los *peers*
 
 ## Streaming de video y distribucion de contenido
 
 Cuanto más alto el bitrate, mejor la calidad del video. 4K precisa aprox 10Mbps. Se crean varias compresiones y se envian a distintas tasas. El usuario elige cual ver en base a su ancho de banda.
 
 En HTTP streaming el video se guarda en un servidor HTTP. En el lado del cliente, una vez que se pasa un umbral en el buffer de recepcion se empieza a reproducir el video. La contra es que todos los clientes reciben los mismo auqnue tengan distinto ancho de banda. Surge el *Dynamic Adaptive Streamig over HTTP (DASH)*, el video se *encodea* en distintas versiones cada una con un bitrate distinto (distinta calidad. El cliente solicita porciones del video dinamicamente (cuando el ancho de banda es alto solicita mejor calidad y viceversa). Cada version del video se guarda en el server HTTP con una URL distinta. En el server HTTP hay un *manifest file* con las URL a estas versiones.
 
 #### Content Distribution Network (CDN)
 
 Casi todas las plataformas de streaming usan CDN. Servidores repartidos geograficamente que almacenan copias multimedia. CDN puede ser privado (Google) o *third-party*.
 Politicas de ubicacion:
 * *Enter Deep*: colocar servidores en access ISPs. Se está mas cerca de los *end systems*. Muy distribuido, mas dificil de mantener.
 * *Bring Home*: servidores en menos lugares (por ej IXPs). Mas fácil de mantener a expensas de un mayor delay
 
 Cuando se hace una request de un video, CDN la intercepta y determina el servidor CDN más conveniente y redirecciona la request. La intersepcion se logra haciendo uso de la DNS. 
 
 ![image](https://user-images.githubusercontent.com/71232328/160663016-832a77c1-3f8f-4cd8-8cce-34fc2fed32a7.png)
 
 Como determinar el cluster de CDN más conveniente? *cluster selection strategy*:
 
 * Más cercano geograficamente
 * *real time measurements*: toman medidas del delay para determinar el más cercano en cuanto a tiempo y no distancia

 También es posible el caso de P2P streaming, muy similar a lo comentado en la seccion de P2P
 
 ## Socket Programming
 
 2 tipos de aplicaciones de red: una opera bajo un especifico protocolo estandar (RFC) y otro que no, donde el porotocolo de la capa de aplicacion es determinado por el equipo de desarrollo. Debe definirse si usar TCP o UDP.
 
 
 En UDP, el paquete tiene direccion de destino (IP). Tambien se debe indiar el puerto para identificar al proceso en el host de destino.
 
 ![image](https://user-images.githubusercontent.com/71232328/160672250-bfa8c588-2b0e-46c9-be6c-68705ab7af78.png)

### Aplicacion UDP
 
Del lado del cliente
 
```python
# traigo el modulo socket
from socket import * 
 
# defino nombre de host (IP o hostname) y puerto 
serverName = ’hostname’
serverPort = 12000
 
# Crea socket
# AF_INET : IPv4, SOCK_DGRAM: UDP
clientSocket = socket(AF_INET, SOCK_DGRAM)
 
# Mensaje a enviar, capturo lo que tipee el usuario
message = raw_input(’Input lowercase sentence:’)
 
# Envio el mensaje, previamente transformandolo de string a byte
clientSocket.sendto(message.encode(),(serverName, serverPort))
 
# Recibo respuesta del servidor
modifiedMessage, serverAddress = clientSocket.recvfrom(2048)

print(modifiedMessage.decode())
 
# Cierro el socket
clientSocket.close()
 
```
 
Del lado del Servidor

```python
 
from socket import *

serverPort = 12000

serverSocket = socket(AF_INET, SOCK_DGRAM)

# Asigna el puerto al socket
serverSocket.bind((’’, serverPort))
 
print(”The server is ready to receive”)
while True:
 # Recibo del  cliente
 message, clientAddress = serverSocket.recvfrom(2048)
 # Convierte mensaje a string, pasa a uppercase
 modifiedMessage = message.decode().upper()
 # Envia el string encodeandolo previamente
 serverSocket.sendto(modifiedMessage.encode(), clientAddress)

```
 
### Aplicacion TCP
 
A diferencia de UDP, una vez establecida la conexion, no hace falta aclarar la direccion IP de destino en cada paquete.
 
 ![image](https://user-images.githubusercontent.com/71232328/160673843-36d457db-5f88-4bb7-9399-0b66e88f0e80.png)

Lado del cliente


```python

 from socket import *
serverName = ’servername’
serverPort = 12000

# SOCK_STREAM: TCP
clientSocket = socket(AF_INET, SOCK_STREAM)

# Establece conexion TCP. El handshake ocurre aca
clientSocket.connect((serverName, serverPort))
sentence = raw_input(’Input lowercase sentence:’)

# Notar no se aclara la dirección IP destino
clientSocket.send(sentence.encode())
modifiedSentence = clientSocket.recv(1024)
print(’From Server: ’, modifiedSentence.decode())

# Genera un mensaje TCP al TCP en el servidor
clientSocket.close()


```

![image](https://user-images.githubusercontent.com/71232328/160674039-75f416c6-83ae-47bb-a07b-f5cad85da805.png)


Del lado del servidor


```python

from socket import *
serverPort = 12000
serverSocket = socket(AF_INET, SOCK_STREAM)

# Es el socket de bienvenida
serverSocket.bind((’’, serverPort))

# Esperamos a que un socket cliente "toque la puerta".
 
serverSocket.listen(1)
print(’The server is ready to receive’)
while True:
 
 # Cuando un cliente "toca la puerta" se invoca accept(), que crea un nuevo
 # socket en el servidor dedicado a ese cliente en particular
 connectionSocket, addr = serverSocket.accept()
 sentence = connectionSocket.recv(1024).decode()
 capitalizedSentence = sentence.upper()
 connectionSocket.send(capitalizedSentence.encode())
 
 # Cerramos el socket dedicado al cliente, pero el de bienvenida
 # sigue abierto, por lo que pueden conectarse nuevos clientes
 connectionSocket.close()

```

 
</details>

<details>
 
 <summary> <h3>Capitulo 3 capa de transporte</h3> 🍾 </summary> </br>
 
Capa de transporte reside entre la de aplicación y la de red. Se encarga de proveer servicios de comunicacion a los procesos de aplicación corriendo en diferentes *hosts*.

En su relacion con la capa de red, se encarga de la comunicacion entre dos procesos de la capa de aplicacion corriendo en dos *end systems* distintos.

## Introducción y servicios de la capa de transporte

La capa de transporte provee **comunicacion lógica** entre dos procesos corriendo en dos *hosts*. Lógica porque hace parecer que los procesos estuvieran directamente conectados. Los procesos usan esta comunicacion lógica para enviarse mensajes abstrayendose de la infraestructura física. Los protocolos de la capa de transporte no se implementan en routers, sí en los *end systems*. Previo a mandar el mensaje, lo convierte en **segmentos**. Le pasa el segmento a la capa de red, donde se lo encapsula en un **datagram** y se lo envia. Los routers actúan sobre el datagram (capa de red). Al llegar, la capa de red extrae el datagram y le pasa el segmento a la capa de transporte que lo procesa y pone a disposicion de la aplicacion.

![image](https://user-images.githubusercontent.com/71232328/161090147-dbfe765a-6197-4dce-b937-8b731d91f789.png)

### Relacion capa de transporte y de red 

Los protocolos de transporte mueven mensajes de la capa de aplicacion a la de red, dentro del *end system*, pero desconocen como se moverá dentro de la red.
Un protocolo de transporte podría ofrecer *reliable data transfer* a una aplicacion, a pesar de que el protocolo de red por debajo no lo haga. De la misma manera podría encriptar el mensaje. No ocurre esto con el ancho de banda, donde el protocolo de transporte se ve atado a lo que ocurra en la capa de red.

### Capa de transporte en el Internet

Dos protocolos en la capa de transporte: UDP (*User Datagram Protocol*) y TCP (*Transmission Control Protocol*). El primero es *unreliable* y *connectionless*. El segundo lo contrario, *reliable* y *connection-oriented*.

**Paquete de la capa de transporte = segmento** (en el caso de UDP a veces puede ser datagram, ojo que también se usa para la capa de red).

El protocolo de la capa de red de internet es IP (*Internet Protocol*), provee comunicación logica entre *hosts*. El servicio es del *mejor esfuerzo* (no garantiza, entonces *unreliable*). Cada *host* tiene una **dirección IP**.
UDP y TCP extienden el servicio de comunicacion del IP entre dos *end systems* a dos procesos. Esto se denomina **transport-layer multiplexing** y **demultiplexin**. Además proveen chequeos de integridad/errores en segmentos (estos son los únicos servicios que provee UDP). TCP provee además **reliable data transfer**, **congestion control**.

## Multiplexing y demultiplexing

Esto es extender el servicio de entrega *host-to-host* provisto por la capa de red a *process-to-process*.

En el destino, la capa de transporte recibe segmentos de la capa de red. Luego se encarga de enviarselos al proceso de aplicación correcto en el *host*. Un proceso puede tener uno o m+as **sockets**. La capa de transporte lleva la data al *socket*. La capa de transporte examina unos campos en el segmento para determinar el socket que los debe recibir y los direcciona, esto es llamado **demultiplexing**. El trabajo de tomar información de los sockets en el *host*, encapsularlos con *headers* y pasar los segmentos a la capa de red es **multiplexing**.

![image](https://user-images.githubusercontent.com/71232328/161094339-ef766436-0a18-43b1-8fcd-05fd9bf3b6e6.png)

Para el **multiplexing** se requiere:
* Sockets tengan id
* Segmentos tengan campos que permitan identificar sockets: **puerto de origen**, **puerto de destino** de 16 bits cada uno. Los puerto de 0 a 1023 son llamados **well-known** y están restringidos para uso de HTTP (puerto 80) y FTP (puerto 21).

![image](https://user-images.githubusercontent.com/71232328/161095780-f0c3458a-16b4-4443-bd7d-d3796d16d062.png)

Con estos datos, queda claro como funciona el **demultiplexing** también, lee campo de puerto de destino y envia el segmento al socket destino.



### Connectionless Multiplexing and Demultiplexing (UDP)

Al crear un socket, la capa de transporte le asigna un numero de puerto. Con *bind*, se puede asociar un puerto especifico al socket. Del lado del servidor se define este puerto, del lado del cliente en general se deja que lo asigne la capa  de transporte. Se incluye tanto el destino como origen para permitir la comunicacion tanto cliente-a-servidor como servidor-a-cliente. Socket UDP queda definido por una tupla conteniendo IP de destino y puerto de destino. Dos segmentos con distinta fuente pero igual destino, van al mismo socket.

![image](https://user-images.githubusercontent.com/71232328/161099040-9baf2991-398e-49f5-a265-b9495e70d233.png)

### Connection-Oriented Multiplexing and Demultiplexing (TCP)

Un socket TCP queda definido por una cuatro-tupla: IP fuente, puerto fuente, IP destino, puerto destino. Dos segmentos con distinta fuente o puerto irán a sockets distintos. EL servidor debe poder soportar múltiples conexiones TCP en simultáneo. Se usan los 4 campos para el **demultiplex**

![image](https://user-images.githubusercontent.com/71232328/161098966-de01e1ae-2fba-4ddf-a563-0aa0c34dd255.png)

### Servidores Web y TCP

Cuando se corre un servidor en un puerto, todos los segmentos que lleguen tendrán el mismo puerto de destino. Los diferencia por la dirección IP. Actualmente los servidores tienen un proceso que lanza hilos por cada conexion.

## Connectionless Transport: UDP

Al elegir UDP, la aplicación prácticamente se está comunicando directamente con IP. UDP toma los mensajes de la aplicacion, les agrega puerto fuente y destino, otros dos campos y lo pasa a la capa de red. En destino, UDP usa el puerto destino para enviarlo al proceso de aplicación. No hay *handshake*, por eso *connectionless*. DNS usa UDP.

Por qué usar UDP y no TCP?

* Más control desde el nivel de aplicación acerca de que data se envía y cuando: esto porque UDP encapsula la data en un segmento y la pasa inmediatamente. TCP tiene control de congestion, reenvia segmento hasta que el receptor confirme que llegó
* No se establece conexión: no tiene delay en esta etapa, TCP tiene por el *three-way-handshake*. Es por esto que DNS corre en UDP, sino sería más lento. QUIC es un protocolo que usa UDP y le agrega *reliability* en un protocolo de la capa de aplicacion
* No mantiene un estado de conexion: TCP lo hace, lo que incluye buffers en ambos *end systems* además de parametros de control de congestion y parámetros para confirmar recepcion. UDP no hace nada, destinando menos recursos.
* El header es chico: en UDP son 8 bytes de overhead, en TCP 20 bytes.

Para tener *realible data transfer* con UDP, hay que construirlo sobre la aplicación.

### estructura del segmendto UDP

El header tiene 4 campos, cada uno de 2 bytes: los puertos, un largo (header + data) y *checksum*, usado por el *host* que recibe para ver si hubo errores en el segmento.

### Cheksum de UDP

Para detección de errores, para ver si los bits se vieron alterados por ruido por ejemplo. Esto lo hace haciendo el complemento  de la suma de los todos los *1* en todas las palabras de 16 bits. Al recibir, el *host* suma todas las palabras al cheksum, si no hubo errores el resultado será todos *1*, si aparece un *0*, hubo errores introducidos en el paquete. Este sistema es un ejemplo del principio **end-end**. OJO! UDP detecta el error, pero no hace nada para recuperar la información corrompida.

## Principios de *Realible Data Transfer*

Esto quiere decir que ningún bit será corrompido o perdido, además serán enviados en el orden correcto. Esto es responsabilidad del protocolo de *reliable data transfer*. Esto es dificil porque la capa por debajo del protocolo puede no ser *realiable*.

<p float="left" align="middle">
  <img src="https://user-images.githubusercontent.com/71232328/161105952-7214bdff-3947-4e38-beae-4e64a60511a2.png" width="340" />
  <img src="https://user-images.githubusercontent.com/71232328/161106055-34ea2161-95cd-4ea7-88ce-47345d0ddef8.png" width="340" /> 
</p>
</br>

Asumimos que los paquetes llegarán en el orden enviado, pero podrán perderse. Consideramos la transferencia en un solo sentido (**unidireccional**). 

### Construyendo un protocolo de transferencia de datos confiable

#### Reliable Data Transfer sobre un canal confiable

**FSM = Finite State Machine**

Se acepta data desde la capa de arriba (*rdt_send(data)*), se crea un paquete y se envia al canal (*udt_send(packet)*).

Del lado que recibe, *rdt* recibe un paquete del canal de abajo via *rdt_rcv(packet)*, saca la data del paquete y pasa la data a la capa de arriba.

![image](https://user-images.githubusercontent.com/71232328/161107383-3cde56f4-3897-451e-a530-df5566c950e2.png)

No hay diferencia entre una unidad de datos y un paquete. Como el canal es confiable, el receptor no debe dar ningún feedback al que envía. Además puede recibir data a la velocidad que envia la fuente.

#### Reliable Data Transfer sobre un canal con errores de bits

bits en un paquete pueden ser corrompidos. El que recibe usa un protocolo de mensajes: **positive acknowledgments (OK)** y **negative acknowledgments (Please repeat that)**. Estos protocolos se conocen como **ARQ (Automatic Repeat reQuest)**. Para manejar errores en bits, se precisan 3 capacidades más:
* Deteccion de errores: cheksum por ejemplo.
* Feedback del receptor: positive (ACK) y negative (NAK)
* Retransmisión: el que envía puede retransmitir paquete que llegó con error.

![image](https://user-images.githubusercontent.com/71232328/161108572-6cdd9a97-adf9-47cc-9449-f75b8e2e3967.png)

Se explica bastante sola la imagen. El que envia espera el **acknowledgment** y en base a eso reenvia o espera otro paquete para enviar de la capa superior. El que recibe si está corrupto envia un NAK, si esta todo OK, extrae la data y envía un ACK. qué pasa si el paquete ACK o NAK es corrupto!? Hay que agregarle cheksums. El que envia no tiene manera de saber si los recibió bien o mal.
Se podrían agregar bits de cheksum para recuperar los perdido. Otra es que el que envia, reeenvie el paquete si recibe un NAK o ACK corrupto, pero esto genera **duplicate packets**, donde el que recibe no sabe si el NAK o ACK que envió llegó bien.
Entonces se agregar un **sequence number** al packet, permitiendo que el receptor pueda determinar si es una retransmision.
Del lado del que envía, la **FSM** queda así: </br>
![image](https://user-images.githubusercontent.com/71232328/161118965-e4d3fde6-bdda-4a19-b37c-598097cd8f4d.png)
</br>
Del lado del receptor:
</br>
![image](https://user-images.githubusercontent.com/71232328/161119114-e87ceaa6-b008-4274-b5b9-294f21023da6.png)
</br>

#### Reliable Data Transfer sobre un canal con errores de bits y pérdida de paquetes

Con lo visto hasta ahora, es posbile recuperar el paquete perdido, pero cómo se detecta? El que envía no recibe respuesta. Puede esperar un determinado tiempo hasta retransmitir, pero cuánto? mínimo RTT más el tiempo de procesamiento. Debe elegirse un tiempo cuidadosemente, aunque no garantice que se haya perdido el paquete. Puede ser que se tarde mucho en responder y termine en **duplicate data packets**. Desde el lado del que envia, solo tiene que retransmitir basado en un **countdown timer**. Lo debe iniciar cada vez que envía un paquete, saber responder a una interrupcion del timer y poder frenar el timer.

El **FSM** del que envía:

![image](https://user-images.githubusercontent.com/71232328/161119250-2999969c-3690-4fd6-9808-902bbe4cef13.png)

Como los números de secuencia de los paquetes cambian entre *0* y *1*, a este protocolo se lo llama **alternatig-bit protocol**. Este protocolo no parece que vaya a tener una buena performance.



<p float="left" align="middle">
  <img src="https://user-images.githubusercontent.com/71232328/161119978-3cc0b1a3-a14e-4851-8ba1-d805fea529b1.png" width="250" />
  <img src="https://user-images.githubusercontent.com/71232328/161120034-8b41992b-3ec2-4aa4-b8d3-3c08f05fb48b.png" width="250" /> 
</p>

</br>

<p float="left" align="middle">
  <img src="https://user-images.githubusercontent.com/71232328/161120062-eb1f3d83-70de-4f82-a4d7-454189c26106.png" width="250" />
  <img src="https://user-images.githubusercontent.com/71232328/161120104-4b52986e-9160-4f08-88e1-cda479f9e007.png" width="300" /> 
</p>



### Pipelined Reliable Data Transfer Protocols

La performance del protocolo anteriror será mala porque es un protocolo de tipo *stop-and-wait*.


<p float="left" align="middle">
  <img src="https://user-images.githubusercontent.com/71232328/161120137-dd9c2d28-f126-462c-9883-48638710bea8.png" width="250" />
  <img src="https://user-images.githubusercontent.com/71232328/161120156-24696756-b896-49f3-a8fb-d176511db438.png" width="250" /> 
</p>


</br>

Para solucionar el problema de performance que acarrea el *stop-and-wait*, el que envía lo hace con multiples paquetes sin esperar **acknowledgments**. Esta tecnología se llama **pipelining**. 

<p float="left" align="middle">
  <img src="https://user-images.githubusercontent.com/71232328/161120747-ebacdba8-354c-4c72-b6e0-57d911466732.png" width="450" />
  <img src="https://user-images.githubusercontent.com/71232328/161120769-da36cb3c-cda2-47e5-8396-f2092e865ef6.png" width="450" /> 
</p>

Este método trae las siguiente consecuencias:
* se debe incrementar el rango del número de secuencia dado que cada paquete en tránsito debe tener un único número
* Ambos lados de la comunicación deben tener buffers para más de un paquete. Del lado del que envía, para los que fueron transmitidos pero aguardan respuesta. Buffer para paquetes recibidos correctametne del lado opuesto.
* Las modificaciones de los items previos van a ser determinadas por las formas en que responda el protocolo a paquetes perdidos, corrompidos, y con delay. Existen dos formas: **Go-Back-N** y **Selective-Repeat**

### Go-Back-N (GBN)

El que envía tiene un máximo de paquetes que puede tener sin respuesta.

Numeros de secuencia :

* [0, base-1]: paquetes que fueron enviados y respondidos
* [base, nextseqnum-1]: paquetes enviados sin respuesta
* [nextseqnum, base+N-1]: paquetes que pueden ser enviados inmediatamente si es requerido de la capa superior
* [base+N, inf]: no ueden ser usador hasta que otros paquetes que por el momento no haya sido respondidos (**unacknowledged**) sean respondidos (**acknowledged**).

![image](https://user-images.githubusercontent.com/71232328/161122569-c8235816-3050-4a62-b23b-bd3a902a0fd8.png)

N: **window size**.
GBN: **sliding-window protocol**
El rango depende del largo del campo. Si es *k*, entonces será [0, 2k-1]

![image](https://user-images.githubusercontent.com/71232328/161122963-a3cd3fbc-6e07-49e4-b6b4-9adb6b4bd6cb.png)
![image](https://user-images.githubusercontent.com/71232328/161122991-e76cd10a-2115-496e-94fa-0529afde4b06.png)

A la FSM se le agregaron variables para *base* y *nextseqnum*. El GBN *sender* debe responder a 3 tipos de eventos:

* Invocación desde arriba (rdt_send): chequea si la ventana está llena. Si no lo está, crea el paquete y actualiza variables. Si está llena, devuelve la data a la capa de arriba, que tendrá que intentar de nuevo
* Receipt of an ACK: al recibir una respuesta de un paquete con numero de secuencia *n*, se asume que los paquetes con número hasta *n* habrán sido correctamente recibidos (**cumulative acknowledgement**)
* Timeout event: se usa timer para detectar paquetes perdidos, pero en este caso reenvia todos los paquetes que no hayan sido respondidos.

Los paquetes recibidos fuera de orden se descartan. El que recibe solo debe mantener es el número de secuencia siguiente al actual: *expectedseqnum*. Si no recibe un paquete con ese número, lo descarta. GBN es programación orientada a eventos.

![image](https://user-images.githubusercontent.com/71232328/161124226-4b6d5c58-202c-499f-8551-93593b0e74f0.png)

### Selective Repeat (SR)

GBN permite llenar el *pipeline* con paquetes. Si el delay del ancho de banda es grande y la ventana también, un error en un paquete podria causar que GBN retransmita mucho paquete innecesariamente. Protocolos **SR** evitan esto, haciendo que el que envía, retransmita solo los paquetes de los que tiene sospecha. Esta retransmision va a qrequerir que el receptor responda individualmente a paquetes. A diferencia de GBN, en la ventana de SR habrá paquetes ya informados como recibidos correctamente por el receptor.
El receptor va a guarda los paquetes fuera de ordenen un buffer hasta que paquetes perdidos (con un número de secuencia menor) lleguen. Una vez ocurrido esto, enviará el conjunto de paquetes a la capa de arriba.

![image](https://user-images.githubusercontent.com/71232328/161125373-72cf2a12-4d84-46cf-956b-8e97c4b03383.png)

Eventos del SR que envía:

* Recibe data de arriba: chequea el próximo número de secuencia. Si está en la ventana, arma el paquete y envía. Sino igual que GBN
* Timeout: cada paquete tendrá su propio timer lógico (se puede simular con un timer de hardware)
* recibe ACK: marca el paquete como recibido. Si el número de secuencia es igual a *send_base*, mueve la ventana. Si al moverse la ventana, caen paquetes que no fueron transmitidos, se transmiten

Eventos del SR que recibe:

* Paquete con nro de secuencia [rcv_base, rcv_base+N-1] es correctamente recibido: el paquete está en la ventana, se envía entonces un ACK. Si no había sido recibido previamente, se lo pone en un buffer. Si el numero de secuencia es igual a la base, el paquete y cualquiera previo en el buffer se envía a la capa superiro, actualizando la ventana
* Paquete con nro de secuencia [rcv_base-N, rcv_base-1] es correctamente recibido: se genera un ACK, a pesar de que fue recibido previamente
* Otro rango: se ignora el paquete

![image](https://user-images.githubusercontent.com/71232328/161126483-b0683f71-2657-4545-a158-2d28e40ca315.png)

Las ventanas del que envía y del que recibe no siempre estarán igual. Trae consecuencias. El ancho de la ventana debe ser menor o igual al rango de los número de secuencia.

![image](https://user-images.githubusercontent.com/71232328/161127162-078d3525-59c0-4162-8074-1047c1bc923f.png)

![image](https://user-images.githubusercontent.com/71232328/161127225-f56add79-fec7-4d7e-9846-9a9696d7331d.png)

Cuando el canal que une al que envia y al que recibe es una red, puede ocurrir el reordenamiento de los paquetes.

Términos a reconocer:

* Mechanism:
* Checksum: detectar errores de bits en paquete.
* Timer: para retransmitir paquete.
* Sequence Number: para numeración secuencial de paquetes fluyendo.
* Acknowledgment: usado por el receptor para informar al que envía que un o varios paquetes fueron recibidos correctamente.
* Negative Acknowledgment: usando por el receptor para informar al que envía que un paquete no fue recibido correctamente.
* Window, pipelining: el que envía, solo puede hacerlo con paquetes que su número de secuencia cae en un range (window). Se puede mejorar la performance permitiendo a varios paquetes ser transmitidos pero sin ser *Acknowledged* (pipelining).

## Transporte orientado a Conección: TCP

### Coneccion TCP

Es **connection-oriented** porque antes de que una aplicación empieze a enviar data a otra, los dos procesos hacen un **handshake**, iniciando varias variables de estado de TCP. La conexión es lógica, el protocolo TCP solo corre en los end-systems. Una conexión TCP provee **full-duplex service**: en una conexion entre A y B, la data de la capa de aplicación puede fluir del proceso A al B al mismo tiempo que del B al A. La conexión también es **point-to-point**: entre un solo receptor y un solo enviador. No es posible el multicasting en TCP (uno envia a muchos).

Para iniciar la conexion, el proceso de aplicacion del cliente informa a la capa de transporte del cliente que quiere iniciar una conexion, indicando el puerto y nombre del server. El cliente envia un segmento TCP, el servidor responde con otro. Finalmente el cliente envia un tercero. Los dos primeros no tienen data  de la capa de aplicación, el tercero puede tener. Por esto se llama **three-way handshake**.
Del lado del cliente, al recibir la data el TCP, la direcciona al **send buffer**, creado durante el handshake. TCP agarra pedazos de ahi y los va pasando a la capa de red para que sean enviados. El maximo tamaño esta definido por el **maximum segment size (MSS)**, determinado por el largo del frame mas largo de la capa de linkeo que puede enviar el local host (**maximum transmission unit (MTU)**. TCP/IP header es 40 bytes aprox. Ethernet tiene un MTU de 1500 bytes, generalmente MSS es 1460 bytes. TCP le agrega un header a la data, formando un **TCP segment**. Al recibir un segmento, TCP los coloca en el buffer de recepcion.

![image](https://user-images.githubusercontent.com/71232328/161608736-ed4825bf-d5d3-4c2e-8b5a-af58ff5c7208.png)

### Estructura de segmento TCP

Tiene un header y un campo de datos. Este último tiene pedazos de datos de aplicación. MSS determina el maximo largo de este campo.
El header tiene número de puerto destino y origen, también tiene un cheksum. El header además tiene:
* campo de número de secuencia de 32 bits y campo de número de acknowledgment de 32 bits
* **receive window** de 16 bits para control de flujo.
* el campo del largo del header de 4 bits
* campo de opciones: para negociar MSS o escalar ventana entre end-systems.
* campo de flag de 6 bits. ACK bit indica que el campo de acknowledgment es válido (el segmento tiene un acknowledgment para un segmento que fue recibido correctamente). RST, SY y FIN para el setup y cierre de la coneccion. CWR y ECE para notificaciones de congestion. PSH indicaría que la data debe ser enviada a la capa de arriba inmediatamente. URG indicaría que la capa de aplicación marcó como urgente. La ubicación del ultimo byte la determina el **urgent data pointer field**.

![image](https://user-images.githubusercontent.com/71232328/161610084-5b9c5418-95c2-43ee-86db-ebea10a7d060.png)

#### Los numeros de secuencia y acknowledgment
Vitales en el servicio de TCP de *reliable data transfer*.

![image](https://user-images.githubusercontent.com/71232328/161611283-6c0619c1-0174-4502-b019-4bf4ec6b953e.png)

TCP ve a los datos como un strem de bytes ordenados. El número de secuencia de un segmento hace referencia al número de byte dentro del stream. En el caso de la imagen, los números de secuencia serían: 0, 1000, 2000, ..., 49900.
Ahora vemos los números de acknowledgement. Una conexion entre A y B, cada segmento que llega de B a A tiene un número de secuencia. El número de acknowledgement que pone A en el segmento es el número de secuencia del proximo byte que espera A de B. A recibe bytes numerados de 0 a 535 de B, en el segmento que A le envíe a B, en el campo de acknowledgement va a poner 536.
Si B envia de 900 a 1000, pero A todavia espera el 536, no va a responder el acknowledgement de ninguno hasta recibir el 536. Esto es **cumulative acknowledgement**. Si se reciben fuera de orden pueden descartarse o acumularse en un buffer hasta recibir los intermedios. Ambos lados del TCP definen un TCP inicial aleatoriamente.
#### Telnet

protocolo de la capa de aplicación usado para login remoto. Corre sobre TCP.

![image](https://user-images.githubusercontent.com/71232328/161613807-c46192e3-3f10-4453-b74a-75758df26680.png)

### Estimación del RTT y Timeout

TCP usa un mecanismo de timeout/retransmision para recuperar segmentos perdidos.

#### Estimar RTT

TCP toma una medida por vez. De esta manera, el RTT de muestra es tomada una vez cada RTT. Nunca se computa un RTT de muestra para un segmento retransmitido. TCP a su vez mantiene un promedio de RTT.

`RTT estimado = 0.875 * RTT estimado + 0.125 *RTT de muestra`
Este promedio es llamado **exponential wighted moving average (EWMA)**, dandole más peso a las muestras recientes.
También se guarda el desvio del RTT
`dev RTT= 0.75 * dev RTT + 0.25 * |RTT de muestra - RTT estimado|`

De esta manera el timeout para TCP será:

`Intervalo de timeout = RTT estimado + 4 * dev RTT`

Iniciando con un timeout de 1 segundo. Cuando ocurre un timeout, el valor se duplica para evitar otro subsecuente. Cuando un segmento es recibido nuevamente y actualizado el RTT estimado, el timeout es calculado nuevamente.

### Reliable Data transfer

El servicio de IP es unreliable. Los segmentos de la capa de transporte pueden sufrir esto. TCP crea un servicio confiable sobre IP. TCP usa un solo timer de retransmision. El timer se inicia al pasar el segmento a IP.
TCP responde a tres eventos principales:
* Recibe data de la aplicación de arriba: crea segmento TCP con el número de secuencia igual a nextseqnum (actualiza sumando los bytes), si el timer no está corriendo lo inicia, pasa el segmento a IP.
* timeout: retransmite el segmento que no haya sido acknowledged con el seqNum más chico
* recibe ACK: si es mayor a sendBase, sendBase = valor de ACK. Si hay segmentos no acknowledeged, inicia el timer.

Cada vez que TCP retransmite por un timeout, resetea el timer al doble del valor que tenia, asi sucesivamente hasta que recibe data de arriba o recibe un ACK y el timeInterval se calcula nuevamente. Este mecanismo sirve para control de congestion, retransmitiendo entre intervalos más largos de tiempo.

El que envía puede detectar la pérdidad de un paquete debido a **ACK iguales**: el que envia recibe un ACK de un segmento del cual ya habia recibido. 
Cuando el que recibe lo hace con un número de secuencia mayor al esperado, reenvía un ACK en referencia último byte en orden recibido correctamente (duplica ACK). Si se reciben 3 ACK iguales, el que envía hace una **fast retransmit**, retransmitiendo el segmento perdido antes de que el timer finalice.

![image](https://user-images.githubusercontent.com/71232328/161748672-33aed8c3-7afe-478a-9adb-7f471b98cc4c.png)

#### GBN o SR?
Los acknowledgements de TCP son acumulativos los segmentos recibidos correctamente pero fuera de orden no son individualmente ACKed. TCP solo debe mantener el número de secuencia más chico del byte transmitido pero no acknowledged y el número de secuencia del siguiente byte a enviar. Parece un GBN con algunas diferencias. Muchos TCP guardan en un buffer los segmentos recibidos fuera de orden. A diferencia de GBN que retransmitiría todos los paquetes desde el perdido en adelante, TCP a lo sumo enviará uno. **Selective acknowledgement** permite al TCP que recibe hacer acknowledge de segmentos fuera de orden selectivamente en vez de acumulativo. El mecanismo de recuperación de errores es un híbrido entre GBN y SR.

### Control de flujo

Los hosts de TCP colocan la data recibida en buffer del cual lee el proceso de aplicación. Si no lee rápido, puede haber un overflow. TCP provee un servicio de control de flujo para evitar esto. El duplicado del timer tenía que ver con un mecanismo de control de congestion. El control de flujo se hace haciendo que el que envia mantenga una variable **receive window**: le da una idea de qué tanto espacio le queda al que recibe en el buffer.
El tamaño del buffer es RCVBuffer. *LastByteRead* es el número del último byte leído por la aplicación del buffer. *LastByteRcvd* es el número del último byte que fue puesto en el buffer. *rwnd* es ventana, entonces `rwnd=RcvBuffer−[LastByteRcvd−LastByteRead]`, es dinámico. Un host le comunica al otro cuánto espacio le queda, colocando el valor de la variable en el campo de la ventana en cada segmento que envia.

![image](https://user-images.githubusercontent.com/71232328/161750983-4c70041d-8807-4297-9523-97c6cff33189.png)


Si la ventanta llega a cero, pero el que enviaba no tiene nada que enviar, entonces va a quedar bloqueado. TCP obliga al que envia a enviar constantemente segmentos con un byte de data cuando la ventana tiene valor cero. Estos segmentos son acknowledged por el que recibe y en algún momento se liberará la ventana

### Manejo de conexión

Para iniciar la conexion, el cliente TCP envía un segmento con el bit de SYN en 1 (**SYN segment**) y con un número de secuencia (*client_isn*) aleatorio en el campo. Al recibirlo, el servidor hace lugar para el buffer y las variables, además envía un segmento informando que la conexion fue garantizada. En este segmento, el bit SYN se pone en 1, en el campo de acknowledgement se coloca *client_isn + 1* y en el campo del número de secuencia coloca el del servidor (*server_isn*). Este segmento se conoce como **SYNACK segment**. Al recibirlo el cliente, envia otro segmento en respuesta (un ACK), poniendo en el campo de acknoledgement el valor *server_isn + 1*, seteando el bt SYN a cero

![image](https://user-images.githubusercontent.com/71232328/161753414-294594d0-926a-4edc-a919-f455a376a95e.png)

Al terminar una conexion, se liberan los recursos. El cliente envia un segmento especial al server, con el bit FIN en 1. El server responde con un ACK. Luego el server envia un segmento con FIN en 1. El cliente responde con un ACK y finaliza

![image](https://user-images.githubusercontent.com/71232328/161753724-3ce4f58c-0a56-452b-8505-39342312437b.png)


Durante la conexion, el TCP para por diferentes estados. Del lado del cliente:

![image](https://user-images.githubusercontent.com/71232328/161753828-f7b096a4-9541-42a7-a6b5-a8035d30be59.png)

Del lado del servidor:

![image](https://user-images.githubusercontent.com/71232328/161753960-54bb4689-a615-4ca8-8214-d4620b6733a3.png)

Si el servidor recibe un segmento con un número de puerto incorrecto, enviará un segmento especial de reseteo con la flag RST en 1. Entonces, si se envía un segmento SYN pueden pasar tres cosas:
* se recibe un SYNACK: ok
* se recibe un RST: no se está corriendo una aplicación en el puerto indicado
* no recibe nada: SYN fue bloqueado por firewall

## Principios de control de congestion

#### 2 senders, 1 router con buffer ilimitado

![image](https://user-images.githubusercontent.com/71232328/161760395-d0273e80-256b-462c-bda0-fc2ae7b8f8b3.png)

si se envia a una tasa entre 0 y la mitad de la capacidad del link, el throughput del que recbie es igual a la tasa de envia. Si se envia por encima de esa tasa, el throughput es la mitad de la capacidad del link. Este límite es consecuencia de compartir la capacidad del link entre dos conexiones. El problema es que a medida que la tasa de envio se acerca a la mitad de la capacidad del link, el delay crece hasta infinito. 
*Se observan delays por colas a medida que la tasa de arribo de los paquetes se acerca a la capacidad del link*

#### 2 senders, 1 router con buffer limitado

![image](https://user-images.githubusercontent.com/71232328/161761256-8ed8fe96-6318-4fad-bade-b00133ecf2dc.png)

Los paquetes que lleguen a un buffer lleno vana ser dropeados. Asumimos que en este caso si dropea, se retransmite automaticamente. La tasa a la que la tasa de transporte envia segmentos a la capa de red es llamada **offered load**. El ejemplo, del total de la tasa de envio, 1/3 es para retransmisiones.
*si hay congestion, el que envia debe realizar retransmisiones para compensar los paquetes perdidos por el overflow del buffer*.
Podria ocurrir que retransmita un paquete que no se perdió (timeout), en este caso el router usaría capacidad del link para enviar el mismo paquete por duplicado.
*retransmisiones innecesarias por el que envía debido a grandes delays puede causar que el router use capacidad del link para enviar paquetes innecesariamente*


#### 4 senders, routers con buffer limitado y caminos con multiples salts

![image](https://user-images.githubusercontent.com/71232328/161762772-59b7b2fa-21cb-4e88-bef9-a8c15dbdd37c.png)

Si un router que no es el primero dropea, el trabajo de los previos se desperdicia. Hubiese sido mejor que dropee el primero.

*cuando se dropea un paquete en el camino, la capacidad de transmision que fue usada en cada etapa para direccionar ese paquete, es desperdiciada*

### Approaches a control de congestion 

* **ent-to-end congestion control**: la capa de red no ofrece apoyo explicito a la de transporte para fines de control de congestion. La presencia de congestion puede ser inferida por los end-systems debido a la perdida de paquetes o delay. TCP toma este approach
* **network-assisted congestion control**: routers proveen feedback al que envia/recibe acerca el estado de congestion de la red.

En el caso de asistida por la red, la informacion llega al que envía de dos maneras: feedback directo, donde un router envia un paquete que indica que hay congestion o feedback indirecto, donde el router puede marcar un campo de un paquete destinado a tal fin. Al llegar al receptor, este informará al que envía de la notificación de congestion. Lleva un RTT


![image](https://user-images.githubusercontent.com/71232328/163653550-51c9974a-c41a-45af-b547-76fc0359fc11.png)

## Control de Congestión TCP

TCP usa control de congestion end-to-end. Apunta a limita la tasa de envío en la conexión. Si el que envía percibe que hay poca congestión, aumenta la tasa de envío. Si percibe lo contrario, la reduce. Cada conexion TCP tiene un buffer de recepcion, envío y variables. El control de congestion de TCP hace que el que envía tenga una **congestion window: cwnd**, que impone una restricción a la tasa de envío.


`LastByteSent−LastByteAcked≤min{cwnd, rwnd}`

Cuando hay excesiva confestión, uno o más buffers de routers se ven desbordados generando dropeos. Esto resulta ,en el que envía, en un timeout o tres ACKs iguales, lo que es tomado como un indicador de congestion. Se disminuye el tamaño de **cwnd**.
Si no hubiera congestion, el que envía tomaría los ACKs como indicadores de que puede aumentar la tasa de envío (aumentando el tamaño de la **cwnd**). Como usa ACKs (o timeouts) para determinar el tamaño, se dice que es **self clocking**.


Si mucho TCP envían a altas tasas, pueden saturar la red. Si envía atasas bajas, la desaprovechan. Para manejarse correctamente, siguen los siguientes principios:

* Un segmento perdido implica congestion, entonces se debe reducir la tasa de envío
* Un ACK de un segmento indica que se puede aumentar la tasa de envío
* La estrategia de TCP es testear el ancho de banda. Esto es incrementar la tasa de envío hasta que ocurra un timeout o tres ACKs iguales (es decir se pierda un paquete).

El **algoritmo de control de congestión de TCP** tiene tres componentes principales:

* **Arranque lento**: cuando empieza una conexion, cwnd se setea a 1 MSS (tasa de envio: MSS/RTT). Por cada ACK, la tasa se incrementa en 1 MSS. Como ocurre por cada paquete, resulta en que se duplica la tasa e envío cada RTT: crece exponencialmente.
![image](https://user-images.githubusercontent.com/71232328/163654105-80542184-00e2-40ed-893f-fef48a251c9a.png)
Si se pierde un paquete, **cwnd** se setea en 1 y vuelve a empezar. También setea otra variable **ssthresh** (slow start treshold) a cwnd/2. Cuando cwnd alcanza el valor de sstresh (la mitad del valor de la ventana la ultima vez que hubo congestion) entra en el modo de evitar congestion (incrementos con más cuidado). Tambien puede terminar cuando recibe 3 ACKs iguales, lo que lleva a una retransmision rapida y entrada en rapida recuperacion.
![image](https://user-images.githubusercontent.com/71232328/163654282-d5f28821-4688-4a06-991d-579df48cd854.png)


* **Evitar congestion**: el valor de cwnd es la mitad de su valor la última vez que hubo congestión. Entonces en vez de duplicar cwnd cada RTT, lo aumenta en 1 MSS cada RTT. El comportamiento se mantiene, actualizando ssthresh. Si se reciben tres ACKs iguales, TCP agrega 3 MSS a cwnd para contar los 3 ACKs y actualiza el valor de ssthresh a cuando llegaron los 3 ACKs. Se entra en recuperación rápida
* **Recuperación rápida**: el valor de cwnd se incrementa en 1 MSS por cada ACK duplicado recibido por el segmento que llevó a TCP a entrar en recuperación rápida. Cuando lelga un ACK por el segmento perdido, se entra en modo evitar congestión. si hay timeout, se pasa a arranque lento.

![image](https://user-images.githubusercontent.com/71232328/163654573-13a7bcb2-b11c-41b0-93e8-9cd920f260ba.png)

Queda claro viendo TCP Tahoe. El control de congestion de TCP es llamado **additive-increase, multiplicative-decrease (AIMD)**. *additive* porque se aumenta cwnd linealmente, y *multiplicative-decrease* cada vez que recibe tres ACKs iguales.

`average throughput of a connection = 1,22 * MSS * RTT * L` L: loss rate.

### Fairness

Si se tienen *K* conexiones TCP y todas pasan por un link con capacidad de conexión R. Se dice que un mecanismo de control de congestión es justo si la tasa de transmision promedio de cada conexión es R/K

![image](https://user-images.githubusercontent.com/71232328/163654761-b0f767b3-26a2-45a4-bb62-5e3d191f2506.png)

Si se tiene en cuenta la forma en que se maneja el mecanismo de control de congestión, donde se testea el ancho de banda hasta que se pierden paquetes, se puede esperar que el throughput oscile cercano a R/K. En el caso de 2 end-systems, sería como lo siguiente:

![image](https://user-images.githubusercontent.com/71232328/163654846-11fffb95-78b2-40ec-a10f-0683018aae14.png)

### Fairness y UDP

Desde el punto de vista de TCP, las conexiones UDP no están siendo justas

### Fairness y conexiones TCP paralelas

Si pudiera hacerse que UDP fuera justo, igualmente habría un problema: las conexiones en paralelo. Si hay 9 aplicaciones cliente-servidor cada una con una conexion TCP y llega una nueva, cada una recibe R/10. Pero si la nueva usa 11 conexiones TCP, se estaría llevando aprox R/2.

### Control de congestión asistido por la Red

**Explicit Congestion Notification (ECN)**: en la capa de red, 2 bits en el campo del Tipo de Servicio del header del datagram de IP se usan para ECN. Unseteo es usado por el routes para indicar congestion. Esto llega al host de destino, que le informa al que envía, seteando el bit ECE en el segmento ACK. El que envía, reacciona modificando la cwnd. Otro seteo posible es usado por el que envía para indicar a los routers que tanto el que envía como el que recibe pueden responder a seteos en ECN.

![image](https://user-images.githubusercontent.com/71232328/163655061-084bd94f-0184-4da8-abc3-9ee19e6b81c6.png)






</details>


<details>
 <summary> <h3>Capítulo 4 Capa de red: plano de datos </h3>🍾</summary>
 
 Capa de red puede dividirse en dos partes que interactuan: plano de datos y plano de control.
 
 ## Análisis de capa de red
 
 El principal rol del plano de datos es direccionar el datagram del link de entrada del router, al de salida. La tarea del plano de control, es coordinar estas acciones locales para que los datagrams sean transferidos ent-to-end a través de los routers
 
 ### *Forwarding* y *Routing*
 
 * **Forwarding**: Cuando llega un paquete al link de entrada de un router, este debe mover el paquete al link de salida apropiado. Implementado en el plano de datos. Accion local del router, implementada en hardware
 * **Routing**: debe determinarse el camino a tomar por lo paquetes, de tal manera que lleguen a destino. estos son llamados **Algoritmos de routeo**. Accion que abarca la totalidad de la red, implementada en software.
 
 Cada router tiene una **forwarding table**, un router forwardea un paquete indexando esta tabla con los campos del header del paquete. El valor indica el link de salida
 
 Cómo se configura esa tabla? El algoritmo de routeo determina el contenido de las tablas
 
 ![image](https://user-images.githubusercontent.com/71232328/163680879-e1b8bf37-cb21-483b-98b6-f2a6fd61b14c.png)
 
 Existen otras maneras de implementar la funcionalidad del plano de contro para determinar el contenido de las tablas de forwardeo. Este es el caso de un controlador remoto, separado fisicamente de los routers
 
 ![image](https://user-images.githubusercontent.com/71232328/163681005-d6f34feb-6105-452b-8764-0a101157dd1e.png)

Esta implementacion es el corazón del **software-defined networking (SDN)**. El controlador que interactúa con los routers está implementado en software.
 
 ### Modelo de servicio de la red
 
 El **network servide model** define características del envío end-to-end de paquetes entre los hosts. La capa de red podría ofrecer:
 
 * Garantizar envío
 * Garantizar envío con un delay límite
 * Los paquetes llegan en orden
 * Garantiza un ancho de banda mínimo
 * seguridad
 
 Sin embargo la capa de red solo ofrece uno: **servicio del mejor esfuerzo** o **best Effort**. Soo garantiza que va a hacer todo lo posible para que llegue el paquete a destino.
 
 ## Qué hay dentro de un router?
 
 En un router se pueden identificar 4 componentes:
 
 ![image](https://user-images.githubusercontent.com/71232328/163681318-4d890d45-c77c-4cd0-a860-c9e0ce99070d.png)

 * input ports o **puertos de entrada**: en la capa física, une link con router. Realiza también tareas de la capa de linkeo (cajitas blancas en foto). Tambíen se realiza una función de *lookup*, donde se determina el puerto de salida. Paquetes de control son direccionados del puerto de entrada al procesador de routeo
 * **Switching fabric**: conecta el puertos de entrada con los de salida
 * **puertos de salida/output ports**: almacena los paquetes recibidos del **switching fabric** y los transmite al link de salida realizando las funciones de capa de linkeo y capa física
 * **Procesador de routeo**: realiza tareas del plano de control (protocolos de routeo, mantener tablas, comunicarse con el controlador remoto para actualizar las tablas de forwarding)
 
 Los puertos de enrtada/salida y switching fabric son implemetnados en hardware, esto porque operan en los nanosegundos. Mientras que el plano de datos opera en los milisegundos (software).
 
 ### Procesamiento en puerto de entrada y forwarding basado en destino
 
 En la función de lookup se hace uso de la tabla de forwarding. La tabla es mantenida por el procesador de routeo o es recibida por un controlador SDN remoto. 
 
 ![image](https://user-images.githubusercontent.com/71232328/163681734-82eff5f7-2f96-402b-a714-488e69564a6e.png)
 
 
 En la tabla de forwarding puede alcanzar con matchear un prefijo para redireccionar el paquete al puerto de salida. Si matchea más de uno, se elige el que tiene el matcheo más largo. Todo esto se realiza en hardware. Una vez determinado el puerto de salida, el paquete se envía a la **switching fabric**. Si hay otros en la fabrica, el paquete se encola en el puerto de entrada. Otras acciones que se realizan en esta etapa son: verificar versión del paquete, checksum, tiempo de vida, admemás contadores usados en la red deben ser actualizados.
 Se dice que es **match plus action**, porque matchea un dirección IP y luego lo envía a la **switching fabric** al puerto de destion ("action").
 
 ### Switching
 
 Los paquetes son direccionados del puerto de entrada al de salida. se puede lograr de varias maneras:
 
 * **via memoria**: el switching lo hacía la CPU. Con los puertos siendo dispositivos de entrada y salida. Se copiaba el contenido del paquete (avisando con una interrupción en el BUS) a la memoria del procesador y se copiaba en el de salida. No se podía direccionar más de un paquete a la vez. Actualmente algunos lo hacen, pero actúan más como multiprocesadores con memoria compartida
 ![image](https://user-images.githubusercontent.com/71232328/163682062-9e7a60f4-37d2-408e-afe3-d5a6b643e9fc.png)
 
 * **via Bus** : un puerto de entrada transfiere el paquete directamente al puerto de salida sobre un bus compartido. Todos los puertos de salida reciben el paquete, pero solo el indicado por el puerto de entrada se lo queda. El label introducido por el puerto de entrada es retirado luego de llegar al puerto de salida. La velocidad de switcheo se ve limitada por la del bus
 
 ![image](https://user-images.githubusercontent.com/71232328/163682268-40205bd3-5075-4b95-b4df-73302ef9e35e.png)

* **via interconnection network**: para superar las restricciones del bus compartido. 2N buses que conectan N puertos de entrada con N puertos de salida. Un **switch crossbar** es no bloqueante, salvo que 2 paquetes provenientes de dos puertos de entrada distinto tengan como destino el mismo puerto de salida.
 
 ![image](https://user-images.githubusercontent.com/71232328/163682354-8aff3669-7d09-41cf-ae69-057ad10f0ed1.png)

 ### Procesamiento en puertos de salida
 
 Se transmiten los paquetes hacia los links de salida. Incluye seleccionar y desencolar los paquetes, ademas de realizar la transmision capa de linkeo y capa fisica.
 ![image](https://user-images.githubusercontent.com/71232328/163682487-8dfc52e6-ab93-4b81-a2bb-4fa4a24c5eb8.png)

 ### Donde ocurre el Queuing
 
 Es en los routers donde se dropean o pierden paquetes.
 
 ### Encolado en puertos de entrada
 
 Si el **switch fabric** no es lo suficientemente rápido para transferir los paquetes que llegan, estos comienzan a encolarse en los puertos de entrada. **head-of-the-line (HOL) blocking** se da cuando un paquete debe esperar a ser tranferido a través de la fabrica (auqneu el puerrto de salida esté libre), porque otro paquete en la cabeza de la fila está bloqueado. Esto puede llevar a pérdida de paquetes.
 
 ![image](https://user-images.githubusercontent.com/71232328/163682630-e57cd4a8-b4bf-449c-9429-b788aec967e9.png)

 
 ### Encolado en puertos de salida
 
 Si el **switching fabric** es considerablemente más rapido que las lineas de los puertos, pueden llegar más paquetes al puerto de los que puede tranmitir al link de salida, teniendo que encolarlos y pudiendo generar pérdida de paquetes. Cuando se supera la capacidad del buffer, se puede dropear (**drop-tail**) o remover ya encolados apra hacer lugar a los recien llegados. Acciones para control de congestion son llamadas **active queue management**, los algoritmos más usados son **random early detection (RED**.
 En los puertos de salida, un **packet scheduler** define que paquete se transmitirá. El tamaño del buffer puede ser RTT * la capacidad del link.
 
 ![image](https://user-images.githubusercontent.com/71232328/163682696-8dcdd9c1-e75b-4237-85ce-f349108c713b.png)

 ### Packet scheduling
 
 #### FIFO
 
 Selecciona los paquetes para ser transmitidos en el mismo orden en que llegaron
 
 ![image](https://user-images.githubusercontent.com/71232328/163682902-df3eaa24-4005-49fc-be71-24168e689062.png)
 
 ![image](https://user-images.githubusercontent.com/71232328/163682973-b35a3cc4-7128-4dcc-8ca6-98e421fe5a13.png)

 #### Priority Queuing
 
 se les asigna una prioridad a los paquetes cuando llegan. Por ejemplo, aquellos que llevan información acerca del manejo de la red tendrán mayor prioridad. Cada clase tendrá su cola. Se transmitirá el paquete de la cola con más alta prioridad
 
 ![image](https://user-images.githubusercontent.com/71232328/163683042-ccf53758-f276-457b-9ca0-833a98c4441b.png)

 Los paquetes claritos tienen menor prioridad que los azul oscuro
 
 ![image](https://user-images.githubusercontent.com/71232328/163683071-d7c01813-3f90-4c1e-bac4-0f6ad29e9834.png)

 **non-preemptive priority queuing** implica que una vez que se comienza a transmitir un paquete, no se interrumpe.
 
 #### RoundRobin y Weighted Fair Queuing (WFQ)
 
RR alterna el servicio entre las clases: por ejemplo clase 1,2,1,2,etc. **work-conserving queuing**, si no hay paquetes en una cola, inmediatamente pasa a la siguiente y así sucesivamente. WFQ es una generalización de RR. Se va a atender cada clase de manera circular.
  ![image](https://user-images.githubusercontent.com/71232328/163683116-894b4bed-a4db-4201-8798-a1be8575d658.png)
 
 A diferencia de RR, en un intervalo de tiempo cada clase recibirá un diferencial de tiempo de atención justo
 
 
 
 ![image](https://user-images.githubusercontent.com/71232328/163683181-89bc666e-6d4c-47aa-b8ce-56ba1725947d.png)
 
 
 ## Protocolo de Internet (IP): IPv4, IPv6

 ### IPv4
 
 el paquete de la capa de red es el *datagram*. Campos clave:
 
 * **número de version**: 4 bits que especifican la versión del protocolo IP
 * **largo del header**: 4 bits. Generalmente 4 bytes de header
 * **Tipo de servicio**: para distinguir distintos tipos de datagrams (real-time por una aplicación de telefonía o non-real-time como FTP). 2 de estos bits son usados para ECN
 * **Largo del datagram**: largo total del datagram (incluido el header). 16 bits de largo el campo. En general son de 1500 bytes
 * **Identificador, flags y offset de fragmentación**: 
 * **Time-to-live**: Para evitar que los datagrams circulen para siempre en loop. Si llega a cero, se dropea
 * **Protocolo**: Se usa cuando el datagram llega al destino. Especifica a que protocolo de la capa de transporte debe ser transferido (TCP si es 6, UDP si es 17)
 * **Cheksum del header**: detectar errores en el datagram. Se toman números de 2 bytes y se suman, se hace el complemento a 1. Si el checksum no coincide con el calculado => error y se dropea.
 * **dirección IP origen y destino**: 
 * **Opciones**: permite extender el header IP
 * **Data (payload)**: contiene el segmento de la capa de transporte (TCP o UDP)
 
  ![image](https://user-images.githubusercontent.com/71232328/163683181-89bc666e-6d4c-47aa-b8ce-56ba1725947d.png)
 
 ### Fragmentacion del *datagram* de IPv4

El máximo tamaño de paquetes de la capa de red que pueden transportar los protocolos de la capa de linkeo son llamados **maximum transmission unit (MTU)**. Cada IP datagram va encapsulado en un marco de la capa de linkeo, entonces el MTU de la capa de linkeo pone un límite al largo del datagram de IP. El problema es si cada link en un camino tiene distintos MTU. Si se tiene que transmitir un datagram a un link de salida con un MTU más chico que el largo del datagram, entonces se debe **fragmentar**. Encapsulando cada parte en datagrams de IP más chicos. Antes de pasar a la capa de transporte deben ser rearmados. Este trabajo se da en los end-systems, no en los routers. Para que pueda realizar esta tarea, se colocan *identification,flag y framentation offset* en el datagram. Los fragmentos tienen el mismo identificador. El offset para determinar donde va el fragmento.
 
 ![image](https://user-images.githubusercontent.com/71232328/163692899-c2717271-779a-4dd1-8203-366ec04da54d.png)

 
### addressing de IPv4
 
 El límite entre el host y el link físico es llamado **interfaz**. De igual manera se llama entre el router y los enlaces de entrada y salida. Las direcciones IP tecnicamente están asociadas con una interfaz. Cada dirección tiene 32 bits, escritas en **dotted-decimal notation** (i.e.:  193.32.216.9)
 
 ![image](https://user-images.githubusercontent.com/71232328/163693009-c4087e75-d6e4-4053-9204-360f0c8f50d5.png)

 La red interconectando las interfaces de 3 hosts y la interfaz del router forma una **subnet**. En este caso, la dirección de la subnet es 223.1.1.0/24. el **/24** es llamado **subnet mask**, indica que los 24 bits definen la dirección de la subnet.
 El **network prefix**, hace referencia a la parte de la dirección que tienen en común los host y determina la subnet.

 Puede haber subnets tanto entre hosts como entre routers.
 
 ![image](https://user-images.githubusercontent.com/71232328/163693252-ac53214b-ff82-4d4f-840d-c22d6c730205.png)
 
 Si se tiene una dirección del estilo a.b.c.d/x, los primeros x bits deben ser considerados para la forwarding table, los restantes 32-x bits sirven para determinar al dispositivo dentro de la subnet. Previamente, las partes de red de una dirección IP estaban restringidas a 8, 16 o 24 bits de largo, este esquema era llamado **classful addressing**, ya que estas subnets eran llamadas de tipo A, B o C.
 
 Existen otro tipo de direcciones IP, las de broadcast: 255.255.255.255. En este caso, el mensaje es enviado a todos los hosts dentro de la subnet.
 
 ### Como una organización obtiene un bloque de direcciones
 
 Para obtener este bloque y usarlo en la subnet, debe contactarse a ISP. Este proveerá de un bloque aún más grande, del cual dará una parte a la organización que hizo el pedido
 
 ![image](https://user-images.githubusercontent.com/71232328/163693401-7d70a053-bcc7-4139-9c24-0d332a3b344a.png)

 A las ISP les de las direcciones la **ICANN**.
 
 ### obteniendo direcciones para host: Dynamic Host configuration Protocol
 
 Una vez obtenido el bloque, se queiren asignar direcciones IP individuales a las interfaces de hosts y routers. Las direcciones de host son configuradas usando **DHCP**. Permite a un host obtener una dirección automáticamente. Al host se le asigna un **dirección IP temporaria** distinta cada vez que se conecta. DHCP tambíen es conocido como **zeroconf** o **plug and play**. DHCP es un protocolo cliente-servidor, donde el clietne es el host recién llegado queriendo obtener información de configuracion de la red (IP para él). Cada subnet tendrá su DHCP server. Si no tiene, un router (DHCP relay agent) sabrá la dirección de un server DHCP.
 
 ![image](https://user-images.githubusercontent.com/71232328/163693482-8eef05e5-f3d2-4a97-bf00-de4a6958aa85.png)

 
 Para un host recién llegado, el protocolo DHCP tiene 4 pasos:
 
 * **Descubriemiento del server DHCP**: debe encontrar al server, se hace usando **DHCP discover message**, que se envía sobre UDP al puerto 67. Como no sabe a quien enviarlo, le pone la direccion de broadcast (255.255.255.255) y una dirección origen de 0.0.0.0
 * **DHCP server offer**: Cuando recibe el *discover message*, responde al cliente con un **DHCP offer message** que se envía a la dirección de broadcast. Como puede haber varios servers, el cliente puede elegir. El mensaje incluye **address lease time**, que es el tiempo que la dirección será valida
 * **DHCP request**: el cliente elige el server y le responde con un **DHCP request message**, devolviendo los parametros de configuración que le llegaron.
 * ** DHCP ACK**: el servidor responde con un **DHCP ACK message** confirmando los parámetros
 
 ![image](https://user-images.githubusercontent.com/71232328/163693575-486e6d80-bc0c-49dd-8ee2-ff833711e16b.png)

 
 DHCP también provee un mecanismo por el cual el cliente puede renovar la dirección IP asignada.
 
 ### Network Address TRanslation (NAT)
 
 Qué pasa si no se puede otorgar un bloque de direcciones seguidas ? Para solucionar esto surge **NAT**. Un router puede tener NAT activado. En una casa, las interfaces tendrán la misma dirección de subnet. En la IP se puede reservar partes para **private network** y **realm with private addresess**. Esta última hace referencia a direcciones que solo tienen sentido para dispositivos dentro de la red. Hay muchas redes de casa, muchas usando la misma dirección. No hay problema si se envían paquetes dentro de la red, pero si se envía pro fuera no pueden usar estas direcciones. Para esto aparece NAT.
 ![image](https://user-images.githubusercontent.com/71232328/163693664-df5aa16c-eede-4f27-8466-c46f4c441185.png)

 El router de NAT es visto como un dispositivo con una dirección IP. Todo el tráfico de salida y entrada pasa por las interfaces correspondientes de este dispositivo. Usa una **NAT translation table** para definir a que host enviar el datagram, ya que los paquetes que llegan tienen como dirección la IP de la interfaz del NAT. Se ayuda también incluyebdo puertos en la entrada de la tabla. Como el puerto es de 16 bits y lo usa NAT, nat puede soportar en simultáneo más de 60000 conexiones simultaneas.
 Como contra tiene que los puertos deberian ser usados para identificar procesos, no hosts. Esto se puede solucionar con **NAT traversal**. Además NAT viola el principio de que los routers deberían ser de la capa 3 (de red), interfiriendo nodos modificando las direcciones IP y números de puerto. Son llamados **middleboxes**: operan en la capa de red pero tienen funciones diferentes a la de los routers.
 
 
 ### IPv6
 
 Surge cuando se empiezan a acabar las direcciones Ipv4
 
 El formato del datagram y los mayores cambios son:
 
 * **Expanded addressing capabilities**: direcciones de 128 bits. Introduce direcciones **anycast**, se puede enviar un datagram a un grupo de hosts
 * **streamlined 40-byte header**: fijo, más facil de procesar
 * **labeling de flow**: Audio y video pueden ser tratados como **flow**, también el trafico llevado por un usuario con alta prioridad
 
 ![image](https://user-images.githubusercontent.com/71232328/163693872-928c2ffa-a110-4ffe-b4a0-cd71c7a474bb.png)

 
 Campos en Ipv6:
 
 * **Version**: 6 bits
 * **Traffic lcass**: para dar prioridad a datagrams en un flujo, o de una aplicacion}
 * **flow Label**: identificar flujos de datagramas
 * **Payload lenght**: cuantos bytes despues del header de 40 bytes
 * **Hop limit**: disminuye en 1 cada vez que un router lo forwardea, cuando llega a cero se descarta el datagram.
 * **Direcciones de origen y destino**:
 * **Data**: al llegar a destino, se remueve y se pasa al protocolo especificado por el header
 
 Headers de IPv4 que no están en IPv6:
 
 * **Fragmentation**: esto lo deben realizar los end systems, si un router recibe un datagram muy grande, lo dropea y envía un aviso (ICMP) al sender. El sender reenvia en datagrams más chicos
 * **Header checksum**:  como ya se hace en la capa de transporte y en la de linkeo, es redudndante
 * **Options**: resulta en un header fijo de 40 bytes que puede procesarse más rapido
 
 ### transicion de IPv4 a IPv6
 
 Los sistemas IPv4 no son capaces de manejar IPv6 (sí al revés). Surge el **tunneling**. A los routers IPv4 entre routers IPv6 se los llama **tunnel**. El nodo IPv6 coloca el datagram IPv6 entero en el campo de data (payload) de un datagram IPv4 y lo envía. Para los routers IPv4 intermedios no es un paquete distinto al resto, cuando llega al nodo IPv6 destino, este determina que el datagram IPv4 contiene un datagram IPv6 (viendo el campo del número de protocolo del datagram IPv4 es 41). Lo extrae y redirecciona como si fuera un datagram IPv6 a su vecino IPv6
 
 ![image](https://user-images.githubusercontent.com/71232328/163694193-e45ba490-f085-4202-b3a7-a381fb8de4ce.png)

 ## Forwaring generalizado y SDN
 
 
 En forwarding generalizado, las decisiones pueden tomarse usando orgien y destino tanto de la capa de enlace como de la capa de red
 
![image](https://user-images.githubusercontent.com/71232328/163718853-5b8f8269-4467-420b-95f5-1c9597281f85.png)

 Hay una matchu-plus-table en cada packet switch, mantenida por el controlador remoto. Primero analizamos a OpenFlow, pionero en este campo. Cada entrada de la **flow table** incluía:
 
 * *Set de valores del campo del header*, sobre los que podía matchear un packet que llegara. Si un paquete no matchea ninguna entrada, se dropea o envía al controlador remoto para mejor procesamiento
 * *contadores* que son actualizados a medida que los paquetes matchean las entradas de la tabla. 
 * *set de acciones a tomar* cuando ocurre un matcheo: redireccionar, dropear, hacer copias o reescribir campos del header.
 
 La flow table termina siendo una API
 
 ### Match
 Los campos del header del paquete que pueden matchear en OpenFlow:
 
 ![image](https://user-images.githubusercontent.com/71232328/163719211-49b79fce-f4b7-45ca-8f8a-46386a74994f.png)
 
 OpenFlow permite matcheos en campos de 3 capas de headers de protocolo. origen y destino MAC son de la capa de enlace. OpenFlow puede comportarse tanto como router (capa 3) redireccionando datagrams, como un switch (capa 2) forwarding frames (de la capa de enlace). Las tablas tambien pueden tener *wildcardas*: por ejemplo 128.119.*.* lo matchea cualquier direccion que los primeros 16 bits tengan 128.119.
Open flow no permite matchear el campo TTL entre otros. Esto por el tradeoff entre funcionalidad y complejidad.
 
 ### Action
 
 Si hay multiples acciones de acuerdo a una entrada en latabla, se realizan en el orden propuesto. Las mas importantes son:
 
 * **Forwarding**: a un puerto de salida, broadcast a todos los puertos o multicast a un set de puertos. También encapsulado y enviado al controlador remoto para procesamiento
 * **Droping**: si la entrada de la tabla no tiene acciones, dropea el packet
 * **Modify-field**: Los valores en 10 campos del header pueden ser reescritos antes de redireccionar al packet
 
 Caso común de uso de la tabla es *load balancing* y *firewall*
 
  
</details>

<details>
 <summary> <h3>Capítulo 5 capa de red: plano de control </h3>🍾</summary>

 Controla como se redireccionan los paquetes entre routers en un camino end-to-end y como se configuran y manejan los componentes y servicios de la capa de red.
 
 <h2> Introducción </h2>
 
 La **forwarding table** (*destination-based forwarding*) y la **flow table** (*generalized forwarding*) solo los principales elementos que enlazaban los planos de datos y control de la capa de red. Vamos a ver como se mantienen, computan e instalan.
 Hay 2 formas de encararlo:

 * **Per-router control**: un algoritmo de routeo corre en cada router
 

 
</details>
