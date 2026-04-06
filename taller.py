
from abc import ABC, abstractmethod


class superheroe(ABC):
    def __init__(self,nombre,poder,nivel_poder):
        self.nombre = nombre
        self.poder = poder
        self.nivel_poder = nivel_poder
    
    @abstractmethod
    def usar_poder(self):
        pass
    @abstractmethod
    def __str__(self):
        pass
class traje:
    def __init__(self,tipo="clasico"):
        self.tipo=tipo

    def equipar_traje(self):
        print(f"equipando traje tipo {self.tipo}") 

class ciudad:
    def __init__(self,nombre_ciudad="ciudad central"):
        self.nombre_ciudad = nombre_ciudad

    def proteger_ciudad(self):
        print(f"protegiendo la ciudad de {self.nombre_ciudad}")


class heroe(superheroe,traje,ciudad):
    def __init__(self,nombre,poder,nivel_poder,tipo_traje,nombre_ciudad,energia):
        superheroe.__init__(self,nombre,poder,nivel_poder)
        traje.__init__(self,tipo_traje)
        ciudad.__init__(self,nombre_ciudad)
        self._energia = None
        self.energia = energia

    @property
    def energia(self):
        return self._energia
    @energia.setter
    def energia(self,valor):
        if not isinstance(valor,int) or valor < 0 or valor > 100:
           print(f"error: la energia de {self.nombre} debe ser entre 0 y 100")
        else:
            self._energia = valor
            print(f"Energia asignada:{self._energia}")

    def usar_poder(self):
        print(f"{self.nombre} usa su poder de {self.poder}(nivel {self.nivel_poder})")
        self.equipar_traje()
        self.proteger_ciudad()

    def __str__(self):
        return f"Héroe: {self.nombre} - Poder: {self.poder} - Nivel: {self.nivel_poder}"
        

if __name__ == "__main__":
    h1 = heroe("Superman","super fuerza","fuerte","kriptoniano","Metropolis",90)
    h2 = heroe("Spider-Man", "Agilidad", "Intermedio", "Arácnido", "Nueva York", 80)
    h3 = heroe("Robin", "Combate", "Débil", "Táctico", "Gotham", 60)

    print("\n--- DEMOSTRACIÓN ---")
    equipo = [h1, h2, h3]

    for h in equipo:
        print(f"\nInfo: {h}")
        h.usar_poder()

    print("\n--- PRUEBA DE ENCAPSULAMIENTO ---")
    print(f"Energía actual de {h1.nombre}: {h1.energia}")

    print("\nActualizando energía a 100...")
    h1.energia = 100
    print(f"Nueva energía: {h1.energia}")

    print("\nIntentando valor inválido (-10)...")
    h1.energia = -10
    print(f"Lectura final: {h1.energia}")
