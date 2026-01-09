# MÓDULO 1: INSTRUMENTOS Y MERCADOS FINANCIEROS (AVANZADO)

## Certificación EFA (Nivel II) - EFPA España

**Ponderación en el examen: 20%**

**Versión:** Actualizada según Guía EFPA V18/25 (marzo 2025)

**Prerrequisito:** Haber superado EIP (Nivel I)

---

# PARTE I: OBJETIVOS Y COMPETENCIAS EFPA - NIVEL II

## ¿Qué diferencia el Nivel II del Nivel I?

El Nivel II (EFA) profundiza en el **análisis cuantitativo** y la **aplicación práctica** de los conceptos del Nivel I. Se exige:

| Aspecto | Nivel I (EIP) | Nivel II (EFA) |
|---------|---------------|----------------|
| **Enfoque** | Conceptual y descriptivo | Analítico y aplicado |
| **Cálculos** | Básicos (TIR, VAN simple) | Complejos (duración modificada, Greeks) |
| **Casos** | Ejemplos ilustrativos | Resolución de casos cliente |
| **Normativa** | Conocimiento general | Aplicación práctica MiFID II |

## Competencias evaluadas en este módulo

| Competencia | Nivel taxonómico | Peso aproximado |
|-------------|------------------|-----------------|
| Análisis de estructura temporal de tipos | Aplicación | 15% |
| Valoración de bonos y sensibilidad | Aplicación | 20% |
| Análisis fundamental y técnico de RV | Análisis | 15% |
| Estrategias con derivados | Aplicación | 25% |
| Productos estructurados | Análisis | 15% |
| Gestión de divisas | Aplicación | 10% |

---

# PARTE II: CONTENIDO TEÓRICO AVANZADO

---

## 1. MERCADOS FINANCIEROS: ANÁLISIS AVANZADO DE ESTRUCTURA

### 1.1 Arquitectura del Sistema Financiero

**Mercado primario vs secundario - Implicaciones para el asesor:**

| Característica | Mercado Primario | Mercado Secundario |
|----------------|------------------|-------------------|
| **Función** | Captación de capital | Liquidez y formación de precios |
| **Precio** | Fijado por emisor/colocador | Determinado por oferta/demanda |
| **Riesgo para inversor** | Riesgo de colocación | Riesgo de mercado |
| **Comisiones típicas** | 0-2% (absorbidas por emisor) | 0,1-0,5% (bid-ask + corretaje) |
| **Información disponible** | Folleto de emisión | Cotización en tiempo real |

**Sistemas de negociación en Europa:**

| Sistema | Características | Ejemplos |
|---------|-----------------|----------|
| **Mercados regulados** | Autorización, supervisión, transparencia | BME, Euronext, Deutsche Börse |
| **SMN (MTF)** | Menores requisitos, acceso alternativo | Chi-X, Turquoise, BATS |
| **OTF** | Productos no equity, discrecionalidad | Plataformas de bonos |
| **Internalizadores sistemáticos** | Ejecución bilateral, reporting | Grandes bancos |

### 1.2 Liquidez del Mercado: Métricas y Análisis

**Indicadores de liquidez que debe conocer el asesor:**

```
Bid-Ask Spread (%) = [(Ask - Bid) / Precio medio] × 100

Precio medio = (Ask + Bid) / 2
```

**Ejemplo numérico:**
```
Acción XYZ:
- Bid (compra): 24,50 €
- Ask (venta): 24,60 €

Spread absoluto = 24,60 - 24,50 = 0,10 €
Precio medio = (24,60 + 24,50) / 2 = 24,55 €
Spread (%) = (0,10 / 24,55) × 100 = 0,41%

Interpretación: Coste implícito de transacción = 0,41%
```

**Profundidad del mercado:**
```
Volumen en el mejor bid + Volumen en el mejor ask

Ratio de profundidad = Volumen negociado diario / Capitalización × 100
```

**Clasificación de liquidez por tipo de activo:**

| Activo | Spread típico | Tiempo de ejecución | Impacto de mercado |
|--------|---------------|---------------------|-------------------|
| **Deuda pública AAA** | 0,01-0,05% | Inmediato | Bajo |
| **Blue chips** | 0,05-0,20% | Inmediato | Bajo |
| **Mid caps** | 0,20-1,00% | Minutos | Medio |
| **Small caps** | 1,00-5,00% | Horas/días | Alto |
| **Bonos corporativos** | 0,50-2,00% | Horas | Medio-Alto |
| **Estructurados** | 2,00-5,00% | Días | Muy alto |

### 1.3 Formación de Precios y Eficiencia

**Hipótesis de Mercados Eficientes (EMH) - Formas:**

| Forma | Información incorporada | Implicación para el asesor |
|-------|------------------------|---------------------------|
| **Débil** | Precios históricos | Análisis técnico inútil |
| **Semifuerte** | Toda información pública | Análisis fundamental inútil |
| **Fuerte** | Toda información (incluida privada) | Ni el insider puede ganar |

**Anomalías de mercado documentadas:**

| Anomalía | Descripción | Explicación conductual |
|----------|-------------|----------------------|
| Efecto enero | Rentabilidades superiores en enero | Tax-loss selling diciembre |
| Efecto lunes | Rentabilidades negativas los lunes | Pesimismo fin de semana |
| Efecto tamaño | Small caps superan a large caps | Prima de iliquidez |
| Efecto valor | Value supera a growth a largo plazo | Sobrerreacción a noticias |
| Momentum | Tendencias persisten 3-12 meses | Infrareacción inicial |

---

## 2. RENTA FIJA AVANZADA

### 2.1 Estructura Temporal de Tipos de Interés (ETTI)

**Curva de tipos - Interpretación:**

| Forma de la curva | Interpretación | Estrategia sugerida |
|-------------------|----------------|---------------------|
| **Normal (pendiente +)** | Expectativas de crecimiento | Posiciones a corto plazo |
| **Invertida (pendiente -)** | Expectativas de recesión | Alargar duración |
| **Plana** | Incertidumbre, transición | Neutral, diversificar |
| **Jorobada** | Subidas de tipos a corto, bajadas a largo | Barbell strategy |

**Teorías de la ETTI:**

1. **Teoría de las expectativas puras:**
```
(1 + r₂)² = (1 + r₁) × (1 + f₁,₂)

Donde:
r₂ = tipo spot a 2 años
r₁ = tipo spot a 1 año
f₁,₂ = tipo forward implícito del año 1 al 2
```

**Ejemplo de cálculo de forward:**
```
Datos:
- Tipo spot 1 año: 3,00%
- Tipo spot 2 años: 3,50%

Cálculo del forward 1 año dentro de 1 año:
(1,035)² = (1,03) × (1 + f₁,₂)
1,071225 = 1,03 × (1 + f₁,₂)
f₁,₂ = (1,071225 / 1,03) - 1 = 4,00%

Interpretación: El mercado espera que el tipo a 1 año sea 4% dentro de 1 año
```

