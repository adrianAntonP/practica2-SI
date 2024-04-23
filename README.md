# practica2-SI

Pr´actica 2
Sistemas de informaci´on 2024/04/16
1 Pr´actica 2: Representaci´on de los datos
En esta segunda pr ´actica de la asignatura simularemos el proceso de creaci ´on de un dashboard o
Cuadro de Mando Integral (CMI). Este dashboard es una representaci ´on visual de los datos obtenidos
tras el tratamiento realizado en la primera pr ´actica, y lo desarrollaremos utilizando el lenguaje de
programaci ´on Python. Adem ´as, se plantear ´an un conjunto de preguntas relacionadas con el dise ˜no
e implementaci ´on de nuestro sistema OLAP. La pr ´actica se realizar ´a en los mismos grupos creados
para la primera pr´actica. La pr´actica s´olo debe ser entregada por un integrante.
2 Entorno de la pr´actica
En esta pr ´actica seguiremos trabajando en el mismo entorno que la pr ´actica anterior. Nuestros
clientes nos han felicitado tras desarrollar el sistema MIS.
El problema es que los informes que hemos generado son est ´aticos (si nos env´ıan datos a tiempo
real, no podemos representarlos), y no permiten personalizar los diagramas. Por ello, ahora quieren
que dise ˜nemos el almac´en de datos. Para despu´es dise ˜nar un CMI que facilite la toma de decisi ´on a
la direcci´on de la empresa.
3 Ejercicio 1 [1 punto]
Para simular el CMI usaremos la librer´ıa de Flask en Python. En este ejercicio, se desarrollar ´an los
procedimientos necesarios para que el usuario muestre por pantalla los siguientes valores.
• El top X de usuarios cr´ıticos. (0.5)
• El top X de p ´aginas web desactualizadas. Esta se considera desactualizada como +1 si no
cumple el aviso, +1 cookies y +1 si no cumple la protecci ´on de datos, es decir, como la suma
de pol´ıticas que no cumple. En caso de empate se puede desempatar con el a˜no. (0.5)
4 Ejercicio 2 [1.5 puntos]
Ahora deberemos crear los procedimientos necesarios para que el CMI pueda visualizar el top X
de usuarios cr´ıticos, pero tambi´en podr ´a seleccionar si desea que se muestre la informaci ´on de los
usuarios que tienen han pulsado m´as del 50% de veces al correo de spam o menos del 50%.
5 Ejercicio 3 [1.5 puntos]
Mostrar las ´ultimas 10 vulnerabilidades basado a tiempo real. En la siguiente web https://www.
cve-search.org/api/ nos muestra esta informaci ´on y para estar actualizados se pide que nuestro
CMI tenga esta informaci´on.
1
6 Ejercicio 4 [3 puntos]
Este ejercicio ser ´a un ejercicio libre. Cada equipo decidir ´a qu´e a ˜nadir a su CMI para que genere
informaci´on de valor (m´ınimo 2).
Algunos ejemplos:
• Sistema de login para usuarios.
• Generaci´on de informes en PDF.
• An´alisis de otras m´etricas (conexiones por d´ıa de usuario, etc.).
• Mostrar datos de alg´un servicio web mediante otra API.
• Modelo basado en inteligencia artificial que detecte si un usuario es cr´ıtico o no.
7 Ejercicio 5 [3 puntos]
Basado en los modelos de aprendizaje supervisados vistos en el tema 6 realizaremos un algoritmo
que dado un usuario nuevo detecte si va a ser un usuario cr´ıtico o no.
Para ello, os hemos dado un archivo llamado users data online clasificado.json clasificado
seg ´un el conjunto de datos de la primera pr ´actica. Esto nos dar ´a si un usuario es cr´ıtico o no para
este ejercicio.
Utilizaremos https://scikit-learn.org/ scikit learn para desarrollar este ´ultimo ejercicio.
• Realizar un m´etodo de Regresi´on Lineal (1 punto)
• Realizar un m´etodo de Decisi´on Tree (1 punto)
• Realizar un m´etodo de Random forest (1 punto)
El prop ´osito de cada ejercicio, adem ´as de obtener un algoritmo de inteligencia artificial, ser ´a
documentar gr´aficamente como obtiene la clasificaci´on cada uno de los algoritmos.
El CMI mostrar ´a una p ´agina con campos de texto para a ˜nadir un usuario y seleccionar el m´etodo de
inteligencia artificial que validar´a si es cr´ıtico o no.
Se tendr ´a que insertar el usuario (nombre, tel´efono, provincia, permisos, total de email enviados,
total de emails con phishing y total de emails clicados), seleccionar el m´etodo y este analizar ´a si es
un usuario cr´ıtico, mostr´andolo por la pantalla.
NOTA: se debe cargar la informaci ´on de los usuarios mediante la base de datos, el json solo se
necesita para cargar si el usuario es cr´ıtico o no.
8 GitHub
Ser ´a de uso obligatorio la creaci ´on de un repositorio de GitHub para la realizaci ´on de las pr ´acticas
con los miembros del grupo.
9 Material a entregar
La entrega de la pr´actica consistir´a en un archivo comprimido con los siguientes ficheros:
• Carpeta src del proyecto de PyCharm.
2
• Archivo SQLite con la base de datos creada.
• Memoria en formato PDF en la que se responda al ejercicio 1, y se justifique las decisiones
tomadas en todos los ejercicios. En caso de resolver el ejercicio 5, las implementaciones deber ´an
estar incluidas.
• La memoria debe incluir el nombre, apellidos de los integrantes del grupo y el enlace al
repositorio de GitHub.
Ante cualquier duda durante la resoluci ´on de la pr ´actica, escribir a isaac.lozano@urjc.es en copia
a roberto.gallardo@urjc.es v´ıa mail. En caso de no poderse resolver la duda v´ıa mail, se puede
concertar una tutor´ıa, siempre y cuando se concierte en un per´ıodo de hasta 48 horas antes de la
fecha de entrega de la pr´actica.
La fecha l´ımite para entregar esta pr ´actica ser ´a el 28 de abril a las 23:55 y se realizar ´a por la
plataforma Aula Virtual.
• Cualquier pr ´actica corrupta, en borrador o entregada fuera del plazo. ser ´a puntuada con un 0.
• En caso de una pr ´actica que no sea posible de evaluar o sin el enlace de GitHub, ser ´a puntuada
con un 0 y ser´a llamado a revisi´on para justificar la misma.
3
