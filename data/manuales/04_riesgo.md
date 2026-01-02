# 📘 MANUAL 4 · RIESGO Y RENTABILIDAD

**Preparación integral orientada a examen**

---

## 🎯 Objetivo del manual

Este manual cubre los conceptos de riesgo, rentabilidad y las medidas estadísticas que aparecen en el examen EFA.

El enfoque es **reconocimiento de fórmulas y cálculo rápido**: identificar qué medida usar y aplicarla correctamente.

**Idea clave EFPA**: En riesgo y rentabilidad, el examen premia reconocer la fórmula correcta más que entender la teoría profunda.

---

## 1️⃣ RENTABILIDAD: Conceptos básicos

### Rentabilidad simple

**Fórmula básica**:

**R = (Valor final - Valor inicial) / Valor inicial × 100**

**Ejemplo**:
> Compras acción a 50€, vendes a 55€
> R = (55 - 50) / 50 × 100 = **10%**

---

### Rentabilidad con dividendos

**Fórmula completa**:

**R = (Vf - Vi + Dividendos) / Vi × 100**

**Ejemplo**:
> Compras acción a 100€, recibes dividendo 3€, vendes a 105€
> R = (105 - 100 + 3) / 100 × 100 = **8%**

**✅ Regla EFPA**: No olvides sumar los dividendos a la rentabilidad.

---

### Rentabilidad anualizada

Si tienes rentabilidad de un período diferente a 1 año, para anualizar:

**Fórmula**:

**R anual = (1 + R período)^(1/n) - 1**

Donde n = número de años

**Ejemplo**:
> Rentabilidad 21% en 2 años
> R anual = (1,21)^(1/2) - 1 = 1,10 - 1 = **10% anual**

---

### Rentabilidad nominal vs real

**Rentabilidad nominal**: La que ves directamente (sin ajustar inflación)

**Rentabilidad real**: Ajustada por inflación

**Fórmula (aproximada)**:

**R real ≈ R nominal - Inflación**

**Fórmula (exacta)**:

**R real = [(1 + R nominal) / (1 + Inflación)] - 1**

**Ejemplo**:
> Rentabilidad nominal: 8%
> Inflación: 3%
> R real (aproximada) = 8% - 3% = **5%**
> R real (exacta) = (1,08 / 1,03) - 1 = **4,85%**

🚨 **Trampa típica**: En examen, si piden "rentabilidad real" usa la fórmula exacta si te dan cifras precisas, o la aproximada si es conceptual.

**✅ Regla EFPA**: R real = (1+Rnom)/(1+Infl) - 1

---

## 2️⃣ RENTABILIDAD DE CARTERAS

### Rentabilidad de una cartera (media ponderada)

**Fórmula**:

**Rc = (w1 × R1) + (w2 × R2) + ... + (wn × Rn)**

Donde:
- w = peso (%) de cada activo
- R = rentabilidad de cada activo

**Ejemplo**:
> Cartera con:
> - 60% en activo A (rentabilidad 8%)
> - 40% en activo B (rentabilidad 3%)
> 
> Rc = (0,60 × 8) + (0,40 × 3) = 4,8 + 1,2 = **6,0%**

**✅ Regla EFPA**: La rentabilidad de cartera es la suma ponderada por pesos.

---

### Pregunta típica EFA

> "Cartera con 70% renta variable (12% anual) y 30% renta fija (4% anual). ¿Rentabilidad esperada?"

**Cálculo**:
Rc = (0,70 × 12) + (0,30 × 4) = 8,4 + 1,2 = **9,6%**

---

## 3️⃣ RIESGO: Tipos y medidas

### Definición de riesgo financiero

**Riesgo** = Incertidumbre sobre la rentabilidad futura (posibilidad de que el resultado real difiera del esperado).

---

### Tipos de riesgo