2. **Teoría de la preferencia por la liquidez:**
```
Los tipos a largo incluyen una prima de liquidez:
r largo = r corto esperado + Prima de liquidez

Prima típica: 0,25% - 0,75% por año adicional
```

3. **Teoría de segmentación del mercado:**
- Cada plazo tiene su propia oferta/demanda
- Fondos de pensiones: demanda de largo plazo
- Tesorerías: demanda de corto plazo

### 2.2 Duración y Convexidad

**Duración de Macaulay:**
```
D = Σ [t × CFt × (1+y)^(-t)] / Precio

Donde:
t = período
CFt = flujo de caja en t
y = TIR del bono
```

**Duración Modificada:**
```
DM = D / (1 + y/n)

Donde:
n = número de pagos por año

Variación precio ≈ -DM × Δy × Precio
```

**Ejemplo completo de duración:**
```
Bono: 
- Nominal: 1.000 €
- Cupón: 5% anual
- Vencimiento: 3 años
- TIR actual: 4%

Flujos descontados:
Año 1: 50 / (1,04)¹ = 48,08 €
Año 2: 50 / (1,04)² = 46,23 €
Año 3: 1.050 / (1,04)³ = 933,51 €
Precio = 1.027,82 €

Duración Macaulay:
D = [1×48,08 + 2×46,23 + 3×933,51] / 1.027,82
D = [48,08 + 92,46 + 2.800,53] / 1.027,82
D = 2.941,07 / 1.027,82 = 2,86 años

Duración Modificada:
DM = 2,86 / 1,04 = 2,75

Interpretación: Si los tipos suben 1%, el precio cae aproximadamente 2,75%
```

**Convexidad:**
```
Convexidad = Σ [t × (t+1) × CFt × (1+y)^(-(t+2))] / Precio

Ajuste por convexidad:
ΔP/P ≈ -DM × Δy + (1/2) × Convexidad × (Δy)²
```

**Ejemplo con convexidad:**
```
Usando el bono anterior con Convexidad = 9,5

Si tipos suben del 4% al 5% (Δy = 0,01):

Sin convexidad: ΔP/P ≈ -2,75 × 0,01 = -2,75%
Con convexidad: ΔP/P ≈ -2,75 × 0,01 + 0,5 × 9,5 × (0,01)² 
                     = -2,75% + 0,0475% = -2,70%

La convexidad "amortigua" la caída: -2,70% vs -2,75%
```

**Propiedades de duración y convexidad:**

| Característica del bono | Efecto en Duración | Efecto en Convexidad |
|------------------------|-------------------|---------------------|
| Mayor vencimiento | ↑ Aumenta | ↑ Aumenta |
| Mayor cupón | ↓ Disminuye | ↓ Disminuye |
| Mayor TIR | ↓ Disminuye | ↓ Disminuye |
| Cupón cero | = Vencimiento | Máxima para su duración |

### 2.3 Estrategias de Gestión de Renta Fija

**Estrategias pasivas:**

| Estrategia | Descripción | Cuándo usar |
|------------|-------------|-------------|
| **Buy & Hold** | Comprar y mantener hasta vencimiento | Matching de pasivos conocidos |
| **Indexación** | Replicar un índice de RF | Costes mínimos, mercado eficiente |
| **Inmunización** | Igualar duración activos = pasivos | Fondos de pensiones, aseguradoras |

**Inmunización - Ejemplo:**
```
Pasivo: Pagar 1.000.000 € en 5 años
Duración del pasivo = 5 años

Estrategia: Comprar bonos con duración = 5 años
- Si tipos suben: precio baja PERO reinversión de cupones mejora
- Si tipos bajan: precio sube PERO reinversión de cupones empeora
- Efecto neto: se compensa si duración = horizonte
```

**Estrategias activas:**

| Estrategia | Expectativa | Implementación |
|------------|-------------|----------------|
| **Riding the curve** | Curva estable | Comprar bonos con vencimiento > horizonte |
| **Bullet** | Movimiento paralelo de curva | Concentrar en un vencimiento |
| **Barbell** | Aplanamiento de curva | Extremos (corto + largo) |
| **Ladder** | Incertidumbre | Escalonar vencimientos |

**Ejemplo Riding the Curve:**
```
Situación: Curva normal, horizonte 1 año
- Tipo 1 año: 3%
- Tipo 2 años: 3,5%

Estrategia: Comprar bono 2 años, vender en 1 año

Si la curva no cambia:
- Compra bono 2 años a par (TIR 3,5%)
- En 1 año, es un bono 1 año que cotiza a TIR 3%
- Ganancia por roll-down: aproximadamente 0,5% adicional

Rentabilidad total ≈ 3,5% (cupón) + 0,5% (roll-down) = 4%
vs Buy & Hold 1 año = 3%
```

### 2.4 Análisis de Crédito

**Spreads de crédito:**
```
Spread = TIR bono corporativo - TIR bono gobierno (mismo plazo)
```

**Componentes del spread:**

| Componente | Descripción | Peso típico |
|------------|-------------|-------------|
| Prima de impago | Pérdida esperada por default | 40-60% |
| Prima de liquidez | Menor negociación | 20-30% |
| Prima de riesgo | Incertidumbre sobre default | 20-30% |

**Ratings y probabilidades de impago:**

| Rating | Probabilidad impago 1 año | Probabilidad impago 5 años | Spread típico |
|--------|---------------------------|---------------------------|---------------|
| AAA | 0,00% | 0,10% | 20-40 pb |
| AA | 0,02% | 0,30% | 40-60 pb |
| A | 0,05% | 0,70% | 60-100 pb |
| BBB | 0,15% | 2,00% | 100-200 pb |
| BB | 0,70% | 8,00% | 250-400 pb |
| B | 3,00% | 20,00% | 400-600 pb |
| CCC | 10,00% | 40,00% | 800+ pb |

**Cálculo de pérdida esperada:**
```
Pérdida esperada = Probabilidad de impago × (1 - Tasa de recuperación)

Ejemplo:
- Bono BBB, probabilidad impago 5 años = 2%
- Tasa de recuperación típica = 40%

Pérdida esperada = 2% × (1 - 0,40) = 1,2% en 5 años
Pérdida anualizada = 1,2% / 5 = 0,24% anual
```

---

## 3. RENTA VARIABLE AVANZADA

### 3.1 Valoración Fundamental

**Modelo de Descuento de Dividendos (DDM):**

```
P₀ = Σ [Dt / (1+k)^t]

Donde:
P₀ = precio actual
Dt = dividendo esperado en t
k = tasa de descuento (coste de capital)
```

**Modelo de Gordon (crecimiento constante):**
```
P₀ = D₁ / (k - g)

Donde:
D₁ = dividendo esperado próximo año = D₀ × (1+g)
k = coste de capital
g = tasa de crecimiento perpetuo de dividendos
```

