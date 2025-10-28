# =========================================================
# PARTICIPANTE 1: DEMETRIO GARCIA
# ROL: INTRODUCCIÓN, SALUDO INICIAL Y ESCENA BASE
# =========================================================

# NOTA: Usar únicamente variables, input() y print()

# 1. SOLICITUD Y ALMACENAMIENTO DE DATOS DEL PROTAGONISTA
print("=== COMIENZA LA CREACIÓN DEL PROTAGONISTA DE LA HISTORIA ===")

nombre_protagonista = input("Ingresa el nombre del protagonista: ")
edad_protagonista = input("Ingresa la edad del protagonista: ")
ciudad_protagonista = input("Ingresa la ciudad de residencia: ")
trabajo_protagonista = input("¿A qué se dedica el protagonista? ")

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

# NOTA PARA EL SIGUIENTE PARTICIPANTE:
# Continuar la historia a partir de la misión de la caja.
# Añadir más variables, descripciones o diálogos para mantener la narrativa.
# Evitar bucles o funciones, solo usar variables, input() y print().

# =========================================================
# PARTICIPANTE 2: YOHEL AMAT
# ROL: DESARROLLO - EL VIAJE Y NUEVO PERSONAJE
# =========================================================

print(f"\n*****ACTO 2: EL VIAJE POR LAS MONTANAS CHIRICANAS *****")
print("Con tu mochila lista y el sol iluminando las montañas de Chiriquí, comienza tu travesía...\n")

print("Caminas entre senderos cubiertos de neblina, escuchando el canto de los pájaros.")
print("De pronto, una luz brillante aparece frente a ti, y una voz misteriosa te llama por tu nombre.\n")

mago = input("¿Cómo quieres llamar al mago mágico que acaba de aparecer?: ")
deseo = input("El mago te saluda y dice: 'Puedo cumplir un deseo... ¿qué deseas pedirme?: ")

print("\nEl mago", mago, "asiente con una sonrisa sabia.")
print("Levanta su bastón, murmura unas palabras antiguas y de pronto...")
print(" ¡Tu deseo de", deseo, "comienza a hacerse realidad! ")
print("El viento sopla con fuerza, las hojas giran a tu alrededor, y el viaje continúa con un nuevo destino misterioso.\n")

print("Fin del Acto 2: El Viaje")

# =========================================================
# PARTICIPANTE 3: JONATHAN VERGARA
# ROL: DESARROLLO - EL OBSTÁCULO Y EL SECRETO
# =========================================================

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

# =========================================================
# PARTICIPANTE 4: JONATHAN VERGARA
# ROL: DESCENLACE - LA ENTREGA FINAL
# =========================================================

print("\n--- ACTO IV: EL SECRETO ENTREGADO ---")
print(f"{nombre_protagonista} se acerca al pedestal en {lugar_nuevo}, sintiendo el peso de la misión.")
print("Colocas la caja vibrante sobre la piedra. El símbolo brilla intensamente y la caja se abre sola.")

contenido_caja = input("¿Qué había dentro de la caja? (Ej: 'una semilla brillante', 'un mapa estelar', 'un libro vacío'): ")
print(f"\nDentro de la caja solo había {contenido_caja}.")
print(f"Tan pronto como {contenido_caja} queda expuesto a la luz de {lugar_nuevo}, se eleva en el aire.")

consecuencia = input("¿Qué sucede en el lugar cuando el objeto se eleva? (Ej: 'las plantas crecen rápidamente', 'el cielo se llena de luces', 'se escucha una melodía antigua'): ")

print(f"\nDe repente, {consecuencia}.")
print("Una voz antigua resuena por toda la sala: 'La entrega ha sido completada. El equilibrio ha sido restaurado'.")
print(f"El {guardian} hace una reverencia. El mago {mago} aparece brevemente y te guiña un ojo.")

print("Sientes un tirón, y en un instante, estás de vuelta en tu habitación, en tu ciudad.")
print(f"\nLa caja ha desaparecido. {nombre_protagonista} mira por la ventana hacia los tejados de {ciudad_protagonista}.")
print(f"Sabes que tu trabajo como {trabajo_protagonista} nunca volverá a ser el mismo.")
print(f"A tus {edad_protagonista} años, acabas de realizar la entrega más importante de tu vida.")
print("Tal vez, después de todo, la disciplina y la paciencia sí sirven para cumplir deseos.")

print("\n=== FIN DE LA HISTORIA ===")