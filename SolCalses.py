class personaje:
    # def __init__ es un constructor, al cual se le deben asignar los atributos
    def __init__(self, nombre, fuerza, inteligencia, defensa, vida):
        self.nombre = nombre
        self.fuerza = fuerza
        self.inteligencia = inteligencia
        self.defensa = defensa
        self.vida = vida

# Creamos una variable " Mi_pj"de tipo clase
Mi_pj = personaje("Turme", 10, 5, 20, 100)

print(" El Nombre de mi personaje es:", Mi_pj.nombre)