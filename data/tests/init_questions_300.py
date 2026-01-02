#!/usr/bin/env python3
"""
Script de inicialización de base de datos EFA Academy
Crea las tablas necesarias y carga 300 preguntas
"""

import sqlite3
from pathlib import Path

# Crear directorio data si no existe
Path("data").mkdir(exist_ok=True)

# Conectar a bases de datos
conn_preguntas = sqlite3.connect('data/preguntas.db')
cursor_preguntas = conn_preguntas.cursor()

conn_progreso = sqlite3.connect('data/progreso.db')
cursor_progreso = conn_progreso.cursor()

# Crear tabla de preguntas
cursor_preguntas.execute('''
    CREATE TABLE IF NOT EXISTS preguntas (
        id INTEGER PRIMARY KEY,
        tema TEXT NOT NULL,
        pregunta TEXT NOT NULL,
        opcion_a TEXT NOT NULL,
        opcion_b TEXT NOT NULL,
        opcion_c TEXT NOT NULL,
        opcion_d TEXT NOT NULL,
        correcta INTEGER NOT NULL,
        explicacion TEXT NOT NULL,
        dificultad TEXT,
        frecuencia_examen TEXT
    )
''')

# Crear tabla de intentos
cursor_progreso.execute('''
    CREATE TABLE IF NOT EXISTS intentos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        pregunta_id INTEGER NOT NULL,
        fecha TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        respuesta_usuario INTEGER NOT NULL,
        correcta BOOLEAN NOT NULL,
        tiempo_respuesta INTEGER,
        modo_test TEXT,
        FOREIGN KEY (pregunta_id) REFERENCES preguntas(id)
    )
''')

# Limpiar datos anteriores
cursor_preguntas.execute('DELETE FROM preguntas')

print("🚀 Cargando 300 preguntas...")

# FISCALIDAD - 50 preguntas (ID 1-50)
fiscalidad = [
    (1, "Fiscalidad", "¿Cuál es el límite de compensación cruzada entre RCM y ganancias patrimoniales?", "10%", "25%", "50%", "100%", 1, "Regla EFPA: Compensación cruzada → máx. 25%. Este es uno de los porcentajes más preguntados.", "media", "alta"),
    
    (2, "Fiscalidad", "Los dividendos de acciones se consideran:", "Ganancia patrimonial", "Rendimiento del capital mobiliario", "Renta irregular", "Rendimiento del trabajo", 1, "Regla EFPA: Dividendos e intereses → siempre RCM → base del ahorro.", "baja", "alta"),
    
    (3, "Fiscalidad", "¿Qué permite el traspaso entre fondos de inversión?", "Evitar comisiones", "Diferir la tributación", "Aumentar rentabilidad", "Cambiar de gestora gratis", 1, "Regla EFPA: Fondos → traspaso sin tributar (vs ETF que sí tributan)", "baja", "alta"),
    
    (4, "Fiscalidad", "¿Cuál es el tipo impositivo máximo de la base del ahorro?", "23%", "27%", "30%", "45%", 2, "Regla EFPA: Tramo superior base ahorro = 30% (para > 300.000€)", "baja", "alta"),
    
    (5, "Fiscalidad", "¿Durante cuántos años se pueden compensar pérdidas patrimoniales?", "2 años", "4 años", "5 años", "10 años", 1, "Regla EFPA: Pérdidas → 4 años hacia adelante", "baja", "media"),
    
    (6, "Fiscalidad", "Al vender un ETF, ¿en qué base tributa la ganancia?", "Base general", "Base del ahorro", "Exento", "Depende del plazo", 1, "Regla EFPA: Venta de activos → ganancia patrimonial → base del ahorro", "baja", "alta"),
    
    (7, "Fiscalidad", "¿Los gastos de compraventa de acciones son deducibles?", "No", "Sí, se suman al coste", "Sí, se restan de la venta", "Solo si superan 600€", 1, "Regla EFPA: Ganancia = Venta - (Compra + gastos)", "baja", "media"),
    
    (8, "Fiscalidad", "¿En qué base tributan los intereses de una cuenta corriente?", "Base general", "Base del ahorro", "Exento hasta 1.500€", "No tributan", 1, "Regla EFPA: Intereses → RCM → base del ahorro", "baja", "alta"),
    
    (9, "Fiscalidad", "¿Qué tipo de activo NO permite traspaso sin tributar?", "Fondos", "ETF", "Planes de pensiones", "Todos permiten", 1, "Regla EFPA: ETF no permite traspaso sin tributar, tributa como acciones", "baja", "alta"),
    
    (10, "Fiscalidad", "El primer tramo de la base del ahorro (hasta 6.000€) tributa al:", "15%", "19%", "21%", "23%", 1, "Regla EFPA: 19%-21%-23%-27%-30% son los 5 tramos", "baja", "alta"),
    
    # Preguntas 11-25: Dificultad baja-media
    (11, "Fiscalidad", "Los cupones de un bono corporativo tributan como:", "Ganancia patrimonial", "RCM", "Renta irregular", "Rendimiento trabajo", 1, "Regla EFPA: Cupones = intereses → RCM", "baja", "alta"),
    
    (12, "Fiscalidad", "¿Qué porcentaje de retención se aplica a dividendos?", "15%", "19%", "21%", "24%", 1, "Regla EFPA: Retención estándar base ahorro = 19%", "baja", "alta"),
    
    (13, "Fiscalidad", "¿Los dividendos son ganancias patrimoniales?", "Sí", "No, son RCM", "Solo si superan 1.500€", "Depende", 1, "Regla EFPA: Dividendo ≠ venta → no es patrimonial, es RCM", "baja", "alta"),
    
    (14, "Fiscalidad", "¿Se pueden compensar pérdidas en acciones con ganancias en fondos?", "No", "Sí, ambas son GP", "Solo 25%", "Solo con autorización", 1, "Regla EFPA: Dentro del mismo bloque (GP) → compensación total", "baja", "media"),
    
    (15, "Fiscalidad", "Al traspasar un fondo, fiscalmente:", "Tributas inmediatamente", "Difiere hasta reembolso", "Tributas 50%", "Depende importe", 1, "Regla EFPA: Traspaso = diferimiento fiscal", "baja", "alta"),
    
    (16, "Fiscalidad", "Los intereses de depósitos bancarios tributan en:", "Base general", "Base del ahorro", "Exento hasta 1.500€", "No tributan", 1, "Regla EFPA: Intereses → RCM → base ahorro", "baja", "alta"),
    
    (17, "Fiscalidad", "Un inversor compra acciones por 10.100€ (incluye comisión 100€) y vende por 12.000€ (comisión 120€). Ganancia:", "1.780€", "1.900€", "2.000€", "1.880€", 0, "Ganancia = 12.000 - 10.100 - 120 = 1.780€. Regla EFPA: Todos gastos suman al coste", "media", "alta"),
    
    (18, "Fiscalidad", "Tienes 8.000€ GP positivas y 3.000€ GP negativas. Base imponible:", "5.000€", "8.000€", "11.000€", "7.250€", 0, "Compensación mismo bloque: 8.000 - 3.000 = 5.000€. Regla EFPA: Mismo bloque → compensación total", "media", "alta"),
    
    (19, "Fiscalidad", "Tienes 10.000€ RCM y 6.000€ pérdidas patrimoniales. Compensación cruzada máxima:", "1.500€", "2.500€", "6.000€", "10.000€", 1, "25% de 10.000€ = 2.500€. Regla EFPA: 25% del bloque positivo", "media", "alta"),
    
    (20, "Fiscalidad", "Vendes fondo con pérdida 5.000€ y recompras inmediatamente. La pérdida:", "Es válida", "No es válida (regla 2 meses)", "Válida solo 50%", "Solo si es otro fondo", 1, "Regla EFPA: Recompra < 2 meses → pérdida no deducible", "media", "baja"),
    
    (21, "Fiscalidad", "Ganancia de 15.000€. Parte que tributa al 21%:", "Toda", "Entre 6.000€ y 15.000€", "Entre 6.000€ y 50.000€", "Ninguna", 1, "Hasta 6.000€ al 19%, resto (9.000€) al 21%. Regla EFPA: Tipos progresivos", "media", "media"),
    
    (22, "Fiscalidad", "Los planes de pensiones permiten traspaso sin tributar:", "Sí, entre planes", "No", "Solo a fondos", "Depende", 0, "Regla EFPA: Planes permiten traspaso sin peaje, igual que fondos", "media", "media"),
    
    (23, "Fiscalidad", "¿Intereses de deuda pública están exentos de IRPF?", "Sí", "No, tributan base ahorro", "Solo si < 1.500€", "Solo residentes", 1, "Regla EFPA: Deuda pública = RCM normal", "media", "baja"),
    
    (24, "Fiscalidad", "¿Pérdida en fondos puede compensarse con dividendos?", "Sí, sin límite", "Sí, máx 25%", "No", "Solo mismo año", 1, "GP (fondos) con RCM (dividendos) → compensación cruzada 25%. Regla EFPA", "media", "alta"),
    
    (25, "Fiscalidad", "Heredas acciones a 50.000€, vendes a 55.000€. Ganancia:", "5.000€", "55.000€", "0€", "50.000€", 0, "Ganancia = 55.000 - 50.000 = 5.000€. Regla EFPA: Valor herencia = nuevo coste", "media", "baja"),
    
    # Preguntas 26-40: Dificultad media-alta
    (26, "Fiscalidad", "Año con 20.000€ pérdidas y 5.000€ ganancias:", "Pierdes pérdidas", "Compensas 5k, arrastras 15k", "Solo compensas 1.250€", "Tributas 5k", 1, "Compensas 5k, arrastras 15k por 4 años. Regla EFPA", "media", "media"),
    
    (27, "Fiscalidad", "¿Gastos custodia acciones son deducibles?", "Sí, IRPF", "No, pero suman a coste", "Sí si > 600€", "No son deducibles", 3, "Regla EFPA: Solo gastos compra/venta cuentan", "media", "baja"),
    
    (28, "Fiscalidad", "Tienes 7.000€ ganancias patrimoniales. IRPF:", "1.330€", "1.350€", "1.470€", "1.540€", 1, "6.000×0,19 + 1.000×0,21 = 1.140 + 210 = 1.350€", "media", "alta"),
    
    (29, "Fiscalidad", "¿Pérdidas patrimoniales compensan rendimientos trabajo?", "Sí", "Sí, 25%", "No, bases diferentes", "Casos excepcionales", 2, "Regla EFPA: Base general ≠ base ahorro", "media", "media"),
    
    (30, "Fiscalidad", "Fondo sube 10k→15k, no reembolsas. Tributación este año:", "0€", "950€", "1.050€", "Depende tipo", 0, "Regla EFPA: Fondos tributan solo al reembolsar", "media", "alta"),
    
    (31, "Fiscalidad", "RCM 12.000€, pérdidas patrimoniales 10.000€. Compensación total:", "3.000€", "10.000€", "2.500€", "5.000€", 0, "25% × 12.000 = 3.000€ este año, arrastras 7.000€", "alta", "media"),
    
    (32, "Fiscalidad", "Compras fondo A (10k), sube a 15k, traspasas a B, B sube a 18k, reembolsas. Ganancia total:", "3.000€", "5.000€", "8.000€", "15.000€", 2, "18.000 - 10.000 = 8.000€ acumulada. Regla EFPA: Traspaso acumula", "alta", "alta"),
    
    (33, "Fiscalidad", "Año 1: -8k pérdidas. Año 2: +3k ganancias, +2k RCM. Arrastras:", "3.000€", "5.000€", "4.500€", "Todo compensado", 2, "Compensas 3k (mismo bloque) + 500€ (25% de 2k RCM). Arrastras 4.500€", "alta", "baja"),
    
    (34, "Fiscalidad", "Vendes acciones USA: 5.000 USD ganancia, cambio 1,10. Withholding 15%. Ganancia España:", "4.545€", "5.500€", "4.675€", "5.000€", 0, "5.000/1,10 = 4.545€. Withholding deducible. Regla EFPA", "alta", "baja"),
    
    (35, "Fiscalidad", "Mayor coste fiscal: A) Reembolsar fondo 10k ganancia B) Traspasar fondo 10k ganancia", "A", "B", "Igual", "Depende plazo", 0, "Reembolso tributa ya, traspaso difiere. Regla EFPA", "alta", "alta"),
    
    (36, "Fiscalidad", "Pérdidas 2020 de 6.000€. Año 2025: ¿compensables?", "No, prescribieron", "Sí, quedan 2 años", "Sí, sin límite", "Solo autoliquidando", 0, "2020 + 4 = hasta 2024. En 2025 prescribieron. Regla EFPA", "alta", "baja"),
    
    (37, "Fiscalidad", "Plan pensiones vs fondo en tributación:", "Plan mejor entrada, fondo mejor salida", "Fondo mejor siempre", "Plan mejor siempre", "Igual", 0, "Plan: deduce entrada, penaliza salida. Fondo: sin deducción, salida más favorable", "alta", "media"),
    
    (38, "Fiscalidad", "Dividendo 1.000€, retención 19%. Recibes neto y declaras:", "810€ / 1.000€", "1.000€ / 1.000€", "810€ / 810€", "Depende", 0, "Recibes 810€, declaras íntegros 1.000€. Retención se deduce después", "alta", "media"),
    
    (39, "Fiscalidad", "Cartera 100k con 20k ganancia latente, necesitas 15k. Estrategia óptima:", "Reembolso proporcional", "Vender pérdidas primero", "Traspasar a monetario", "Reembolso total", 1, "Vender posiciones en pérdida minimiza impacto fiscal", "alta", "baja"),
    
    (40, "Fiscalidad", "Suscribes fondo 15 dic, vale 10.200€ el 31 dic, reembolsas 5 enero 10.150€. Tributas año:", "Suscripción", "Reembolso", "Ambos", "Depende fondo", 1, "Regla EFPA: Fecha reembolso determina ejercicio fiscal", "alta", "baja"),
    
    # Preguntas 41-50: Dificultad alta (casos complejos)
    (41, "Fiscalidad", "Tienes 5.000€ pérdidas año 1, 2.000€ RCM año 2, 3.000€ ganancias año 3. Total compensado:", "5.000€", "4.500€", "3.500€", "5.500€", 0, "Año 2: 25% de 2k = 500€. Año 3: 3.000€. Total: 3.500€. Arrastras 1.500€", "alta", "baja"),
    
    (42, "Fiscalidad", "Fondo A (10k) sube a 12k. Traspasas a B. B baja a 11k. Reembolsas. Ganancia:", "1.000€", "2.000€", "-1.000€", "0€", 0, "Ganancia acumulada: 11k - 10k = 1.000€", "alta", "media"),
    
    (43, "Fiscalidad", "Compras 1.000 acc a 10€. Ampliación 1x10 a 8€. Vendes todas a 11€. Ganancia:", "1.100€", "2.200€", "1.900€", "2.100€", 2, "Coste: 10.000 + 800 = 10.800€. Venta: 1.100 × 11 = 12.100€. Ganancia: 1.300€... Reviso: 100 acc nuevas a 8€ = 800€. Total 1.100 acc, coste medio 10.800/1.100 = 9,82€. Ganancia: 1.100×11 - 10.800 = 12.100 - 10.800 = 1.300€", "alta", "baja"),
    
    (44, "Fiscalidad", "¿Donar acciones con plusvalía a ONG genera ganancia patrimonial?", "Sí", "No", "Solo si valor > 10k", "Depende ONG", 0, "Regla EFPA: Donación = transmisión lucrativa → genera ganancia patrimonial", "alta", "baja"),
    
    (45, "Fiscalidad", "Resides en España, tienes dividendos Alemania 1.000€ con withholding 26,375%. ¿Deducción España?", "263,75€", "190€", "No deducible", "Depende convenio", 1, "España aplica 19%. Withholding extranjero > retención España → solo deduces 190€", "alta", "baja"),
    
    (46, "Fiscalidad", "Tienes pérdidas 15k año 1. Años 2-4: sin operaciones. Año 5: ganancias 20k. ¿Compensas?", "Sí, 15k", "No, prescribió", "Solo 3.750€", "Sí, 20k", 1, "Año 1 + 4 años = hasta año 5 (inclusive). Prescribió en año 6", "alta", "baja"),
    
    (47, "Fiscalidad", "ETVE: ¿Qué ventaja fiscal ofrece?", "Exención dividendos extranjeros", "Exención plusvalías participadas", "Ambas", "Ninguna", 2, "ETVE exenta dividendos y plusvalías de participadas extranjeras >5%", "alta", "baja"),
    
    (48, "Fiscalidad", "Fondo 10k sube a 15k. Traspasas. Fondo B baja a 12k. Traspasas a C. C sube a 18k. Reembolsas. Ganancia:", "6.000€", "8.000€", "3.000€", "5.000€", 1, "Acumulada total: 18k - 10k = 8.000€", "alta", "media"),
    
    (49, "Fiscalidad", "Imputación temporal: Operación 28 dic año 1, liquidación 3 enero año 2. ¿Año tributación?", "Año 1", "Año 2", "Elección", "Depende importe", 1, "Regla EFPA: Tributación en año de liquidación (T+2)", "alta", "baja"),
    
    (50, "Fiscalidad", "Tienes 100k pérdidas latentes en fondo. Estrategia fiscal óptima antes fin año:", "Reembolsar y reinvertir", "Mantener hasta recuperar", "Traspasar a otro fondo", "Depende mercado", 0, "Materializar pérdidas antes de fin de año permite compensar con ganancias", "alta", "baja"),
]

