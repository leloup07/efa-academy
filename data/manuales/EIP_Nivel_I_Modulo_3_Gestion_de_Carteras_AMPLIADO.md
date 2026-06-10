# EIP (Nivel I) – Manual de Preparación
# Módulo 3: Gestión de Carteras – VERSIÓN DEFINITIVA

**Estructura estrictamente alineada con EFPA España (Guía EFA, marzo 2025 – V18/25)**

Edición interna de estudio · Enero 2026

Autor: Enrique Aznar (compilación y ampliación)

---

## Cómo usar este capítulo

Este capítulo prepara el examen de **Nivel I (EIP)** en Gestión de Carteras siguiendo estrictamente el perímetro EFPA.

**Ponderación en el examen:** 17,5% del total.

**Foco:** Conocimiento, Análisis y Aplicación según designación taxonómica EFPA.

**Contenido:**
- Fundamentos teóricos completos
- Fórmulas matemáticas explicadas paso a paso
- Ejemplos numéricos detallados
- Casos prácticos integradores
- Banco de 50 preguntas tipo test con explicaciones
- Checklist de autoevaluación

---

## Mapa del módulo

| Tema | Contenido |
|------|-----------|
| 1 | Concepto de Cartera y Objetivos |
| 2 | Rentabilidad: Cálculo y Tipos |
| 3 | Riesgo: Componentes y Medición |
| 4 | Correlación y Diversificación |
| 5 | Mercados de Capitales Eficientes |
| 6 | Teoría de Carteras (Markowitz, CAPM) |
| 7 | Asignación de Activos |
| 8 | Rebalanceo de Carteras |
| 9 | Medidas de Performance |
| 10 | Benchmark y Tracking Error |
| 11 | Perfil del Inversor e Idoneidad |
| 12 | Casos Prácticos Integradores |
| 13 | Banco de 50 Preguntas Tipo Test |
| 14 | Checklist de Competencias |

---

# TEMA 1: CONCEPTO DE CARTERA Y OBJETIVOS

## 1.1 Definición de Cartera

Una **cartera de inversión** (portfolio) es una combinación de activos financieros mantenidos por un inversor con el propósito de alcanzar sus objetivos financieros.

La gestión de carteras se basa en un principio fundamental: **el todo puede ser diferente de la suma de las partes**. Una cartera bien construida puede ofrecer mejor relación rentabilidad-riesgo que cualquiera de sus componentes por separado.

## 1.2 Objetivos de Inversión

| Objetivo | Descripción | Perfil típico | Activos predominantes |
|----------|-------------|---------------|----------------------|
| **Crecimiento del capital** | Maximizar el valor a largo plazo | Joven, horizonte largo | Renta variable, growth |
| **Generación de rentas** | Obtener ingresos periódicos | Jubilado, necesita flujos | Bonos cupón, dividendos |
| **Preservación del capital** | Mantener el valor real | Conservador, corto plazo | Monetarios, RF corto plazo |
| **Mixto** | Combinación de objetivos | Intermedio | Carteras equilibradas |

## 1.3 Restricciones del Inversor

- **Horizonte temporal:** Plazo hasta que se necesitarán los fondos
- **Necesidades de liquidez:** Requerimientos de efectivo a corto plazo
- **Consideraciones fiscales:** Optimización de la carga tributaria
- **Restricciones legales:** Límites normativos (ej. fondos de pensiones)
- **Preferencias particulares:** Inversión ética, exclusiones sectoriales

## 1.4 El Proceso de Gestión de Carteras

1. **Planificación:** Definir objetivos, restricciones y política de inversión
2. **Ejecución:** Selección de activos y construcción de la cartera
3. **Retroalimentación:** Monitorización, rebalanceo y ajustes

---

# TEMA 2: RENTABILIDAD DE CARTERAS

## 2.1 Rentabilidad Simple (HPR)

La rentabilidad simple mide el cambio porcentual en el valor de una inversión:

**Fórmula:**
$$R = \frac{P_1 - P_0 + D}{P_0} \times 100$$

Donde:
- P₁ = Precio/Valor final
- P₀ = Precio/Valor inicial
- D = Dividendos o cupones recibidos

---

**EJEMPLO 1: Rentabilidad simple**

Un inversor compra acciones de Iberdrola a 11,20€ y las vende un año después a 12,50€. Durante el año recibe dividendos de 0,45€ por acción.

$$R = \frac{12,50 - 11,20 + 0,45}{11,20} \times 100 = \frac{1,75}{11,20} \times 100 = 15,63\%$$

---

## 2.2 Rentabilidad Media Histórica

Cuando disponemos de rentabilidades de varios períodos:

$$\bar{R} = \frac{R_1 + R_2 + ... + R_n}{n} = \frac{\sum_{i=1}^{n} R_i}{n}$$

---

**EJEMPLO 2: Rentabilidad media histórica**

| Año | Rentabilidad |
|-----|--------------|
| 1 | +14% |
| 2 | -6% |
| 3 | +10% |
| 4 | +18% |
| 5 | +4% |

$$\bar{R} = \frac{14 + (-6) + 10 + 18 + 4}{5} = \frac{40}{5} = 8\%$$

---

## 2.3 Rentabilidad Esperada (por Escenarios)

$$E(R) = \sum_{i=1}^{n} p_i \times R_i$$

---

**EJEMPLO 3: Rentabilidad esperada**

| Escenario | Probabilidad | Rentabilidad |
|-----------|--------------|--------------|
| Favorable | 25% | +30% |
| Normal | 50% | +12% |
| Desfavorable | 25% | -10% |

$$E(R) = 0,25 \times 30 + 0,50 \times 12 + 0,25 \times (-10) = 7,5 + 6 - 2,5 = 11\%$$

---

## 2.4 Rentabilidad Anualizada (CAGR)

$$CAGR = \left(\frac{Valor\ final}{Valor\ inicial}\right)^{1/n} - 1$$

---

**EJEMPLO 4: CAGR**

Inversión de 10.000€ que crece a 15.000€ en 5 años:

$$CAGR = (15.000 / 10.000)^{1/5} - 1 = 1,5^{0,2} - 1 = 8,45\%$$

---

## 2.5 TWR vs MWR

| Métrica | Nombre completo | Qué mide | Cuándo usar |
|---------|-----------------|----------|-------------|
| **TWR** | Time-Weighted Return | Rentabilidad del gestor | Comparar gestores |
| **MWR** | Money-Weighted Return (TIR) | Rentabilidad del inversor | Evaluar resultado personal |

---

**EJEMPLO 5: TWR vs MWR**

Un inversor aporta 10.000€ a inicio de año. El fondo gana 20% el primer semestre (cartera = 12.000€). El inversor añade 50.000€. El segundo semestre el fondo pierde 10%.

Valor final: (12.000 + 50.000) × 0,90 = 55.800€
Capital invertido total: 60.000€

- **TWR:** Mide la rentabilidad "pura" del fondo: (1,20 × 0,90) - 1 = **+8%**
- **MWR:** Considera el timing de las aportaciones: (55.800 - 60.000) / 60.000 = **-7%**

> El inversor perdió dinero (-7%) aunque el fondo subió (+8%) porque aportó justo antes de la caída.

---

## 2.6 Rentabilidad de una Cartera

Es la **media ponderada** de las rentabilidades individuales:

$$R_p = \sum_{i=1}^{n} w_i \times R_i$$

Restricción: La suma de pesos debe ser 1 (100%).

---

