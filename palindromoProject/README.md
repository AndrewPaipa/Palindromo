# API Palíndromo en Python-Django

Este es un servicio capaz de reconocer palíndromos dentro de una cadena de texto, sus condiciones son:
- Los espacios en blanco no se eliminan
- Se diferencia entre mayúsculas y minúsculas.
- No se reemplazan caracteres en las cadenas.

Sus solicitudes se realizan a través de los métodos HTTP, GET y POST, las respuestas y peticiones se realizan con formato JSON . También cuenta con respuesta a los métodos PUT y DELETE, sin embargo, estos no realizan ningún proceso, además cuenta con manejo de excepciones.

#### Requerimientos

En la maquina o entorno en el que se desee utilizar la API debe de tener:

- Python 3.5 o superior
- Pip instalado 

#### despliegue en entorno local
Debes tener instalado Python para realizar las instrucciones del despliegue local.
Puedes crear un entorno virtual o realizar el proceso directamente en tu computadora. Una vez hayas clonado el proyecto deberás ejecutar el comando: 

*Pip install -r requirements.txt*

En el directorio donde se haya clonado el proyecto.
Este comando instalará todas las librerías que se encuentran grabadas en el archivo requirement.txt.
Con la consola ubicada en el mismo directorio deberás ejecutar el comando:

*Python manage.py runserver*

Con esto se ejecutará un servidor local. ¡Ahora podrás observar los endpoints!
Para observar la respuesta entregada por los endpoints deberás dirigirte a un 
navegador y colocar la url:

*http://localhost:8000/*

con esto entraras al endpoint genérico y con el url:

*http://localhost:8000/palindromo/*

entraras al enpoint donde se podrán realizar las peticiones HTTP para recibir las respuestas del palíndromo.


#### instrucciones de uso
Su uso se puede observar con la ayuda de Visual Studio Code, en Visual Studio Code debemos instalar la extensión Thunder Client, una vez instalada se podrá observar un icono nuevo en la interfaz de Visual Studio Code; llamado “Thunder Client”, seleccionaremos el icono e iremos al botón de llamado “New Request”. Ahora se desplegará una interfaz donde se pueden seleccionar los diferentes métodos HTTP, puedes seleccionar GET introducir la url:

*http://localhost:8000/palindromo/*

y clickear en el botón “Send”, podremos observar una respuesta del servidor.

Para realizar el método POST, se selecciona este método se introduce la url:

*http://localhost:8000/palindromo/*

Selecciona Body y escribes el siguiente JSON:

*{*

  *"expression":" La cadena que quieras enviar  "*
  
*}*

La API te responderá con un JSON como el siguiente:

*{*

  *"message": "POST success",*
  *"cadena": "Anita lava la tina",*
  *"palindromo mas largo": "ava"*
  
*}*