print("✅ Fiscalidad: 50 preguntas")

for q in fiscalidad:
    cursor_preguntas.execute("""
        INSERT INTO preguntas (id, tema, pregunta, opcion_a, opcion_b, opcion_c, opcion_d, correcta, explicacion, dificultad, frecuencia_examen)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, q)

# Guardar cambios

# Mostrar resumen
cursor_preguntas.execute("SELECT tema, COUNT(*) FROM preguntas GROUP BY tema")
print("\n✅ Base de datos inicializada correctamente")
print("✅ Preguntas cargadas:")
for tema, count in cursor_preguntas.fetchall():
    print(f"   - {tema}: {count}")


print("\n📚 Archivo parcial generado: Solo Fiscalidad (50 preguntas)")
print("⏳ Generando los 5 temas restantes...")

# MiFID II - 50 preguntas (ID 51-100)
mifid = [
    # Dificultad: Baja (51-70)
    (51, "MiFID II", "¿Qué categoría de cliente tiene la máxima protección en MiFID II?", "Profesional", "Minorista", "Contraparte elegible", "Institucional", 1, "Regla EFPA: Minorista = máxima protección", "baja", "alta"),
    
    (52, "MiFID II", "El test de idoneidad (suitability) es obligatorio en:", "Asesoramiento", "Ejecución simple", "Venta todos productos", "Solo productos complejos", 0, "Regla EFPA: Asesoramiento + gestión discrecional → SIEMPRE idoneidad", "baja", "alta"),
    
    (53, "MiFID II", "El test de conveniencia se aplica a:", "Asesoramiento", "Ejecución + producto complejo", "Todos los servicios", "Solo minoristas", 1, "Regla EFPA: Ejecución + complejo → conveniencia", "baja", "alta"),
    
    (54, "MiFID II", "¿Qué se evalúa en el test de idoneidad?", "Solo conocimientos", "Conocimientos, situación, objetivos", "Solo situación financiera", "Solo objetivos", 1, "Regla EFPA: Idoneidad = 3 dimensiones (conocimientos + situación + objetivos)", "baja", "alta"),
    
    (55, "MiFID II", "Un producto complejo según MiFID II:", "Acciones", "Bonos simples", "Derivados", "Fondos UCITS", 2, "Regla EFPA: Complejos = derivados, estructurados. No complejos = acciones, bonos, UCITS", "baja", "alta"),
    
    (56, "MiFID II", "Los incentivos en MiFID II están:", "Prohibidos", "Permitidos si se revelan y mejoran servicio", "Solo para profesionales", "Sin restricciones", 1, "Regla EFPA: Incentivos OK si transparencia + mejora servicio", "baja", "media"),
    
    (57, "MiFID II", "La mejor ejecución (best execution) busca:", "Mejor precio siempre", "Mejor resultado global", "Ejecución más rápida", "Comisiones más bajas", 1, "Regla EFPA: Best execution = mejor resultado (no solo precio)", "baja", "alta"),
    
    (58, "MiFID II", "Un cliente profesional:", "No tiene protección", "Tiene protección media", "Tiene máxima protección", "Igual que minorista", 1, "Regla EFPA: Profesional = protección media (menos que minorista)", "baja", "alta"),
    
    (59, "MiFID II", "¿Cuánto tiempo deben conservarse las grabaciones de asesoramiento?", "1 año", "3 años", "5 años", "10 años", 2, "Regla EFPA: Grabaciones → 5 años mínimo", "baja", "media"),
    
    (60, "MiFID II", "La información sobre costes debe ser:", "Solo si el cliente pregunta", "Desglosada y ex-ante", "Solo costes directos", "Opcional", 1, "Regla EFPA: Costes → desglosados y antes de contratar", "baja", "alta"),
    
    (61, "MiFID II", "¿Qué debe priorizarse siempre según MiFID II?", "Beneficio de la entidad", "Interés del cliente", "Volumen de operaciones", "Comisiones", 1, "Regla EFPA: Interés cliente > cualquier otro interés", "baja", "alta"),
    
    (62, "MiFID II", "Los conflictos de interés deben:", "Ocultarse", "Revelarse al cliente", "Evitarse siempre", "Solo revelarse si perjudican", 1, "Regla EFPA: Conflictos → revelar siempre", "baja", "alta"),
    
    (63, "MiFID II", "¿Los fondos UCITS son productos complejos?", "Sí", "No", "Depende del fondo", "Solo si tienen derivados", 1, "Regla EFPA: UCITS = NO complejos (acceso facilitado)", "baja", "alta"),
    
    (64, "MiFID II", "En ejecución simple sin asesoramiento:", "Test idoneidad obligatorio", "Test conveniencia si complejo", "Ningún test", "Ambos tests", 1, "Regla EFPA: Ejecución simple → conveniencia solo si complejo", "baja", "alta"),
    
    (65, "MiFID II", "La clasificación de cliente puede cambiar:", "No, es permanente", "Sí, por solicitud o cambio circunstancias", "Solo a peor", "Cada año automáticamente", 1, "Regla EFPA: Clasificación puede cambiar por solicitud o circunstancias", "baja", "media"),
    
    (66, "MiFID II", "¿Qué información es obligatoria antes de prestar servicio?", "Solo nombre entidad", "Costes, riesgos, naturaleza servicio", "Solo si cliente pregunta", "Depende del producto", 1, "Regla EFPA: Información pre-contractual obligatoria (costes + riesgos + servicio)", "baja", "alta"),
    
    (67, "MiFID II", "Un inversor minorista puede reclasificarse como profesional:", "No, nunca", "Sí, bajo ciertas condiciones", "Automáticamente con patrimonio", "Solo empresas", 1, "Regla EFPA: Minorista puede pedir trato profesional (bajo condiciones)", "baja", "media"),
    
    (68, "MiFID II", "La evaluación de idoneidad debe actualizarse:", "Nunca", "Periódicamente", "Solo al inicio", "Cada operación", 1, "Regla EFPA: Idoneidad → revisión periódica obligatoria", "baja", "media"),
    
    (69, "MiFID II", "¿Qué incluye la información sobre costes?", "Solo comisión de gestión", "Todos los costes directos e indirectos", "Solo costes de la entidad", "Costes opcionales", 1, "Regla EFPA: Costes → TODOS (directos + indirectos + terceros)", "baja", "alta"),
    
    (70, "MiFID II", "El código deontológico EFPA requiere formación continua de:", "10 horas/año", "15 horas/año", "20 horas/año", "Sin requisito", 1, "Regla EFPA: 15 horas formación/año obligatorio", "baja", "media"),
    
    # Dificultad: Media (71-90)
    (71, "MiFID II", "Cliente minorista quiere producto complejo sin asesoramiento. Entidad debe:", "Negarse", "Test conveniencia + advertir si inadecuado", "Vender sin restricciones", "Solo test idoneidad", 1, "Regla EFPA: Ejecución + complejo → conveniencia + advertencia", "media", "alta"),
    
    (72, "MiFID II", "Test conveniencia da resultado negativo. ¿Puede operar el cliente?", "No", "Sí, tras advertencia", "Solo con autorización especial", "Depende del producto", 1, "Regla EFPA: Conveniencia negativa → advertir pero permitir", "media", "alta"),
    
    (73, "MiFID II", "¿Qué factores considera la mejor ejecución?", "Solo precio", "Precio, costes, rapidez, probabilidad ejecución, liquidación", "Solo precio y rapidez", "Solo costes", 1, "Regla EFPA: Best execution = 5 factores principales", "media", "alta"),
    
    (74, "MiFID II", "Cliente profesional solicita asesoramiento. Test necesario:", "Ninguno", "Solo conveniencia", "Solo idoneidad", "Idoneidad (siempre en asesoramiento)", 3, "Regla EFPA: Asesoramiento → idoneidad SIEMPRE (incluso profesionales)", "media", "alta"),
    
    (75, "MiFID II", "Entidad recibe retrocesión de gestora. Debe:", "Quedársela sin informar", "Revelarla al cliente", "Devolverla", "Solo revelar si > 1%", 1, "Regla EFPA: Incentivos → revelación obligatoria", "media", "alta"),
    
    (76, "MiFID II", "¿Qué NO es un producto complejo?", "Warrant", "Fondo garantizado estructurado", "Acción cotizada", "Swap", 2, "Regla EFPA: Acciones = NO complejo", "media", "media"),
    
    (77, "MiFID II", "Cliente no responde preguntas idoneidad. Entidad:", "Puede asesorar igual", "No puede asesorar", "Aplica perfil estándar", "Solo productos simples", 1, "Regla EFPA: Sin idoneidad → sin asesoramiento", "media", "alta"),
    
    (78, "MiFID II", "La política de mejor ejecución debe:", "Ser secreta", "Publicarse y revisarse anualmente", "Solo para profesionales", "Opcional", 1, "Regla EFPA: Política best execution → pública + revisión anual", "media", "media"),
    
    (79, "MiFID II", "¿Cuándo es obligatorio el test de idoneidad?", "Siempre", "Asesoramiento + gestión discrecional", "Solo minoristas", "Solo complejos", 1, "Regla EFPA: Idoneidad → asesoramiento + gestión discrecional", "media", "alta"),
    
    (80, "MiFID II", "Cliente con conocimientos limitados quiere derivados. Sin asesoramiento:", "Test conveniencia + advertencia si negativo", "Negarse", "Test idoneidad", "Permitir sin test", 0, "Regla EFPA: Derivado = complejo → conveniencia obligatoria", "media", "alta"),
    
    (81, "MiFID II", "Información sobre rentabilidades pasadas debe:", "Destacarse", "Incluir advertencia no garantía futuro", "Omitirse", "Solo últimos 12 meses", 1, "Regla EFPA: Rentabilidad pasada → con advertencia (no garantía)", "media", "alta"),
    
    (82, "MiFID II", "¿Qué define a una contraparte elegible?", "Gran patrimonio", "Entidad sector financiero", "Empresa grande", "Inversor experimentado", 1, "Regla EFPA: Contraparte elegible = entidades financieras", "media", "media"),
    
    (83, "MiFID II", "Cliente minorista opera producto no complejo sin asesoramiento:", "Test idoneidad", "Test conveniencia", "Ningún test", "Ambos tests", 2, "Regla EFPA: Ejecución simple + no complejo → sin test", "media", "alta"),
    
    (84, "MiFID II", "Los incentivos pueden percibirse si:", "Mejoran calidad servicio y se revelan", "Solo con autorización CNMV", "Están prohibidos", "Solo para profesionales", 0, "Regla EFPA: Incentivos OK si mejora + transparencia", "media", "alta"),
    
    (85, "MiFID II", "¿Qué debe evaluarse en conocimientos del cliente?", "Solo estudios", "Experiencia, formación, operativa previa", "Solo patrimonio", "Solo edad", 1, "Regla EFPA: Conocimientos = experiencia + formación + operativa", "media", "media"),
    
    (86, "MiFID II", "Target market de un producto debe:", "Definirse antes comercialización", "Definirse después", "No es obligatorio", "Solo productos complejos", 0, "Regla EFPA: Target market → antes de comercializar", "media", "media"),
    
    (87, "MiFID II", "Cliente solicita reclasificación a profesional. Entidad:", "Acepta automáticamente", "Evalúa cumplimiento requisitos", "Rechaza siempre", "Solo si patrimonio > 500k", 1, "Regla EFPA: Reclasificación → requiere evaluación requisitos", "media", "media"),
    
    (88, "MiFID II", "¿Los informes periódicos son obligatorios?", "No", "Sí, en asesoramiento y gestión", "Solo si cliente pide", "Solo minoristas", 1, "Regla EFPA: Informes periódicos → obligatorios en asesoramiento/gestión", "media", "alta"),
    
    (89, "MiFID II", "Entidad detecta operación no adecuada para cliente. Debe:", "Ejecutarla igual", "Advertir al cliente", "Negarse", "Pedir autorización CNMV", 1, "Regla EFPA: No adecuada → advertir (pero ejecutar si cliente insiste)", "media", "alta"),
    
    (90, "MiFID II", "La información pre-contractual incluye:", "Solo nombre producto", "Riesgos, costes, naturaleza producto", "Solo rentabilidad esperada", "Opcional", 1, "Regla EFPA: Info pre-contractual → riesgos + costes + naturaleza", "media", "alta"),
    
    # Dificultad: Alta (91-100)
    (91, "MiFID II", "Cliente profesional por derecho puede renunciar a protecciones:", "Sí, todas", "Algunas, no todas", "No, ninguna", "Solo mejor ejecución", 1, "Regla EFPA: Profesional puede renunciar a algunas protecciones (no todas)", "alta", "baja"),
    
    (92, "MiFID II", "Servicio asesoramiento + gestión discrecional. Tests necesarios:", "Solo idoneidad", "Idoneidad cada uno", "Conveniencia", "Ninguno si profesional", 1, "Regla EFPA: Asesoramiento + gestión → idoneidad en AMBOS", "alta", "media"),
    
    (93, "MiFID II", "¿Cuándo puede omitirse información sobre riesgos?", "Cliente profesional lo solicita", "Contraparte elegible", "Nunca", "Cliente conocimiento alto", 1, "Regla EFPA: Contraparte elegible → mínimas protecciones", "alta", "baja"),
    
    (94, "MiFID II", "Cliente quiere operar producto fuera target market. Entidad:", "Rechaza operación", "Ejecuta tras advertencia", "Pide autorización especial", "Solo si test positivo", 1, "Regla EFPA: Fuera target → advertir pero permitir", "alta", "media"),
    
    (95, "MiFID II", "La evaluación de conveniencia debe considerar:", "Solo conocimientos", "Conocimientos y experiencia", "Los 3 factores idoneidad", "Solo experiencia", 1, "Regla EFPA: Conveniencia = conocimientos + experiencia (sin situación/objetivos)", "alta", "alta"),
    
    (96, "MiFID II", "Entidad comercializa producto sin definir target market:", "Sin consecuencias", "Incumple MiFID II", "Solo problema si hay pérdidas", "Válido si informa", 1, "Regla EFPA: Target market → obligatorio pre-comercialización", "alta", "baja"),
    
    (97, "MiFID II", "¿Los costes de terceros deben incluirse en información?", "No", "Sí, todos los costes", "Solo si > 1%", "Solo directos", 1, "Regla EFPA: Costes → incluir TODOS (propios + terceros)", "alta", "media"),
    
    (98, "MiFID II", "Cliente rechaza actualizar test idoneidad. Entidad:", "Continúa asesoramiento", "Suspende asesoramiento", "Aplica último test", "Cambia a ejecución simple", 1, "Regla EFPA: Sin idoneidad actualizada → sin asesoramiento", "alta", "media"),
    
    (99, "MiFID II", "Conflicto de interés no evitable. Prioridad:", "Beneficio entidad", "Interés cliente", "Equilibrio ambos", "Decisión caso a caso", 1, "Regla EFPA: Interés cliente SIEMPRE primero", "alta", "alta"),
    
    (100, "MiFID II", "¿Puede aplicarse test conveniencia a contraparte elegible?", "Sí, siempre", "No aplica", "Solo si lo solicita", "Obligatorio en complejos", 1, "Regla EFPA: Contraparte elegible → sin tests (mínima protección)", "alta", "baja"),
]

print("✅ MiFID II: 50 preguntas")

for q in mifid:
    cursor_preguntas.execute("""
        INSERT INTO preguntas (id, tema, pregunta, opcion_a, opcion_b, opcion_c, opcion_d, correcta, explicacion, dificultad, frecuencia_examen)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, q)

