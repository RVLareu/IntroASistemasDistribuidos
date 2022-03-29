# Introducción A Sistemas Distribuidos - 75.43

### Resumen del Libro

<details>
 <summary>  Capitulo 1 🍾 </summary> 
 


*host* o *end systems*: dispositivos conectados a la red (lapotot, tablet, reloj, etc).

Estos ultimos conectados por una red de *communication links* y *packet switches*.

![image](https://user-images.githubusercontent.com/71232328/160488180-daf2192f-ce6a-45b4-ac0f-9b4b0ba07cc0.png)

Los *links*  transmiten de acuerda a una *transmission rate* medida en bits/segundo.

*Packet*: paquete de informacion a ser enviado a través de la red.

El *packet switch* toma el *packet* que viene de su *comunication link* de entrada y lo redirecciona a uno de salida. Un *packet switch* puede ser un *router* (en *network core*) o un *link-layer switch*(en *acces network*).

El camino recorrido por el *packet* es el *route* o *path*.

#### Analogia

*packets* = camiones.
*comunication links* = rutas.
*packet switches* = intersecciones.

*end systems* accedent a internet a traves de *Internet Service Providers (ISPs)*. Cada *ISP* es en si mismo una red aparte. Los *ISPs* o *lower tier ISPs* estan interconectados por *upper tier ISP* (fibra optica).

Las piezas que componen internet corren protocolos para controlar envio y recepcion de datos. El *Transmission Control Protocol (TCP)* y *Internet Protocol (IP)* son los mas importantes. 

*internet standards* son desarrollados por la *IETF*. Estos documentos son llamados *request for comments (RFCs* y definen los protocolos

El internet tambíen puede ser descripto como una infraestructura que provee servicios a aplicaciones (*distributed applications*). Corren en *end systems*.
Los *end systems* proveen interfaces para *sockets* que especifican como solicitar y enviar informacion a otro *end system*

#### Protocolo

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

#### Core

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

### Protocol Layering

cada protocolo se corresponde con una capa.

Protocolos de la capa de aplicacion siempre estan implementadas en software. La capa fisica y de linkeo son las encargadas de manejar la comunicacion en un link (en general Ethernet o WIFI asociadas con un *link*). La cpa de red es un mix entre fisica y hardware

![image](https://user-images.githubusercontent.com/71232328/160524387-999652a6-db64-4d99-9ed4-cc0fc7e4193f.png)

#### Capa de aplicaciones

donde residen las aplicaciones de red y sus protocolos como HTTP, SMTP, FTP, DNS. Se distribuye sobre muchos *end systems*. La aplicacion en uno intercambiendo *packets* con la aplicación en otro *host* siguiendo un protocolo. En esta capa la data son mensajes.

#### Capa de transporte

transporta los mensajes de la capa de aplicacion entre *end points*. Protocolos: TCP y UDP

#### Capa de red

Mueve los *packets* de la capa de red llamados *datagrams* de un *host* a otro. Protocolo IP, que define los campos en el *datagram*. También hay *routing protocols* para determinar las rutas que toman los *datagrams*.

#### Capa de linkeo

Para mover un *packet* entre un nodo y tro (*host* o *router*), la capa de red acude a la capa de linkeo. Aquí se pasa el *datagram* a la capa de linkeo, que lo lleva al proximo nodo, donde vuelve a la capa de red. Como ejemplo son Ethernet, Wifi. Un *datagram* puede ser manejado por distintos protocolos en la capa de linkeo.

#### Capa de física

Su trabajo es mover bits entre un nodo y el siguiente. Los protocolos dependen del medio (fibra, par trenzado, etc). Ethernet tiene varias protocolos en esta capa: una para par trenzado, otro para coaxial, fibnra, etc.

![image](https://user-images.githubusercontent.com/71232328/160525485-3d8082b6-c118-4180-8700-5750eb3e8fae.png)

Notar que routers y switches de la capa de linkeo no implementan todas las capas. En cada capa un *packet* tiene dos campos: *header* y *payload*. El ultimo es un *packet* de la capa anterior y *header* sirve para que la capa actual actue. A esto se llama encapsulacion.

### OSI

Otra forma de ver los protocolos distinta al *stack*.

![image](https://user-images.githubusercontent.com/71232328/160525375-169cb37b-6664-40fa-9a2a-4b125961864e.png)

Malware (?)



</details>


<details>
 
 <summary>Capitulo 2 🍾</summary>
 
Al desarrollar una aplicación, hay que escribir software de tal manera que pueda correr en multiples sistemas (no es necesario en *routers* o *link-layer switches*, estos no funcionan en la capa de aplicación). La arquitectura de la aplicación está diseñada por el desarrollador, a diferencia de la arquitectura de la red. Esta puede ser cliente-servidor o *peer-to-peer*.

En la arquitectura cliente-servidor , siempre hay un *host* llamado servidor que recibe peticiones de otros *host* llamados clientes. En esta arquitectura los clientes no se comunican directamente entre si. El servidor tiene una dirección IP fija. Para aplicaciones con muchos clientes, se tiene un *data center* con varios *host* creando un servidor virtual grande.
 
En la arquitectura P2P no hay servidores dedicados, se basa en la comunicacion entre usuarios (ej: Torrent). Esta arquitectura es auto escalable.
 
### Comunicacion
 
Los que se comunican no son los programas, sino los procesos en diferentes (o el mismo) *end systes*. Lo hacen mediante mensajes. En general en una comunicacion, uno es el cliente y el otro el servidor. El que inicia la conexion es el cliente, el que espera a ser conectado, el servidor. Los mensajes se envian y reciben a través de una interfaz de software llamada *socket*. El *socket* es la interfaz entre la capa de aplicacion y la de transporte. También llamada *application programming interface (API)* entre la aplicacion y la red.
 
Para identificar al proceso que recibe mensajes debe tenerse la direccion del host (IP) y un algo que identifique al proceso receptor en el host de destino. Al host lo define la dirección IP (32 bits). Para identificar al proceso, su utiliza el número de puerto.
 
La aplicacion envia mensajes por el socket, la capa de transporte debe llevarlos al socket de destino. Un protocolo de la capa de transporte puede ofrecer varios servicios:

* *Reliable Data Transfer*: asegura que no habrá pérdida de paquetes. Si no lo asegura, esto puede ser tolerable para ciertas aplicaciones (*loss-tolerant applications*) pero no para otras como son las aplicaciones multimedia
* *Throughput*: asegura una tasa mínima de **r** bits/sec. Las aplicaciones que requieren una tasa especifica son *bandwidth-sensitive applications*. Las que no so *elastic applications*.
* *Timing*: un tiempo máximo de arribo del paquete desde que sale hasta que llega al socket receptor (delay).
* *Security*: puede proveer mas de un servicio de seguridad. Puede encriptar los datos al salir y desencriptarlos al llegar.
 
### Servicios de transporte provistos por internet
 
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
 
### Protocolos de capa de aplicación
 
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
 
 
</details>