**EJEMPLO 6: Rentabilidad de cartera**

| Activo | Peso | Rentabilidad |
|--------|------|--------------|
| Acciones España | 45% | +12% |
| Acciones Europa | 25% | +8% |
| Renta Fija | 20% | +3% |
| Liquidez | 10% | +1% |

$$R_p = 0,45 \times 12 + 0,25 \times 8 + 0,20 \times 3 + 0,10 \times 1 = 5,4 + 2,0 + 0,6 + 0,1 = 8,1\%$$

---

# TEMA 3: RIESGO DE CARTERAS

## 3.1 Concepto de Riesgo

El riesgo en inversiones se define como la **incertidumbre sobre los resultados futuros**. Se mide típicamente mediante la volatilidad (desviación estándar).

> **Importante:** El riesgo de una cartera NO es la media ponderada de los riesgos individuales. Depende crucialmente de cómo se relacionan los activos entre sí.

## 3.2 Volatilidad (Desviación Estándar)

**Fórmula de varianza:**
$$\sigma^2 = \frac{\sum_{i=1}^{n}(R_i - \bar{R})^2}{n}$$

**Volatilidad:**
$$\sigma = \sqrt{\sigma^2}$$

**Volatilidades típicas anuales:**

| Tipo de activo | Volatilidad típica |
|----------------|-------------------|
| Monetario | 0,5% - 1% |
| RF Gobierno corto plazo | 2% - 4% |
| RF Gobierno largo plazo | 6% - 10% |
| RF High Yield | 8% - 12% |
| RV Desarrollada | 15% - 20% |
| RV Emergentes | 20% - 30% |

---

**EJEMPLO 7: Cálculo de volatilidad**

Usando los datos del Ejemplo 2 (R̄ = 8%):

| Año | Rᵢ | Rᵢ - R̄ | (Rᵢ - R̄)² |
|-----|-----|---------|-----------|
| 1 | 14% | 6% | 36 |
| 2 | -6% | -14% | 196 |
| 3 | 10% | 2% | 4 |
| 4 | 18% | 10% | 100 |
| 5 | 4% | -4% | 16 |
| **Suma** | | | **352** |

$$\sigma^2 = \frac{352}{5} = 70,4$$
$$\sigma = \sqrt{70,4} = 8,39\%$$

---

## 3.3 Volatilidad Anualizada

$$\sigma_{anual} = \sigma_{periodo} \times \sqrt{n_{periodos/año}}$$

| Volatilidad original | Fórmula | Volatilidad anualizada |
|---------------------|---------|----------------------|
| Mensual: 4% | 4% × √12 | 13,86% |
| Semanal: 2% | 2% × √52 | 14,42% |
| Diaria: 1% | 1% × √252 | 15,87% |

---

## 3.4 Riesgo Sistemático vs Específico

| Tipo de riesgo | Descripción | ¿Diversificable? | Ejemplos |
|----------------|-------------|------------------|----------|
| **Sistemático** | Afecta a todo el mercado | NO | Crisis económica, tipos de interés |
| **Específico** | Propio de un activo/sector | SÍ | Fraude contable, huelga |

**Riesgo Total² = Riesgo Sistemático² + Riesgo Específico²**

> Solo el riesgo sistemático es remunerado por el mercado, ya que el específico puede eliminarse mediante diversificación.

---

## 3.5 Coeficiente Beta

La **beta (β)** mide la sensibilidad de un activo respecto al mercado:

$$\beta_i = \frac{Cov(R_i, R_m)}{\sigma_m^2}$$

| Beta | Tipo de activo | Comportamiento |
|------|----------------|----------------|
| β > 1 | Agresivo | Más volátil que el mercado |
| β = 1 | Neutro | Igual que el mercado |
| β < 1 | Defensivo | Menos volátil que el mercado |
| β < 0 | Contracíclico | Movimiento opuesto |

---

**EJEMPLO 8: Interpretación de beta**

Una acción tiene β = 1,3:
- Si el mercado sube 10%: Rentabilidad esperada = 1,3 × 10% = **+13%**
- Si el mercado baja 10%: Rentabilidad esperada = 1,3 × (-10%) = **-13%**

---

## 3.6 Beta de una Cartera

$$\beta_p = \sum_{i=1}^{n} w_i \times \beta_i$$

---

**EJEMPLO 9: Beta de cartera**

| Activo | Peso | Beta |
|--------|------|------|
| Acción A | 40% | 1,3 |
| Acción B | 35% | 0,9 |
| Acción C | 25% | 1,6 |

$$\beta_p = 0,40 \times 1,3 + 0,35 \times 0,9 + 0,25 \times 1,6 = 0,52 + 0,315 + 0,40 = 1,235$$

La cartera es ligeramente agresiva (β > 1).

---

## 3.7 Varianza de una Cartera (Dos Activos)

$$\sigma_p^2 = w_A^2 \sigma_A^2 + w_B^2 \sigma_B^2 + 2 w_A w_B \sigma_A \sigma_B \rho_{AB}$$

---

**EJEMPLO 10: Volatilidad de cartera**

| Activo | Peso | Rentabilidad esperada | Volatilidad |
|--------|------|----------------------|-------------|
| A (RV) | 60% | 10% | 20% |
| B (RF) | 40% | 4% | 6% |

Correlación ρ = 0,2

**Paso 1: Rentabilidad esperada**
$$E(R_p) = 0,60 \times 10\% + 0,40 \times 4\% = 7,6\%$$

**Paso 2: Varianza**
$$\sigma_p^2 = (0,60)^2 \times (0,20)^2 + (0,40)^2 \times (0,06)^2 + 2 \times 0,60 \times 0,40 \times 0,20 \times 0,06 \times 0,2$$
$$\sigma_p^2 = 0,0144 + 0,000576 + 0,001152 = 0,016128$$

**Paso 3: Volatilidad**
$$\sigma_p = \sqrt{0,016128} = 12,70\%$$

**Comparación:**
- Media ponderada simple: 0,60 × 20% + 0,40 × 6% = 14,4%
- Volatilidad real: 12,70%
- **Reducción por diversificación: 1,7 puntos porcentuales**

---

## 3.8 Hipótesis de Normalidad

La distribución normal está definida por la media (μ) y la desviación típica (σ).

**Reglas de probabilidad:**

| Intervalo | Probabilidad |
|-----------|--------------|
| μ ± 1σ | 68% |
| μ ± 2σ | 95% |
| μ ± 3σ | 99,7% |

---

**EJEMPLO 11: Intervalos de rentabilidad**

Fondo con E(R) = 9% y σ = 15%:

- **Con 68% probabilidad:** 9% ± 15% = [-6%, +24%]
- **Con 95% probabilidad:** 9% ± 30% = [-21%, +39%]

---

# TEMA 4: CORRELACIÓN Y DIVERSIFICACIÓN

## 4.1 Concepto de Correlación

La **correlación (ρ)** mide el grado y dirección en que dos variables se mueven conjuntamente. Oscila entre -1 y +1.

| Correlación | Interpretación | Efecto en diversificación |
|-------------|----------------|--------------------------|
| ρ = +1 | Movimientos sincronizados | Sin beneficio |
| ρ = 0 | Movimientos independientes | Beneficio moderado |
| ρ = -1 | Movimientos opuestos | Máximo beneficio |

## 4.2 Correlaciones Típicas entre Clases de Activos