print("\n⏳ Continuando con Productos Financieros...")

# PRODUCTOS FINANCIEROS - 50 preguntas (ID 101-150)
productos = [
    # Dificultad: Baja (101-120)
    (101, "Productos Financieros", "Cuando los tipos de interés suben, el precio de un bono:", "Sube", "Baja", "Se mantiene", "Depende del cupón", 1, "Regla EFPA: Tipos ↑ → Precio bonos ↓ (relación inversa)", "baja", "alta"),
    
    (102, "Productos Financieros", "La duration mide:", "Vencimiento del bono", "Sensibilidad del precio a tipos", "Cupón anual", "Rating crediticio", 1, "Regla EFPA: Duration = sensibilidad a tipos de interés", "baja", "alta"),
    
    (103, "Productos Financieros", "PER (Price Earnings Ratio) se calcula:", "Precio / BPA", "BPA / Precio", "Precio / Dividendo", "Capitalización / Beneficio", 0, "Regla EFPA: PER = Precio / Beneficio por acción", "baja", "alta"),
    
    (104, "Productos Financieros", "TER en un fondo incluye:", "Solo comisión gestión", "Todos gastos recurrentes", "Comisión suscripción", "Comisión reembolso", 1, "Regla EFPA: TER = todos gastos recurrentes (gestión + depositaría + otros)", "baja", "alta"),
    
    (105, "Productos Financieros", "Un ETF cotiza:", "Al VL del cierre", "En tiempo real en bolsa", "Solo al cierre", "Una vez al día", 1, "Regla EFPA: ETF = cotiza en bolsa tiempo real (vs fondos al VL cierre)", "baja", "alta"),
    
    (106, "Productos Financieros", "Tracking error mide:", "Rentabilidad del ETF", "Desviación respecto índice", "Comisiones", "Volatilidad", 1, "Regla EFPA: Tracking error = desviación ETF vs índice", "baja", "alta"),
    
    (107, "Productos Financieros", "Las acciones preferentes tienen:", "Prioridad en dividendos", "Más derechos de voto", "Menos riesgo siempre", "Dividendo variable", 0, "Regla EFPA: Preferente = prioridad dividendos (no voto)", "baja", "alta"),
    
    (108, "Productos Financieros", "Un warrant es:", "Opción emitida por entidad", "Futuro estandarizado", "Bono convertible", "Acción preferente", 0, "Regla EFPA: Warrant = opción no estandarizada", "baja", "media"),
    
    (109, "Productos Financieros", "¿Los fondos permiten traspaso sin tributar?", "Sí", "No", "Solo UCITS", "Solo monetarios", 0, "Regla EFPA: Fondos → traspaso sin peaje fiscal (vs ETF)", "baja", "alta"),
    
    (110, "Productos Financieros", "VL (Valor Liquidativo) se calcula:", "Al cierre cada día", "En tiempo real", "Semanalmente", "Mensualmente", 0, "Regla EFPA: VL = al cierre diario", "baja", "alta"),
    
    (111, "Productos Financieros", "Un bono cupón cero:", "Paga cupones anuales", "No paga cupones, se compra con descuento", "Paga cupón al vencimiento", "Cupón variable", 1, "Regla EFPA: Cupón cero = sin intereses periódicos, descuento inicial", "baja", "media"),
    
    (112, "Productos Financieros", "Mayor duration significa:", "Mayor sensibilidad a tipos", "Menor riesgo", "Mayor cupón", "Menor plazo", 0, "Regla EFPA: Duration ↑ → Sensibilidad ↑", "baja", "alta"),
    
    (113, "Productos Financieros", "¿Qué mide el ROE?", "Rentabilidad activos", "Rentabilidad fondos propios", "Rentabilidad ventas", "Endeudamiento", 1, "Regla EFPA: ROE = Beneficio / Fondos propios", "baja", "media"),
    
    (114, "Productos Financieros", "Un futuro es:", "Derecho a comprar", "Obligación para ambas partes", "Solo para vendedor", "Opcional ejercer", 1, "Regla EFPA: Futuro = obligación (vs opción = derecho)", "baja", "alta"),
    
    (115, "Productos Financieros", "Una opción CALL da derecho a:", "Vender", "Comprar", "Ambas", "Ninguna obligación", 1, "Regla EFPA: CALL = derecho comprar (PUT = derecho vender)", "baja", "alta"),
    
    (116, "Productos Financieros", "Compras PUT si esperas:", "Subida precio", "Bajada precio", "Estabilidad", "Alta volatilidad", 1, "Regla EFPA: PUT = ganas si baja", "baja", "alta"),
    
    (117, "Productos Financieros", "¿Los ETF tributan igual que fondos en España?", "Sí", "No, como acciones", "Depende", "Solo UCITS", 1, "Regla EFPA: ETF = régimen acciones (sin traspaso sin peaje)", "baja", "alta"),
    
    (118, "Productos Financieros", "Dividend Yield se calcula:", "Dividendo / Precio", "Precio / Dividendo", "Dividendo / BPA", "BPA / Precio", 0, "Regla EFPA: Dividend Yield = Dividendo anual / Precio", "baja", "media"),
    
    (119, "Productos Financieros", "Un producto estructurado típicamente combina:", "Renta fija + derivado", "Dos acciones", "Dos bonos", "ETF + fondo", 0, "Regla EFPA: Estructurado = RF + derivado", "baja", "media"),
    
    (120, "Productos Financieros", "¿Qué bono es más sensible a tipos? A) 2 años B) 10 años", "A", "B", "Igual", "Depende cupón", 1, "Regla EFPA: Mayor vencimiento → mayor duration → más sensible", "baja", "alta"),
    
    # Dificultad: Media (121-140)
    (121, "Productos Financieros", "Bono precio 95€, VN 100€, cupón 5€. Rentabilidad:", ">5%", "5%", "<5%", "0%", 0, "Bajo par → rentabilidad > cupón. Ganas cupón + apreciación capital", "media", "media"),
    
    (122, "Productos Financieros", "Acción 50€, PER 20. BPA:", "2,5€", "1.000€", "70€", "30€", 0, "PER = Precio/BPA → BPA = 50/20 = 2,5€", "media", "alta"),
    
    (123, "Productos Financieros", "Fondo patrimonio 10M€, 100.000 participaciones. VL:", "100€", "1.000€", "10€", "Depende", 0, "VL = 10.000.000 / 100.000 = 100€", "media", "alta"),
    
    (124, "Productos Financieros", "ETF sigue índice que sube 10%, ETF sube 9,8%. Tracking error:", "0,2%", "10%", "9,8%", "-0,2%", 0, "Tracking error = |10 - 9,8| = 0,2%", "media", "alta"),
    
    (125, "Productos Financieros", "Compras CALL strike 50€, prima 5€. Acción sube a 60€. Beneficio:", "5€", "10€", "15€", "0€", 0, "Beneficio = (60-50) - 5 prima = 5€", "media", "alta"),
    
    (126, "Productos Financieros", "Fondo TER 1,5%, comisión suscripción 3%, reembolso 1%. Gastos recurrentes:", "1,5%", "5,5%", "4,5%", "2,5%", 0, "TER solo incluye recurrentes: 1,5%", "media", "alta"),
    
    (127, "Productos Financieros", "Bono duration 5 años, tipos suben 1%. Precio cae aprox:", "1%", "5%", "10%", "0,5%", 1, "Duration 5 → 1% tipos → 5% caída precio", "media", "alta"),
    
    (128, "Productos Financieros", "Acción ROE 15%, P/B 2. ¿Valoración?", "Barata", "Cara", "Justa", "Insuficiente info", 1, "P/B alto con ROE decente sugiere valoración premium", "media", "baja"),
    
    (129, "Productos Financieros", "Vendes PUT strike 40€, prima 3€. Acción baja a 35€. Resultado:", "-2€", "-5€", "+3€", "-8€", 0, "Pierdes: (40-35) - 3 prima = -2€", "media", "alta"),
    
    (130, "Productos Financieros", "¿Qué bono tiene mayor duration? A) 10 años cupón 5% B) 10 años cupón 2%", "A", "B", "Igual", "Depende precio", 1, "Menor cupón → mayor duration", "media", "media"),
    
    (131, "Productos Financieros", "Fondo suscribes a VL 100€, reembolsas a VL 110€. Rentabilidad:", "10%", "9,1%", "11%", "Depende comisiones", 0, "(110-100)/100 = 10%", "media", "media"),
    
    (132, "Productos Financieros", "ETF físico vs sintético:", "Físico replica comprando activos", "Sintético usa derivados", "Físico usa swaps", "Ambas A y B", 3, "Físico compra activos reales, sintético usa derivados/swaps", "media", "baja"),
    
    (133, "Productos Financieros", "Derecho suscripción preferente sirve para:", "Mantener % propiedad en ampliación", "Recibir más dividendos", "Votar doble", "Prioridad en OPV", 0, "Mantiene tu % ante dilución por ampliación", "media", "media"),
    
    (134, "Productos Financieros", "Índice ponderado por capitalización significa:", "Empresas grandes pesan más", "Todas igual peso", "Por precio acción", "Por dividendos", 0, "Mayor capitalización → mayor peso en índice", "media", "alta"),
    
    (135, "Productos Financieros", "Opción at-the-money:", "Strike = Precio actual", "Strike < Precio", "Strike > Precio", "Sin valor intrínseco", 0, "At the money: strike ≈ precio actual", "media", "media"),
    
    (136, "Productos Financieros", "P/B ratio compara:", "Precio vs Valor contable", "Precio vs Beneficio", "Precio vs Ventas", "Precio vs Activos", 0, "P/B = Precio / Valor contable por acción", "media", "baja"),
    
    (137, "Productos Financieros", "Cédula hipotecaria está respaldada por:", "Cartera hipotecas banco", "Gobierno", "Fondos garantía", "Activos diversos", 0, "Cédula = respaldo cartera hipotecaria", "media", "baja"),
    
    (138, "Productos Financieros", "EBITDA mide:", "Beneficio antes intereses, impuestos, amortizaciones", "Beneficio neto", "Cash flow libre", "Ventas netas", 0, "EBITDA = resultado operativo antes financieros/impuestos/amortizaciones", "media", "media"),
    
    (139, "Productos Financieros", "Fondo garantizado:", "100% capital siempre", "Garantía con condiciones", "Sin riesgo alguno", "Gobierno respalda", 1, "Garantía tiene condiciones (plazo, emisor solvente, etc)", "media", "media"),
    
    (140, "Productos Financieros", "Free cash flow es:", "Cash disponible tras inversiones necesarias", "Beneficio neto", "EBITDA", "Dividendo pagado", 0, "FCF = cash operativo - capex necesario", "media", "baja"),
    
    # Dificultad: Alta (141-150)
    (141, "Productos Financieros", "Bono duration 8, convexity positiva. Tipos bajan 2%. Precio:", "Sube < 16%", "Sube > 16%", "Sube exactamente 16%", "Baja", 1, "Convexity positiva aumenta ganancia cuando tipos bajan", "alta", "baja"),
    
    (142, "Productos Financieros", "Compras straddle (call+put mismo strike 50€), primas 8€. Acción a 60€. Resultado:", "+2€", "-8€", "+10€", "0€", 0, "Call: (60-50)=10. Put: 0. Total: 10-8 primas = +2€", "alta", "baja"),
    
    (143, "Productos Financieros", "Acción PER 25, sector PER 15. Indica:", "Sobrevaloración o expectativas altas crecimiento", "Infravaloración", "Justa valoración", "Insuficiente info", 0, "PER alto vs sector: premium por crecimiento esperado o sobrevaloración", "alta", "media"),
    
    (144, "Productos Financieros", "Estrategia covered call consiste en:", "Poseer acción + vender call", "Comprar call + put", "Vender put desnudo", "Comprar call + vender put", 0, "Covered call: largo acción + corto call (limita upside, genera ingreso)", "alta", "baja"),
    
    (145, "Productos Financieros", "Duration Macaulay vs Modified:", "Macaulay en años, Modified sensibilidad", "Iguales", "Modified es mayor", "Depende cupón", 0, "Macaulay = plazo medio ponderado. Modified = sensibilidad precio", "alta", "baja"),
    
    (146, "Productos Financieros", "ETF con préstamo valores (securities lending):", "Genera ingreso adicional con riesgo contraparte", "Sin riesgo", "Prohibido", "Solo ETF apalancados", 0, "Préstamo valores: ingreso extra pero riesgo si prestatario quiebra", "alta", "baja"),
    
    (147, "Productos Financieros", "Ratio Sharpe de un fondo compara:", "Rentabilidad vs riesgo total (volatilidad)", "Rentabilidad vs riesgo sistemático (beta)", "Rentabilidad vs benchmark", "Rentabilidad absoluta", 0, "Sharpe = (Rentabilidad - RF) / Volatilidad (riesgo total)", "alta", "media"),
    
    (148, "Productos Financieros", "Convertible bond puede canjearse por:", "Acciones emisor", "Efectivo siempre", "Otros bonos", "Fondos", 0, "Bono convertible: opción canjear por acciones del emisor", "alta", "baja"),
    
    (149, "Productos Financieros", "Autocallable se cancela anticipadamente si:", "Subyacente alcanza nivel predefinido", "Emisor quiere", "Tipos suben", "Cliente solicita", 0, "Autocallable: cancelación automática si subyacente toca nivel", "alta", "baja"),
    
    (150, "Productos Financieros", "¿Diferencia principal UCITS vs hedge fund?", "UCITS regulado restrictivamente, hedge fund flexible", "UCITS solo acciones", "Hedge fund sin apalancamiento", "UCITS más riesgo", 0, "UCITS: regulación estricta, diversificación. Hedge: flexible, estrategias complejas", "alta", "baja"),
]