**Riesgo sistemático (de mercado)**:
- Afecta a todos los activos del mercado
- **No se puede eliminar** con diversificación
- Ejemplos: crisis económica, cambios regulatorios, guerras
- También llamado: riesgo no diversificable

**Riesgo no sistemático (específico o idiosincrático)**:
- Afecta solo a una empresa o sector concreto
- **SÍ se puede reducir** con diversificación
- Ejemplos: cambio de CEO, huelga en una empresa, problemas de un sector
- También llamado: riesgo diversificable

🚨 **Trampa típica**: Preguntar qué riesgo se elimina con diversificación → **No sistemático**.

**✅ Regla EFPA**: 
- Sistemático = NO eliminable
- No sistemático = SÍ reducible con diversificación

---

### Otros tipos de riesgo (reconocimiento)

**Riesgo de tipo de interés**:
- Afecta principalmente a renta fija
- Mayor en bonos de larga duración

**Riesgo de tipo de cambio (divisa)**:
- Al invertir en activos en moneda extranjera
- Puede ser positivo (si divisa se aprecia) o negativo

**Riesgo de liquidez**:
- Dificultad para vender un activo rápidamente sin pérdidas significativas

**Riesgo de crédito**:
- Que el emisor no pague (default)
- Importante en bonos corporativos

**Riesgo de reinversión**:
- Incertidumbre sobre rentabilidad al reinvertir cupones/dividendos

---

## 4️⃣ VOLATILIDAD (Desviación estándar)

### Definición

**Volatilidad (σ)** = Medida estadística de la **dispersión de rentabilidades** respecto a su media.

A mayor volatilidad → Mayor riesgo → Rentabilidades más variables

---

### Interpretación práctica

**Ejemplo**:
> Fondo A: Rentabilidad media 8%, volatilidad 5%
> Fondo B: Rentabilidad media 8%, volatilidad 15%

**Interpretación**: Ambos tienen misma rentabilidad esperada, pero B tiene mayor riesgo (sus rentabilidades varían más).

**Regla aproximada (distribución normal)**:
- 68% de las veces, rentabilidad estará en: Media ± 1 × Volatilidad
- 95% de las veces, rentabilidad estará en: Media ± 2 × Volatilidad

**Aplicación al ejemplo del Fondo B**:
> 68% de las veces: entre 8-15 = -7% y 8+15 = 23%
> 95% de las veces: entre 8-30 = -22% y 8+30 = 38%

**✅ Regla EFPA**: Volatilidad ↑ → Riesgo ↑ (mayor dispersión de rentabilidades).

---

## 5️⃣ DIVERSIFICACIÓN

### Principio fundamental

**"No pongas todos los huevos en la misma cesta"**

Al combinar activos con rentabilidades que **no se mueven igual** (baja correlación), el riesgo total de la cartera se reduce.

---

### Correlación

**Correlación** = Medida de cómo se mueven dos activos entre sí.

**Valores**:
- **+1**: Se mueven exactamente igual (perfecta correlación positiva)
- **0**: No hay relación entre movimientos
- **-1**: Se mueven en direcciones opuestas (perfecta correlación negativa)

**Para diversificar mejor**: Buscar activos con correlación **baja o negativa**.

**Ejemplo**:
> Activo A: Acciones tecnología
> Activo B: Bonos del Estado
> Correlación baja (cercana a 0 o negativa)
> → Buena diversificación

---

### Riesgo de cartera vs riesgo individual

**Regla fundamental**:

**Riesgo de cartera < Suma de riesgos individuales**

(Siempre que correlación < 1)

**Ejemplo conceptual**:
> Activo A: volatilidad 20%
> Activo B: volatilidad 20%
> Cartera 50%-50%: volatilidad **< 20%** (si correlación < 1)

**✅ Regla EFPA**: Diversificación reduce riesgo no sistemático.

---

## 6️⃣ BETA (β)

### Definición

**Beta** = Medida del **riesgo sistemático** de un activo respecto al mercado.

