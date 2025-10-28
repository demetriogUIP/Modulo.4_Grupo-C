# =========================================================
# PARTICIPANTE 4: JONATHAN VERGARA
# ROL: DESCENLACE - LA ENTREGA FINAL
# =========================================================

def acto_4_el_desenlace(nombre_protagonista, ciudad_protagonista, trabajo_protagonista, edad_protagonista, mago, lugar_nuevo, guardian):
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