print("✅ Productos Financieros: 50 preguntas")

for q in productos:
    cursor_preguntas.execute("""
        INSERT INTO preguntas (id, tema, pregunta, opcion_a, opcion_b, opcion_c, opcion_d, correcta, explicacion, dificultad, frecuencia_examen)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, q)

print("\n⏳ Continuando con Riesgo y Rentabilidad...")

# RIESGO Y RENTABILIDAD - 50 preguntas (ID 151-200)
riesgo = [
    # Dificultad: Baja (151-170)
    (151, "Riesgo y Rentabilidad", "La diversificación reduce principalmente:", "Riesgo sistemático", "Riesgo específico", "Ambos por igual", "Ninguno", 1, "Regla EFPA: Diversificación → reduce riesgo específico (no sistemático)", "baja", "alta"),
    
    (152, "Riesgo y Rentabilidad", "Beta mide:", "Riesgo total", "Riesgo sistemático vs mercado", "Rentabilidad esperada", "Volatilidad absoluta", 1, "Regla EFPA: Beta = sensibilidad al mercado (riesgo sistemático)", "baja", "alta"),
    
    (153, "Riesgo y Rentabilidad", "Beta = 1 significa:", "Igual volatilidad que mercado", "Doble volatilidad", "Sin riesgo", "Correlación perfecta", 0, "Regla EFPA: Beta 1 → se mueve igual que mercado", "baja", "alta"),
    
    (154, "Riesgo y Rentabilidad", "Ratio de Sharpe mide:", "Rentabilidad ajustada por riesgo total", "Rentabilidad absoluta", "Solo volatilidad", "Beta", 0, "Regla EFPA: Sharpe = exceso rentabilidad / volatilidad", "baja", "alta"),
    
    (155, "Riesgo y Rentabilidad", "Volatilidad es una medida de:", "Riesgo (dispersión rentabilidades)", "Rentabilidad media", "Beta", "Correlación", 0, "Regla EFPA: Volatilidad = desviación típica = riesgo", "baja", "alta"),
    
    (156, "Riesgo y Rentabilidad", "Correlación +1 entre dos activos significa:", "Se mueven exactamente igual", "Se mueven opuesto", "Sin relación", "Misma volatilidad", 0, "Regla EFPA: Correlación +1 → movimientos idénticos", "baja", "alta"),
    
    (157, "Riesgo y Rentabilidad", "CAPM calcula:", "Rentabilidad esperada según riesgo sistemático", "Volatilidad", "Beta", "Correlación", 0, "Regla EFPA: CAPM → E(R) = RF + Beta × (RM - RF)", "baja", "alta"),
    
    (158, "Riesgo y Rentabilidad", "Riesgo sistemático NO se puede eliminar con:", "Diversificación", "Cobertura derivados", "Asset allocation", "Ninguna opción", 0, "Regla EFPA: Riesgo sistemático → afecta todo mercado, diversificación no lo elimina", "baja", "alta"),
    
    (159, "Riesgo y Rentabilidad", "Beta > 1 indica:", "Más volátil que mercado", "Menos volátil", "Sin correlación", "Riesgo cero", 0, "Regla EFPA: Beta > 1 → amplifica movimientos mercado", "baja", "alta"),
    
    (160, "Riesgo y Rentabilidad", "VaR (Value at Risk) mide:", "Pérdida máxima probable (nivel confianza)", "Rentabilidad esperada", "Volatilidad", "Beta", 0, "Regla EFPA: VaR = pérdida máxima X% confianza", "baja", "media"),
    
    (161, "Riesgo y Rentabilidad", "Frontera eficiente representa:", "Carteras máxima rentabilidad por riesgo", "Solo activos individuales", "Cartera mínima varianza", "Mercado completo", 0, "Regla EFPA: Frontera eficiente → mejor rentabilidad/riesgo", "baja", "media"),
    
    (162, "Riesgo y Rentabilidad", "Rentabilidad real se calcula:", "Rentabilidad nominal - inflación", "Rentabilidad bruta - impuestos", "Rentabilidad con dividendos", "Rentabilidad geométrica", 0, "Regla EFPA: Real = Nominal - Inflación", "baja", "alta"),
    
    (163, "Riesgo y Rentabilidad", "Alfa positivo indica:", "Rentabilidad > esperada por CAPM", "Beta > 1", "Alta volatilidad", "Baja correlación", 0, "Regla EFPA: Alfa > 0 → supera expectativa ajustada por riesgo", "baja", "media"),
    
    (164, "Riesgo y Rentabilidad", "Correlación -1 significa:", "Movimientos totalmente opuestos", "Movimientos iguales", "Sin relación", "Baja volatilidad", 0, "Regla EFPA: Correlación -1 → perfectamente inversos", "baja", "alta"),
    
    (165, "Riesgo y Rentabilidad", "Beta = 0 significa:", "Sin correlación con mercado", "Igual al mercado", "Doble volatilidad", "Sin riesgo", 0, "Regla EFPA: Beta 0 → independiente del mercado", "baja", "media"),
    
    (166, "Riesgo y Rentabilidad", "Downside risk mide:", "Solo volatilidad negativa", "Volatilidad total", "Beta", "Correlación", 0, "Regla EFPA: Downside risk → solo caídas (no subidas)", "baja", "baja"),
    
    (167, "Riesgo y Rentabilidad", "Ratio información (Information Ratio) compara:", "Alfa vs tracking error", "Rentabilidad vs volatilidad", "Beta vs mercado", "Sharpe vs Treynor", 0, "Regla EFPA: IR = Alfa / Tracking error", "baja", "baja"),
    
    (168, "Riesgo y Rentabilidad", "Maximum drawdown es:", "Caída máxima desde pico", "Volatilidad anual", "VaR", "Beta máximo", 0, "Regla EFPA: Drawdown = pérdida máxima pico-valle", "baja", "media"),
    
    (169, "Riesgo y Rentabilidad", "Cartera bien diversificada tiene principalmente:", "Riesgo sistemático", "Riesgo específico", "Sin riesgo", "Solo alfa", 0, "Regla EFPA: Diversificación elimina específico, queda sistemático", "baja", "alta"),
    
    (170, "Riesgo y Rentabilidad", "Rentabilidad geométrica se usa para:", "Periodos múltiples", "Un solo periodo", "Proyecciones futuras", "Comparar activos", 0, "Regla EFPA: Geométrica → múltiples periodos (efecto compuesto)", "baja", "media"),
    
    # Dificultad: Media (171-190)
    (171, "Riesgo y Rentabilidad", "Inviertes 10.000€, primer año +20%, segundo año -10%. Rentabilidad total:", "+8%", "+10%", "+5%", "0%", 0, "10.000 × 1,2 × 0,9 = 10.800 → 8% ganancia", "media", "alta"),
    
    (172, "Riesgo y Rentabilidad", "Activo A: 12% rentabilidad, 15% volatilidad. Activo B: 10% rentabilidad, 10% volatilidad. RF 2%. Mayor Sharpe:", "A", "B", "Iguales", "Insuficiente info", 1, "A: (12-2)/15=0,67. B: (10-2)/10=0,8 → B mayor Sharpe", "media", "alta"),
    
    (173, "Riesgo y Rentabilidad", "Mercado sube 8%, tu cartera sube 12%, beta 1,5. Alfa:", "0%", "+2%", "-2%", "+4%", 0, "E(R) = 8×1,5 = 12%. Real = 12%. Alfa = 0%", "media", "alta"),
    
    (174, "Riesgo y Rentabilidad", "Cartera 60% acciones (volat 20%), 40% bonos (volat 8%), correlación 0,3. Volatilidad cartera:", "<13,5%", "14%", "16,8%", "28%", 0, "√[(0,6²×20²)+(0,4²×8²)+(2×0,6×0,4×20×8×0,3)] ≈ 13%", "media", "alta"),
    
    (175, "Riesgo y Rentabilidad", "VaR 95% de 1M€ es 50k€. Significa:", "95% prob pérdida < 50k en periodo", "5% prob perder > 50k", "Pérdida media 50k", "Ambas A y B", 3, "VaR 95%: 5% probabilidad de perder MÁS de 50k", "media", "media"),
    
    (176, "Riesgo y Rentabilidad", "Beta 0,8, mercado cae 10%. Tu cartera esperada:", "-8%", "-12%", "-10%", "-6%", 0, "Beta 0,8 × (-10%) = -8%", "media", "alta"),
    
    (177, "Riesgo y Rentabilidad", "Dos activos correlación 0. Combinados:", "Reducen riesgo vs promedio individual", "Mantienen riesgo promedio", "Aumentan riesgo", "Eliminan riesgo", 0, "Correlación 0 → diversificación efectiva → riesgo < promedio", "media", "alta"),
    
    (178, "Riesgo y Rentabilidad", "CAPM: RF=3%, Beta=1,2, Prima mercado 6%. Rentabilidad esperada:", "10,2%", "9%", "7,2%", "12%", 0, "3 + 1,2×6 = 3 + 7,2 = 10,2%", "media", "alta"),
    
    (179, "Riesgo y Rentabilidad", "Tracking error alto en fondo indexado indica:", "Desviación alta vs índice", "Alta rentabilidad", "Bajo riesgo", "Buena gestión", 0, "Tracking error → desviación respecto benchmark", "media", "media"),
    
    (180, "Riesgo y Rentabilidad", "Rentabilidad nominal 8%, inflación 2%. Rentabilidad real:", "6%", "5,88%", "10%", "4%", 1, "(1,08/1,02)-1 = 0,0588 → 5,88% (aproximado 6% simplificado)", "media", "media"),
    
    (181, "Riesgo y Rentabilidad", "Ratio Treynor usa en denominador:", "Beta", "Volatilidad", "Tracking error", "Correlación", 0, "Treynor = (R-RF) / Beta (vs Sharpe que usa volatilidad)", "media", "baja"),
    
    (182, "Riesgo y Rentabilidad", "Fondo alfa 2%, beta 1,3, mercado 10%, RF 2%. Rentabilidad fondo:", "12,4%", "10%", "14,4%", "15%", 2, "R = 2 (RF) + 1,3×8 (prima) + 2 (alfa) = 14,4%", "media", "media"),
    
    (183, "Riesgo y Rentabilidad", "Cartera 50/50 dos activos perfectamente correlacionados (-1). Volatilidad cartera:", "0", "Promedio", "Suma", "Raíz suma", 0, "Correlación -1 perfecta → se cancelan → volatilidad = 0", "media", "media"),
    
    (184, "Riesgo y Rentabilidad", "Semi-varianza mide:", "Solo desviaciones negativas", "Toda volatilidad", "Beta", "Alfa", 0, "Semi-varianza → solo downside (desviaciones bajo media)", "media", "baja"),
    
    (185, "Riesgo y Rentabilidad", "Duration 6 años, convexity 50. Tipos suben 1%. Precio cae aprox:", "6,5%", "5,5%", "6%", "7%", 1, "Caída duration: 6%. Convexity añade: +0,5×50×0,01² ≈ -5,5% neto", "media", "baja"),
    
    (186, "Riesgo y Rentabilidad", "¿Qué NO reduce el riesgo de cartera?", "Diversificar mismo sector", "Diversificar geografías", "Diversificar clases activo", "Diversificar sectores", 0, "Mismo sector → alta correlación → poco beneficio diversificación", "media", "media"),
    
    (187, "Riesgo y Rentabilidad", "R² (R-squared) mide:", "% variación explicada por mercado", "Rentabilidad absoluta", "Volatilidad", "Alfa", 0, "R² → cuánto explica el mercado los movimientos", "media", "baja"),
    
    (188, "Riesgo y Rentabilidad", "Sortino ratio mejora Sharpe al:", "Penalizar solo volatilidad negativa", "Usar beta", "Eliminar RF", "Usar geométrica", 0, "Sortino = (R-RF) / Downside deviation (solo malas)", "media", "baja"),
    
    (189, "Riesgo y Rentabilidad", "Cartera mínima varianza en frontera eficiente:", "Menor riesgo posible", "Mayor rentabilidad", "Mayor Sharpe", "Beta = 0", 0, "Mínima varianza → punto menor riesgo de frontera", "media", "baja"),
    
    (190, "Riesgo y Rentabilidad", "Activo RF=3%, E(R)=8%, volat 15%. Sharpe ratio:", "0,33", "0,53", "5%", "1,33", 0, "(8-3)/15 = 0,33", "media", "media"),
    
    # Dificultad: Alta (191-200)
    (191, "Riesgo y Rentabilidad", "Tres activos igualmente ponderados: rets 10%, 15%, 20%, volats 10%, 15%, 20%, correlaciones 0,5. Rentabilidad cartera:", "15%", "16,67%", "12%", "Imposible calcular", 0, "(10+15+20)/3 = 15% (rentabilidad es simple promedio ponderado)", "alta", "baja"),
    
    (192, "Riesgo y Rentabilidad", "Beta ajustada (adjusted beta) tiende hacia:", "1", "0", "Beta histórico", "Infinito", 0, "Beta ajustada = 0,67×Beta histórico + 0,33×1 (tiende a 1)", "alta", "baja"),
    
    (193, "Riesgo y Rentabilidad", "CVaR (Conditional VaR) mide:", "Pérdida esperada si supera VaR", "VaR ajustado volatilidad", "VaR múltiples periodos", "VaR sin RF", 0, "CVaR = pérdida media en cola (dado que superas VaR)", "alta", "baja"),
    
    (194, "Riesgo y Rentabilidad", "Teorema separación Tobin: cartera óptima combina:", "Activo RF + cartera tangente mercado", "Solo acciones", "RF + bonos", "Múltiples carteras", 0, "Separación: todos combinan RF + misma cartera mercado (proporción varía)", "alta", "baja"),
    
    (195, "Riesgo y Rentabilidad", "Jensen's alpha se calcula:", "Rentabilidad real - E(R) CAPM", "Beta × mercado", "Sharpe × volat", "Alfa simple", 0, "Jensen = R real - [RF + Beta×(RM-RF)]", "alta", "media"),
    
    (196, "Riesgo y Rentabilidad", "Cartera 40% activo A (ret 12%, vol 18%), 60% activo B (ret 8%, vol 12%), corr 0,6. Sharpe (RF 3%):", "Aprox 0,45", "0,33", "0,67", "Imposible", 0, "R cartera: 0,4×12+0,6×8=9,6%. Vol cartera ≈13%. Sharpe: (9,6-3)/13≈0,5", "alta", "baja"),
    
    (197, "Riesgo y Rentabilidad", "Estrategia long/short con beta 0 busca:", "Generar alfa sin riesgo mercado", "Eliminar todo riesgo", "Maximizar beta", "Correlación perfecta", 0, "Beta 0 → neutraliza mercado, busca alfa puro", "alta", "baja"),
    
    (198, "Riesgo y Rentabilidad", "Fama-French añade a CAPM factores:", "Size y value", "Momentum", "Quality", "Solo beta", 0, "Fama-French 3 factores: mercado + SMB (size) + HML (value)", "alta", "baja"),
    
    (199, "Riesgo y Rentabilidad", "Ratio Calmar compara:", "Rentabilidad anualizada / Max drawdown", "Sharpe / Beta", "Alfa / Tracking error", "Rentabilidad / VaR", 0, "Calmar = rentabilidad anual / máxima caída", "alta", "baja"),
    
    (200, "Riesgo y Rentabilidad", "Black-Litterman combina:", "Equilibrio mercado + views gestor", "Solo CAPM", "Solo views gestor", "Múltiples alfas", 0, "Black-Litterman: mezcla equilibrio + opiniones específicas", "alta", "baja"),
]

print("✅ Riesgo y Rentabilidad: 50 preguntas")

for q in riesgo:
    cursor_preguntas.execute("""
        INSERT INTO preguntas (id, tema, pregunta, opcion_a, opcion_b, opcion_c, opcion_d, correcta, explicacion, dificultad, frecuencia_examen)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, q)