Indica cómo se mueve un activo cuando el mercado se mueve.

---

### Interpretación de valores

**β = 1**: El activo se mueve igual que el mercado
- Si mercado sube 10% → activo sube 10%
- Riesgo sistemático igual al del mercado

**β > 1**: El activo amplifica los movimientos del mercado (más volátil)
- Si β = 1,5 y mercado sube 10% → activo sube aprox. 15%
- Mayor riesgo sistemático que el mercado

**β < 1**: El activo amortigua los movimientos del mercado (menos volátil)
- Si β = 0,5 y mercado sube 10% → activo sube aprox. 5%
- Menor riesgo sistemático que el mercado

**β = 0**: El activo no se ve afectado por movimientos del mercado
- Ejemplo: Letras del Tesoro

**β negativo**: El activo se mueve en dirección opuesta al mercado
- Raro, pero puede ocurrir (ej: ciertos seguros, oro)

---

### Ejemplos prácticos

> Acción de empresa cíclica (construcción): β = 1,8
> Significado: Más volátil que el mercado, amplifica subidas y bajadas

> Acción de utilities (eléctricas): β = 0,7
> Significado: Menos volátil que el mercado, defensiva

**✅ Regla EFPA**: β > 1 → más volátil que mercado | β < 1 → menos volátil.

---

### Beta de una cartera

**Fórmula**:

**βc = (w1 × β1) + (w2 × β2) + ... + (wn × βn)**

Igual que la rentabilidad, la beta de cartera es la media ponderada.

**Ejemplo**:
> Cartera con:
> - 60% en activo A (β = 1,2)
> - 40% en activo B (β = 0,8)
> 
> βc = (0,60 × 1,2) + (0,40 × 0,8) = 0,72 + 0,32 = **1,04**

---

## 7️⃣ CAPM (Capital Asset Pricing Model)

### Definición

Modelo que relaciona **rentabilidad esperada** de un activo con su **riesgo sistemático** (beta).

---

### Fórmula (la más importante del manual)

**E(Ri) = Rf + βi × [E(Rm) - Rf]**

Donde:
- **E(Ri)** = Rentabilidad esperada del activo i
- **Rf** = Tasa libre de riesgo (ej: Letras del Tesoro)
- **βi** = Beta del activo
- **E(Rm)** = Rentabilidad esperada del mercado
- **[E(Rm) - Rf]** = Prima de riesgo del mercado

---

### Interpretación componentes

**Rf (tasa libre de riesgo)**:
- Rentabilidad de un activo sin riesgo
- Típicamente: Letras del Tesoro a corto plazo
- Ejemplo: 2%

**Prima de riesgo del mercado [E(Rm) - Rf]**:
- Rentabilidad adicional que exige el mercado por asumir riesgo
- Ejemplo: Si E(Rm) = 10% y Rf = 2%, prima = 8%

**βi × Prima de riesgo**:
- Rentabilidad adicional exigida al activo según su riesgo sistemático

---

### Ejemplo de cálculo (pregunta típica EFA)

**Datos**:
- Tasa libre de riesgo: 3%
- Rentabilidad esperada del mercado: 11%
- Beta de la acción: 1,5

**Pregunta**: ¿Rentabilidad esperada de la acción según CAPM?

**Solución**:
E(Ri) = 3 + 1,5 × (11 - 3)  
E(Ri) = 3 + 1,5 × 8  
E(Ri) = 3 + 12  
**E(Ri) = 15%**

**Interpretación**: Por tener β = 1,5 (mayor riesgo sistemático), el activo debe ofrecer mayor rentabilidad (15% vs 11% del mercado).

---

### Casos típicos con CAPM

**Caso 1: β = 1**
> E(Ri) = Rf + 1 × [E(Rm) - Rf] = **E(Rm)**
> Rentabilidad igual al mercado

**Caso 2: β = 0**
> E(Ri) = Rf + 0 × [E(Rm) - Rf] = **Rf**
> Rentabilidad igual a tasa libre de riesgo

