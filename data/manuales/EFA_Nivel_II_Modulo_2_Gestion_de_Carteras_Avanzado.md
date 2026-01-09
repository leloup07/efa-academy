# MÓDULO 2: GESTIÓN DE CARTERAS (AVANZADO)

## Certificación EFA (Nivel II) - EFPA España

**Ponderación en el examen: 20%**

**Versión:** Actualizada según Guía EFPA V18/25 (marzo 2025)

**Prerrequisito:** Módulo de Gestión de Carteras Nivel I (EIP)

---

# PARTE I: OBJETIVOS Y COMPETENCIAS EFPA - NIVEL II

## Diferencias con Nivel I

| Aspecto | Nivel I (EIP) | Nivel II (EFA) |
|---------|---------------|----------------|
| **Teoría de carteras** | Conceptos básicos | Aplicación y optimización |
| **Modelos** | CAPM introductorio | CAPM completo, APT, multifactoriales |
| **Medidas de rendimiento** | Sharpe básico | Sharpe, Treynor, Jensen, Information Ratio |
| **Asset Allocation** | Conceptual | Estratégico y táctico con cálculos |
| **Gestión del riesgo** | Descriptivo | VaR, stress testing, límites |

## Competencias evaluadas

| Competencia | Nivel taxonómico | Peso aproximado |
|-------------|------------------|-----------------|
| Teoría moderna de carteras (Markowitz) | Aplicación | 20% |
| Modelos de valoración (CAPM, APT) | Aplicación | 20% |
| Medidas de performance | Aplicación | 20% |
| Asset Allocation estratégico y táctico | Análisis | 20% |
| Gestión y control de riesgos | Aplicación | 20% |

---

# PARTE II: CONTENIDO TEÓRICO AVANZADO

---

## 1. TEORÍA MODERNA DE CARTERAS (MARKOWITZ)

### 1.1 Fundamentos Matemáticos

**Rentabilidad esperada de una cartera:**
```
E(Rp) = Σ wi × E(Ri)

Donde:
wi = peso del activo i en la cartera
E(Ri) = rentabilidad esperada del activo i
Σ wi = 1 (suma de pesos = 100%)
```

**Ejemplo:**
```
Cartera de 3 activos:
- Activo A: peso 50%, rentabilidad esperada 8%
- Activo B: peso 30%, rentabilidad esperada 12%
- Activo C: peso 20%, rentabilidad esperada 5%

E(Rp) = 0,50 × 8% + 0,30 × 12% + 0,20 × 5%
E(Rp) = 4% + 3,6% + 1% = 8,6%
```

**Varianza de una cartera de 2 activos:**
```
σ²p = w₁²σ₁² + w₂²σ₂² + 2w₁w₂σ₁σ₂ρ₁₂

Donde:
σ²p = varianza de la cartera
σᵢ = desviación típica del activo i
ρ₁₂ = coeficiente de correlación entre activos 1 y 2
```

**Varianza de una cartera de n activos:**
```
σ²p = Σᵢ Σⱼ wᵢwⱼσᵢⱼ

Donde σᵢⱼ = cov(Rᵢ, Rⱼ) = σᵢσⱼρᵢⱼ
```

**Ejemplo de cálculo de varianza (2 activos):**
```
Activo A: peso 60%, σ = 20%
Activo B: peso 40%, σ = 15%
Correlación ρ = 0,3

σ²p = (0,60)²×(0,20)² + (0,40)²×(0,15)² + 2×0,60×0,40×0,20×0,15×0,3

σ²p = 0,36×0,04 + 0,16×0,0225 + 2×0,60×0,40×0,20×0,15×0,3
σ²p = 0,0144 + 0,0036 + 0,00432 = 0,02232

σp = √0,02232 = 14,94%

Nota: La volatilidad de la cartera (14,94%) es menor que el 
promedio ponderado de volatilidades (60%×20% + 40%×15% = 18%)
¡Este es el efecto diversificación!
```

### 1.2 El Efecto de la Correlación

| Correlación (ρ) | Efecto en la cartera | Diversificación |
|-----------------|---------------------|-----------------|
| ρ = +1 | Volatilidad = promedio ponderado | Ninguna |
| 0 < ρ < 1 | Volatilidad < promedio ponderado | Parcial |
| ρ = 0 | Reducción significativa de riesgo | Alta |
| -1 < ρ < 0 | Mayor reducción de riesgo | Muy alta |
| ρ = -1 | Posible eliminar todo el riesgo | Perfecta |

**Fórmula para correlación perfectamente negativa (ρ = -1):**
```
Cartera de mínima varianza (riesgo cero):
w₁ = σ₂ / (σ₁ + σ₂)
w₂ = σ₁ / (σ₁ + σ₂)
```

**Ejemplo:**
```
Si σ₁ = 20% y σ₂ = 10% con ρ = -1:
w₁ = 10% / (20% + 10%) = 33,3%
w₂ = 20% / (20% + 10%) = 66,7%

Esta combinación elimina completamente el riesgo.
```

### 1.3 La Frontera Eficiente

**Definición:** Conjunto de carteras que ofrecen la máxima rentabilidad esperada para cada nivel de riesgo.

**Propiedades:**
- Tiene forma de hipérbola en el espacio rentabilidad-riesgo
- Todas las carteras en la frontera son "eficientes"
- Ninguna cartera fuera de la frontera domina a una en la frontera
- El punto más a la izquierda es la cartera de mínima varianza global

**Cartera de mínima varianza global (2 activos):**
```
w₁ = (σ₂² - σ₁σ₂ρ) / (σ₁² + σ₂² - 2σ₁σ₂ρ)
w₂ = 1 - w₁
```

**Ejemplo:**
```
Activo A: σ = 25%
Activo B: σ = 15%
Correlación: ρ = 0,4

w₁ = (0,15² - 0,25×0,15×0,4) / (0,25² + 0,15² - 2×0,25×0,15×0,4)
w₁ = (0,0225 - 0,015) / (0,0625 + 0,0225 - 0,03)
w₁ = 0,0075 / 0,055 = 13,6%

w₂ = 1 - 0,136 = 86,4%

La cartera de mínima varianza: 13,6% Activo A + 86,4% Activo B
```

### 1.4 La Línea del Mercado de Capitales (CML)

**Introducción del activo libre de riesgo:**

Con un activo libre de riesgo (Rf), la frontera eficiente se convierte en una línea recta que:
- Parte de Rf en el eje Y
- Es tangente a la frontera eficiente de activos arriesgados
- El punto de tangencia es la cartera de mercado (M)