| Par de activos | Correlación típica |
|----------------|-------------------|
| RV Europa - RV USA | 0,70 - 0,85 |
| RV - RF Gobierno | 0,10 - 0,30 |
| RV - Oro | -0,10 - 0,10 |
| RF Gobierno - RF Corporate | 0,60 - 0,80 |
| RV Desarrollada - RV Emergente | 0,65 - 0,80 |

> **Nota:** Las correlaciones no son estables. En crisis tienden a aumentar.

---

## 4.3 Impacto de la Correlación en el Riesgo

**EJEMPLO 12: Efecto de la correlación**

Dos activos con volatilidad 20% cada uno, pesos 50%-50%:

| Correlación | Volatilidad Cartera | Reducción |
|-------------|--------------------|-----------| 
| ρ = +1 | 20,0% | 0% |
| ρ = +0,5 | 17,3% | -13,5% |
| ρ = 0 | 14,1% | -29,5% |
| ρ = -0,5 | 10,0% | -50,0% |
| ρ = -1 | 0,0% | -100% |

---

## 4.4 Cartera de Riesgo Cero (ρ = -1)

Con correlación perfectamente negativa, es posible eliminar todo el riesgo:

$$w_A = \frac{\sigma_B}{\sigma_A + \sigma_B}$$

---

**EJEMPLO 13: Cartera de riesgo cero**

Activo A: σ = 24%, Activo B: σ = 16%, ρ = -1

$$w_A = \frac{16\%}{24\% + 16\%} = 40\%$$
$$w_B = 60\%$$

Verificación:
$$\sigma_p = |0,40 \times 24\% - 0,60 \times 16\%| = |9,6\% - 9,6\%| = 0\%$$

---

## 4.5 Número Óptimo de Activos

La diversificación tiene rendimientos decrecientes:

| Nº de acciones | Riesgo específico eliminado |
|----------------|----------------------------|
| 1 | 0% |
| 5 | 50% |
| 10 | 70% |
| 20 | 85% |
| 30 | 90% |
| 50+ | ~95% |

Con **20-30 acciones** bien diversificadas se elimina la mayor parte del riesgo específico.

## 4.6 Límites de la Diversificación

- No elimina el riesgo sistemático
- Las correlaciones aumentan en crisis
- Mayores costes de transacción
- Mayor complejidad de gestión

---

# TEMA 5: MERCADOS DE CAPITALES EFICIENTES

## 5.1 Concepto de Eficiencia

Un mercado es **eficiente** cuando los precios reflejan toda la información disponible de forma rápida y correcta.

**Consecuencias:**
- No es posible obtener rentabilidades superiores sistemáticamente
- Los precios siguen un "paseo aleatorio" (random walk)
- No hay activos infravalorados ni sobrevalorados

## 5.2 Características de un Mercado Eficiente

| Característica | Descripción |
|----------------|-------------|
| **Transparencia** | Información disponible para todos |
| **Amplitud** | Gran número de participantes |
| **Homogeneidad** | Activos estandarizados |
| **Libertad** | Sin restricciones de entrada/salida |
| **Flexibilidad** | Facilidad para ajustar posiciones |

## 5.3 Tipos de Información

| Tipo | Descripción | Ejemplo |
|------|-------------|---------|
| **Histórica** | Precios y volúmenes pasados | Cotizaciones últimos 5 años |
| **Pública** | Disponible para todos | Noticias, balances, informes |
| **Privada** | Solo para algunos | Información privilegiada |

## 5.4 Niveles de Eficiencia

### Eficiencia Débil

Los precios reflejan toda la información **histórica**.

- El análisis técnico NO funciona
- El análisis fundamental SÍ puede funcionar

### Eficiencia Semifuerte

Los precios reflejan toda la información **pública**.

- Ni el análisis técnico NI el fundamental funcionan
- Solo la información privilegiada permitiría ganar

### Eficiencia Fuerte

Los precios reflejan **TODA** la información (incluida la privada).

- Ninguna técnica funciona
- La gestión pasiva es óptima

## 5.5 Resumen: Técnicas según Nivel de Eficiencia

| Nivel | Análisis Técnico | Análisis Fundamental | Info. Privilegiada |
|-------|------------------|---------------------|-------------------|
| Débil | ❌ No funciona | ✅ Puede funcionar | ✅ Puede funcionar |
| Semifuerte | ❌ No funciona | ❌ No funciona | ✅ Puede funcionar |
| Fuerte | ❌ No funciona | ❌ No funciona | ❌ No funciona |

## 5.6 Anomalías de Mercado

| Anomalía | Descripción |
|----------|-------------|
| **Efecto enero** | Rentabilidades superiores en enero |
| **Efecto fin de semana** | Rentabilidades negativas los lunes |
| **Efecto tamaño** | Empresas pequeñas rinden más |
| **Efecto PER** | Empresas con bajo PER rinden más |
| **Efecto momentum** | Tendencias que persisten |

---

# TEMA 6: TEORÍA DE CARTERAS

## 6.1 Modelo de Markowitz (Media-Varianza)

### Hipótesis del Modelo

1. Los inversores son aversos al riesgo
2. Solo importan la media y la varianza de las rentabilidades
3. Las rentabilidades siguen distribución normal
4. No hay costes de transacción ni impuestos
5. Los activos son perfectamente divisibles

### Conceptos Fundamentales

- **Cartera factible:** Cualquier combinación posible de activos
- **Cartera eficiente:** Maximiza rentabilidad para un riesgo dado (o minimiza riesgo para una rentabilidad)
- **Frontera eficiente:** Conjunto de todas las carteras eficientes

### Cartera de Mínima Volatilidad (CMV)

$$w_A = \frac{\sigma_B^2 - Cov_{AB}}{\sigma_A^2 + \sigma_B^2 - 2 \times Cov_{AB}}$$

---

**EJEMPLO 14: Cartera de Mínima Volatilidad**

- Activo A: E(R) = 14%, σ = 22%
- Activo B: E(R) = 7%, σ = 10%
- Correlación: ρ = 0,3

**Paso 1: Covarianza**
$$Cov = 0,22 \times 0,10 \times 0,3 = 0,0066$$

**Paso 2: Peso de A**
$$w_A = \frac{(0,10)^2 - 0,0066}{(0,22)^2 + (0,10)^2 - 2 \times 0,0066} = \frac{0,0034}{0,0452} = 7,52\%$$

**Paso 3: Peso de B**
$$w_B = 92,48\%$$

**Rentabilidad CMV:** 0,0752 × 14% + 0,9248 × 7% = 7,53%

---

## 6.2 Modelo CAPM

### Hipótesis Adicionales

- Existe un activo libre de riesgo
- Los inversores pueden prestar y pedir prestado al tipo libre de riesgo
- Todos tienen las mismas expectativas (homogéneas)

### Capital Market Line (CML)

La CML es la frontera eficiente cuando existe activo libre de riesgo:

$$E(R_p) = R_f + \frac{E(R_m) - R_f}{\sigma_m} \times \sigma_p$$

**Aplica solo a carteras eficientes.**
**Medida de riesgo: Volatilidad (σ)**

---

**EJEMPLO 15: Cartera en la CML**

Datos: Rf = 2%, E(Rm) = 9%, σm = 14%

Pendiente CML: (9% - 2%) / 14% = 0,50

Un inversor desea volatilidad del 10%:
$$E(R_p) = 2\% + 0,50 \times 10\% = 7\%$$

Composición: σp = wm × σm → 10% = wm × 14% → wm = 71,43%