**Ejemplo Gordon:**
```
Datos empresa ABC:
- Dividendo actual (D₀): 2,00 €
- Crecimiento esperado (g): 3%
- Coste de capital (k): 8%

P₀ = 2,00 × 1,03 / (0,08 - 0,03) = 2,06 / 0,05 = 41,20 €

Si cotiza a 35 €: INFRAVALORADA (potencial +17,7%)
Si cotiza a 50 €: SOBREVALORADA (potencial -17,6%)
```

**Modelo de crecimiento en dos etapas:**
```
P₀ = Σ [Dt / (1+k)^t] + [Pn / (1+k)^n]

Donde Pn = Dn+1 / (k - g) para la fase de crecimiento estable
```

**Ejemplo dos etapas:**
```
Empresa XYZ:
- D₀ = 1,00 €
- Crecimiento años 1-5: 15%
- Crecimiento perpetuo después: 3%
- k = 10%

Dividendos fase 1:
D₁ = 1,00 × 1,15 = 1,15
D₂ = 1,15 × 1,15 = 1,32
D₃ = 1,32 × 1,15 = 1,52
D₄ = 1,52 × 1,15 = 1,75
D₅ = 1,75 × 1,15 = 2,01

Valor terminal (año 5):
D₆ = 2,01 × 1,03 = 2,07
P₅ = 2,07 / (0,10 - 0,03) = 29,57

Valor actual:
VA dividendos = 1,15/1,1 + 1,32/1,1² + 1,52/1,1³ + 1,75/1,1⁴ + 2,01/1,1⁵
              = 1,05 + 1,09 + 1,14 + 1,20 + 1,25 = 5,73

VA terminal = 29,57 / 1,1⁵ = 18,37

P₀ = 5,73 + 18,37 = 24,10 €
```

### 3.2 Múltiplos de Valoración

**PER (Price Earnings Ratio):**
```
PER = Precio / BPA

PER justificado = Pay-out / (k - g)
```

**Ejemplo de PER justificado:**
```
Empresa con:
- Pay-out = 40%
- k = 10%
- g = 4%

PER justificado = 0,40 / (0,10 - 0,04) = 6,67x

Si PER actual = 10x → Sobrevalorada
Si PER actual = 5x → Infravalorada
```

**Otros múltiplos relevantes:**

| Múltiplo | Fórmula | Uso principal | Ventajas |
|----------|---------|---------------|----------|
| **EV/EBITDA** | Enterprise Value / EBITDA | Comparación sectorial | Ignora estructura capital |
| **P/B** | Precio / Valor contable | Bancos, inmobiliarias | Activos tangibles |
| **P/S** | Precio / Ventas | Empresas sin beneficios | Siempre positivo |
| **P/FCF** | Precio / Free Cash Flow | Empresas maduras | Caja real generada |

**Enterprise Value:**
```
EV = Capitalización + Deuda neta - Caja

Ejemplo:
- Capitalización: 1.000 M€
- Deuda financiera: 400 M€
- Caja: 50 M€

EV = 1.000 + 400 - 50 = 1.350 M€
```

### 3.3 Análisis Técnico

**Soportes y resistencias:**

| Concepto | Definición | Señal |
|----------|------------|-------|
| **Soporte** | Nivel donde la demanda frena caídas | Compra si se mantiene |
| **Resistencia** | Nivel donde la oferta frena subidas | Venta si no rompe |
| **Ruptura** | Precio atraviesa soporte/resistencia | Confirma tendencia |
| **Pull-back** | Retroceso tras ruptura | Oportunidad de entrada |

**Indicadores técnicos principales:**

| Indicador | Cálculo | Interpretación |
|-----------|---------|----------------|
| **Media móvil simple (SMA)** | Media de últimos n precios | Tendencia |
| **Media móvil exponencial (EMA)** | Pondera más los recientes | Tendencia más reactiva |
| **RSI** | 100 - [100/(1+RS)] | >70 sobrecompra, <30 sobreventa |
| **MACD** | EMA12 - EMA26 | Cruce con señal = cambio tendencia |
| **Bandas Bollinger** | SMA ± 2×Desv.típica | Volatilidad, reversión |

**RSI - Relative Strength Index:**
```
RS = Media ganancias (n días) / Media pérdidas (n días)
RSI = 100 - [100 / (1 + RS)]

Ejemplo (14 días):
- Media subidas: 1,2%
- Media bajadas: 0,8%

RS = 1,2 / 0,8 = 1,5
RSI = 100 - [100 / (1 + 1,5)] = 100 - 40 = 60

Interpretación: Zona neutral (ni sobrecompra ni sobreventa)
```

**Patrones chartistas:**

| Patrón | Tipo | Implicación |
|--------|------|-------------|
| Hombro-cabeza-hombro | Reversión | Cambio de alcista a bajista |
| Doble suelo | Reversión | Cambio de bajista a alcista |
| Triángulo ascendente | Continuación | Ruptura alcista probable |
| Bandera | Continuación | Pausa antes de continuar |

---

## 4. DERIVADOS FINANCIEROS: NIVEL AVANZADO

### 4.1 Opciones: Valoración y Estrategias

**Factores que afectan al precio de una opción:**

| Factor | Efecto en CALL | Efecto en PUT |
|--------|----------------|---------------|
| ↑ Precio subyacente | ↑ Sube | ↓ Baja |
| ↑ Strike | ↓ Baja | ↑ Sube |
| ↑ Tiempo a vencimiento | ↑ Sube | ↑ Sube |
| ↑ Volatilidad | ↑ Sube | ↑ Sube |
| ↑ Tipo de interés | ↑ Sube | ↓ Baja |
| ↑ Dividendos | ↓ Baja | ↑ Sube |

**Las Griegas:**

| Griega | Mide | Fórmula simplificada | Rango típico |
|--------|------|---------------------|--------------|
| **Delta (Δ)** | Sensibilidad al precio | ΔPrima / ΔSubyacente | Call: 0 a 1; Put: -1 a 0 |
| **Gamma (Γ)** | Cambio en Delta | ΔDelta / ΔSubyacente | Máximo en ATM |
| **Theta (Θ)** | Decaimiento temporal | ΔPrima / ΔTiempo | Siempre negativo (comprador) |
| **Vega (ν)** | Sensibilidad a volatilidad | ΔPrima / ΔVolatilidad | Máximo en ATM |
| **Rho (ρ)** | Sensibilidad a tipos | ΔPrima / ΔTipo interés | Poco relevante corto plazo |

**Ejemplo de Delta:**
```
Call sobre Telefónica:
- Strike: 4,00 €
- Prima: 0,30 €
- Delta: 0,55

Si Telefónica sube de 4,10 € a 4,20 € (+0,10 €):
Nueva prima ≈ 0,30 + (0,55 × 0,10) = 0,355 €

Interpretación: Por cada 1€ que sube el subyacente, 
la call sube 0,55€ (55 céntimos)
```