**Ecuación de la CML:**
```
E(Rp) = Rf + [(E(Rm) - Rf) / σm] × σp

Donde:
(E(Rm) - Rf) / σm = Ratio de Sharpe del mercado = pendiente de la CML
```

**Interpretación:**
- La pendiente indica el "precio del riesgo"
- Cuánta rentabilidad adicional se obtiene por unidad de riesgo
- Todas las carteras eficientes están sobre esta línea

**Ejemplo:**
```
Rf = 2%
E(Rm) = 8%
σm = 15%

Pendiente CML = (8% - 2%) / 15% = 0,4

Si un inversor quiere una cartera con σ = 10%:
E(Rp) = 2% + 0,4 × 10% = 6%

Para lograr σ = 10% con σm = 15%:
Peso en mercado = 10% / 15% = 66,7%
Peso en Rf = 33,3%
```

---

## 2. MODELOS DE VALORACIÓN DE ACTIVOS

### 2.1 Capital Asset Pricing Model (CAPM)

**Ecuación del CAPM:**
```
E(Ri) = Rf + βi × [E(Rm) - Rf]

Donde:
E(Ri) = rentabilidad esperada del activo i
Rf = tipo libre de riesgo
βi = beta del activo i
E(Rm) - Rf = prima de riesgo del mercado
```

**Cálculo de Beta:**
```
βi = Cov(Ri, Rm) / Var(Rm) = ρim × σi / σm

Donde:
ρim = correlación entre activo i y mercado
σi = desviación típica del activo i
σm = desviación típica del mercado
```

**Ejemplo de cálculo de beta:**
```
Acción XYZ:
- Correlación con IBEX: 0,75
- Volatilidad de XYZ: 30%
- Volatilidad del IBEX: 18%

β = 0,75 × (30% / 18%) = 0,75 × 1,67 = 1,25

Interpretación: Por cada 1% que se mueve el mercado,
XYZ se mueve aproximadamente 1,25%
```

**Ejemplo de rentabilidad esperada:**
```
Datos:
- Rf = 3%
- E(Rm) = 9%
- β acción = 1,4

E(Ri) = 3% + 1,4 × (9% - 3%) = 3% + 8,4% = 11,4%

Si la acción ofrece 13%, está INFRAVALORADA (alfa positivo)
Si la acción ofrece 10%, está SOBREVALORADA (alfa negativo)
```

**Interpretación de Beta:**

| Beta | Significado | Ejemplo típico |
|------|-------------|----------------|
| β > 1 | Más volátil que el mercado | Tecnológicas, cíclicas |
| β = 1 | Igual volatilidad que mercado | Índice de mercado |
| 0 < β < 1 | Menos volátil que mercado | Utilities, consumo básico |
| β = 0 | Sin correlación con mercado | Oro, algunos hedge funds |
| β < 0 | Correlación negativa | Muy raro, algunos inversos |

### 2.2 Security Market Line (SML)

**Diferencia CML vs SML:**

| Característica | CML | SML |
|----------------|-----|-----|
| Eje X | Riesgo total (σ) | Riesgo sistemático (β) |
| Aplica a | Carteras eficientes | Todos los activos |
| Pendiente | Sharpe del mercado | Prima de riesgo del mercado |

**Ecuación de la SML:**
```
E(Ri) = Rf + βi × [E(Rm) - Rf]

Es la misma ecuación del CAPM expresada gráficamente
```

**Uso en valoración:**
- Activos por encima de la SML: Infravalorados (comprar)
- Activos sobre la SML: Correctamente valorados
- Activos por debajo de la SML: Sobrevalorados (vender)

### 2.3 Alfa de Jensen

**Definición:**
```
αi = Ri - [Rf + βi × (Rm - Rf)]

Donde:
αi = alfa de Jensen
Ri = rentabilidad real obtenida
El resto es la rentabilidad esperada según CAPM
```

**Interpretación:**
- α > 0: Gestor ha generado valor (mejor que CAPM)
- α = 0: Gestor replica el mercado ajustado por riesgo
- α < 0: Gestor ha destruido valor

**Ejemplo:**
```
Fondo de inversión:
- Rentabilidad obtenida: 14%
- Beta del fondo: 1,2
- Rf: 2%
- Rm: 10%

Rentabilidad esperada CAPM = 2% + 1,2 × (10% - 2%) = 11,6%
Alfa = 14% - 11,6% = 2,4%

El gestor ha generado 2,4% de alfa (valor añadido)
```

### 2.4 Arbitrage Pricing Theory (APT)

**Modelo multifactorial:**
```
E(Ri) = Rf + β₁×RP₁ + β₂×RP₂ + ... + βn×RPn

Donde:
βk = sensibilidad al factor k
RPk = prima de riesgo del factor k
```

**Factores comunes en modelos APT:**

| Factor | Descripción | Prima típica |
|--------|-------------|--------------|
| Mercado | Riesgo de mercado general | 4-6% |
| Tamaño (SMB) | Small minus Big | 2-3% |
| Valor (HML) | High minus Low (B/P) | 3-4% |
| Momentum (MOM) | Winners minus Losers | 3-5% |
| Calidad (QMJ) | Quality minus Junk | 2-4% |

**Modelo de Fama-French (3 factores):**
```
E(Ri) - Rf = βm×(Rm-Rf) + βSMB×SMB + βHML×HML

Donde:
SMB = Small Minus Big (prima de tamaño)
HML = High Minus Low (prima de valor)
```

**Ejemplo Fama-French:**
```
Acción con:
- βm = 1,1
- βSMB = 0,5 (exposición a small caps)
- βHML = 0,3 (exposición a value)

Primas históricas:
- Prima mercado = 5%
- SMB = 2%
- HML = 3%

E(Ri) - Rf = 1,1×5% + 0,5×2% + 0,3×3%
E(Ri) - Rf = 5,5% + 1% + 0,9% = 7,4%

Si Rf = 2%, entonces E(Ri) = 9,4%
```

---

## 3. MEDIDAS DE PERFORMANCE

### 3.1 Ratio de Sharpe

**Fórmula:**
```
Sharpe = (Rp - Rf) / σp

Donde:
Rp = rentabilidad de la cartera
Rf = tipo libre de riesgo
σp = volatilidad de la cartera
```

**Interpretación:**
- Mide el exceso de rentabilidad por unidad de riesgo total
- Útil para comparar carteras no diversificadas
- Valores típicos: 0,5 (aceptable), 1,0 (bueno), >1,5 (excelente)

**Ejemplo:**
```
Cartera A: Rentabilidad 12%, Volatilidad 18%
Cartera B: Rentabilidad 9%, Volatilidad 10%
Rf = 2%

Sharpe A = (12% - 2%) / 18% = 0,56
Sharpe B = (9% - 2%) / 10% = 0,70

Conclusión: Cartera B es superior ajustada por riesgo total
```