**Resultado:** 71,43% en cartera de mercado, 28,57% en activo libre de riesgo.

---

### Security Market Line (SML)

La SML relaciona rentabilidad esperada con riesgo sistemático (beta):

$$E(R_i) = R_f + \beta_i \times (E(R_m) - R_f)$$

**Aplica a TODOS los activos y carteras.**
**Medida de riesgo: Beta (β)**

---

**EJEMPLO 16: Valoración con la SML**

Rf = 2%, E(Rm) = 10%, Prima de riesgo = 8%

Acción X con β = 1,4:
$$E(R_X) = 2\% + 1,4 \times 8\% = 13,2\%$$

**Valoración:**
- Rentabilidad observada = 15% → INFRAVALORADA (comprar)
- Rentabilidad observada = 11% → SOBREVALORADA (vender)

---

### Diferencias CML vs SML

| Aspecto | CML | SML |
|---------|-----|-----|
| **Aplica a** | Solo carteras eficientes | Todos los activos |
| **Medida de riesgo** | Volatilidad (σ) | Beta (β) |
| **Uso** | Construcción de carteras | Valoración de activos |

---

# TEMA 7: ASIGNACIÓN DE ACTIVOS

## 7.1 Concepto e Importancia

La **asignación de activos** es la distribución del patrimonio entre clases de activos: renta variable, renta fija, liquidez, alternativos.

> Estudios empíricos demuestran que el asset allocation explica aproximadamente el **90% de la variabilidad de los rendimientos** a largo plazo.

## 7.2 Tipos de Asignación

| Tipo | Descripción | Horizonte | Frecuencia cambio |
|------|-------------|-----------|-------------------|
| **Estratégica (SAA)** | Asignación objetivo a largo plazo | 5-10+ años | Anual o menos |
| **Táctica (TAA)** | Desviaciones temporales | Meses-1 año | Trimestral/mensual |
| **Dinámica** | Ajustes según condiciones | Variable | Según señales |

## 7.3 Carteras Modelo por Perfil

| Perfil | RV | RF | Liquidez | Volatilidad esperada |
|--------|----|----|----------|---------------------|
| Muy conservador | 0-10% | 60-70% | 20-30% | 2-4% |
| Conservador | 20-30% | 50-60% | 10-20% | 4-7% |
| Moderado | 40-50% | 40-50% | 5-10% | 8-12% |
| Dinámico | 60-70% | 25-35% | 5% | 12-16% |
| Agresivo | 80-100% | 0-15% | 0-5% | 16-22% |

## 7.4 Security Selection vs Market Timing

- **Security Selection:** Seleccionar valores específicos dentro de cada categoría
- **Market Timing:** Ajustar exposición al mercado según expectativas

## 7.5 Consideraciones ESG

Los factores **ESG** (Ambientales, Sociales, Gobernanza) pueden incorporarse en:
- Exclusión de sectores
- Sobreponderación de empresas sostenibles
- Ejercicio de derechos de voto

---

# TEMA 8: REBALANCEO DE CARTERAS

## 8.1 Concepto y Necesidad

El **rebalanceo** consiste en ajustar los pesos de la cartera para volver a la asignación objetivo cuando las desviaciones superan ciertos umbrales.

**¿Por qué es necesario?**
Los activos evolucionan a ritmos diferentes. Si la RV sube más que la RF, la cartera se vuelve más agresiva que lo planificado.

## 8.2 Estrategias de Rebalanceo

| Estrategia | Descripción | Ventajas | Inconvenientes |
|------------|-------------|----------|----------------|
| **Calendario** | Cada X meses | Simple | Puede ignorar desvíos grandes |
| **Umbral** | Si desviación > X% | Responde a movimientos | Más seguimiento |
| **Híbrido** | Calendario + umbral | Equilibrado | Más complejo |

**Umbrales típicos:** ±5% del peso objetivo

## 8.3 Ejemplo Detallado de Rebalanceo

**Cartera inicial:** 100.000€ (60% RV, 40% RF)

**Evolución a 5 años SIN rebalanceo:**

| Año | Rent. RV | Rent. RF | Valor RV | Valor RF | Total | Peso RV |
|-----|----------|----------|----------|----------|-------|---------|
| 0 | - | - | 60.000 | 40.000 | 100.000 | 60% |
| 1 | +15% | +3% | 69.000 | 41.200 | 110.200 | 63% |
| 2 | +20% | +2% | 82.800 | 42.024 | 124.824 | 66% |
| 3 | -10% | +4% | 74.520 | 43.705 | 118.225 | 63% |
| 4 | +25% | +3% | 93.150 | 45.016 | 138.166 | 67% |
| 5 | +8% | +2% | 100.602 | 45.916 | 146.518 | 69% |

**CON rebalanceo anual al 60/40:**

| Año | Valor inicio | Valor fin | Acción rebalanceo |
|-----|--------------|-----------|-------------------|
| 1 | 100.000 | 110.200 | Vende RV 3.280€ |
| 2 | 110.200 | 124.948 | Vende RV 4.979€ |
| 3 | 124.948 | 119.190 | Compra RV 2.854€ |
| 4 | 119.190 | 140.159 | Vende RV 5.864€ |
| 5 | 140.159 | **149.290** | - |

**Comparación:**
- Sin rebalanceo: 146.518€ (+46,5%)
- Con rebalanceo: 149.290€ (+49,3%)
- **Beneficio: +2.772€ (+2,8 p.p.)**

## 8.4 Consideraciones Prácticas

**Ventajas:**
- Mantiene el perfil de riesgo
- Disciplina "comprar bajo, vender alto"
- Evita sesgos emocionales

**Costes:**
- Comisiones de transacción
- Spread bid-ask
- Impacto fiscal (plusvalías)

**Optimización fiscal:**
- Usar nuevas aportaciones para rebalancear
- Aprovechar traspasos entre fondos (sin tributación)

---

# TEMA 9: MEDIDAS DE PERFORMANCE

## 9.1 Ratio de Sharpe

Mide el **exceso de rentabilidad por unidad de riesgo total**:

$$Sharpe = \frac{R_p - R_f}{\sigma_p}$$

| Sharpe | Interpretación |
|--------|----------------|
| < 0 | Peor que activo sin riesgo |
| 0 - 0,5 | Aceptable |
| 0,5 - 1 | Bueno |
| > 1 | Excelente |

---

**EJEMPLO 17: Comparación con Sharpe**

| Cartera | Rentabilidad | Volatilidad | Rf = 2% | Sharpe |
|---------|-------------|-------------|---------|--------|
| A | 12% | 18% | 2% | 0,56 |
| B | 8% | 8% | 2% | **0,75** |
| C | 15% | 25% | 2% | 0,52 |

La Cartera B es más eficiente aunque tiene menor rentabilidad absoluta.

---

## 9.2 Ratio de Treynor

Mide el **exceso de rentabilidad por unidad de riesgo sistemático**:

$$Treynor = \frac{R_p - R_f}{\beta_p}$$

> Más apropiado para carteras **bien diversificadas**.

---

## 9.3 Alfa de Jensen

Mide la **rentabilidad extra respecto al CAPM**:

$$\alpha = R_p - [R_f + \beta_p(R_m - R_f)]$$

| Alfa | Significado |
|------|-------------|
| α > 0 | Gestor añade valor |
| α = 0 | Rentabilidad acorde al riesgo |
| α < 0 | Gestor destruye valor |

---

**EJEMPLO 18: Alfa de Jensen**