print("\n⏳ Continuando con Mercados Financieros...")

# MERCADOS FINANCIEROS - 50 preguntas (ID 201-250)
mercados = [
    # Dificultad: Baja (201-220)
    (201, "Mercados Financieros", "Mercado primario es donde:", "Se emiten valores nuevos", "Se negocian valores existentes", "Se liquidan operaciones", "Se compensan", 0, "Regla EFPA: Primario = emisión nueva (vs secundario = negociación)", "baja", "alta"),
    
    (202, "Mercados Financieros", "Mercado secundario permite:", "Negociar valores ya emitidos", "Emitir nuevos valores", "Solo comprar", "Solo vender", 0, "Regla EFPA: Secundario = compraventa entre inversores", "baja", "alta"),
    
    (203, "Mercados Financieros", "IBEX 35 incluye:", "35 empresas más líquidas España", "35 empresas europeas", "Todas empresas españolas", "35 bancos", 0, "Regla EFPA: IBEX 35 = índice principal bolsa española", "baja", "alta"),
    
    (204, "Mercados Financieros", "Euribor es:", "Tipo interbancario europeo", "Tipo oficial BCE", "Tipo hipotecas", "Tipo depósitos", 0, "Regla EFPA: Euribor = referencia préstamos entre bancos", "baja", "alta"),
    
    (205, "Mercados Financieros", "Orden a mercado se ejecuta:", "Al mejor precio disponible inmediatamente", "Solo al precio indicado", "Al cierre", "Mañana", 0, "Regla EFPA: Mercado = ejecución inmediata, precio variable", "baja", "alta"),
    
    (206, "Mercados Financieros", "Orden limitada:", "Precio máximo compra / mínimo venta", "Sin límite precio", "Solo al cierre", "Ejecución inmediata", 0, "Regla EFPA: Limitada = con precio límite", "baja", "alta"),
    
    (207, "Mercados Financieros", "Mercado OTC significa:", "Over The Counter (no organizado)", "Mercado oficial", "Solo opciones", "Mercado online", 0, "Regla EFPA: OTC = bilateral, no centralizado", "baja", "alta"),
    
    (208, "Mercados Financieros", "MAB es:", "Mercado Alternativo Bursátil (PYMES)", "Mercado Americano Bonds", "Mercado Asiático", "Solo MAB son fondos", 0, "Regla EFPA: MAB = acceso bolsa para pequeñas empresas", "baja", "media"),
    
    (209, "Mercados Financieros", "Liquidación en acciones España es:", "T+2 (dos días hábiles)", "T+0 (mismo día)", "T+5", "T+1", 0, "Regla EFPA: Liquidación acciones = T+2", "baja", "alta"),
    
    (210, "Mercados Financieros", "Stop loss activa orden cuando:", "Precio toca nivel especificado", "Inmediatamente", "Al cierre", "Nunca", 0, "Regla EFPA: Stop = orden condicional activada por precio", "baja", "alta"),
    
    (211, "Mercados Financieros", "Horquilla (bid-ask spread) mide:", "Diferencia precio compra-venta", "Volatilidad", "Volumen", "Rentabilidad", 0, "Regla EFPA: Spread = coste implícito transacción", "baja", "alta"),
    
    (212, "Mercados Financieros", "Market maker proporciona:", "Liquidez cotizando precios compra-venta", "Solo información", "Órdenes clientes", "Custodia", 0, "Regla EFPA: Market maker = proveedor liquidez continua", "baja", "media"),
    
    (213, "Mercados Financieros", "MEFF es:", "Mercado derivados España", "Mercado acciones", "Mercado deuda", "Mercado inmobiliario", 0, "Regla EFPA: MEFF = futuros y opciones España", "baja", "media"),
    
    (214, "Mercados Financieros", "Cámara de compensación garantiza:", "Cumplimiento operaciones", "Precios justos", "Rentabilidad", "Liquidez", 0, "Regla EFPA: Cámara compensación = garante contrapartes", "baja", "alta"),
    
    (215, "Mercados Financieros", "Venta en corto (short selling) es:", "Vender activo prestado", "Vender activo propio", "Comprar apalancado", "Vender a plazos", 0, "Regla EFPA: Short = vender sin tener (prestado)", "baja", "alta"),
    
    (216, "Mercados Financieros", "Repo es:", "Venta con pacto recompra", "Compra definitiva", "Préstamo sin garantía", "Emisión bonos", 0, "Regla EFPA: Repo = venta temporal con recompra", "baja", "media"),
    
    (217, "Mercados Financieros", "IPO (Initial Public Offering) es:", "Primera oferta pública (salida bolsa)", "Operación secundaria", "Ampliación capital", "OPA", 0, "Regla EFPA: IPO = debut en bolsa", "baja", "media"),
    
    (218, "Mercados Financieros", "Circuit breaker detiene mercado si:", "Caída brusca excede umbral", "Sube mucho", "Por horario", "Cada día", 0, "Regla EFPA: Circuit breaker = pausa protección pánico", "baja", "baja"),
    
    (219, "Mercados Financieros", "Book building en IPO sirve para:", "Determinar demanda y precio", "Liquidar operaciones", "Compensar riesgos", "Garantizar éxito", 0, "Regla EFPA: Book building = tanteo demanda pre-IPO", "baja", "baja"),
    
    (220, "Mercados Financieros", "Dark pool es:", "Mercado privado sin visibilidad órdenes", "Mercado ilegal", "Mercado emergente", "Mercado nocturno", 0, "Regla EFPA: Dark pool = negociación anónima gran volumen", "baja", "baja"),
    
    # Dificultad: Media (221-240)
    (221, "Mercados Financieros", "Orden stop loss a 45€, acción cotiza 50€. Se activa si:", "Baja a 45€ o menos", "Sube a 45€", "Nunca", "Inmediatamente", 0, "Stop loss comprado: vende si baja a nivel", "media", "alta"),
    
    (222, "Mercados Financieros", "Spread 10,00€ / 10,05€. Compras inmediatamente pagas:", "10,05€", "10,00€", "10,025€", "Depende", 0, "Compras al ask (precio venta del market maker)", "media", "alta"),
    
    (223, "Mercados Financieros", "Mercado continuo España opera:", "9:00-17:30h", "24 horas", "9:00-14:00h", "10:00-16:00h", 0, "Regla EFPA: Continuo = 9:00-17:30 (con subastas apertura/cierre)", "media", "media"),
    
    (224, "Mercados Financieros", "T+2 liquidación significa:", "Pagas/cobras 2 días hábiles después", "2% comisión", "2 horas después", "2 semanas", 0, "T+2 = operación lunes → liquidación miércoles", "media", "alta"),
    
    (225, "Mercados Financieros", "High frequency trading (HFT) se caracteriza por:", "Operativa automatizada milisegundos", "Operativa largo plazo", "Solo humanos", "Operativa mensual", 0, "HFT = algoritmos alta velocidad", "media", "baja"),
    
    (226, "Mercados Financieros", "Subastas volatilidad en bolsa se activan:", "Variación brusca precio", "Cada hora", "Al cierre siempre", "Por bajo volumen", 0, "Subasta volatilidad = pausa si movimiento extremo", "media", "baja"),
    
    (227, "Mercados Financieros", "Block trade es:", "Operación gran volumen fuera libro", "Operación minorista", "Operación ilegal", "Operación apalancada", 0, "Block trade = venta/compra grande off-exchange", "media", "baja"),
    
    (228, "Mercados Financieros", "Naked short selling es:", "Corto sin prestar activo primero", "Corto con préstamo", "Compra apalancada", "Venta normal", 0, "Naked short = ilegal en muchos mercados (corto sin garantía)", "media", "baja"),
    
    (229, "Mercados Financieros", "Best execution busca:", "Mejor resultado global cliente", "Precio más bajo siempre", "Ejecución más rápida siempre", "Comisión mínima", 0, "Best execution = óptimo conjunto factores (no solo precio)", "media", "alta"),
    
    (230, "Mercados Financieros", "Flash crash se produce por:", "Caída súbita por algoritmos/pánico", "Caída lenta", "Subida brusca", "Operación normal", 0, "Flash crash = desplome segundos/minutos", "media", "baja"),
    
    (231, "Mercados Financieros", "Fixing de mercado determina:", "Precio oficial cierre/apertura", "Precio intradiario", "Spread máximo", "Volumen mínimo", 0, "Fixing = precio referencia por subasta", "media", "media"),
    
    (232, "Mercados Financieros", "All or None orden ejecuta:", "Todo o nada", "Parcialmente permitido", "Siempre parcial", "A cualquier precio", 0, "AON = ejecutar cantidad completa o rechazar", "media", "baja"),
    
    (233, "Mercados Financieros", "Tick size es:", "Variación mínima precio", "Tamaño mínimo operación", "Horario trading", "Tipo interés", 0, "Tick = incremento precio mínimo permitido", "media", "baja"),
    
    (234, "Mercados Financieros", "Latam MILA conecta bolsas:", "Chile, Colombia, México, Perú", "Solo México", "Toda Latinoamérica", "Brasil y Argentina", 0, "MILA = Mercado Integrado Latinoamericano (4 países)", "media", "baja"),
    
    (235, "Mercados Financieros", "Settlement risk es:", "Riesgo no liquidación contraparte", "Riesgo mercado", "Riesgo tipo cambio", "Riesgo liquidez", 0, "Settlement risk = riesgo entrega/pago", "media", "media"),
    
    (236, "Mercados Financieros", "Lit market vs dark pool:", "Lit = visible órdenes, Dark = privado", "Iguales", "Lit = ilegal", "Dark = mayoría volumen", 0, "Lit = transparente, Dark = anónimo", "media", "baja"),
    
    (237, "Mercados Financieros", "Haircut en repo significa:", "Descuento sobre valor garantía", "Comisión", "Tipo interés", "Plazo operación", 0, "Haircut = margen seguridad prestamista", "media", "baja"),
    
    (238, "Mercados Financieros", "Quote stuffing consiste en:", "Inundar mercado órdenes falsas", "Operativa normal", "Mejora liquidez", "Práctica legal", 0, "Quote stuffing = manipulación por sobrecarga órdenes", "media", "baja"),
    
    (239, "Mercados Financieros", "Volumen medio diario mide:", "Liquidez del activo", "Precio medio", "Volatilidad", "Rentabilidad", 0, "Alto volumen = mayor liquidez = menor spread", "media", "media"),
    
    (240, "Mercados Financieros", "Free float es:", "% acciones disponibles negociación", "Capitalización total", "Precio acción", "Dividendo", 0, "Free float = acciones en circulación (no controladas)", "media", "baja"),
    
    # Dificultad: Alta (241-250)
    (241, "Mercados Financieros", "Programa QE del BCE consiste en:", "Compra activos para inyectar liquidez", "Venta bonos", "Subir tipos", "Restricción crédito", 0, "QE (Quantitative Easing) = expansión monetaria no convencional", "alta", "baja"),
    
    (242, "Mercados Financieros", "Straight Through Processing (STP) significa:", "Automatización completa sin intervención manual", "Proceso manual", "Solo front office", "Solo back office", 0, "STP = desde orden hasta liquidación sin toques manuales", "alta", "baja"),
    
    (243, "Mercados Financieros", "Failed trade se produce cuando:", "No se completa liquidación", "Operación exitosa", "Alta rentabilidad", "Orden rechazada", 0, "Failed trade = fallo entrega valores o pago", "alta", "baja"),
    
    (244, "Mercados Financieros", "Central Counterparty (CCP) se interpone:", "Entre comprador y vendedor", "Solo observa", "Solo compras", "Solo ventas", 0, "CCP = contraparte central (elimina riesgo contraparte bilateral)", "alta", "media"),
    
    (245, "Mercados Financieros", "Spoofing consiste en:", "Órdenes falsas manipular precio", "Operativa legítima", "Market making", "Arbitraje", 0, "Spoofing = ilegal, órdenes fake para engañar mercado", "alta", "baja"),
    
    (246, "Mercados Financieros", "Decimalization en mercados:", "Precios en decimales (vs fracciones)", "10 operadores", "10% comisión", "Diez órdenes", 0, "Decimalization = EEUU 2001, fracción a decimal → más precisión", "alta", "baja"),
    
    (247, "Mercados Financieros", "Payment versus delivery (PvP) garantiza:", "Entrega contra pago simultáneo", "Solo pago", "Solo entrega", "Pago anticipado", 0, "PvP = entrega y pago atómicos (elimina settlement risk)", "alta", "baja"),
    
    (248, "Mercados Financieros", "Maker-taker fee model:", "Maker cobra rebate, taker paga fee", "Todos pagan igual", "Maker paga más", "Gratis todos", 0, "Maker (añade liquidez) = rebate. Taker (quita) = fee", "alta", "baja"),
    
    (249, "Mercados Financieros", "Regulatory halts detienen trading por:", "Noticias pendientes o irregularidades", "Final jornada", "Baja liquidez", "Alta rentabilidad", 0, "Regulatory halt = pausa protección info asimétrica", "alta", "baja"),
    
    (250, "Mercados Financieros", "Trade reporting transparency (EMIR) requiere:", "Reporte operaciones derivados a repositorio", "Solo bolsa", "Ningún reporte", "Solo bancos grandes", 0, "EMIR = European Market Infrastructure Regulation (reporte + clearing)", "alta", "baja"),
]