### 3.2 Ratio de Treynor

**Fórmula:**
```
Treynor = (Rp - Rf) / βp

Donde:
βp = beta de la cartera respecto al mercado
```

**Interpretación:**
- Mide el exceso de rentabilidad por unidad de riesgo sistemático
- Útil para comparar carteras bien diversificadas
- Asume que el riesgo específico está diversificado

**Ejemplo:**
```
Cartera A: Rentabilidad 12%, Beta 1,3
Cartera B: Rentabilidad 10%, Beta 0,9
Rf = 2%

Treynor A = (12% - 2%) / 1,3 = 7,69%
Treynor B = (10% - 2%) / 0,9 = 8,89%

Conclusión: Cartera B es superior ajustada por riesgo sistemático
```

### 3.3 Information Ratio

**Fórmula:**
```
IR = (Rp - Rb) / TE

Donde:
Rb = rentabilidad del benchmark
TE = Tracking Error = σ(Rp - Rb)
```

**Interpretación:**
- Mide el exceso de rentabilidad sobre benchmark por unidad de riesgo activo
- Útil para evaluar gestión activa
- IR > 0,5 es bueno, IR > 1,0 es excelente

**Ejemplo:**
```
Fondo activo:
- Rentabilidad fondo: 11%
- Rentabilidad benchmark: 9%
- Tracking Error: 4%

IR = (11% - 9%) / 4% = 0,50

El gestor genera 0,50% de exceso de rentabilidad por cada 1% 
de desviación respecto al benchmark
```

### 3.4 Ratio de Sortino

**Fórmula:**
```
Sortino = (Rp - MAR) / Downside Deviation

Donde:
MAR = Minimum Acceptable Return (normalmente Rf)
Downside Deviation = σ de rentabilidades por debajo del MAR
```

**Interpretación:**
- Similar a Sharpe pero solo penaliza volatilidad negativa
- Más apropiado cuando las distribuciones son asimétricas
- Mejor para evaluar estrategias de protección del capital

**Ejemplo:**
```
Cartera con:
- Rentabilidad: 10%
- MAR: 3%
- Downside Deviation: 8%

Sortino = (10% - 3%) / 8% = 0,875
```

### 3.5 Comparativa de Medidas

| Medida | Riesgo utilizado | Mejor para | Limitaciones |
|--------|------------------|------------|--------------|
| **Sharpe** | Total (σ) | Carteras únicas/no diversificadas | Asume normalidad |
| **Treynor** | Sistemático (β) | Carteras diversificadas | Ignora riesgo específico |
| **Alfa Jensen** | CAPM | Evaluar gestión activa | Depende del β estimado |
| **Information Ratio** | Activo (TE) | Fondos vs benchmark | Sensible al benchmark |
| **Sortino** | Downside | Protección de capital | Requiere más datos |

### 3.6 Atribución de Rentabilidad

**Descomposición básica:**
```
Rentabilidad total = Asset Allocation + Security Selection + Interacción

Asset Allocation: Σ (wpi - wbi) × Rbi
Security Selection: Σ wbi × (Rpi - Rbi)
Interacción: Σ (wpi - wbi) × (Rpi - Rbi)
```

**Ejemplo de atribución:**
```
                    Benchmark           Cartera
                   Peso    Rent.      Peso    Rent.
Renta Variable     60%     10%        70%     12%
Renta Fija         40%     4%         30%     3%

Rent. Benchmark = 0,60×10% + 0,40×4% = 7,6%
Rent. Cartera = 0,70×12% + 0,30×3% = 9,3%
Exceso = 1,7%

Asset Allocation:
RV: (0,70-0,60) × 10% = 1,0%
RF: (0,30-0,40) × 4% = -0,4%
Total AA = 0,6%

Security Selection:
RV: 0,60 × (12%-10%) = 1,2%
RF: 0,40 × (3%-4%) = -0,4%
Total SS = 0,8%

Interacción:
RV: (0,70-0,60) × (12%-10%) = 0,2%
RF: (0,30-0,40) × (3%-4%) = 0,1%
Total Int = 0,3%

Verificación: 0,6% + 0,8% + 0,3% = 1,7% ✓
```

---

## 4. ASSET ALLOCATION

### 4.1 Asset Allocation Estratégico (SAA)

**Definición:** Distribución de activos a largo plazo basada en:
- Objetivos del inversor
- Horizonte temporal
- Tolerancia al riesgo
- Expectativas de mercado a largo plazo

**Proceso de SAA:**

1. **Definir universo de activos**
2. **Estimar expectativas (CMAs - Capital Market Assumptions)**
3. **Optimizar (Markowitz o variantes)**
4. **Implementar y rebalancear periódicamente**

**CMAs típicas (ejemplo):**

| Clase de activo | Rentabilidad esperada | Volatilidad | Correlación con RV |
|-----------------|----------------------|-------------|-------------------|
| Cash | 2,5% | 0,5% | 0,0 |
| RF Gobierno | 3,5% | 5% | -0,2 |
| RF Corporativa IG | 4,5% | 7% | 0,3 |
| RF High Yield | 6,0% | 12% | 0,6 |
| RV Desarrollada | 7,5% | 16% | 1,0 |
| RV Emergente | 9,0% | 22% | 0,8 |
| Inmobiliario | 6,0% | 14% | 0,5 |
| Materias primas | 4,0% | 18% | 0,2 |

### 4.2 Asset Allocation Táctico (TAA)

**Definición:** Desviaciones temporales del SAA para aprovechar oportunidades de corto/medio plazo.

**Límites típicos de TAA:**

| Clase de activo | SAA | Rango TAA | Límite desviación |
|-----------------|-----|-----------|-------------------|
| RV | 50% | 40-60% | ±10% |
| RF | 40% | 30-50% | ±10% |
| Alternativos | 10% | 5-15% | ±5% |

**Señales para TAA:**

| Señal | Interpretación | Acción TAA |
|-------|----------------|------------|
| Valoración extrema (PE histórico) | RV cara/barata | Infra/sobreponderar |
| Momentum de mercado | Tendencia | Seguir tendencia |
| Curva de tipos invertida | Recesión probable | Reducir RV |
| Spreads de crédito elevados | Estrés financiero | Reducir crédito |
| Volatilidad (VIX) elevada | Miedo | Oportunidad o cobertura |

### 4.3 Rebalanceo

**Estrategias de rebalanceo:**

