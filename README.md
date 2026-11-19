# Sistema Integral de Gestión de Clientes, Servicios y Reservas - Software FJ

Proyecto desarrollado para el curso **Programación (213023)** – Fase 4 (Componente práctico - Prácticas simuladas), Universidad Nacional Abierta y a Distancia (UNAD).

## Descripción
Aplicación orientada a objetos en Python, sin uso de bases de datos, diseñada para gestionar clientes, servicios especializados (salas, alquiler de equipos y asesorías técnicas) y reservas en memoria. El sistema implementa validaciones estrictas, polimorfismo, sobrecarga de cálculo de costos y manejo avanzado de excepciones con registro continuo en archivos de log.

## Estructura del Proyecto
```text
Sistema_Software_FJ/
├── excepciones/
│   ├── __init__.py
│   └── errores_sistema.py      # Jerarquía de excepciones personalizadas
├── modelos/
│   ├── __init__.py
│   ├── entidad_base.py         # Clase abstracta general EntidadSistema
│   ├── cliente.py              # Clase Cliente con encapsulación y validaciones
│   ├── servicio.py             # Clase abstracta Servicio + 3 subclases + sobrecarga
│   └── reserva.py              # Clase Reserva y control de estados
├── controladores/
│   ├── __init__.py
│   ├── registro_logs.py        # Configuración de logging en archivo y consola
│   └── gestor_fj.py            # Gestión en memoria con try/except/else/finally
├── logs/
│   └── eventos_fj.log          # Registro de eventos y errores del sistema
├── main.py                     # Simulación de 13 operaciones completas
└── README.md