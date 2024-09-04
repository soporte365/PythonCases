class personaje: #Creamos el objeto personaje el cual es una clase
    # def __init__ es un constructor, al cual se le deben asignar los atributos
    def __init__(self, nombre, fuerza, inteligencia, defensa, vida):
        self.nombre = nombre
        self.fuerza = fuerza
        self.inteligencia = inteligencia
        self.defensa = defensa
        self.vida = vida
 # Creamos una metodo (funcion) que muestre los valores
    def atributos (self):
        print(self.nombre, ": ", sep="")
        print("- Fuerza:", self.fuerza)
        print("- Inteligencia:", self.inteligencia)
        print("- Defensa:", self.defensa)
        print("- Vida:", self.vida)

    def sube_niv(self, fuerza, inteligencia, defensa, vida):
        self.fuerza += fuerza
        self.inteligencia += inteligencia
        self.defensa += defensa
        self.vida += vida

    def estaVivo(self):
        return self.vida > 0

    def morir(self):
        self.vida = 0
        print(self.nombre, "ha muerto")

    def daño(self, enemigo):
        return self.fuerza - enemigo.defensa

    def atacar(self, enemigo):
        daño = self.daño(enemigo)
        enemigo.vida = enemigo.vida - daño
        print(self.nombre, "ha realziado", daño, "puntos de daño a ", enemigo.nombre)
        if enemigo.estaVivo():
            print("la vida de enemigo ", enemigo.nombre, "es ", enemigo.vida)
        else:
            enemigo.morir()

# HERENCIA
# Se crea una clase guerrero y se envian los parametro del objeto personaje (padre) y se modifican algunas cosas
class guerrero(personaje):

    def __init__(self, nombre, fuerza, inteligencia, defensa, vida, espada):
        #se usa super(). para llamar a los atributos del padre
        super().__init__(nombre, fuerza, inteligencia, defensa, vida)
        self.espada = espada

    def cambia_arma(self):
        opcion = int(input("Elige Arma: (1) Acero Valyrio, daño 8. (2) Matadragones, daño 9: "))
        if opcion == 1:
            self.espada = 8
        elif opcion == 2:
            self.espada = 9
        else:
            print("Númeo de arma incorrecto")

    def atributos(self):
        super().atributos()
        print("- Espada: ", self.espada)

    def daño(self, enemigo):
        return self.fuerza * self.espada - enemigo.defensa


class mago(personaje):

    def __init__(self, nombre, fuerza, inteligencia, defensa, vida, libro):
        #se usa super(). para llamar a los atributos del padre
        super().__init__(nombre, fuerza, inteligencia, defensa, vida)
        self.libro = libro

    def cambia_arma(self):
        opcion = int(input("Elige Arma: (1) Libro magico, daño 8. (2) Libro Epico, daño 9: "))
        if opcion == 1:
            self.libro = 8
        elif opcion == 2:
            self.libro = 9
        else:
            print("Númeo de arma incorrecto")

    def atributos(self):
        super().atributos()
        print("- Libro: ", self.libro)

    def daño(self, enemigo):
        return self.fuerza * self.libro - enemigo.defensa

# Creamos una variable " Mi_pj"de tipo clase
Norm = personaje("Turme", 10, 5, 20, 100)
Guerr = guerrero("Guerero", 4, 2, 5, 100, 5)
Mago = mago("Maguito", 4, 2, 5, 100, 5)

Norm.atributos()
Guerr.cambia_arma()
Guerr.atributos()
Mago.cambia_arma()
Mago.atributos()


#Mi_pj.atacar(Mi_enemy)
#Mi_pj.atributos()
#Mi_enemy.atributos()
#print(Mi_pj.estaVivo()) #imprime si está vivo

#Mi_pj.sube_niv(3, 2, 4 ,100)  #iincrementa los atributos