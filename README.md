# Introducción A Sistemas Distribuidos - 75.43


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

Por caa *link* que tiene el *packet switch*, va a tener un *output buffer* o *output queue*.