| Estrategia | Descripción | Pros | Contras |
|------------|-------------|------|---------|
| **Calendario** | Periódico (mensual, trimestral) | Simple | Puede ser ineficiente |
| **Banda** | Cuando desviación > umbral | Eficiente | Más complejo |
| **Híbrido** | Calendario + banda | Equilibrado | Requiere seguimiento |

**Ejemplo de rebalanceo por bandas:**
```
SAA: 60% RV / 40% RF
Bandas: ±5%
Umbral de actuación: RV fuera de 55-65%

Situación actual tras rally de mercado:
- RV: 68% (valor 680.000 € de 1.000.000 €)
- RF: 32% (valor 320.000 €)

Acción: Vender RV y comprar RF hasta restaurar 60/40
- Vender RV: 80.000 € (de 680.000 a 600.000)
- Comprar RF: 80.000 € (de 320.000 a 400.000)
```

### 4.4 Asignación por Perfil de Riesgo

| Perfil | RV | RF | Alternativos | Volatilidad esperada |
|--------|----|----|--------------|---------------------|
| **Conservador** | 20% | 70% | 10% | 4-6% |
| **Moderado** | 40% | 50% | 10% | 7-10% |
| **Equilibrado** | 60% | 30% | 10% | 10-13% |
| **Dinámico** | 80% | 10% | 10% | 13-17% |
| **Agresivo** | 95% | 0% | 5% | 16-20% |

---

## 5. GESTIÓN Y CONTROL DE RIESGOS

### 5.1 Value at Risk (VaR) - Métodos de Cálculo

**A) VaR Paramétrico (Varianza-Covarianza):**
```
VaR = V × σ × z × √t

Donde:
V = valor de la posición
σ = volatilidad (diaria si VaR diario)
z = valor crítico de la normal
t = horizonte temporal en días

z valores:
- 90% confianza: 1,28
- 95% confianza: 1,65
- 99% confianza: 2,33
```

**Ejemplo VaR paramétrico:**
```
Cartera: 5.000.000 €
Volatilidad diaria: 1,2%
Confianza: 95%
Horizonte: 10 días

VaR (1 día, 95%) = 5.000.000 × 0,012 × 1,65 = 99.000 €
VaR (10 días, 95%) = 99.000 × √10 = 313.050 €
```

**B) VaR Histórico:**
```
1. Ordenar rentabilidades históricas de menor a mayor
2. Encontrar el percentil correspondiente al nivel de confianza
3. Aplicar a la cartera actual

Ejemplo con 500 observaciones diarias, VaR 95%:
- Percentil 5% = observación número 25 (500 × 5%)
- Si la 25ª peor rentabilidad fue -2,1%
- VaR (95%) = 5.000.000 × 2,1% = 105.000 €
```

**C) VaR por Simulación Monte Carlo:**
```
1. Generar miles de escenarios aleatorios
2. Calcular valor de la cartera en cada escenario
3. Ordenar resultados y encontrar percentil

Ventajas: Captura no-linealidades (opciones)
Desventajas: Computacionalmente intensivo
```

### 5.2 Expected Shortfall (CVaR)

**Definición:**
```
ES = Pérdida esperada dado que se ha superado el VaR
ES = E[Pérdida | Pérdida > VaR]

Relación típica: ES ≈ 1,25 × VaR (para distribución normal)
```

**Ejemplo:**
```
VaR (95%) = 100.000 €
Las 25 peores pérdidas (de 500) fueron:
120.000, 115.000, 110.000, ..., 100.000

ES = Media de las 25 peores = 108.000 €

Interpretación: Si el VaR se supera, la pérdida esperada 
es 108.000 € (no solo los 100.000 € del VaR)
```

### 5.3 Stress Testing

**Escenarios históricos:**

| Evento | Fecha | Caída RV | Impacto RF | Impacto EUR/USD |
|--------|-------|----------|------------|-----------------|
| Crisis 2008 | Sep-Oct 2008 | -35% | +5% (flight to quality) | -15% |
| Flash Crash | May 2010 | -10% (intradiario) | +1% | -3% |
| Crisis Euro | Jul-Ago 2011 | -25% | Mixto | -10% |
| COVID-19 | Mar 2020 | -35% | +3% | Volátil |

**Stress test hipotético:**
```
Escenario: Recesión severa
- RV: -40%
- RF Gobierno: +10%
- RF Corporativa: -15%
- High Yield: -30%

Cartera 60/40 (RV/RF Gov):
Impacto = 0,60 × (-40%) + 0,40 × (+10%) = -24% + 4% = -20%

Cartera 60/40 (RV/RF Corp):
Impacto = 0,60 × (-40%) + 0,40 × (-15%) = -24% - 6% = -30%
```

### 5.4 Límites de Riesgo

**Tipos de límites:**

| Tipo | Descripción | Ejemplo |
|------|-------------|---------|
| **VaR absoluto** | Máxima pérdida en € | VaR < 500.000 € |
| **VaR relativo** | % del patrimonio | VaR < 5% del AUM |
| **Tracking Error** | Desviación del benchmark | TE < 3% |
| **Concentración** | Peso máximo por posición | <5% por emisor |
| **Liquidez** | % liquidable en X días | >80% en 5 días |
| **Apalancamiento** | Gross/Net exposure | <150% / <110% |

### 5.5 Análisis de Sensibilidad

**Para carteras de renta fija:**
```
DV01 = Cambio en valor por 1 pb de movimiento en tipos
DV01 = -DM × Valor × 0,0001

Ejemplo:
Cartera RF: 10.000.000 €
Duración Modificada: 5 años
DV01 = -5 × 10.000.000 × 0,0001 = -5.000 €

Si tipos suben 25 pb: Pérdida ≈ 25 × 5.000 = 125.000 €
```

**Para carteras de renta variable:**
```
Beta × Valor = Exposición equivalente al mercado

Ejemplo:
Cartera RV: 8.000.000 €
Beta: 1,2
Exposición equivalente = 1,2 × 8.000.000 = 9.600.000 €

Si mercado cae 5%: Pérdida ≈ 9.600.000 × 5% = 480.000 €
```

---

## 6. GESTIÓN DE CARTERAS EN LA PRÁCTICA

### 6.1 Proceso de Inversión Institucional

**Fases del proceso:**

1. **Política de inversión (IPS):**
   - Objetivos de rentabilidad
   - Tolerancia al riesgo
   - Restricciones (liquidez, legales, ESG)
   - Horizonte temporal

2. **Asset Allocation Estratégico:**
   - CMAs y optimización
   - Definición de benchmark
   - Bandas de tolerancia

3. **Implementación:**
   - Selección de gestores/vehículos
   - Trading y ejecución
   - Gestión de liquidez