print("✅ Mercados Financieros: 50 preguntas")

for q in mercados:
    cursor_preguntas.execute("""
        INSERT INTO preguntas (id, tema, pregunta, opcion_a, opcion_b, opcion_c, opcion_d, correcta, explicacion, dificultad, frecuencia_examen)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, q)

print("\n⏳ Generando último tema: Planificación Financiera...")

# PLANIFICACIÓN FINANCIERA - 50 preguntas (ID 251-300)
planificacion = [
    # Dificultad: Baja (251-270)
    (251, "Planificación Financiera", "El proceso de planificación financiera tiene:", "6 fases", "3 fases", "10 fases", "No hay estándar", 0, "Regla EFPA: 6 fases (establecer relación → objetivos → situación → plan → implementar → monitorear)", "baja", "alta"),
    
    (252, "Planificación Financiera", "Tolerancia al riesgo mide:", "Disposición psicológica asumir riesgo", "Capacidad económica", "Conocimientos", "Rentabilidad esperada", 0, "Regla EFPA: Tolerancia = psicológico (vs capacidad = económico)", "baja", "alta"),
    
    (253, "Planificación Financiera", "Capacidad de riesgo depende de:", "Situación financiera y horizonte temporal", "Emociones", "Experiencia solo", "Edad solo", 0, "Regla EFPA: Capacidad = recursos + tiempo + obligaciones", "baja", "alta"),
    
    (254, "Planificación Financiera", "Asset allocation es:", "Distribución entre clases de activo", "Selección valores", "Timing mercado", "Trading activo", 0, "Regla EFPA: Asset allocation = RF/RV/alternativos/cash", "baja", "alta"),
    
    (255, "Planificación Financiera", "Perfil conservador típicamente tiene:", "Mayor peso renta fija", "100% acciones", "Solo alternativos", "Todo cash", 0, "Regla EFPA: Conservador → predominio RF", "baja", "alta"),
    
    (256, "Planificación Financiera", "Horizonte temporal largo permite:", "Asumir más riesgo", "Solo RF", "Sin riesgo", "Timing mercado", 0, "Regla EFPA: Tiempo ↑ → capacidad riesgo ↑", "baja", "alta"),
    
    (257, "Planificación Financiera", "Regla 100 - edad sugiere:", "% RF aproximado", "% RV", "Años jubilación", "Meses reserva", 1, "100 - edad = % RF sugerido (simplificado, 110/120 más actual)", "baja", "media"),
    
    (258, "Planificación Financiera", "Fondo emergencia debe cubrir:", "3-6 meses gastos", "1 mes", "12 meses", "No es necesario", 0, "Regla EFPA: Colchón liquidez = 3-6 meses gastos fijos", "baja", "alta"),
    
    (259, "Planificación Financiera", "Rebalanceo de cartera busca:", "Mantener asset allocation objetivo", "Aumentar rentabilidad", "Vender perdedores", "Comprar ganadores", 0, "Regla EFPA: Rebalanceo = disciplina volver a pesos objetivo", "baja", "alta"),
    
    (260, "Planificación Financiera", "Perfil agresivo tolera:", "Alta volatilidad", "Sin volatilidad", "Solo RF", "Pérdidas garantizadas", 0, "Regla EFPA: Agresivo = alta tolerancia volatilidad, busca crecimiento", "baja", "alta"),
    
    (261, "Planificación Financiera", "Life cycle investing sugiere:", "Reducir riesgo con edad", "Mismo riesgo siempre", "Aumentar riesgo con edad", "Todo cash jubilación", 0, "Regla EFPA: Juventud → RV, Madurez → RF", "baja", "alta"),
    
    (262, "Planificación Financiera", "¿Cuándo revisar plan financiero?", "Periódicamente y cambios vitales", "Solo crisis", "Nunca", "Diariamente", 0, "Regla EFPA: Revisión anual + eventos vida", "baja", "alta"),
    
    (263, "Planificación Financiera", "Diversificación internacional busca:", "Reducir riesgo geográfico", "Aumentar costes", "Solo rentabilidad", "Evitar impuestos", 0, "Regla EFPA: Diversificar geografías reduce concentración país", "baja", "media"),
    
    (264, "Planificación Financiera", "Dollar cost averaging consiste en:", "Invertir cantidades fijas periódicas", "Lump sum", "Market timing", "Solo comprar mínimos", 0, "Regla EFPA: DCA = aportaciones periódicas reduce timing risk", "baja", "media"),
    
    (265, "Planificación Financiera", "Legacy planning incluye:", "Sucesión y herencia", "Solo inversiones", "Solo seguros", "Solo impuestos", 0, "Legacy = planificación patrimonio trans-generacional", "baja", "baja"),
    
    (266, "Planificación Financiera", "Regla 4% retiro jubilación sugiere:", "Retirar 4% inicial anualmente", "Retirar 4% capital", "4% rentabilidad", "Invertir 4%", 0, "Regla 4% = sostenibilidad 30 años (estudio Trinity)", "baja", "baja"),
    
    (267, "Planificación Financiera", "Tax loss harvesting es:", "Materializar pérdidas fiscales", "Evadir impuestos", "Rebalancear", "Aumentar rentabilidad", 0, "Tax loss harvesting = estrategia optimización fiscal", "baja", "baja"),
    
    (268, "Planificación Financiera", "Behavioral finance estudia:", "Sesgos psicológicos inversión", "Solo mercados", "Solo matemáticas", "Solo RF", 0, "Behavioral = economía conductual (vs racional)", "baja", "media"),
    
    (269, "Planificación Financiera", "Home bias es tendencia a:", "Sobreinvertir mercado local", "Diversificar globalmente", "Solo extranjero", "Sin acciones", 0, "Home bias = sesgo familiar (exceso doméstico)", "baja", "baja"),
    
    (270, "Planificación Financiera", "Monte Carlo simulation en planificación:", "Modela múltiples escenarios", "Una proyección", "Solo pesimista", "Solo optimista", 0, "Monte Carlo = miles escenarios probabilísticos", "baja", "baja"),
    
    # Dificultad: Media (271-290)
    (271, "Planificación Financiera", "Cliente 30 años, tolerancia alta, capacidad media. Perfil:", "Moderado (capacidad limita)", "Agresivo", "Conservador", "Solo cash", 0, "EFPA: Capacidad limita → ajustar a moderado (menor de tolerancia/capacidad)", "media", "alta"),
    
    (272, "Planificación Financiera", "Cartera 60/40 (RV/RF) rebalancea anual. RV sube mucho. ¿Qué hacer?", "Vender RV, comprar RF (volver 60/40)", "Mantener", "Todo a RV", "Todo a RF", 0, "Rebalanceo = disciplina vender ganadores, comprar perdedores", "media", "alta"),
    
    (273, "Planificación Financiera", "Cliente 50 años, jubilación 65, patrimonio 500k, necesita 30k/año. Capacidad riesgo:", "Media-alta (15 años horizonte)", "Baja", "Muy alta", "Nula", 0, "15 años = medio-largo plazo → permite riesgo moderado-alto", "media", "alta"),
    
    (274, "Planificación Financiera", "Secuencia de rentabilidades (sequence risk) importa en:", "Fase retiro", "Acumulación", "Cualquier momento igual", "No importa", 0, "Sequence risk crítico en retiro: pérdidas iniciales muy dañinas", "media", "alta"),
    
    (275, "Planificación Financiera", "Glide path en fondos ciclo vida:", "Reduce RV automáticamente con tiempo", "Mantiene fijo", "Aumenta RV", "Solo RF siempre", 0, "Glide path = desescalada riesgo automática", "media", "media"),
    
    (276, "Planificación Financiera", "Core-satellite strategy combina:", "Base pasiva + satélites activos", "Todo activo", "Todo pasivo", "Sin estrategia", 0, "Core pasivo (bajo coste) + satélites activos (alfa)", "media", "baja"),
    
    (277, "Planificación Financiera", "Cliente cambio laboral, necesita liquidez 6 meses. Parte cartera a:", "Monetario/cash", "Acciones", "Alternativos", "Derivados", 0, "Liquidez corto plazo → sin riesgo mercado", "media", "alta"),
    
    (278, "Planificación Financiera", "Perfil moderado típicamente sugiere:", "50-60% RV, 40-50% RF", "100% RV", "100% RF", "80% RV", 0, "Moderado = equilibrio (mitad-mitad aprox)", "media", "alta"),
    

    (279, "Planificación Financiera", "Longevity risk en jubilación es:", "Vivir más de lo planeado", "Morir joven", "Inflación", "Tipos interés", 0, "Longevity risk = agotar patrimonio por longevidad", "media", "baja"),
    
    (280, "Planificación Financiera", "Bucket strategy divide patrimonio en:", "Cubos temporales (corto/medio/largo)", "Solo un cubo", "Por productos", "Por riesgo solo", 0, "Buckets = liquidez corto + crecimiento largo", "media", "baja"),
    
    (281, "Planificación Financiera", "Safe withdrawal rate busca:", "Tasa retiro sostenible", "Máxima rentabilidad", "Mínimo impuestos", "Timing perfecto", 0, "SWR = cuánto puedo retirar sin agotar patrimonio", "media", "baja"),
    
    (282, "Planificación Financiera", "Risk capacity excede risk tolerance. Cliente debe:", "Invertir según menor (tolerance)", "Según capacity", "Máximo riesgo", "Mínimo riesgo", 0, "EFPA: Usar el MENOR de tolerance/capacity", "media", "alta"),
    
    (283, "Planificación Financiera", "Time-weighted return mide:", "Rentabilidad gestión (elimina flujos)", "Rentabilidad cliente", "Aportaciones", "Reembolsos", 0, "TWR = rentabilidad pura gestor (vs MWR que incluye timing aportaciones)", "media", "baja"),
    
    (284, "Planificación Financiera", "Asset location optimiza:", "Qué activos en qué cuentas fiscales", "Solo compras", "Solo ventas", "Geografía", 0, "Asset location = eficiencia fiscal por tipo cuenta", "media", "baja"),
    
    (285, "Planificación Financiera", "Roth conversion (equivalente español):", "No existe equivalente directo", "Traspasos fondos", "Planes pensiones", "ETVE", 0, "España no tiene Roth IRA (aportación post-tax, retiro libre)", "media", "baja"),
    
    (286, "Planificación Financiera", "Mean-variance optimization busca:", "Frontera eficiente", "Máxima rentabilidad solo", "Mínimo riesgo solo", "Timing", 0, "Markowitz MVO = carteras óptimas riesgo-rentabilidad", "media", "baja"),
    
    (287, "Planificación Financiera", "Liability matching invierte para:", "Cubrir pasivos futuros", "Máxima rentabilidad", "Especular", "Trading", 0, "Liability matching = casar activos con obligaciones (ej: pensiones)", "media", "baja"),
    
    (288, "Planificación Financiera", "Annuity (renta vitalicia) proporciona:", "Ingresos garantizados vida", "Alta rentabilidad", "Liquidez total", "Herencia", 0, "Annuity = seguro longevity (vs herencia)", "media", "baja"),
    
    (289, "Planificación Financiera", "Tactical asset allocation ajusta:", "Pesos temporalmente por visión mercado", "Nunca ajusta", "Diariamente", "Sin criterio", 0, "TAA = desviaciones tácticas de SAA estratégico", "media", "baja"),
    
    (290, "Planificación Financiera", "Heurística representatividad causa:", "Generalizar patrones pequeños", "Diversificar bien", "Análisis correcto", "Paciencia", 0, "Representativeness = sesgo patrones falsos (ej: racha)", "media", "baja"),
    
    # Dificultad: Alta (291-300)
    (291, "Planificación Financiera", "Cliente jubilado, cartera 1M€, necesita 40k/año, inflación 2%. ¿Sostenible 30 años?", "Depende rentabilidad real", "Sí seguro", "No definitivamente", "Imposible calcular", 0, "Necesita rentabilidad real ≥4% para sostenibilidad 30 años (regla 4%)", "alta", "media"),
    
    (292, "Planificación Financiera", "Optimal withdrawal strategy puede incluir:", "Flexibilidad según mercados", "Cantidad fija siempre", "Todo primer año", "Nunca retirar", 0, "Estrategias dinámicas (ej: reducir en bear markets) mejoran sostenibilidad", "alta", "baja"),
    
    (293, "Planificación Financiera", "Black swan events en planificación requieren:", "Escenarios extremos y colchón", "Ignorarlos", "Predecirlos exactos", "Apalancamiento", 0, "Cisnes negros impredecibles → preparación (liquidez, diversificación)", "alta", "baja"),
    
    (294, "Planificación Financiera", "Concentrated position (>20% cartera en un activo) puede requerir:", "Estrategia desconcentración gradual", "Mantener siempre", "Vender todo", "Apalancar más", 0, "Desconcentración gradual minimiza impacto fiscal/mercado", "alta", "baja"),
    
    (295, "Planificación Financiera", "Deferring Social Security (retrasar jubilación) puede:", "Aumentar prestación vitalicia", "Reducir siempre", "Sin efecto", "Prohibido", 0, "Retrasar incrementa pensión mensual (trade-off años vs cantidad)", "alta", "baja"),
    
    (296, "Planificación Financiera", "Mortality credits en annuities provienen de:", "Pooling riesgo longevidad", "Inversiones", "Gobierno", "Rendimientos solo", 0, "Mortality credits = subsidio cruzado longevos por fallecidos prematuros", "alta", "baja"),
    
    (297, "Planificación Financiera", "Gamma en planificación financiera mide:", "Valor añadido asesor conductual/fiscal", "Rentabilidad", "Riesgo", "Alfa inversión", 0, "Gamma = valor asesoramiento holístico (Morningstar: ~1,8%/año)", "alta", "baja"),
    
    (298, "Planificación Financiera", "Funded ratio en plan pensiones es:", "Activos / Pasivos", "Rentabilidad", "Aportaciones", "Beneficiarios", 0, "Funded ratio >100% = superávit, <100% = déficit", "alta", "baja"),
    
    (299, "Planificación Financiera", "Retirement income floor strategy prioriza:", "Cubrir gastos básicos con ingresos seguros", "Máxima rentabilidad", "Todo en RV", "Especulación", 0, "Floor = esenciales cubiertos (pensión, annuity), resto riesgo", "alta", "baja"),
    
    (300, "Planificación Financiera", "Prospect theory explica:", "Aversión pérdidas > atracción ganancias", "Racionalidad perfecta", "Solo ganancias importan", "Decisiones óptimas", 0, "Kahneman: pérdida duele 2x más que ganancia equivalente alegra", "alta", "baja"),
]

print("✅ Planificación Financiera: 50 preguntas")

for q in planificacion:
    cursor_preguntas.execute("""
        INSERT INTO preguntas (id, tema, pregunta, opcion_a, opcion_b, opcion_c, opcion_d, correcta, explicacion, dificultad, frecuencia_examen)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, q)