**Caso 3: β = 2**
> E(Ri) = Rf + 2 × [E(Rm) - Rf]
> Rentabilidad mucho mayor al mercado (por alto riesgo)

**✅ Regla EFPA**: CAPM → Memoriza la fórmula exacta, es pregunta recurrente.

---

## 8️⃣ RATIO DE SHARPE

### Definición

**Ratio de Sharpe** = Medida de **rentabilidad ajustada por riesgo total**.

Indica cuánta rentabilidad adicional obtienes por cada unidad de riesgo asumido.

---

### Fórmula

**Sharpe = (Rp - Rf) / σp**

Donde:
- **Rp** = Rentabilidad de la cartera
- **Rf** = Tasa libre de riesgo
- **σp** = Volatilidad (desviación estándar) de la cartera

---

### Interpretación

**Sharpe alto**: Mejor rentabilidad por unidad de riesgo → Más eficiente

**Sharpe bajo**: Poca rentabilidad adicional por el riesgo asumido

**Comparación**: Al comparar fondos/carteras, el que tenga **mayor Sharpe** es más eficiente (mejor relación rentabilidad/riesgo).

---

### Ejemplo de cálculo

**Fondo A**:
- Rentabilidad: 12%
- Volatilidad: 15%
- Rf: 2%

**Sharpe A = (12 - 2) / 15 = 10 / 15 = 0,67**

**Fondo B**:
- Rentabilidad: 10%
- Volatilidad: 8%
- Rf: 2%

**Sharpe B = (10 - 2) / 8 = 8 / 8 = 1,00**

**Conclusión**: Aunque Fondo A tiene mayor rentabilidad absoluta, **Fondo B es más eficiente** (mejor Sharpe).

**✅ Regla EFPA**: Mayor Sharpe → mejor eficiencia (rentabilidad/riesgo).

---

### Pregunta típica EFA

> "¿Qué ratio mide la rentabilidad ajustada por riesgo total?"
> A) Beta
> B) **Ratio de Sharpe** ✅
> C) Ratio de Treynor
> D) Alpha de Jensen

---

## 9️⃣ FRONTERA EFICIENTE (concepto básico)

### Definición

**Frontera eficiente** = Conjunto de carteras que ofrecen la **máxima rentabilidad para cada nivel de riesgo**.

---

### Concepto visual

Imagina un gráfico:
- Eje X: Riesgo (volatilidad)
- Eje Y: Rentabilidad

La frontera eficiente es la curva superior de todas las combinaciones posibles de carteras.

**Carteras en la frontera**: Eficientes (no puedes mejorar rentabilidad sin aumentar riesgo)

**Carteras bajo la frontera**: Ineficientes (puedes mejorar rentabilidad sin aumentar riesgo)

---

### Cartera de mínima varianza

**Cartera de mínima varianza** = Cartera en la frontera eficiente con **menor riesgo**.

Es el punto más a la izquierda de la frontera eficiente.

**✅ Regla EFPA**: Frontera eficiente = máxima rentabilidad para cada nivel de riesgo.

---

## 🔟 MEDIDAS DE RIESGO ESPECÍFICAS

### VaR (Value at Risk)

**Definición**: Pérdida máxima esperada en un horizonte temporal dado, con un nivel de confianza determinado.

**Ejemplo**:
> VaR 95% a 1 día = 50.000€
> Significa: Hay 95% de probabilidad de que la pérdida no supere 50.000€ en 1 día (o 5% de probabilidad de pérdida mayor a 50.000€)

**Limitaciones**: No dice nada sobre pérdidas en el 5% peor de casos.

---

### Drawdown

**Definición**: Caída máxima desde un pico hasta un valle (pérdida máxima desde el punto más alto).

**Ejemplo**:
> Cartera sube de 100.000€ a 150.000€, luego cae a 120.000€
> Drawdown = (150.000 - 120.000) / 150.000 = **20%**