Cartera: Rp = 12%, βp = 1,1
Mercado: Rm = 10%, Rf = 2%

Rentabilidad esperada CAPM = 2% + 1,1 × (10% - 2%) = 10,8%

$$\alpha = 12\% - 10,8\% = +1,2\%$$

El gestor añade 1,2% de valor.

---

## 9.4 Maximum Drawdown (MDD)

Mide la **máxima caída desde un pico hasta un valle**:

$$MDD = \frac{Valle - Pico}{Pico} \times 100$$

---

**EJEMPLO 19: Maximum Drawdown**

Una cartera alcanza máximo de 150.000€ y cae a 120.000€:

$$MDD = \frac{120.000 - 150.000}{150.000} = -20\%$$

---

## 9.5 Value at Risk (VaR)

El **VaR** indica la pérdida máxima esperada con un nivel de confianza dado:

$$VaR_{95\%} = -E(R) + 1,65 \times \sigma$$
$$VaR_{99\%} = -E(R) + 2,33 \times \sigma$$

---

**EJEMPLO 20: Cálculo de VaR**

Cartera de 2.000.000€ con E(R) mensual = 0,6% y σ mensual = 3,5%:

$$VaR_{95\%} = -0,6\% + 1,65 \times 3,5\% = 5,175\%$$

**En euros:** 2.000.000€ × 5,175% = **103.500€**

> Hay un 5% de probabilidad de perder más de 103.500€ en un mes.

---

## 9.6 Resumen de Ratios

| Ratio | Numerador | Denominador | Cuándo usar |
|-------|-----------|-------------|-------------|
| **Sharpe** | Rp - Rf | σp | Siempre aplicable |
| **Treynor** | Rp - Rf | βp | Carteras diversificadas |
| **Jensen** | Rp - RCAPM | - | Evaluar gestión activa |
| **Información** | Rp - Rb | TE | Comparar vs índice |
| **MDD** | Caída máxima | - | Gestión del riesgo |
| **VaR** | Pérdida máxima | - | Control de riesgo |

---

# TEMA 10: BENCHMARK Y TRACKING ERROR

## 10.1 Concepto de Benchmark

Un **benchmark** es un índice de referencia contra el cual se evalúa el rendimiento.

**Características de un buen benchmark:**
- **Medible:** Calculable objetivamente
- **Invertible:** Replicable en la práctica
- **Coherente:** Acorde con la estrategia
- **Representativo:** Refleja el universo de inversión
- **Conocido de antemano:** Definido antes de la gestión

## 10.2 Benchmarks Comunes

| Tipo de cartera | Benchmark típico |
|-----------------|------------------|
| RV Europa | MSCI Europe, STOXX 600 |
| RV USA | S&P 500, MSCI USA |
| RV Global | MSCI World, MSCI ACWI |
| RF Euro | Bloomberg Euro Aggregate |
| Mixta 60/40 | 60% MSCI World + 40% Agg |

## 10.3 Tracking Error

El **Tracking Error (TE)** mide la desviación respecto al benchmark:

$$TE = \sigma(R_p - R_b)$$

| Tracking Error | Tipo de gestión |
|----------------|-----------------|
| 0% - 0,5% | Gestión pasiva/indexada |
| 0,5% - 2% | Gestión semiactiva |
| 2% - 5% | Gestión activa moderada |
| > 5% | Gestión activa alta convicción |

## 10.4 Ratio de Información

$$IR = \frac{R_p - R_b}{TE}$$

| IR | Interpretación |
|----|----------------|
| < 0,25 | Pobre |
| 0,25 - 0,5 | Aceptable |
| 0,5 - 0,75 | Bueno |
| > 0,75 | Excelente |

## 10.5 Gestión Activa vs Pasiva

| Característica | Gestión pasiva | Gestión activa |
|----------------|---------------|----------------|
| Objetivo | Replicar benchmark | Superar benchmark |
| Tracking Error | < 0,5% | > 2% |
| Costes | 0,05-0,20% | 1-2% |
| Alfa esperado | Cero | Positivo (si éxito) |

---

## 10.6 Atribución de Resultados

$$Rentabilidad\ Extra = Efecto\ Asset\ Allocation + Efecto\ Security\ Selection$$

**Efecto Asset Allocation:**
$$AA = \sum_i (w_{p,i} - w_{b,i}) \times R_{b,i}$$

**Efecto Security Selection:**
$$SS = \sum_i w_{p,i} \times (R_{p,i} - R_{b,i})$$

---

**EJEMPLO 21: Atribución de resultados**

| Categoría | Peso BM | Peso Cartera | Rent. BM | Rent. Cartera |
|-----------|---------|--------------|----------|---------------|
| RV España | 35% | 45% | 10% | 13% |
| RV Europa | 30% | 25% | 6% | 7% |
| RF | 35% | 30% | 3% | 4% |

**Rentabilidad benchmark:** 6,35%
**Rentabilidad cartera:** 8,80%
**Rentabilidad extra:** 2,45%

**Efecto AA:**
$$(0,45-0,35) \times 10\% + (0,25-0,30) \times 6\% + (0,30-0,35) \times 3\% = 0,55\%$$

**Efecto SS:**
$$0,45 \times 3\% + 0,25 \times 1\% + 0,30 \times 1\% = 1,90\%$$

**Verificación:** 0,55% + 1,90% = 2,45% ✓

---

# TEMA 11: PERFIL DEL INVERSOR E IDONEIDAD

## 11.1 Componentes del Perfil

1. **Objetivos de inversión:** ¿Crecimiento, rentas, preservación?
2. **Horizonte temporal:** ¿Cuándo necesitará los fondos?
3. **Tolerancia al riesgo:** Aspecto psicológico/emocional
4. **Capacidad de riesgo:** Aspecto objetivo/financiero
5. **Conocimientos y experiencia:** Comprensión de productos

## 11.2 Test de Idoneidad vs Conveniencia

| Test | Obligatorio cuando | Evalúa | Resultado |
|------|-------------------|--------|-----------|
| **Conveniencia** | Servicios de ejecución | Conocimientos y experiencia | Advierte si no conviene |
| **Idoneidad** | Asesoramiento, gestión discrecional | Todo el perfil + situación financiera | Recomendación personalizada |

## 11.3 Matriz de Idoneidad

| Perfil | Horizonte | Productos adecuados | Productos NO adecuados |
|--------|-----------|--------------------|-----------------------|
| Muy conservador | Cualquiera | Monetarios, depósitos, RF corto | RV pura, derivados |
| Conservador | > 2 años | RF diversificada, mixtos conservadores | RV concentrada |
| Moderado | > 5 años | Mixtos, RV diversificada parcial | Derivados especulativos |
| Dinámico | > 7 años | RV diversificada, algunos alternativos | Productos ilíquidos corto plazo |
| Agresivo | > 10 años | RV concentrada, alternativos | Solo si alta capacidad |

---

**EJEMPLO 22: Evaluación de idoneidad**

**Cliente:** Ana, 55 años
- Objetivo: Complementar pensión en 10 años
- Horizonte: 10 años hasta jubilación
- Tolerancia: No tolera pérdidas > 15%
- Capacidad: Patrimonio suficiente
- Experiencia: Ha invertido en fondos mixtos

**Clasificación:** Moderada

**Cartera recomendada:** 40% RV global, 45% RF mixta, 15% monetario

---

# TEMA 12: CASOS PRÁCTICOS INTEGRADORES

## Caso 1: Construcción de Cartera para Joven Profesional