**Ejemplo de Theta:**
```
Call ATM con 30 días a vencimiento:
- Prima: 1,20 €
- Theta: -0,03 €/día

Si pasan 10 días sin cambios en el subyacente:
Nueva prima ≈ 1,20 + (10 × -0,03) = 0,90 €

Interpretación: La opción pierde 0,03 € de valor cada día
por el paso del tiempo
```

### 4.2 Estrategias con Opciones

**Estrategias direccionales:**

| Estrategia | Construcción | Expectativa | Riesgo máximo | Beneficio máximo |
|------------|--------------|-------------|---------------|------------------|
| **Long Call** | Compra Call | Alcista | Prima pagada | Ilimitado |
| **Long Put** | Compra Put | Bajista | Prima pagada | Strike - Prima |
| **Covered Call** | Acción + Venta Call | Moderadamente alcista | Precio acción - Prima | Strike - Coste + Prima |
| **Protective Put** | Acción + Compra Put | Alcista con protección | Prima pagada | Ilimitado |

**Estrategias de volatilidad:**

| Estrategia | Construcción | Expectativa | Break-even |
|------------|--------------|-------------|------------|
| **Straddle** | Call + Put (mismo strike) | Alta volatilidad | Strike ± Primas |
| **Strangle** | Call (OTM) + Put (OTM) | Alta volatilidad, más barato | Strikes ± Primas |
| **Butterfly** | 2 Calls ATM vendidas + 1 Call ITM + 1 Call OTM | Baja volatilidad | Complejo |

**Ejemplo Straddle:**
```
Acción XYZ a 50 €, esperas movimiento fuerte pero incierto:

Compra Call strike 50: Prima = 2,50 €
Compra Put strike 50: Prima = 2,30 €
Coste total: 4,80 €

Break-even superior: 50 + 4,80 = 54,80 €
Break-even inferior: 50 - 4,80 = 45,20 €

Resultados:
- XYZ = 60 €: Beneficio Call = 10 - 4,80 = 5,20 €
- XYZ = 40 €: Beneficio Put = 10 - 4,80 = 5,20 €
- XYZ = 50 €: Pérdida máxima = 4,80 €
```

**Spreads verticales:**

| Spread | Construcción | Coste | Beneficio máx | Pérdida máx |
|--------|--------------|-------|---------------|-------------|
| **Bull Call Spread** | Compra Call K1 + Venta Call K2 (K2>K1) | Débito neto | K2-K1-Coste | Coste |
| **Bear Put Spread** | Compra Put K2 + Venta Put K1 (K2>K1) | Débito neto | K2-K1-Coste | Coste |
| **Bull Put Spread** | Venta Put K2 + Compra Put K1 (K2>K1) | Crédito neto | Crédito | K2-K1-Crédito |

**Ejemplo Bull Call Spread:**
```
Acción a 100 €, expectativa moderadamente alcista:

Compra Call strike 100: Prima = 5,00 €
Venta Call strike 110: Prima = 2,00 €
Coste neto: 3,00 €

Resultados:
- Acción ≤ 100 €: Pérdida = 3,00 € (máxima)
- Acción = 105 €: Beneficio = 5 - 3 = 2,00 €
- Acción ≥ 110 €: Beneficio = 10 - 3 = 7,00 € (máximo)

Ratio beneficio/riesgo: 7/3 = 2,33x
```

### 4.3 Futuros: Estrategias de Cobertura

**Ratio de cobertura óptimo:**
```
h* = ρ × (σS / σF)

Donde:
h* = ratio de cobertura
ρ = correlación entre spot y futuro
σS = volatilidad del activo a cubrir
σF = volatilidad del futuro
```

**Número de contratos:**
```
N = (h* × Valor posición) / (Precio futuro × Multiplicador)
```

**Ejemplo de cobertura con futuros:**
```
Cartera de acciones españolas: 500.000 €
Beta de la cartera: 1,2
Futuro IBEX-35: 10.000 puntos
Multiplicador: 10 €

Valor nocional por contrato = 10.000 × 10 = 100.000 €

Contratos necesarios = (1,2 × 500.000) / 100.000 = 6 contratos

Para cobertura total: VENDER 6 contratos de futuro IBEX
```

**Ajuste de beta con futuros:**
```
Contratos = [(Beta objetivo - Beta actual) × Valor cartera] / Valor contrato

Ejemplo: Reducir beta de 1,2 a 0,8
Contratos = [(0,8 - 1,2) × 500.000] / 100.000 = -2 contratos
(Vender 2 contratos adicionales)
```

---

## 5. PRODUCTOS ESTRUCTURADOS

### 5.1 Anatomía de un Estructurado

**Componentes básicos:**
```
Estructurado = Bono cupón cero + Opción(es)

Ejemplo capital garantizado:
- Inversión: 10.000 €
- Plazo: 3 años
- Tipo sin riesgo: 3%

Bono cupón cero necesario: 10.000 / (1,03)³ = 9.151 €
Disponible para opciones: 10.000 - 9.151 = 849 €
```

**Tipos de estructurados:**

| Tipo | Estructura | Rentabilidad | Riesgo capital |
|------|------------|--------------|----------------|
| **Capital garantizado** | Bono + Call | Participación en subida | 0% |
| **Capital protegido** | Bono + Put vendida | Cupón + riesgo bajista | Parcial |
| **Reverse convertible** | Bono + Put vendida | Cupón alto | Total (conversión) |
| **Autocallable** | Bono + opciones barrera | Cupón si no toca barrera | Variable |

### 5.2 Autocallables - Análisis Detallado

**Ejemplo de Autocallable:**
```
Subyacente: Eurostoxx 50 (nivel inicial 4.000)
Plazo máximo: 3 años
Observación: Trimestral

Barrera de autocall: 100% (4.000)
Cupón por trimestre: 2% (8% anual)
Barrera de protección: 60% (2.400)

Escenarios:
1) Trimestre 1: Eurostoxx ≥ 4.000 → Autocall, devuelve 102%
2) Año 1: Eurostoxx < 4.000 cada trimestre → No autocall, sigue
3) Vencimiento con Eurostoxx = 3.500 (87,5%): Devuelve 100% + cupones
4) Vencimiento con Eurostoxx = 2.200 (55%): Pérdida = 45% del capital
```

**Riesgos de los estructurados:**

| Riesgo | Descripción | Mitigación |
|--------|-------------|------------|
| **Emisor** | Default del banco emisor | Diversificar emisores |
| **Mercado** | Caída del subyacente | Entender barrera |
| **Liquidez** | Spread alto en secundario | Mantener hasta vencimiento |
| **Complejidad** | Difícil valoración | KID/DFI obligatorio |

---

## 6. MERCADO DE DIVISAS AVANZADO

### 6.1 Paridad de Tipos de Interés

**Paridad cubierta de tipos de interés (CIP):**
```
F/S = (1 + rd) / (1 + rf)

Donde:
F = tipo forward
S = tipo spot
rd = tipo de interés doméstico
rf = tipo de interés extranjero
```