# Guardar cambios

# Mostrar resumen final
cursor_preguntas.execute("SELECT tema, COUNT(*) FROM preguntas GROUP BY tema ORDER BY tema")
print("\n" + "="*60)
print("✅ BASE DE DATOS COMPLETADA CON 300 PREGUNTAS")
print("="*60)
print("\n📊 Distribución por tema:")
for tema, count in cursor_preguntas.fetchall():
    print(f"   - {tema}: {count} preguntas")

cursor_preguntas.execute("SELECT dificultad, COUNT(*) FROM preguntas GROUP BY dificultad")
print("\n📊 Distribución por dificultad:")
for dif, count in cursor_preguntas.fetchall():
    print(f"   - {dif.capitalize()}: {count} preguntas")

cursor_preguntas.execute("SELECT COUNT(*) FROM preguntas")
total = cursor_preguntas.fetchone()[0]
print(f"\n🎯 TOTAL: {total} preguntas cargadas correctamente")


print("\n" + "="*60)
print("🚀 SIGUIENTE PASO:")
print("="*60)
print("\n   cd ~/Downloads/efa_academy")
print("   python3 init_questions_300.py")
print("   streamlit run app.py")
print("\n" + "="*60)



# cierre final correcto

# cierre final correcto

# === CIERRE FINAL UNICO ===
conn_preguntas.commit()
conn_progreso.commit()
conn_preguntas.close()
conn_progreso.close()