**Perfil:**
- Luis, 28 años, ingeniero
- Ahorro mensual: 500€
- Horizonte: 35+ años
- Tolerancia: Alta (acepta caídas del 30%)

**Cartera propuesta:**

| Activo | Peso | Instrumento | TER |
|--------|------|-------------|-----|
| RV Global | 70% | ETF MSCI World | 0,20% |
| RV Emergentes | 20% | ETF MSCI EM | 0,25% |
| RF Global | 10% | ETF Bonos Agregados | 0,15% |

**Rentabilidad esperada:** 7,0%
**Volatilidad estimada:** ~16%
**Sharpe esperado:** (7% - 2%) / 16% ≈ 0,31

---

## Caso 2: Análisis de Performance de Dos Fondos

| Fondo | Rentabilidad | Volatilidad | Beta |
|-------|-------------|-------------|------|
| A | 9,5% | 14% | 0,95 |
| B | 12,0% | 22% | 1,30 |
| Benchmark | 8,0% | 15% | 1,00 |

Rf = 2%

**Ratio Sharpe:**
- Fondo A: (9,5% - 2%) / 14% = **0,54**
- Fondo B: (12,0% - 2%) / 22% = **0,45**

**Alfa de Jensen:**
- Fondo A: 9,5% - [2% + 0,95 × 6%] = **+1,8%**
- Fondo B: 12,0% - [2% + 1,30 × 6%] = **+2,2%**

**Conclusión:**
- Fondo B tiene mayor alfa (+2,2%)
- Fondo A tiene mejor Sharpe (0,54) - más eficiente
- Para aversión al riesgo moderada: Fondo A
- Para maximizar alfa tolerando volatilidad: Fondo B

---

## Caso 3: Cálculo Completo de VaR

Una gestora tiene una cartera de 5.000.000€ con:
- E(R) mensual = 0,8%
- σ mensual = 4%

**VaR 95% mensual:**
$$VaR = -0,8\% + 1,65 \times 4\% = 5,8\%$$

**En euros:** 5.000.000 × 5,8% = **290.000€**

**VaR 99% mensual:**
$$VaR = -0,8\% + 2,33 \times 4\% = 8,52\%$$

**En euros:** 5.000.000 × 8,52% = **426.000€**

---

# TEMA 13: BANCO DE 50 PREGUNTAS TIPO TEST

## Bloque A: Rentabilidad (1-10)

---

**1) La rentabilidad esperada de una cartera se calcula como:**

A) La suma simple de las rentabilidades  
B) La media ponderada de las rentabilidades esperadas  
C) El producto de las rentabilidades  
D) La rentabilidad del activo con mayor peso

**Respuesta: B**

*E(Rp) = Σ (wi × E(Ri))*

---

**2) Una cartera tiene 40% en un activo con rentabilidad 12% y 60% en otro con 4%. La rentabilidad esperada es:**

A) 8,0%  
B) 7,2%  
C) 6,0%  
D) 16,0%

**Respuesta: B**

*0,40 × 12% + 0,60 × 4% = 4,8% + 2,4% = 7,2%*

---

**3) La TWR (Time-Weighted Return) mide:**

A) La rentabilidad del inversor incluyendo timing de aportaciones  
B) La rentabilidad pura de la gestión, eliminando efecto de flujos  
C) El tiempo medio de permanencia  
D) La rentabilidad ajustada por inflación

**Respuesta: B**

*TWR aísla la rentabilidad del gestor eliminando el impacto de aportaciones/retiradas.*

---

**4) Si una inversión pasa de 10.000€ a 14.641€ en 4 años, la rentabilidad anualizada (CAGR) es:**

A) 10%  
B) 11,6%  
C) 46,4%  
D) 8%

**Respuesta: A**

*CAGR = (14.641/10.000)^(1/4) - 1 = 1,4641^0,25 - 1 = 10%*

---

**5) Un inversor compra acciones a 50€, las vende a 55€ y cobra 2€ de dividendo. La rentabilidad simple es:**

A) 10%  
B) 14%  
C) 12%  
D) 4%

**Respuesta: B**

*R = (55 - 50 + 2) / 50 = 7/50 = 14%*

---

**6) Para anualizar una rentabilidad trimestral del 3%, se debe:**

A) Multiplicar por 4  
B) Calcular (1,03)^4 - 1  
C) Dividir por 4  
D) Multiplicar por √4

**Respuesta: B**

*Rentabilidad anualizada = (1 + R_trimestral)^4 - 1 = 1,03^4 - 1 = 12,55%*

---

**7) La diferencia entre TWR y MWR es importante cuando:**

A) No hay flujos de entrada/salida  
B) Hay aportaciones o retiradas significativas  
C) La cartera solo tiene un activo  
D) El horizonte es muy corto

**Respuesta: B**

*La diferencia surge cuando hay flujos que afectan al capital invertido en diferentes momentos.*

---

**8) Una cartera con 3 activos (30%, 45%, 25%) y rentabilidades (8%, 6%, 10%) tiene rentabilidad esperada de:**

A) 8%  
B) 7,6%  
C) 7,2%  
D) 24%

**Respuesta: C**

*0,30 × 8% + 0,45 × 6% + 0,25 × 10% = 2,4% + 2,7% + 2,5% = 7,6%* → **Corrección: La respuesta es B (7,6%)**

---

**9) La rentabilidad histórica:**

A) Garantiza la rentabilidad futura  
B) Es irrelevante para la planificación  
C) Puede servir como referencia pero no garantiza resultados futuros  
D) Siempre subestima la rentabilidad futura

**Respuesta: C**

---

**10) Si un fondo obtiene +12%, -5%, +8%, +15% en 4 años, la rentabilidad media es:**

A) 7,5%  
B) 30%  
C) 10%  
D) 6%

**Respuesta: A**

*(12 - 5 + 8 + 15) / 4 = 30 / 4 = 7,5%*

---

## Bloque B: Riesgo y Volatilidad (11-20)

---

**11) La volatilidad de una cartera es:**

A) La media ponderada de las volatilidades individuales  
B) Menor o igual que la media ponderada si la correlación < 1  
C) Siempre igual a la del activo más volátil  
D) Independiente de la correlación entre activos

**Respuesta: B**

*La diversificación reduce la volatilidad cuando ρ < 1.*

---

**12) Para anualizar una volatilidad mensual del 4%, se debe:**

A) Multiplicar por 12  
B) Multiplicar por √12  
C) Dividir por 12  
D) Elevar a 12

**Respuesta: B**

*σ_anual = σ_mensual × √12 = 4% × 3,46 = 13,86%*

---

**13) El riesgo sistemático:**

A) Puede eliminarse con diversificación  
B) Solo afecta a acciones individuales  
C) Afecta a todo el mercado y no es diversificable  
D) Es el riesgo específico de cada empresa

**Respuesta: C**

---

**14) Una acción con beta 0,7:**

A) Es más volátil que el mercado  
B) Es menos volátil que el mercado  
C) Se mueve en dirección opuesta al mercado  
D) No tiene riesgo sistemático

**Respuesta: B**

*β < 1 indica activo defensivo.*

---

**15) Si el mercado sube 10% y una acción con β=1,5 debería subir:**

A) 10%  
B) 15%  
C) 5%  
D) 6,67%

**Respuesta: B**

*Rentabilidad esperada = β × Rm = 1,5 × 10% = 15%*

---