**Cálculo de forward EUR/USD:**
```
Spot EUR/USD: 1,1000
Tipo EUR (1 año): 3%
Tipo USD (1 año): 5%

Forward 1 año = 1,1000 × (1,05 / 1,03) = 1,1214

Interpretación: El EUR se aprecia a futuro porque 
los tipos en EUR son menores
```

**Puntos forward:**
```
Puntos forward = (F - S) × 10.000

En el ejemplo: (1,1214 - 1,1000) × 10.000 = 214 puntos

Si puntos > 0: Moneda cotizada con prima (forward > spot)
Si puntos < 0: Moneda cotizada con descuento (forward < spot)
```

### 6.2 Cobertura del Riesgo de Cambio

**Estrategias de cobertura:**

| Estrategia | Coste | Protección | Participación |
|------------|-------|------------|---------------|
| **Forward** | Cero | Total | Ninguna |
| **Opción Put** | Prima | Total | Total |
| **Collar** | Bajo/Cero | Parcial | Limitada |
| **Participating forward** | Cero | Parcial | Parcial |

**Ejemplo de cobertura con forward:**
```
Empresa española espera cobrar 1.000.000 USD en 6 meses
Spot actual: EUR/USD = 1,1000
Forward 6 meses: EUR/USD = 1,1100

Sin cobertura:
- Si EUR/USD = 1,0500: Recibe 1.000.000/1,05 = 952.381 €
- Si EUR/USD = 1,1500: Recibe 1.000.000/1,15 = 869.565 €

Con forward a 1,1100:
- Recibe siempre: 1.000.000/1,11 = 900.901 €
- Coste de oportunidad si USD se aprecia
- Protección si USD se deprecia
```

---

## 7. ANÁLISIS INTEGRADO DE RIESGOS

### 7.1 Mapa de Riesgos por Instrumento

| Instrumento | Riesgo Mercado | Riesgo Crédito | Riesgo Liquidez | Riesgo Divisa |
|-------------|----------------|----------------|-----------------|---------------|
| **Deuda pública EUR** | Medio | Bajo | Bajo | No |
| **Deuda corporativa IG** | Medio-Alto | Medio | Medio | Posible |
| **Deuda HY** | Alto | Alto | Alto | Posible |
| **Acciones blue chip** | Alto | Bajo | Bajo | Posible |
| **Acciones small cap** | Muy alto | Medio | Alto | Posible |
| **Derivados** | Variable | Contraparte | Variable | Variable |
| **Estructurados** | Variable | Emisor | Alto | Variable |

### 7.2 Value at Risk (VaR) - Conceptos

**Definición:**
```
VaR = Pérdida máxima esperada en un período dado 
      con un nivel de confianza determinado

Ejemplo: VaR 1 día, 95% = 50.000 €
Significa: Con 95% de probabilidad, la pérdida diaria no superará 50.000 €
```

**VaR paramétrico (varianza-covarianza):**
```
VaR = Valor posición × σ × z

Donde:
σ = volatilidad del activo (diaria si VaR diario)
z = valor crítico de la normal (1,65 para 95%, 2,33 para 99%)
```

**Ejemplo VaR:**
```
Cartera de acciones: 1.000.000 €
Volatilidad diaria: 1,5%
Nivel de confianza: 95%

VaR 1 día (95%) = 1.000.000 × 0,015 × 1,65 = 24.750 €

Interpretación: En el 95% de los días, 
la pérdida será menor a 24.750 €
```

---

## 8. SELECCIÓN DE INSTRUMENTOS EN ASESORAMIENTO

### 8.1 Matching Perfil-Producto

| Perfil Cliente | Horizonte | Instrumentos Recomendados | Instrumentos a Evitar |
|----------------|-----------|---------------------------|----------------------|
| **Conservador** | Corto | Monetarios, RF CP IG | RV, Derivados, HY |
| **Moderado** | Medio | RF diversificada, RV IG 20-40% | Derivados especulativos |
| **Dinámico** | Largo | RV 60-80%, RF táctica | Concentración sectorial |
| **Agresivo** | Largo | RV 80-100%, alternativos | Sin restricciones razonables |

### 8.2 Due Diligence de Productos

**Checklist para el asesor:**

1. **Comprensión del producto:**
   - ¿Entiendo completamente cómo funciona?
   - ¿Puedo explicarlo al cliente en 2 minutos?

2. **Idoneidad:**
   - ¿Es coherente con el perfil de riesgo?
   - ¿Encaja en el horizonte temporal?
   - ¿Cumple los objetivos del cliente?

3. **Costes:**
   - ¿Cuál es el coste total (TER, comisiones, spread)?
   - ¿Hay costes ocultos o de salida?

4. **Liquidez:**
   - ¿Puede el cliente salir cuando quiera?
   - ¿A qué coste?

5. **Documentación:**
   - ¿Tengo el KID/DFI?
   - ¿He entregado la información precontractual?

---

# PARTE III: CASOS PRÁCTICOS TIPO EFA

---

## CASO 1: Cliente con Horizonte de Jubilación

**Situación:**
María, 55 años, funcionaria. Patrimonio financiero: 300.000 €.
Objetivo: Complementar pensión en 10 años.
Perfil: Moderado. Capacidad de ahorro: 1.000 €/mes.

**Pregunta:** Diseñe una estrategia de inversión con los instrumentos estudiados.

**Solución razonada:**
```
Horizonte: 10 años → Permite asumir volatilidad a corto plazo

Asignación propuesta:
- Renta Fija (60%): 180.000 €
  · RF Gobierno EUR corto plazo: 60.000 € (20%)
  · RF Corporativa IG: 90.000 € (30%)
  · RF Ligada a inflación: 30.000 € (10%)
  
- Renta Variable (35%): 105.000 €
  · RV Europa: 45.000 € (15%)
  · RV Global desarrollada: 45.000 € (15%)
  · RV Emergentes: 15.000 € (5%)
  
- Liquidez (5%): 15.000 €

Duración RF: ~4 años (matching parcial con horizonte)
Beta cartera: ~0,4

Aportaciones mensuales: 60% RF, 40% RV

Rebalanceo: Anual o cuando desviación > 5%

Glide path: Reducir RV 5% cada 2 años a partir de año 6
```

---

## CASO 2: Cobertura de Cartera ante Evento de Riesgo

**Situación:**
Gestor con cartera RV española de 2.000.000 €, beta 1,1.
Elecciones en 2 meses generan incertidumbre.
No quiere vender pero busca protección.

**Pregunta:** Proponga estrategias de cobertura con derivados.

