# 🦸‍♂️ Sistema de Superhéroes en Python

## 📌 Descripción

Este proyecto implementa un sistema basado en **Programación Orientada a Objetos (POO)** utilizando Python.

Se modela un conjunto de **superhéroes**, aplicando conceptos fundamentales como:

* Clases abstractas (ABC)
* Herencia múltiple
* Encapsulamiento
* Polimorfismo
* Uso de propiedades (`@property` y `@setter`)

---

## 🧠 Analogía utilizada

Se representa un sistema de superhéroes donde cada héroe posee:

* Nombre
* Poder
* Nivel de poder (Fuerte, Intermedio, Débil)

Además, cada héroe puede:

* Usar su poder
* Equipar un traje
* Proteger una ciudad

---

## 🏗️ Estructura del código

### 🔹 Clase abstracta

* `superheroe`

  * Define atributos base
  * Obliga a implementar:

    * `usar_poder()`
    * `__str__()`

---

### 🔹 Clases adicionales

* `traje`

  * Permite equipar un traje

* `ciudad`

  * Permite proteger una ciudad

---

### 🔹 Clase principal

* `heroe`

  * Hereda de:

    * `superheroe`
    * `traje`
    * `ciudad`
  * Implementa los métodos abstractos
  * Aplica encapsulamiento en el atributo `_energia`

---

## 🔐 Encapsulamiento

Se utiliza el atributo protegido:

```python
self._energia
```

Con acceso controlado mediante:

* Getter: `@property`
* Setter: `@energia.setter`

Validación:

* La energía debe estar entre **0 y 100**
* Debe ser un número entero

---

## 🔁 Polimorfismo

Se demuestra al ejecutar el método:

```python
usar_poder()
```

en diferentes objetos, obteniendo comportamientos según los datos de cada héroe.

---

## ▶️ Ejecución del programa

Para ejecutar el proyecto:

```bash
python taller.py
```

---

## 🧪 Pruebas realizadas

El programa incluye:

* Creación de 3 héroes distintos
* Uso del método `usar_poder()`
* Uso de métodos heredados (`equipar_traje`, `proteger_ciudad`)
* Lectura de atributo protegido (`energia`)
* Modificación mediante setter
* Validación de datos incorrectos

---

## 📁 Estructura del proyecto

```
nivelacion_python/
│
├── taller.py
└── README.md
```

---

## 🎯 Conclusión

Este proyecto permite aplicar de forma práctica los conceptos de la POO, demostrando cómo modelar problemas del mundo real mediante clases, herencia y encapsulamiento, logrando un código organizado, reutilizable y escalable.

---

## 👨‍💻 Autor

Estudiante de Ingeniería de Sistemas
4° semestre