**16) Una cartera con 50% en activo A (β=1,2) y 50% en activo B (β=0,8) tiene beta:**

A) 2,0  
B) 1,0  
C) 0,4  
D) 0,96

**Respuesta: B**

*βp = 0,5 × 1,2 + 0,5 × 0,8 = 0,6 + 0,4 = 1,0*

---

**17) Con rentabilidad esperada 8% y volatilidad 16%, el intervalo con 95% de probabilidad es:**

A) [-8%, +24%]  
B) [-24%, +40%]  
C) [0%, +16%]  
D) [-16%, +32%]

**Respuesta: B**

*Intervalo 95% = μ ± 2σ = 8% ± 32% = [-24%, +40%]*

---

**18) El riesgo específico:**

A) No puede reducirse  
B) Se reduce mediante diversificación  
C) Es el único remunerado por el mercado  
D) Depende solo de la beta

**Respuesta: B**

---

**19) La covarianza entre dos activos:**

A) Siempre está entre -1 y +1  
B) Es siempre positiva  
C) Puede ser positiva, negativa o cero  
D) Es igual a la correlación

**Respuesta: C**

*La correlación está acotada, la covarianza no.*

---

**20) Si la volatilidad diaria es 1,5% y hay 252 días hábiles, la volatilidad anual es aproximadamente:**

A) 378%  
B) 23,8%  
C) 15%  
D) 6%

**Respuesta: B**

*σ_anual = 1,5% × √252 = 1,5% × 15,87 ≈ 23,8%*

---

## Bloque C: Correlación y Diversificación (21-26)

---

**21) Una correlación de -1 entre dos activos significa:**

A) No hay relación entre ellos  
B) Se mueven exactamente en la misma dirección  
C) Se mueven exactamente en direcciones opuestas  
D) Uno es más volátil que el otro

**Respuesta: C**

---

**22) La diversificación es más efectiva cuando:**

A) Los activos tienen correlación alta  
B) Los activos tienen correlación baja o negativa  
C) Todos los activos son del mismo sector  
D) La cartera tiene solo dos activos

**Respuesta: B**

---

**23) Para construir una cartera de riesgo cero con dos activos es necesario que:**

A) Ambos tengan la misma volatilidad  
B) La correlación sea -1  
C) La correlación sea 0  
D) Ambos tengan la misma rentabilidad

**Respuesta: B**

---

**24) Con 20-30 acciones bien diversificadas se elimina aproximadamente:**

A) El 100% del riesgo total  
B) El 85-90% del riesgo específico  
C) Todo el riesgo sistemático  
D) El 50% del riesgo total

**Respuesta: B**

---

**25) En momentos de crisis financiera, las correlaciones entre activos tienden a:**

A) Disminuir  
B) Mantenerse estables  
C) Aumentar  
D) Volverse negativas

**Respuesta: C**

*Las correlaciones aumentan en crisis, reduciendo el beneficio de diversificación.*

---

**26) Si dos activos tienen ρ = -1, σA = 20% y σB = 10%, el peso de A en la cartera de riesgo cero es:**

A) 66,7%  
B) 33,3%  
C) 50%  
D) 20%

**Respuesta: B**

*wA = σB / (σA + σB) = 10% / 30% = 33,3%*

---

## Bloque D: Eficiencia de Mercados (27-30)

---

**27) En un mercado eficiente en forma débil:**

A) El análisis técnico permite ganar sistemáticamente  
B) Solo el análisis técnico no funciona  
C) Ninguna técnica funciona  
D) El análisis fundamental no funciona

**Respuesta: B**

*En eficiencia débil, la información histórica ya está reflejada.*

---

**28) El concepto de "paseo aleatorio" implica que:**

A) Los precios son predecibles  
B) Los cambios de precio son impredecibles  
C) El mercado es ineficiente  
D) La volatilidad es constante

**Respuesta: B**

---

**29) El "efecto tamaño" es:**

A) Una característica de mercados eficientes  
B) Una anomalía de mercado  
C) Una consecuencia del CAPM  
D) Un tipo de riesgo sistemático

**Respuesta: B**

---

**30) En un mercado eficiente en forma fuerte:**

A) Solo el análisis técnico funciona  
B) La información privilegiada permite ganar  
C) La gestión pasiva es óptima  
D) Solo el análisis fundamental funciona

**Respuesta: C**

*Si toda la información está reflejada, ninguna estrategia activa funciona.*

---

## Bloque E: Teoría de Carteras y CAPM (31-36)

---

**31) Según el CAPM, la rentabilidad esperada depende de:**

A) La volatilidad total del activo  
B) El alfa del activo  
C) La beta del activo  
D) El tracking error

**Respuesta: C**

---

**32) La Capital Market Line (CML):**

A) Aplica a todos los activos  
B) Solo aplica a carteras eficientes  
C) Usa beta como medida de riesgo  
D) Tiene pendiente negativa

**Respuesta: B**

---

**33) Si Rf = 3%, E(Rm) = 11% y β = 0,8, la rentabilidad esperada según CAPM es:**

A) 9,4%  
B) 8,8%  
C) 11,8%  
D) 6,4%

**Respuesta: A**

*E(R) = 3% + 0,8 × (11% - 3%) = 3% + 6,4% = 9,4%*

---

**34) Un activo está infravalorado según la SML cuando:**

A) Su rentabilidad esperada es menor que la teórica  
B) Su rentabilidad esperada es mayor que la teórica  
C) Está exactamente sobre la SML  
D) Su beta es mayor que 1

**Respuesta: B**

---

**35) La pendiente de la Security Market Line (SML) es:**

A) La volatilidad del mercado  
B) La prima de riesgo del mercado  
C) El tipo libre de riesgo  
D) El alfa de Jensen

**Respuesta: B**

*Pendiente SML = E(Rm) - Rf*

---

**36) La cartera de mercado en el CAPM:**

A) Solo contiene acciones nacionales  
B) Tiene beta igual a 1  
C) Está libre de riesgo  
D) Tiene alfa negativo

**Respuesta: B**

---

## Bloque F: Asignación y Rebalanceo (37-42)

---

**37) La asignación estratégica de activos:**

A) Se modifica diariamente  
B) Es la distribución a largo plazo basada en el perfil del inversor  
C) Ignora el perfil de riesgo  
D) Solo incluye renta variable

**Respuesta: B**

---

**38) Un benchmark adecuado debe ser:**

A) Imposible de replicar  
B) Coherente con la estrategia y universo de inversión  
C) El más rentable del mercado  
D) Secreto para el inversor

**Respuesta: B**

---

**39) El rebalanceo sirve principalmente para:**

A) Maximizar la rentabilidad garantizada  
B) Eliminar todo el riesgo  
C) Mantener el perfil de riesgo objetivo  
D) Evitar todos los costes

**Respuesta: C**

---

**40) En una cartera 70/30 (RV/RF), si la RV sube 20% y la RF 2%, el nuevo peso de RV es aproximadamente:**

A) 70%  
B) 73%  
C) 77%  
D) 90%

**Respuesta: B**

*RV = 70 × 1,20 = 84. RF = 30 × 1,02 = 30,6. Total = 114,6. Peso RV = 84/114,6 = 73,3%*

---

**41) El rebalanceo con estrategia de umbral significa:**

A) Rebalancear cada mes sin excepción  
B) Rebalancear cuando la desviación supera un porcentaje definido  
C) Nunca rebalancear  
D) Rebalancear solo en mercados alcistas

**Respuesta: B**

---