**Solución razonada:**
```
Opción A: Cobertura con futuros IBEX

Futuro IBEX a 10.500, multiplicador 10€
Valor contrato = 105.000 €
Contratos = (1,1 × 2.000.000) / 105.000 = 21 contratos

Coste: Solo margen de garantía (~10%)
Renuncia: Toda la subida potencial

Opción B: Compra de Puts OTM

Put IBEX strike 9.500 (10% OTM)
Prima estimada: 200 puntos = 2.000 € por contrato
Contratos: 21
Coste total: 21 × 2.000 = 42.000 € (2,1% de la cartera)

Protección: Limita pérdidas al 12% (10% caída + 2% prima)
Mantiene: Toda la subida potencial

Opción C: Collar (coste cero)

Compra Put 9.500 + Venta Call 11.500
Prima Put: 200 puntos
Prima Call: 200 puntos
Coste neto: 0

Protección: Pérdida máxima ~10%
Renuncia: Subida por encima de 11.500 (~10%)

Recomendación: Opción B si presupuesto disponible,
               Opción C si presupuesto limitado
```

---

## CASO 3: Análisis de Producto Estructurado

**Situación:**
Cliente recibe propuesta de autocallable:
- Subyacente: Santander
- Cupón: 8% anual (observación trimestral)
- Barrera autocall: 100%
- Barrera de protección: 70%
- Plazo máximo: 3 años

**Pregunta:** Analice el producto y determine su idoneidad.

**Solución razonada:**
```
Análisis de riesgos:

1. Riesgo subyacente único:
   - Concentración en un solo valor
   - Santander: Beta ~1,2, alta correlación con ciclo económico
   - Volatilidad histórica: ~30%

2. Escenarios de pérdida:
   Probabilidad de tocar barrera 70% en 3 años:
   Con volatilidad 30%, aproximadamente 20-25%
   
   Si barrera tocada: Pérdida potencial hasta 100%

3. Cupón vs Riesgo:
   - Cupón 8% vs Tipo sin riesgo ~3%
   - Prima de riesgo implícita: 5%
   - ¿Compensa el riesgo de pérdida del 30%+?

4. Coste implícito:
   - El emisor captura parte del valor de las opciones
   - Estimación: 2-4% del nominal

Perfil adecuado:
- Cliente que entiende renta variable
- Acepta riesgo de pérdida significativa
- Horizonte mínimo 3 años
- Diversificado (este producto < 10% cartera)

Perfil NO adecuado:
- Conservador o moderado
- Necesidad de liquidez
- Sin exposición previa a RV
```

---

# PARTE IV: BANCO DE PREGUNTAS TIPO TEST

---

## Instrucciones

- 40 preguntas de selección múltiple
- Una sola respuesta correcta
- Tiempo recomendado: 60 minutos
- Para aprobar: 70% (28 correctas)

---

### Preguntas 1-10: Mercados y Estructura

**1.** Un internalizador sistemático se caracteriza por:

A) Ser un mercado regulado con autorización de la CNMV

B) Ejecutar órdenes de clientes por cuenta propia de forma organizada

C) Ser un sistema multilateral de negociación

D) Solo operar con instrumentos derivados

**Respuesta: B**

*Explicación: Los internalizadores sistemáticos son entidades que ejecutan órdenes de clientes por cuenta propia de forma bilateral, fuera de mercados regulados o SMN.*

---

**2.** El bid-ask spread de un activo es de 0,8%. Si un inversor compra y vende inmediatamente el mismo activo, su pérdida aproximada será:

A) 0,4%

B) 0,8%

C) 1,6%

D) No hay pérdida si el precio no varía

**Respuesta: B**

*Explicación: Compra al ask y vende al bid. La diferencia es el spread completo (0,8%).*

---

**3.** Según la hipótesis de mercados eficientes en su forma semifuerte:

A) El análisis técnico puede generar rentabilidades extraordinarias

B) El análisis fundamental puede generar rentabilidades extraordinarias

C) Solo la información privilegiada puede generar rentabilidades extraordinarias

D) Ningún análisis puede generar rentabilidades extraordinarias

**Respuesta: C**

*Explicación: En forma semifuerte, toda información pública está incorporada en precios. Solo información privilegiada (no pública) podría generar alfa.*

---

**4.** El efecto "momentum" en los mercados financieros se refiere a:

A) La tendencia de los activos pequeños a superar a los grandes

B) La tendencia de los precios a continuar en la misma dirección durante 3-12 meses

C) El mejor comportamiento de las acciones en enero

D) La sobrerreacción de los inversores a las noticias negativas

**Respuesta: B**

*Explicación: El momentum es la anomalía por la cual los activos que han subido tienden a seguir subiendo (y viceversa) en horizontes de 3-12 meses.*

---

**5.** Un mercado con spread de 0,05% y ratio de profundidad del 2% diario se considera:

A) Muy líquido

B) Moderadamente líquido

C) Poco líquido

D) Ilíquido

**Respuesta: A**

*Explicación: Spread muy bajo (<0,1%) y alta rotación (2% del capital negociado diariamente) indican liquidez elevada.*

---

**6.** La diferencia principal entre un SMN (MTF) y un mercado regulado es:

A) El SMN no tiene supervisión

B) El SMN tiene menores requisitos de admisión a cotización

C) El SMN solo negocia derivados

D) El SMN no permite acceso a inversores minoristas

**Respuesta: B**

*Explicación: Los SMN tienen requisitos más flexibles que los mercados regulados, aunque también están supervisados por el regulador.*

---

**7.** Si la curva de tipos está invertida, la expectativa del mercado es:

A) Crecimiento económico acelerado

B) Inflación al alza

C) Posible recesión económica

D) Estabilidad de tipos

**Respuesta: C**

*Explicación: Una curva invertida (tipos cortos > tipos largos) históricamente ha precedido a recesiones económicas.*

---

**8.** El teorema de la separación de Tobin implica que:

A) Todos los inversores deberían tener la misma cartera de activos arriesgados

B) La cartera óptima depende del perfil de riesgo individual

C) No se debe mezclar renta fija y variable

D) Los activos internacionales deben mantenerse separados

**Respuesta: A**

*Explicación: Tobin demostró que la cartera de activos arriesgados óptima es la misma para todos; solo varía la proporción entre esta cartera y el activo libre de riesgo.*

---

**9.** En el modelo CAPM, el riesgo sistemático se mide por:

A) La varianza total del activo

B) La desviación típica

C) El coeficiente beta

D) El ratio de Sharpe

**Respuesta: C**

*Explicación: Beta mide la sensibilidad del activo al mercado, es decir, su riesgo sistemático (no diversificable).*

---

**10.** Un índice PMI de 48 indica:

A) Expansión económica

B) Contracción económica

C) Estabilidad económica

D) Aceleración del crecimiento

**Respuesta: B**

*Explicación: PMI < 50 indica contracción de la actividad manufacturera.*

---

### Preguntas 11-20: Renta Fija Avanzada

**11.** Un bono con duración modificada de 5 y convexidad de 30 experimentará una variación de precio aproximada de ___% si los tipos suben 100 puntos básicos:

A) -5,00%

B) -4,85%

C) -5,15%

D) -4,70%

**Respuesta: B**

