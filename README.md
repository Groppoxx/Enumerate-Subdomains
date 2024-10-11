# Enumerate Subdomains

`Enumerate Subdomains` es un script en Python que utiliza la API de crt.sh para obtener los subdominios de un dominio específico. El resultado se muestra en la consola, incluyendo la cantidad total de subdominios encontrados.

## Características

* Obtención de subdominios utilizando la API pública de crt.sh.
* Validación de que los subdominios obtenidos pertenezcan realmente al dominio principal.
* Uso de un banner ASCII para una interfaz visual en la consola.
* Presentación clara del número total de subdominios encontrados.

## Requisitos

Este script requiere Python 3.x y las siguientes librerías externas:

* `requests`
* `pyfiglet`

```sh
pip install requests pyfiglet
```

## Uso

Para ejecutar el script, utiliza el siguiente comando:

```sh
python enumsbdm.py <dominio>
```

Por ejemplo:

```sh
python enumsbdm.py google.com
```

El script generará un banner y mostrará los subdominios relacionados con el dominio indicado.

```sh
 _____                                      _       
| ____|_ __  _   _ _ __ ___   ___ _ __ __ _| |_ ___
|  _| | '_ \| | | | '_ ` _ \ / _ \ '__/ _` | __/ _ \
| |___| | | | |_| | | | | | |  __/ | | (_| | ||  __/
|_____|_| |_|\__,_|_| |_| |_|\___|_|  \__,_|\__\___|

 ____        _         _                       _
/ ___| _   _| |__   __| | ___  _ __ ___   __ _(_)_ __  ___
\___ \| | | | '_ \ / _` |/ _ \| '_ ` _ \ / _` | | '_ \/ __|
 ___) | |_| | |_) | (_| | (_) | | | | | | (_| | | | | \__ \
|____/ \__,_|_.__/ \__,_|\___/|_| |_| |_|\__,_|_|_| |_|___/


Searching subdomains from: google.com

aarjav-b480g7k2ab9@checkout.google.com
accounts.flexpack.google.com

...

Amount of subdomains found (98)
```

## Manejo de errores

En caso de que ocurra un error durante la obtención de los subdominios (por ejemplo, problemas de conexión o con la API), el script mostrará un mensaje de error en la consola y terminará su ejecución de manera segura.