**42) Security selection se refiere a:**

A) Elegir el benchmark  
B) Seleccionar valores específicos dentro de cada categoría  
C) Determinar la exposición total al mercado  
D) Definir el horizonte temporal

**Respuesta: B**

---

## Bloque G: Medidas de Performance (43-50)

---

**43) El ratio de Sharpe mide:**

A) La rentabilidad total  
B) El exceso de rentabilidad por unidad de riesgo total  
C) El exceso de rentabilidad por unidad de beta  
D) La diferencia con el benchmark

**Respuesta: B**

---

**44) Si Rf = 2%, Rp = 14%, σp = 18%, el ratio de Sharpe es:**

A) 0,67  
B) 0,78  
C) 0,56  
D) 0,89

**Respuesta: A**

*Sharpe = (14% - 2%) / 18% = 0,67*

---

**45) El ratio de Treynor es más apropiado que el de Sharpe cuando:**

A) La cartera está poco diversificada  
B) La cartera está bien diversificada  
C) No existe benchmark  
D) La volatilidad es muy baja

**Respuesta: B**

---

**46) Si un fondo tiene Rp = 11%, Rf = 2%, β = 1,2, Rm = 9%, el alfa de Jensen es:**

A) +0,6%  
B) +2,0%  
C) -1,4%  
D) +9,4%

**Respuesta: A**

*α = 11% - [2% + 1,2 × (9% - 2%)] = 11% - 10,4% = +0,6%*

---

**47) Un tracking error del 0,5% indica:**

A) Gestión activa muy agresiva  
B) Gestión pasiva o muy cercana al índice  
C) Mala gestión  
D) Alta rentabilidad

**Respuesta: B**

---

**48) El VaR al 95% representa:**

A) La pérdida máxima posible  
B) La pérdida que solo se superará el 5% de las veces  
C) La rentabilidad esperada  
D) El riesgo sistemático

**Respuesta: B**

---

**49) El Maximum Drawdown (MDD) mide:**

A) La rentabilidad máxima histórica  
B) La caída máxima desde un pico hasta un valle  
C) La volatilidad mensual  
D) El tracking error máximo

**Respuesta: B**

---

**50) El ratio de información relaciona:**

A) Rentabilidad y volatilidad  
B) Exceso de rentabilidad sobre el benchmark y tracking error  
C) Alfa y beta  
D) Rentabilidad y tipo sin riesgo

**Respuesta: B**

*IR = (Rp - Rb) / TE*

---

# TEMA 14: CHECKLIST DE COMPETENCIAS

## Conceptos Fundamentales
- [ ] Defino qué es una cartera y sus objetivos principales
- [ ] Comprendo la diferencia entre crecimiento, rentas y preservación
- [ ] Identifico las restricciones típicas del inversor

## Rentabilidad
- [ ] Calculo rentabilidad simple y esperada
- [ ] Distingo entre rentabilidad simple y compuesta (CAGR)
- [ ] Comprendo la diferencia entre TWR y MWR
- [ ] Calculo rentabilidad de cartera como media ponderada

## Riesgo
- [ ] Defino volatilidad y calculo desviación típica
- [ ] Distingo riesgo sistemático y específico
- [ ] Calculo e interpreto la beta de un activo y cartera
- [ ] Calculo volatilidad de cartera con dos activos
- [ ] Aplico la hipótesis de normalidad (intervalos 68%, 95%)

## Correlación y Diversificación
- [ ] Interpreto correlaciones (+1, 0, -1)
- [ ] Comprendo el impacto de la correlación en el riesgo
- [ ] Conozco los límites de la diversificación
- [ ] Calculo cartera de riesgo cero con ρ = -1

## Eficiencia de Mercados
- [ ] Defino mercado eficiente
- [ ] Describo los tres niveles de eficiencia
- [ ] Identifico qué técnicas funcionan en cada nivel
- [ ] Conozco las principales anomalías de mercado

## Teoría de Carteras
- [ ] Conozco las hipótesis de Markowitz
- [ ] Defino cartera eficiente y frontera eficiente
- [ ] Calculo la cartera de mínima volatilidad
- [ ] Comprendo el CAPM y distingo CML de SML
- [ ] Valoro activos usando la SML

## Asset Allocation y Rebalanceo
- [ ] Distingo asignación estratégica y táctica
- [ ] Identifico carteras modelo por perfil
- [ ] Comprendo el proceso y beneficios del rebalanceo
- [ ] Calculo ajustes de rebalanceo

## Medidas de Performance
- [ ] Calculo e interpreto Ratio de Sharpe
- [ ] Calculo e interpreto Ratio de Treynor
- [ ] Calculo el Alfa de Jensen
- [ ] Defino Maximum Drawdown
- [ ] Calculo VaR paramétrico (95%, 99%)
- [ ] Calculo Tracking Error y Ratio de Información

## Benchmark y Atribución
- [ ] Identifico características de un buen benchmark
- [ ] Distingo gestión activa de pasiva por tracking error
- [ ] Descompongo rentabilidad en efectos AA y SS

## Perfil e Idoneidad
- [ ] Distingo componentes del perfil del inversor
- [ ] Comprendo diferencia entre test idoneidad y conveniencia
- [ ] Asocio perfiles con carteras adecuadas

---

# ANEXO: FÓRMULAS CLAVE

## Rentabilidad

| Concepto | Fórmula |
|----------|---------|
| Rentabilidad simple | R = (P₁ - P₀ + D) / P₀ |
| Rentabilidad cartera | Rp = Σ wᵢ × Rᵢ |
| CAGR | (VF / VI)^(1/n) - 1 |

## Riesgo

| Concepto | Fórmula |
|----------|---------|
| Volatilidad | σ = √[Σ(Rᵢ - R̄)² / n] |
| Volatilidad anualizada | σ_anual = σ_periodo × √n |
| Varianza cartera 2 activos | σp² = wA²σA² + wB²σB² + 2wAwBσAσBρ |
| Beta | β = Cov(Rᵢ, Rm) / σm² |
| Beta cartera | βp = Σ wᵢ × βᵢ |

## CAPM

| Concepto | Fórmula |
|----------|---------|
| CML | E(Rp) = Rf + [(E(Rm) - Rf) / σm] × σp |
| SML (CAPM) | E(Rᵢ) = Rf + βᵢ × (E(Rm) - Rf) |
| CMV (peso A) | wA = (σB² - Cov) / (σA² + σB² - 2Cov) |
| Cartera riesgo cero | wA = σB / (σA + σB) cuando ρ = -1 |

## Medidas de Performance

| Concepto | Fórmula |
|----------|---------|
| Sharpe | (Rp - Rf) / σp |
| Treynor | (Rp - Rf) / βp |
| Alfa de Jensen | Rp - [Rf + βp(Rm - Rf)] |
| Tracking Error | σ(Rp - Rb) |
| Ratio de Información | (Rp - Rb) / TE |
| VaR 95% | -E(R) + 1,65σ |
| VaR 99% | -E(R) + 2,33σ |
| Maximum Drawdown | (Valle - Pico) / Pico |

## Atribución

| Concepto | Fórmula |
|----------|---------|
| Asset Allocation | AA = Σ (wp,i - wb,i) × Rb,i |
| Security Selection | SS = Σ wp,i × (Rp,i - Rb,i) |

---

*Fin del Módulo 3 – Gestión de Carteras – Versión Definitiva*

*Documento fusionado según Guía EFPA España (marzo 2025 – V18/25)*
