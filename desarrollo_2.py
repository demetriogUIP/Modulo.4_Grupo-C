# =========================================================
# PARTICIPANTE 3: JONATHAN VERGARA
# ROL: DESARROLLO - EL OBSTÁCULO Y EL SECRETO
#===================================================
def acto_3(nombre_protagonista, mago, deseo, trabajo_protagonista):
    print("\n--- ACTO III: EL DESTINO REVELADO ---")
    print(f"El viento mágico que levantó el mago {mago} finalmente se detiene.")
    print(f"Ya no estás en las montañas. El deseo de '{deseo}' te ha transportado a un lugar completamente nuevo.")

    lugar_nuevo = input("¿Dónde has aparecido? (Ej: 'un templo antiguo en la selva', 'una cueva de cristales', 'una torre en las nubes'): ")
    print(f"\n{nombre_protagonista} mira a su alrededor. Estás en {lugar_nuevo}.")
    print("Sientes un calor en tu mochila. ¡La misteriosa caja (la de tu primera entrega) está vibrando!")
    print("El extraño símbolo en el papel marrón ahora brilla con una luz dorada.")

    print(f"Frente a ti, en {lugar_nuevo}, hay un pedestal de piedra que parece esperar la caja.")
    print("Pero el camino no está libre. Un guardián protege el pedestal.")
    guardian = input("¿Qué tipo de guardián es? (Ej: 'un golem de piedra', 'un espíritu del bosque', 'un acertijo viviente'): ")

    print(f"\nEl {guardian} te bloquea el paso. No parece hostil, pero te observa fijamente, esperando algo.")
    print(f"Como {trabajo_protagonista} experimentado, sabes que a veces la diplomacia es mejor que la fuerza.")

    ofrenda = input(f"¿Qué objeto sacas de tu mochila para ofrecerle al {guardian}? (Ej: 'una brújula vieja', 'una manzana', 'una herramienta de tu trabajo'): ")

    print(f"\n{nombre_protagonista} saca {ofrenda} y se lo muestra con respeto al {guardian}.")
    print(f"El {guardian} estudia el objeto por un momento y luego, lentamente, se hace a un lado.")
    print("El camino hacia el pedestal está libre.")

    print("\nFin del Acto 3: El Obstáculo Superado")

    return lugar_nuevo, guardian, ofrenda