4. **Monitorización:**
   - Medición de performance
   - Control de riesgos
   - Rebalanceo

5. **Reporting:**
   - Informes periódicos
   - Atribución de resultados
   - Cumplimiento normativo

### 6.2 Selección de Fondos de Inversión

**Criterios cuantitativos:**

| Criterio | Métrica | Umbral típico |
|----------|---------|---------------|
| Rentabilidad | Alfa Jensen | > 0 consistente |
| Riesgo ajustado | Sharpe, Information Ratio | > mediana del peer group |
| Consistencia | % trimestres en 1º/2º cuartil | > 60% |
| Drawdown | Máxima caída | < benchmark |
| Tracking Error | σ(Rp-Rb) | Coherente con estilo |

**Criterios cualitativos:**

| Criterio | Aspectos a evaluar |
|----------|-------------------|
| Equipo gestor | Experiencia, estabilidad, skin in the game |
| Proceso inversión | Claridad, repetibilidad, ventaja competitiva |
| Infraestructura | Sistemas, control de riesgos, compliance |
| Alineación intereses | Comisiones, co-inversión, governance |

### 6.3 Costes y su Impacto

**Componentes del coste total:**

| Componente | Rango típico | Impacto 20 años (1M€) |
|------------|--------------|----------------------|
| TER (gestión) | 0,1%-2,0% | 20.000-400.000 € |
| Costes transacción | 0,1%-0,5% | Según rotación |
| Spread bid-ask | 0,05%-0,50% | Según rotación |
| Custodia | 0,02%-0,10% | 4.000-20.000 € |
| Asesoramiento | 0,25%-1,00% | 50.000-200.000 € |

**Impacto del TER a largo plazo:**
```
Inversión inicial: 100.000 €
Rentabilidad bruta: 7%
Horizonte: 20 años

Con TER 0,5%: 100.000 × (1,065)²⁰ = 352.365 €
Con TER 2,0%: 100.000 × (1,050)²⁰ = 265.330 €

Diferencia: 87.035 € (25% menos patrimonio final)
```

---

# PARTE III: CASOS PRÁCTICOS TIPO EFA

---

## CASO 1: Construcción de Cartera Óptima

**Situación:**
Un inversor dispone de 500.000 € y tiene acceso a tres activos:

| Activo | Rent. esperada | Volatilidad |
|--------|----------------|-------------|
| A (RV Europa) | 8% | 18% |
| B (RF Corporativa) | 4% | 6% |
| C (Inmobiliario) | 6% | 12% |

Correlaciones: ρAB = 0,2; ρAC = 0,5; ρBC = 0,3
Tipo libre de riesgo: 2%

**Preguntas:**
1. Calcule la rentabilidad y volatilidad de una cartera equiponderada
2. ¿Cómo mejoraría la cartera?

**Solución:**

```
1. Cartera equiponderada (33,3% cada uno):

Rentabilidad esperada:
E(Rp) = 0,333×8% + 0,333×4% + 0,333×6% = 6%

Varianza (usando fórmula completa):
σ²p = (0,333)²×(0,18)² + (0,333)²×(0,06)² + (0,333)²×(0,12)²
    + 2×0,333×0,333×0,18×0,06×0,2
    + 2×0,333×0,333×0,18×0,12×0,5
    + 2×0,333×0,333×0,06×0,12×0,3

σ²p = 0,00360 + 0,00040 + 0,00160
    + 0,00048 + 0,00240 + 0,00048
σ²p = 0,00896

σp = 9,47%

Sharpe = (6% - 2%) / 9,47% = 0,42

2. Para mejorar, reducir peso en A (alta volatilidad, baja correlación 
con B es buena pero no suficiente) y aumentar B:

Propuesta optimizada: 20% A, 50% B, 30% C
E(Rp) = 0,20×8% + 0,50×4% + 0,30×6% = 5,4%
σp ≈ 6,5% (menor volatilidad)
Sharpe = (5,4% - 2%) / 6,5% = 0,52 (mejor)
```

---

## CASO 2: Evaluación de Gestores

**Situación:**
Un comité de inversiones debe elegir entre dos fondos de renta variable:

| Métrica | Fondo X | Fondo Y | Benchmark |
|---------|---------|---------|-----------|
| Rentabilidad 3 años (anual) | 12% | 10% | 9% |
| Volatilidad | 20% | 14% | 16% |
| Beta | 1,25 | 0,85 | 1,00 |
| Tracking Error | 6% | 3% | - |

Tipo libre de riesgo: 2%

**Preguntas:**
1. Calcule Sharpe, Treynor, Alfa y Information Ratio de cada fondo
2. ¿Qué fondo recomendaría y por qué?

**Solución:**

```
FONDO X:
- Sharpe = (12% - 2%) / 20% = 0,50
- Treynor = (12% - 2%) / 1,25 = 8,0%
- Alfa = 12% - [2% + 1,25×(9%-2%)] = 12% - 10,75% = 1,25%
- IR = (12% - 9%) / 6% = 0,50

FONDO Y:
- Sharpe = (10% - 2%) / 14% = 0,57
- Treynor = (10% - 2%) / 0,85 = 9,4%
- Alfa = 10% - [2% + 0,85×(9%-2%)] = 10% - 7,95% = 2,05%
- IR = (10% - 9%) / 3% = 0,33

Resumen:
| Medida | Fondo X | Fondo Y | Mejor |
|--------|---------|---------|-------|
| Sharpe | 0,50 | 0,57 | Y |
| Treynor | 8,0% | 9,4% | Y |
| Alfa | 1,25% | 2,05% | Y |
| IR | 0,50 | 0,33 | X |

Recomendación: FONDO Y

Razones:
1. Mejor Sharpe (más rentabilidad por unidad de riesgo total)
2. Mejor Treynor (más rentabilidad por unidad de riesgo sistemático)
3. Mayor alfa (más valor añadido vs CAPM)
4. Aunque IR es menor, esto se debe a menor TE (más cercano al benchmark)
5. Menor volatilidad absoluta (14% vs 20%)
6. Menor beta = menor riesgo en caídas de mercado
```

---

## CASO 3: Control de Riesgos

**Situación:**
Una cartera de 10.000.000 € tiene la siguiente composición:
- 60% RV (volatilidad 18%, beta 1,1)
- 30% RF (volatilidad 5%, DM 4,5)
- 10% Alternativos (volatilidad 10%)

Correlación RV-RF: -0,2
Correlación RV-Alt: 0,4
Correlación RF-Alt: 0,1

**Preguntas:**
1. Calcule el VaR paramétrico (95%, 1 día)
2. ¿Cuál es el impacto si tipos suben 50 pb?
3. ¿Cuál es el impacto si RV cae 10%?