*Explicación: ΔP/P ≈ -DM × Δy + 0,5 × C × (Δy)² = -5 × 0,01 + 0,5 × 30 × 0,0001 = -5% + 0,15% = -4,85%*

---

**12.** La estrategia de "riding the curve" es más rentable cuando:

A) La curva de tipos es plana

B) La curva de tipos es ascendente y estable

C) Los tipos a corto plazo suben

D) La curva se invierte

**Respuesta: B**

*Explicación: Con curva ascendente estable, el bono "rueda" hacia tipos más bajos a medida que se acerca a vencimiento, generando plusvalía adicional.*

---

**13.** Un bono BBB tiene spread de 150 pb sobre el bono gobierno equivalente. Si la probabilidad de impago a 5 años es 2% y la tasa de recuperación esperada es 40%, el spread atribuible a otros factores (liquidez, riesgo) es aproximadamente:

A) 126 pb

B) 24 pb

C) 150 pb

D) 60 pb

**Respuesta: A**

*Explicación: Pérdida esperada = 2% × 60% = 1,2% en 5 años = 24 pb anualizados. Resto del spread: 150 - 24 = 126 pb.*

---

**14.** La inmunización de una cartera de renta fija consiste en:

A) Eliminar el riesgo de crédito

B) Igualar la duración de activos y pasivos

C) Invertir solo en bonos AAA

D) Mantener bonos hasta vencimiento

**Respuesta: B**

*Explicación: La inmunización iguala duración de activos y pasivos para que los efectos de cambios en tipos sobre precio y reinversión se compensen.*

---

**15.** La teoría de las expectativas puras de la ETTI implica que:

A) Los tipos forward son predictores insesgados de los tipos spot futuros

B) Existe una prima de liquidez en los tipos largos

C) Cada segmento del mercado tiene su propia curva

D) Los tipos a largo siempre superan a los cortos

**Respuesta: A**

*Explicación: Según esta teoría, el forward es la mejor estimación del tipo spot que habrá en el futuro, sin primas adicionales.*

---

**16.** Si el tipo spot a 1 año es 3% y el tipo spot a 2 años es 4%, el tipo forward implícito del año 1 al 2 es aproximadamente:

A) 3,5%

B) 4,0%

C) 5,0%

D) 7,0%

**Respuesta: C**

*Explicación: (1,04)² = (1,03) × (1 + f). Por tanto, f = (1,0816/1,03) - 1 = 5,01%*

---

**17.** Una estrategia "barbell" en renta fija consiste en:

A) Concentrar inversiones en un solo vencimiento

B) Escalonar vencimientos uniformemente

C) Invertir en los extremos de la curva (corto y largo plazo)

D) Invertir solo en plazos intermedios

**Respuesta: C**

*Explicación: Barbell combina posiciones en vencimientos cortos y largos, útil cuando se espera aplanamiento de la curva.*

---

**18.** El riesgo de reinversión de un bono:

A) Aumenta con la duración

B) Disminuye con el cupón

C) Aumenta con el cupón

D) Es independiente del cupón

**Respuesta: C**

*Explicación: Mayor cupón = más flujos a reinvertir = mayor incertidumbre sobre la tasa de reinversión.*

---

**19.** Un bono con duración de Macaulay de 6 años tiene una duración modificada de 5,66 años. El TIR del bono es aproximadamente:

A) 4%

B) 5%

C) 6%

D) 7%

**Respuesta: C**

*Explicación: DM = D / (1+y). Por tanto, y = D/DM - 1 = 6/5,66 - 1 = 6%*

---

**20.** La convexidad de un bono cupón cero comparada con un bono con cupón del mismo vencimiento es:

A) Menor

B) Igual

C) Mayor

D) Depende del nivel de tipos

**Respuesta: C**

*Explicación: El cupón cero tiene la máxima duración y convexidad para un vencimiento dado, ya que todo el flujo está concentrado al final.*

---

### Preguntas 21-30: Renta Variable y Derivados

**21.** Según el modelo de Gordon, si el dividendo actual es 2€, el crecimiento esperado es 4% y el coste de capital es 9%, el precio justo de la acción es:

A) 40,00 €

B) 41,60 €

C) 44,44 €

D) 50,00 €

**Respuesta: B**

*Explicación: P = D₁/(k-g) = 2×1,04/(0,09-0,04) = 2,08/0,05 = 41,60 €*

---

**22.** Un PER de 15x con un crecimiento esperado del 10% implica un ratio PEG de:

A) 0,67

B) 1,00

C) 1,50

D) 2,50

**Respuesta: C**

*Explicación: PEG = PER / Crecimiento = 15 / 10 = 1,5*

---

**23.** El Enterprise Value (EV) de una empresa se calcula como:

A) Capitalización + Caja - Deuda

B) Capitalización + Deuda - Caja

C) Capitalización × (1 + Deuda/Capital)

D) EBITDA × Múltiplo del sector

**Respuesta: B**

*Explicación: EV = Capitalización bursátil + Deuda financiera neta (deuda - caja).*

---

**24.** El indicador RSI con valor de 25 indica:

A) Sobrecompra

B) Sobreventa

C) Tendencia neutral

D) Cambio de tendencia inminente

**Respuesta: B**

*Explicación: RSI < 30 indica zona de sobreventa (posible rebote alcista).*

---

**25.** El delta de una opción call at-the-money es aproximadamente:

A) 0,00

B) 0,25

C) 0,50

D) 1,00

**Respuesta: C**

*Explicación: Una call ATM tiene delta cercano a 0,50 (probabilidad aproximada de terminar ITM).*

---

**26.** Si un inversor compra una call y vende una call de strike superior sobre el mismo subyacente, está creando:

A) Un straddle

B) Un bull call spread

C) Un strangle

D) Un collar

**Respuesta: B**

*Explicación: Compra call K1 + Venta call K2 (K2>K1) = Bull Call Spread (visión moderadamente alcista).*

---

**27.** El theta de una opción representa:

A) La sensibilidad al precio del subyacente

B) La sensibilidad a la volatilidad

C) El decaimiento temporal del valor

D) La sensibilidad a los tipos de interés

**Respuesta: C**

*Explicación: Theta mide cuánto valor pierde la opción por cada día que pasa (todo lo demás constante).*

---

**28.** Una estrategia de covered call (acción + venta de call) es adecuada cuando se espera:

A) Fuerte subida del subyacente

B) Estabilidad o ligera subida del subyacente

C) Fuerte caída del subyacente

D) Alta volatilidad

**Respuesta: B**

*Explicación: La covered call genera ingresos adicionales (prima) a cambio de limitar el potencial alcista. Óptima con expectativa moderadamente alcista o lateral.*

---

**29.** Para cubrir una cartera de acciones españolas con beta de 1,3 y valor de 650.000 €, con futuros IBEX a 10.000 puntos (multiplicador 10€), se necesitan:

A) 7 contratos

B) 8 contratos

C) 9 contratos

