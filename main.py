import modulo_auditoria
import logging

try:
    from controladores.gestor_fj import SistemaSoftwareFJ
    from modelos.servicio import Servicio
    MODULOS_DISPONIBLES = True
except ImportError as e:
    MODULOS_DISPONIBLES = False
    logging.error(f"Dependencia faltante en repositorio base: {e}")
    print(f"Aviso: Módulos base no encontrados ({e}). Ejecutando módulo de auditoría...")

def ejecutar_pruebas():
    if not MODULOS_DISPONIBLES:
        modulo_auditoria.ejecutar_pruebas_auditoria()
        return

    app = SistemaSoftwareFJ()
    print("\n--- INICIANDO PRUEBAS DEL SISTEMA SOFTWARE FJ ---\n")


    # Operación 1: Registro válido de cliente
    app.agregar_cliente("C001", "Valentina Gómez", "valentina.gomez@correo.com", "3104455667")

    # Operación 2: Registro válido de segundo cliente
    app.agregar_cliente("C002", "Julián Morales", "jmorales@empresa.co", "3158899001")

    # Operación 3: Registro inválido de cliente (correo mal escrito)
    app.agregar_cliente("C003", "Pedro Ramírez", "pedro_sin_arroba.com", "3001234567")

    # Operación 4: Registro inválido de cliente (teléfono muy corto)
    app.agregar_cliente("C004", "Camila Ortiz", "camila@correo.com", "123")

    # Operación 5: Creación válida de servicio tipo Sala
    app.agregar_servicio(ReservaSala, "S001", "Sala Juntas Principal", 90000, 10)

    # Operación 6: Creación válida de servicio tipo Equipo
    app.agregar_servicio(AlquilerEquipo, "E001", "Portátil Workstation Dell", 55000, "Cómputo")

    # Operación 7: Creación válida de servicio tipo Asesoría
    app.agregar_servicio(AsesoriaEspecializada, "A001", "Consultoría Seguridad Web", 140000, "Ciberseguridad")

    # Operación 8: Creación inválida de servicio (tarifa negativa)
    app.agregar_servicio(AsesoriaEspecializada, "A002", "Asesoría Errónea", -50000, "Redes")

    # Operación 9: Reserva exitosa de Sala (usando sobrecarga: con descuento 10% e IVA 19%)
    app.realizar_reserva("R001", "C001", "S001", duracion=3, descuento=10, impuesto=19)

    # Operación 10: Reserva fallida porque la sala ya está ocupada
    app.realizar_reserva("R002", "C002", "S001", duracion=2)

    # Operación 11: Reserva fallida por cliente inexistente
    app.realizar_reserva("R003", "C999", "E001", duracion=2)

    # Operación 12: Reserva exitosa de Equipo (sin descuento, con IVA 19%)
    app.realizar_reserva("R004", "C002", "E001", duracion=2, impuesto=19)

    # Operación 13: Cancelación de reserva R001 y nueva reserva exitosa sobre la sala liberada
    app.cancelar_reserva("R001")
    app.realizar_reserva("R005", "C002", "S001", duracion=5, descuento=5, impuesto=19)

    print("\n--- RESUMEN FINAL EN MEMORIA ---")
    print(f"Total clientes válidos: {len(app.clientes)}")
    for c in app.clientes:
        print("  *", c.obtener_detalle())

    print(f"\nTotal servicios válidos: {len(app.servicios)}")
    for s in app.servicios:
        print("  *", s.obtener_detalle())

    print(f"\nTotal reservas registradas: {len(app.reservas)}")
    for r in app.reservas:
        print("  *", r.obtener_detalle())


if __name__ == "__main__":
    ejecutar_pruebas()
    modulo_auditoria.ejecutar_pruebas_auditoria()
