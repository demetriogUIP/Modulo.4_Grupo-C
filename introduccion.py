# =========================================================
# PARTICIPANTE 1:
# ROL: INTRODUCCIÓN, SALUDO INICIAL Y ESCENA BASE
# =========================================================


# 1. SOLICITUD Y ALMACENAMIENTO DE DATOS DEL PROTAGONISTA
def crear_protagonista():
    print("=== COMIENZA LA CREACIÓN DEL PROTAGONISTA DE LA HISTORIA ===")

    nombre_protagonista = input("Ingresa el nombre del protagonista: ")
    edad_protagonista = input("Ingresa la edad del protagonista: ")
    ciudad_protagonista = input("Ingresa la ciudad de residencia: ")
    trabajo_protagonista = input("¿A qué se dedica el protagonista? ")

    return nombre_protagonista, edad_protagonista, ciudad_protagonista, trabajo_protagonista

def acto_1(nombre_protagonista, edad_protagonista, ciudad_protagonista, trabajo_protagonista):
    # 2. SALUDO PERSONALIZADO Y PRESENTACIÓN
    print("\n--- ACTO I: EL DESPERTAR ---")
    print(f"¡Hola, {nombre_protagonista}! Tienes {edad_protagonista} años y vives en {ciudad_protagonista}.")
    print(f"Trabajas como {trabajo_protagonista}, una labor que te ha enseñado disciplina y paciencia.")

    # 3. FRAGMENTO DE LA HISTORIA 
    print(f"\nLa mañana se abrió paso entre los tejados antiguos de {ciudad_protagonista}.")
    print(f"En una pequeña habitación, {nombre_protagonista} se preparaba para otro día de trabajo como {trabajo_protagonista}.")
    print(f"A sus {edad_protagonista} años, conocía cada calle y esquina de la ciudad, pero aquel día no sería uno cualquiera.")
    print(f"Sobre la mesa descansaba una pequeña caja envuelta en papel marrón, marcada solo con un símbolo extraño.")
    print("Su primera entrega del día… pero algo en esa caja parecía diferente, como si escondiera un secreto importante.")