D) 10 contratos

**Respuesta: C**

*Explicación: Contratos = (Beta × Valor) / Valor contrato = (1,3 × 650.000) / (10.000 × 10) = 845.000/100.000 = 8,45 ≈ 9 contratos*

---

**30.** Un straddle comprado genera beneficios cuando:

A) El subyacente sube moderadamente

B) El subyacente baja moderadamente

C) El subyacente se mueve significativamente en cualquier dirección

D) El subyacente se mantiene estable

**Respuesta: C**

*Explicación: El straddle (call + put mismo strike) gana si el subyacente se mueve más allá de los break-even, en cualquier dirección.*

---

### Preguntas 31-40: Productos Estructurados, Divisas y Asesoramiento

**31.** Un producto estructurado "reverse convertible" expone al inversor a:

A) Solo el riesgo de tipos de interés

B) El riesgo de caída del subyacente (conversión en acciones)

C) Solo el riesgo de crédito del emisor

D) No tiene riesgo de pérdida de capital

**Respuesta: B**

*Explicación: En un reverse convertible, si el subyacente cae por debajo de la barrera, el emisor puede entregar acciones (que valen menos que el nominal invertido).*

---

**32.** En un autocallable, si el subyacente está por encima del nivel inicial en la primera fecha de observación:

A) El producto continúa hasta vencimiento

B) Se activa el autocall y se devuelve el capital más cupón

C) Se pierde el cupón de ese período

D) Se convierte en un bono tradicional

**Respuesta: B**

*Explicación: Si el subyacente está por encima del nivel de autocall (normalmente 100% del inicial), el producto cancela anticipadamente pagando capital + cupón.*

---

**33.** La paridad cubierta de tipos de interés establece que:

A) El tipo forward depende solo del tipo spot

B) El tipo forward incorpora el diferencial de tipos de interés entre divisas

C) No existe relación entre tipos spot y forward

D) Los tipos de interés deben ser iguales en todas las divisas

**Respuesta: B**

*Explicación: F/S = (1+rd)/(1+rf). El forward refleja el diferencial de tipos para evitar arbitraje.*

---

**34.** Si el EUR/USD spot es 1,10 y el forward a 1 año es 1,12, significa que:

A) El mercado espera apreciación del dólar

B) Los tipos en EUR son superiores a los tipos en USD

C) Los tipos en USD son superiores a los tipos en EUR

D) No hay diferencial de tipos

**Respuesta: C**

*Explicación: Forward > Spot implica que USD tiene tipos más altos que EUR (la moneda con tipos más altos cotiza con descuento a futuro).*

---

**35.** Un collar de divisas consiste en:

A) Comprar call y vender put de la misma divisa

B) Comprar put y vender call de la misma divisa

C) Comprar forward y opción sobre la misma divisa

D) Dos forwards a diferentes plazos

**Respuesta: B**

*Explicación: Un collar combina compra de put (protección bajista) y venta de call (limita beneficio alcista), reduciendo o eliminando el coste neto.*

---

**36.** El VaR (95%, 1 día) de una posición de 1 millón de euros con volatilidad diaria del 2% es aproximadamente:

A) 20.000 €

B) 33.000 €

C) 40.000 €

D) 46.500 €

**Respuesta: B**

*Explicación: VaR = Posición × σ × z = 1.000.000 × 0,02 × 1,65 = 33.000 €*

---

**37.** Para un cliente conservador con horizonte de 3 años, el instrumento más adecuado sería:

A) Acciones de pequeña capitalización

B) Fondo de renta fija a corto plazo investment grade

C) Autocallable sobre acciones individuales

D) Fondo de renta variable emergente

**Respuesta: B**

*Explicación: Cliente conservador + horizonte corto = RF de calidad y baja duración.*

---

**38.** Según MiFID II, el test de idoneidad debe verificar:

A) Solo los conocimientos del cliente

B) Solo la situación financiera del cliente

C) Conocimientos, experiencia, situación financiera y objetivos

D) Solo si el cliente ha operado antes con ese producto

**Respuesta: C**

*Explicación: El test de idoneidad (para asesoramiento) evalúa los cuatro elementos: conocimientos, experiencia, situación financiera y objetivos de inversión.*

---

**39.** Un cliente con patrimonio de 500.000 € y perfil moderado debería tener en un solo producto estructurado como máximo:

A) 100.000 € (20%)

B) 50.000 € (10%)

C) 25.000 € (5%)

D) Sin límite si entiende el producto

**Respuesta: B**

*Explicación: Los productos estructurados, por su complejidad y riesgo de concentración, no deberían superar el 10% de una cartera de perfil moderado.*

---

**40.** La principal ventaja de usar futuros frente a opciones para cobertura es:

A) Mayor protección

B) Participación en movimientos favorables

C) Menor coste inicial

D) Mayor flexibilidad

**Respuesta: C**

*Explicación: Los futuros no requieren pago de prima (solo margen), mientras que las opciones tienen coste de prima. A cambio, los futuros no permiten participar en movimientos favorables.*

---

# PARTE V: CHECKLIST DE DOMINIO DEL MÓDULO

Antes de presentarte al examen, verifica que puedes:

## Mercados y Estructura
- [ ] Explicar las diferencias entre mercados regulados, SMN, OTF e internalizadores
- [ ] Calcular e interpretar medidas de liquidez (spread, profundidad)
- [ ] Describir las formas de eficiencia del mercado y sus implicaciones

## Renta Fija
- [ ] Calcular tipos forward a partir de la curva spot
- [ ] Calcular duración y convexidad de un bono
- [ ] Estimar variación de precio usando duración y convexidad
- [ ] Diseñar estrategias de inmunización
- [ ] Analizar spreads de crédito y calcular pérdida esperada

## Renta Variable
- [ ] Valorar acciones con el modelo de Gordon y en dos etapas
- [ ] Calcular e interpretar múltiplos (PER, EV/EBITDA, P/B)
- [ ] Interpretar indicadores técnicos básicos (RSI, MACD, medias móviles)

## Derivados
- [ ] Explicar las Griegas y su impacto en el precio de opciones
- [ ] Diseñar estrategias de cobertura con futuros
- [ ] Construir spreads verticales y calcular sus resultados
- [ ] Determinar cuándo usar straddle, strangle o collar

## Productos Estructurados
- [ ] Descomponer un estructurado en sus componentes
- [ ] Analizar escenarios de un autocallable
- [ ] Identificar riesgos de productos complejos

## Divisas
- [ ] Calcular tipos forward de divisas
- [ ] Diseñar estrategias de cobertura cambiaria

## Asesoramiento
- [ ] Seleccionar instrumentos según perfil del cliente
- [ ] Realizar due diligence de productos
- [ ] Aplicar criterios MiFID II de idoneidad

---

**Fin del Módulo 1 - Nivel II**

*Tiempo estimado de estudio: 15-20 horas*

*Próxima revisión recomendada: 1 semana antes del examen*
