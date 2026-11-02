def clasificar_solicitud(titulo, prioridad, urgencia):
    # 1. Validar primero
    if prioridad not in [1, 2, 3] or urgencia not in ['s', 'n']:
        return "Error: Datos inválidos."
    
    # 2. Clasificar combinando condiciones
    if prioridad <= 2 and urgencia == 's':
        return f"{titulo} -> Crítica"
    elif prioridad == 3 and urgencia == 'n':
        return f"{titulo} -> Baja"
    else:
        return f"{titulo} -> Normal"

# ==========================================
# ZONA DE PRUEBAS (Fuera de la función)
# ==========================================

# Pruebas de la función clasificar_solicitud
print(clasificar_solicitud("Servidor caído", 1, 's'))
print(clasificar_solicitud("Mantenimiento", 2, 'n'))
print(clasificar_solicitud("Cambiar mouse", 3, 'n'))
print(clasificar_solicitud("Limpieza", 5, 'x')) # Prueba de error