**Solución:**

```
1. VaR paramétrico:

Primero, volatilidad de la cartera (simplificada):
σ²p ≈ (0,6)²×(0,18)² + (0,3)²×(0,05)² + (0,1)²×(0,10)²
    + 2×0,6×0,3×0,18×0,05×(-0,2)
    + 2×0,6×0,1×0,18×0,10×0,4
    + 2×0,3×0,1×0,05×0,10×0,1

σ²p = 0,01166 + 0,000225 + 0,0001
    - 0,000648 + 0,000864 + 0,00003
σ²p = 0,01163

σp = 10,78% anual
σp diaria = 10,78% / √252 = 0,68%

VaR (95%, 1 día) = 10.000.000 × 0,68% × 1,65 = 112.200 €

2. Impacto de subida de tipos 50 pb:

Solo afecta a la RF:
Valor RF = 30% × 10.000.000 = 3.000.000 €
Impacto = -DM × Δy × Valor = -4,5 × 0,005 × 3.000.000
Impacto = -67.500 €

3. Impacto de caída RV 10%:

Valor RV = 60% × 10.000.000 = 6.000.000 €
Impacto = Beta × Caída mercado × Valor = 1,1 × 10% × 6.000.000
Impacto = -660.000 €

Nota: También hay efecto correlación en RF (flight to quality)
pero lo ignoramos para simplificar.
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

### Preguntas 1-10: Teoría de Carteras

**1.** Una cartera formada por dos activos con correlación +1 tendrá una volatilidad:

A) Menor que el promedio ponderado de volatilidades

B) Igual al promedio ponderado de volatilidades

C) Mayor que el promedio ponderado de volatilidades

D) Igual a cero

**Respuesta: B**

*Explicación: Con correlación perfectamente positiva (+1), no hay efecto diversificación. La volatilidad de la cartera es exactamente el promedio ponderado de las volatilidades individuales.*

---

**2.** La frontera eficiente de Markowitz representa:

A) Todas las carteras posibles con dos activos

B) Las carteras que minimizan el riesgo para cada nivel de rentabilidad

C) Las carteras de renta fija únicamente

D) Las carteras con beta igual a 1

**Respuesta: B**

*Explicación: La frontera eficiente incluye todas las carteras que ofrecen la máxima rentabilidad para cada nivel de riesgo (o mínimo riesgo para cada rentabilidad).*

---

**3.** Si dos activos tienen correlación -1 y volatilidades de 20% y 10%, la cartera de riesgo cero requiere pesos de:

A) 50% y 50%

B) 33% y 67%

C) 67% y 33%

D) 25% y 75%

**Respuesta: B**

*Explicación: w₁ = σ₂/(σ₁+σ₂) = 10%/(20%+10%) = 33,3%. El activo más volátil tiene menor peso.*

---

**4.** La Línea del Mercado de Capitales (CML):

A) Relaciona rentabilidad esperada con beta

B) Relaciona rentabilidad esperada con riesgo total

C) Solo incluye activos de renta variable

D) Tiene pendiente negativa en mercados bajistas

**Respuesta: B**

*Explicación: La CML muestra la relación entre rentabilidad esperada y riesgo total (medido por volatilidad) para carteras eficientes.*

---

**5.** El ratio de Sharpe del mercado es 0,5. Si Rf = 3% y un inversor desea volatilidad del 10%, su rentabilidad esperada será:

A) 5%

B) 6%

C) 8%

D) 10%

**Respuesta: C**

*Explicación: E(R) = Rf + Sharpe × σ = 3% + 0,5 × 10% = 8%*

---

**6.** La cartera de mínima varianza global:

A) Siempre tiene rentabilidad esperada cero

B) Es el punto más a la izquierda de la frontera eficiente

C) Tiene la máxima rentabilidad

D) Solo incluye el activo libre de riesgo

**Respuesta: B**

*Explicación: La cartera de mínima varianza global tiene el menor riesgo posible y está en el punto más a la izquierda de la frontera eficiente.*

---

**7.** El efecto diversificación es máximo cuando la correlación entre activos es:

A) +1

B) 0

C) -1

D) Variable según la volatilidad

**Respuesta: C**

*Explicación: Con correlación -1 es posible eliminar todo el riesgo (máxima diversificación posible).*

---

**8.** Si una cartera tiene 40% en un activo con σ=15% y 60% en otro con σ=25%, y correlación 0,5, la varianza de la cartera es aproximadamente:

A) 0,0225

B) 0,0315

C) 0,0405

D) 0,0441

**Respuesta: B**

*Explicación: σ²p = (0,4)²×(0,15)² + (0,6)²×(0,25)² + 2×0,4×0,6×0,15×0,25×0,5 = 0,0036 + 0,0225 + 0,009 = 0,0351*

---

**9.** El teorema de separación de Tobin implica que:

A) Cada inversor debe tener una cartera diferente de activos arriesgados

B) Todos los inversores deben tener la misma cartera de activos arriesgados

C) No se debe combinar activo libre de riesgo con activos arriesgados

D) La diversificación no es relevante

**Respuesta: B**

*Explicación: Tobin demostró que la cartera óptima de activos arriesgados es única (cartera de mercado). Los inversores solo varían la proporción entre esta cartera y el activo libre de riesgo.*

---

**10.** Una cartera eficiente en el sentido de Markowitz:

A) Tiene el máximo ratio de Sharpe

B) Ofrece la máxima rentabilidad para su nivel de riesgo

C) Siempre incluye todos los activos disponibles

D) Tiene correlación cero con el mercado

**Respuesta: B**

*Explicación: Una cartera es eficiente si no existe otra cartera que ofrezca mayor rentabilidad con el mismo riesgo (o menor riesgo con la misma rentabilidad).*

---

### Preguntas 11-20: CAPM y Modelos de Valoración

**11.** Según el CAPM, la rentabilidad esperada de un activo depende de:

A) Su riesgo total

B) Su riesgo específico

C) Su riesgo sistemático (beta)

D) Su volatilidad histórica

**Respuesta: C**

*Explicación: El CAPM establece que solo el riesgo sistemático (medido por beta) es remunerado, ya que el riesgo específico puede diversificarse.*

---

**12.** Una acción tiene beta 1,5, Rf = 2%, y prima de mercado 6%. Su rentabilidad esperada según CAPM es:

A) 9%

B) 11%

C) 13%

D) 15%

**Respuesta: B**

*Explicación: E(R) = Rf + β×(Rm-Rf) = 2% + 1,5×6% = 11%*

---

**13.** Un activo que cotiza por encima de la Security Market Line (SML) está:

A) Correctamente valorado

B) Sobrevalorado

C) Infravalorado

D) En equilibrio

**Respuesta: C**

*Explicación: Si la rentabilidad esperada es mayor que la que predice CAPM (por encima de la SML), el activo ofrece más rentabilidad de la justa para su riesgo → infravalorado.*

---

**14.** El alfa de Jensen de un fondo que obtuvo 15% con beta 1,2, cuando Rf=3% y Rm=10%, es:

A) 1,6%

B) 2,0%

C) 3,6%

D) 5,0%

**Respuesta: C**

*Explicación: α = R - [Rf + β×(Rm-Rf)] = 15% - [3% + 1,2×7%] = 15% - 11,4% = 3,6%*

---

**15.** La diferencia principal entre CML y SML es que:

A) La CML usa beta y la SML usa volatilidad

B) La CML aplica a carteras eficientes y la SML a todos los activos

C) La CML solo aplica a renta fija

D) No hay diferencia

**Respuesta: B**

*Explicación: La CML (eje X = σ) aplica a carteras eficientes. La SML (eje X = β) aplica a cualquier activo.*

---

**16.** En el modelo de Fama-French de 3 factores, HML representa:

A) La prima por tamaño

B) La prima por valor (alto valor contable / precio)

C) La prima por momentum

D) La prima de mercado

**Respuesta: B**

*Explicación: HML = High Minus Low se refiere al factor valor, calculado como la diferencia entre rentabilidad de acciones con alto B/P (value) y bajo B/P (growth).*

---

**17.** Si la beta de una acción es 0,8, esto significa que:

A) La acción es más volátil que el mercado

B) La acción se mueve en dirección opuesta al mercado

C) Por cada 1% que mueve el mercado, la acción mueve 0,8%

D) La acción no tiene riesgo sistemático

**Respuesta: C**

*Explicación: Beta mide la sensibilidad al mercado. Beta 0,8 significa que si el mercado sube/baja 1%, la acción sube/baja 0,8%.*

---

**18.** El modelo APT (Arbitrage Pricing Theory) difiere del CAPM en que:

A) No requiere activo libre de riesgo

B) Considera múltiples factores de riesgo

C) Solo aplica a renta fija

D) Ignora la diversificación

**Respuesta: B**

*Explicación: APT es un modelo multifactorial que considera varios factores de riesgo (mercado, tamaño, valor, etc.) mientras CAPM solo considera el factor mercado.*

---

**19.** Para calcular beta se utiliza:

A) La varianza del activo

B) La covarianza entre activo y mercado dividida por varianza del mercado

C) El ratio de Sharpe del activo

D) La desviación típica del activo

**Respuesta: B**

*Explicación: β = Cov(Ri, Rm) / Var(Rm)*

---

**20.** Una cartera con beta 0 tiene:

A) Rentabilidad esperada igual a cero

B) Rentabilidad esperada igual al tipo libre de riesgo

C) Riesgo total igual a cero

D) Correlación perfecta con el mercado

**Respuesta: B**

*Explicación: Según CAPM, E(R) = Rf + β×(Rm-Rf). Si β=0, entonces E(R) = Rf.*

---

### Preguntas 21-30: Medidas de Performance

**21.** El ratio de Sharpe mide:

A) Exceso de rentabilidad por unidad de riesgo sistemático

B) Exceso de rentabilidad por unidad de riesgo total

C) Rentabilidad total sin ajustar por riesgo

D) La sensibilidad al mercado

**Respuesta: B**

*Explicación: Sharpe = (Rp - Rf) / σp, donde σp es el riesgo total (volatilidad).*

---

**22.** Un fondo con rentabilidad 8%, Rf 2% y Tracking Error 4% tiene Information Ratio de:

A) 0,5 si el benchmark rindió 6%

B) 1,5 si el benchmark rindió 2%

C) 2,0 si el benchmark rindió 4%

D) A y B son correctas

**Respuesta: D**

*Explicación: IR = (Rp - Rb) / TE. Con Rb=6%: IR=(8-6)/4=0,5. Con Rb=2%: IR=(8-2)/4=1,5.*

---

**23.** El ratio de Treynor es preferible al de Sharpe cuando:

A) La cartera no está diversificada

B) La cartera está bien diversificada

C) Se evalúa un fondo de renta fija

D) No se conoce el beta

**Respuesta: B**

*Explicación: Treynor usa beta (riesgo sistemático). Es apropiado cuando el riesgo específico está diversificado y solo importa el sistemático.*

---

**24.** Un Information Ratio de 0,75 significa que:

A) El fondo supera al benchmark en 75% del tiempo

B) Por cada 1% de tracking error, se genera 0,75% de exceso de rentabilidad

C) El alfa es 0,75

D) El beta es 0,75

**Respuesta: B**

*Explicación: IR = (Rp - Rb) / TE. Un IR de 0,75 indica 0,75% de exceso de rentabilidad por cada punto porcentual de tracking error.*

---

**25.** El ratio de Sortino difiere del de Sharpe en que:

A) Usa el benchmark en lugar de Rf

B) Solo considera la volatilidad negativa (downside)

C) Usa beta en lugar de volatilidad

D) Ignora la rentabilidad

**Respuesta: B**

*Explicación: Sortino usa Downside Deviation (volatilidad solo de rentabilidades negativas) en lugar de volatilidad total, penalizando solo la volatilidad "mala".*

---

**26.** En la atribución de rentabilidad, el "efecto selección" mide:

A) El impacto de las decisiones de ponderación sectorial

B) El impacto de la selección de valores dentro de cada sector

C) El efecto de la interacción entre allocation y selección

D) La rentabilidad total del benchmark

**Respuesta: B**

*Explicación: Security Selection mide el valor añadido por elegir mejores valores que el benchmark dentro de cada categoría.*

---

**27.** Una cartera con Sharpe 0,8 y otra con Sharpe 0,6:

A) La primera siempre tiene mayor rentabilidad

B) La primera tiene mejor relación rentabilidad/riesgo

C) La primera tiene menor volatilidad

D) La primera tiene mayor beta

**Respuesta: B**

*Explicación: Mayor Sharpe = mejor rentabilidad ajustada por riesgo total. No implica mayor rentabilidad ni menor volatilidad en términos absolutos.*

---

**28.** El Tracking Error se calcula como:

A) La diferencia entre rentabilidad del fondo y del benchmark

B) La desviación típica de la diferencia de rentabilidades

C) El beta del fondo respecto al benchmark

D) El exceso de rentabilidad dividido por sigma

**Respuesta: B**

*Explicación: TE = σ(Rp - Rb), la volatilidad de los excesos de rentabilidad.*

---

**29.** Si un gestor tiene alfa positivo pero Information Ratio negativo, significa que:

A) Es imposible, siempre van en la misma dirección

B) Genera exceso de rentabilidad pero con muy alto tracking error

C) Supera al benchmark pero con menor volatilidad

D) Es un error de cálculo

**Respuesta: A**

*Explicación: Si α > 0, entonces Rp > esperado CAPM. El IR = (Rp-Rb)/TE. Si Rp > Rb, ambos deberían ser positivos (asumiendo TE positivo por definición).*

---

**30.** Para evaluar un fondo que debe replicar un índice, la medida más apropiada es:

A) Ratio de Sharpe

B) Alfa de Jensen

C) Tracking Error

D) Ratio de Treynor

**Respuesta: C**

*Explicación: Para fondos pasivos/indexados, el objetivo es minimizar la desviación respecto al benchmark. El Tracking Error mide exactamente esto.*

---

### Preguntas 31-40: Asset Allocation y Gestión de Riesgos

**31.** El Asset Allocation Estratégico se caracteriza por:

A) Cambios frecuentes basados en timing de mercado

B) Distribución de largo plazo basada en perfil del inversor

C) Solo incluir renta variable

D) Ignorar las expectativas de mercado

**Respuesta: B**

*Explicación: SAA define la distribución de activos a largo plazo basándose en objetivos, horizonte y tolerancia al riesgo del inversor.*

---

**32.** El Asset Allocation Táctico busca:

A) Mantener los pesos constantes en todo momento

B) Aprovechar oportunidades de corto plazo desviándose del SAA

C) Eliminar todo riesgo de la cartera

D) Replicar exactamente un índice

**Respuesta: B**

*Explicación: TAA permite desviaciones temporales del SAA para aprovechar valoraciones atractivas o evitar riesgos de corto plazo.*

---

**33.** El VaR (95%, 1 día) de una posición de 2 millones con volatilidad diaria del 1,5% es aproximadamente:

A) 30.000 €

B) 49.500 €

C) 69.900 €

D) 99.000 €

**Respuesta: B**

*Explicación: VaR = V × σ × z = 2.000.000 × 0,015 × 1,65 = 49.500 €*

---

**34.** El Expected Shortfall (CVaR) al 95%:

A) Es siempre menor que el VaR al 95%

B) Es la pérdida esperada cuando se supera el VaR

C) Ignora las pérdidas extremas

D) Es igual al VaR multiplicado por 0,95

**Respuesta: B**

*Explicación: ES (o CVaR) es la pérdida promedio esperada en los casos donde se supera el VaR. Siempre es mayor o igual que el VaR.*

---

**35.** Una estrategia de rebalanceo por bandas:

A) Rebalancea con frecuencia fija independientemente de los pesos

B) Rebalancea cuando los pesos se desvían más allá de un umbral

C) Nunca rebalancea

D) Solo rebalancea cuando el mercado cae

**Respuesta: B**

*Explicación: El rebalanceo por bandas actúa cuando la desviación respecto al SAA supera un umbral predefinido.*

---

**36.** El DV01 de una cartera de renta fija mide:

A) La duración modificada

B) El cambio de valor por 1 punto básico de movimiento en tipos

C) La convexidad

D) El riesgo de crédito

**Respuesta: B**

*Explicación: DV01 (Dollar Value of 01) es el cambio en valor de la cartera por 1 pb de movimiento en tipos de interés.*

---

**37.** Para un cliente conservador con horizonte de 3 años, el SAA más apropiado sería:

A) 80% RV, 20% RF

B) 60% RV, 40% RF

C) 20% RV, 80% RF

D) 100% RV

**Respuesta: C**

*Explicación: Perfil conservador + horizonte corto = predominio de RF para proteger capital.*

---

**38.** El stress testing difiere del VaR en que:

A) El VaR considera escenarios extremos y el stress test no

B) El stress test evalúa escenarios específicos, no probabilísticos

C) El stress test solo aplica a renta variable

D) No hay diferencia significativa

**Respuesta: B**

*Explicación: VaR es una medida probabilística. Stress testing evalúa el impacto de escenarios específicos (históricos o hipotéticos) sin asignar probabilidades.*

---

**39.** El TER de un fondo incluye:

A) Solo la comisión de gestión

B) Comisión de gestión más otros gastos corrientes

C) Los costes de transacción

D) El spread bid-ask

**Respuesta: B**

*Explicación: TER (Total Expense Ratio) incluye comisión de gestión, depositaría, auditoría y otros gastos corrientes. No incluye costes de transacción.*

---

**40.** Si la correlación entre RV y RF es -0,2, en un escenario de caída de RV:

A) La RF también caerá

B) La RF tenderá a subir (flight to quality)

C) La correlación es irrelevante

D) La cartera no se verá afectada

**Respuesta: B**

*Explicación: Correlación negativa significa que cuando un activo cae, el otro tiende a subir. Esto es el "flight to quality" típico en crisis.*

---

# PARTE V: CHECKLIST DE DOMINIO DEL MÓDULO

Antes de presentarte al examen, verifica que puedes:

## Teoría de Carteras
- [ ] Calcular rentabilidad y varianza de carteras de 2 y más activos
- [ ] Entender el efecto de la correlación en la diversificación
- [ ] Identificar carteras eficientes y la frontera eficiente
- [ ] Explicar la CML y el teorema de separación

## CAPM y Modelos
- [ ] Calcular rentabilidad esperada usando CAPM
- [ ] Calcular e interpretar beta
- [ ] Calcular alfa de Jensen
- [ ] Distinguir CML de SML
- [ ] Describir modelo de Fama-French y APT

## Medidas de Performance
- [ ] Calcular Sharpe, Treynor, Information Ratio
- [ ] Elegir la medida apropiada según contexto
- [ ] Realizar atribución básica de rentabilidad
- [ ] Interpretar y comparar gestores usando estas métricas

## Asset Allocation
- [ ] Diseñar SAA según perfil del cliente
- [ ] Implementar TAA con señales de mercado
- [ ] Diseñar estrategia de rebalanceo
- [ ] Justificar decisiones de asset allocation

## Gestión de Riesgos
- [ ] Calcular VaR paramétrico
- [ ] Interpretar Expected Shortfall
- [ ] Diseñar escenarios de stress test
- [ ] Calcular DV01 y sensibilidades
- [ ] Establecer límites de riesgo apropiados

---

**Fin del Módulo 2 - Nivel II**

*Tiempo estimado de estudio: 15-20 horas*

*Próxima revisión recomendada: 1 semana antes del examen*