Mide la peor caída experimentada.

---

## 1️⃣1️⃣ Casos prácticos resueltos

### Caso 1: Rentabilidad de cartera

**Situación**:
> Cartera con:
> - 50% en renta variable (rentabilidad esperada 10%)
> - 30% en renta fija (rentabilidad esperada 4%)
> - 20% en monetario (rentabilidad esperada 2%)

**Pregunta**: ¿Rentabilidad esperada de la cartera?

**Solución**:
Rc = (0,50 × 10) + (0,30 × 4) + (0,20 × 2)  
Rc = 5 + 1,2 + 0,4  
**Rc = 6,6%**

---

### Caso 2: CAPM

**Datos**:
- Rf = 2,5%
- E(Rm) = 9%
- β acción = 1,3

**Pregunta**: ¿Rentabilidad esperada según CAPM?

**Solución**:
E(Ri) = 2,5 + 1,3 × (9 - 2,5)  
E(Ri) = 2,5 + 1,3 × 6,5  
E(Ri) = 2,5 + 8,45  
**E(Ri) = 10,95%**

---

### Caso 3: Comparación eficiencia

**Fondo X**: Rentabilidad 15%, volatilidad 20%  
**Fondo Y**: Rentabilidad 12%, volatilidad 10%  
**Rf = 3%**

**Pregunta**: ¿Qué fondo es más eficiente?

**Solución**:

Sharpe X = (15 - 3) / 20 = 12 / 20 = **0,60**

Sharpe Y = (12 - 3) / 10 = 9 / 10 = **0,90**

**Respuesta**: Fondo Y es más eficiente (mayor Sharpe).

---

### Caso 4: Diversificación

**Pregunta**: ¿Qué tipo de riesgo se reduce mediante diversificación?

A) Riesgo sistemático  
B) **Riesgo no sistemático** ✅  
C) Riesgo de mercado  
D) Ninguno

**Respuesta**: B (no sistemático = específico = diversificable)

---

## 1️⃣2️⃣ Resumen de fórmulas clave (memoriza)

**Rentabilidad simple**: R = (Vf - Vi) / Vi × 100

**Rentabilidad real**: R real = (1 + Rnom) / (1 + Infl) - 1

**Rentabilidad cartera**: Rc = Σ(wi × Ri)

**Beta cartera**: βc = Σ(wi × βi)

**CAPM**: E(Ri) = Rf + βi × [E(Rm) - Rf]

**Sharpe**: Sharpe = (Rp - Rf) / σp

---

## 1️⃣3️⃣ Resumen ultra-operativo

- **Riesgo sistemático**: NO eliminable con diversificación
- **Riesgo no sistemático**: SÍ reducible con diversificación
- **Volatilidad**: Dispersión de rentabilidades (riesgo)
- **Beta > 1**: Más volátil que mercado
- **Beta < 1**: Menos volátil que mercado
- **CAPM**: Relaciona rentabilidad con beta
- **Sharpe**: Rentabilidad ajustada por riesgo total (mayor = mejor)
- **Diversificación**: Reduce riesgo específico mediante baja correlación

---

## ✅ Checklist de conceptos dominados

- [ ] Rentabilidad simple y con dividendos
- [ ] Rentabilidad real (ajustada por inflación)
- [ ] Rentabilidad de cartera (media ponderada)
- [ ] Riesgo sistemático vs no sistemático
- [ ] Diversificación (qué reduce y qué no)
- [ ] Volatilidad (interpretación)
- [ ] Beta (valores e interpretación)
- [ ] Beta de cartera
- [ ] CAPM (fórmula completa)
- [ ] Ratio de Sharpe
- [ ] Frontera eficiente (concepto)

**Objetivo**: 11/11 antes del examen.

---

*Fin del Manual 4 • Continúa con Manual 5: Mercados Financieros*
