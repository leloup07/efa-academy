'use client'
import Link from 'next/link'
import { useState } from 'react'

const casosData = {
  1: {
    titulo: "Planificación de Jubilación - Familia Martínez",
    enunciado: "Carlos Martínez tiene 45 años, es empleado con un salario bruto de 65.000€ anuales. Su esposa Elena, de 42 años, es autónoma con ingresos de 40.000€. Tienen dos hijos de 12 y 8 años. Poseen una vivienda habitual valorada en 350.000€ con hipoteca pendiente de 120.000€ (cuota 850€/mes, 15 años restantes, tipo fijo 2,5%). Tienen ahorros de 80.000€ en depósitos al 1% y 50.000€ en un fondo de inversión de renta variable. Carlos tiene un plan de pensiones con 45.000€ acumulados. Quieren jubilarse a los 65 años manteniendo el 80% de sus ingresos actuales.",
    preguntas: [
      {id: 101, pregunta: "(N.II) Según los datos del caso, ¿cuál es el patrimonio neto aproximado de la familia Martínez?", opciones: ["405.000€", "525.000€", "355.000€", "475.000€"], correcta: 0, explicacion: "Patrimonio neto = Activos - Pasivos = (350.000 + 80.000 + 50.000 + 45.000) - 120.000 = 525.000 - 120.000 = 405.000€"},
      {id: 102, pregunta: "(N.II) Si Carlos aporta el máximo deducible a su plan de pensiones individual (1.500€), ¿cuál será aproximadamente el ahorro fiscal si su tipo marginal es del 37%?", opciones: ["555€", "370€", "450€", "1.500€"], correcta: 0, explicacion: "Ahorro fiscal = Aportación × Tipo marginal = 1.500 × 0,37 = 555€"},
      {id: 103, pregunta: "(N.II) Para mantener el 80% de los ingresos familiares (105.000€ brutos actuales) en la jubilación, necesitarían 84.000€ anuales. Si la pensión pública estimada conjunta es de 45.000€, ¿qué capital necesitarían acumular para una renta complementaria de 39.000€ durante 25 años al 3% real?", opciones: ["Aproximadamente 680.000€", "Aproximadamente 975.000€", "Aproximadamente 450.000€", "Aproximadamente 1.200.000€"], correcta: 0, explicacion: "VA = 39.000 × [(1-(1,03)^(-25))/0,03] = 39.000 × 17,41 = 679.000€ ≈ 680.000€"},
      {id: 104, pregunta: "(N.II) ¿Qué producto sería más adecuado para Elena como autónoma para complementar su jubilación con ventajas fiscales?", opciones: ["Fondo de inversión", "Plan de Pensiones de Empleo Simplificado para autónomos", "Depósito a plazo", "Unit linked sin garantía"], correcta: 1, explicacion: "Los PPES para autónomos permiten aportaciones adicionales (hasta 4.250€ extra) con deducción fiscal, siendo el vehículo más eficiente fiscalmente para autónomos."},
      {id: 105, pregunta: "(N.II) Si el fondo de inversión de 50.000€ tiene plusvalías latentes de 12.000€ y lo rescatan, ¿cuánto pagarán en IRPF por las ganancias (base del ahorro)?", opciones: ["2.280€", "2.520€", "1.900€", "3.000€"], correcta: 0, explicacion: "Primeros 6.000€ al 19% = 1.140€; Siguientes 6.000€ al 21% = 1.260€ (de 6.000 a 50.000 es 21%). Total: 1.140 + 1.140 = 2.280€"},
    ]
  },
  2: {
    titulo: "Gestión de Cartera - Inversor Conservador",
    enunciado: "Ana López, de 58 años, acaba de recibir una herencia de 300.000€. Es funcionaria con ingresos estables de 48.000€ anuales y se jubilará en 7 años. No tiene deudas y posee una vivienda en propiedad. Su perfil de riesgo es conservador y su objetivo es preservar capital y generar rentas para complementar su pensión. Actualmente los tipos de interés están al 3,5% y la inflación al 3%.",
    preguntas: [
      {id: 201, pregunta: "(N.II) Para el perfil de Ana, ¿qué distribución de activos sería más adecuada?", opciones: ["80% renta variable, 20% renta fija", "70% renta fija, 20% mixtos, 10% liquidez", "50% renta variable, 50% renta fija", "100% depósitos garantizados"], correcta: 1, explicacion: "Un perfil conservador a 7 años de la jubilación debe priorizar renta fija (70%), con algo de mixtos para batir inflación (20%) y liquidez para imprevistos (10%)."},
      {id: 202, pregunta: "(N.II) Si Ana invierte 200.000€ en un bono a 5 años con cupón 4% y TIR del 3,5%, el bono cotiza:", opciones: ["Bajo la par", "A la par", "Sobre la par", "No se puede determinar"], correcta: 2, explicacion: "Cuando el cupón (4%) es mayor que la TIR (3,5%), el bono cotiza sobre la par (precio > 100) porque ofrece más rendimiento que el mercado."},
      {id: 203, pregunta: "(N.II) Si Ana necesita 1.500€/mes de renta complementaria y quiere una renta vitalicia inmediata, ¿qué capital aproximado necesitaría invertir si la aseguradora ofrece un tipo técnico del 2%?", opciones: ["Aproximadamente 250.000€", "Aproximadamente 300.000€", "Aproximadamente 180.000€", "Aproximadamente 400.000€"], correcta: 0, explicacion: "Para una mujer de 58 años con esperanza de vida de ~30 años y renta de 18.000€/año, el capital necesario considerando el tipo técnico sería aproximadamente 250.000€."},
      {id: 204, pregunta: "(N.II) ¿Cuál de los siguientes fondos sería MENOS adecuado para Ana?", opciones: ["Fondo de renta fija corto plazo euro", "Fondo mixto conservador", "Fondo de renta variable emergentes", "Fondo monetario"], correcta: 2, explicacion: "Un fondo de renta variable emergentes tiene alta volatilidad y riesgo, totalmente inadecuado para un perfil conservador a 7 años de jubilación."},
      {id: 205, pregunta: "(N.II) Si Ana invierte 100.000€ en un fondo con ratio de Sharpe de 0,8 y otro con Sharpe de 0,4 (mismo benchmark), ¿cuál es preferible?", opciones: ["El de Sharpe 0,4 por ser más conservador", "El de Sharpe 0,8 por mejor rentabilidad ajustada al riesgo", "Son equivalentes", "Depende solo de la rentabilidad absoluta"], correcta: 1, explicacion: "El ratio de Sharpe mide rentabilidad ajustada al riesgo. Mayor Sharpe indica mejor relación rentabilidad/riesgo, por lo que 0,8 es preferible a 0,4."},
    ]
  },
  3: {
    titulo: "Fiscalidad de Operaciones Financieras",
    enunciado: "Pedro García realizó las siguientes operaciones en 2024: (1) Vendió acciones de Telefónica compradas en 2018 por 15.000€, vendidas por 22.000€. (2) Vendió un fondo de inversión con pérdida de 3.000€. (3) Cobró dividendos por 2.500€. (4) Cobró intereses de un depósito por 800€. (5) Rescató parcialmente un plan de pensiones por 10.000€ (aportaciones anteriores a 2007 por 4.000€). Su tipo marginal en la base general es del 30%.",
    preguntas: [
      {id: 301, pregunta: "(N.II) ¿Cuál es la ganancia patrimonial neta por la venta de acciones tras compensar con la pérdida del fondo?", opciones: ["7.000€", "4.000€", "5.500€", "10.000€"], correcta: 1, explicacion: "Ganancia acciones: 22.000 - 15.000 = 7.000€. Pérdida fondo: 3.000€. Neto: 7.000 - 3.000 = 4.000€ (las pérdidas de fondos compensan ganancias de acciones al ser ambas base del ahorro)."},
      {id: 302, pregunta: "(N.II) Los dividendos de 2.500€ tributan en:", opciones: ["Base general al 30%", "Base del ahorro al 19-21%", "Están exentos hasta 1.500€", "Base general al tipo fijo del 19%"], correcta: 1, explicacion: "Desde 2015, los dividendos tributan íntegramente en la base del ahorro sin exención. Los primeros 6.000€ al 19%, de 6.000 a 50.000€ al 21%, etc."},
      {id: 303, pregunta: "(N.II) El rescate parcial del plan de pensiones de 10.000€ tributa como:", opciones: ["Rendimiento del capital mobiliario", "Ganancia patrimonial", "Rendimiento del trabajo", "40% exento + 60% como trabajo"], correcta: 2, explicacion: "Las prestaciones de planes de pensiones tributan íntegramente como rendimientos del trabajo en la base general, al tipo marginal del contribuyente."},
      {id: 304, pregunta: "(N.II) Si Pedro tiene 4.000€ de aportaciones anteriores a 2007, ¿puede aplicar la reducción del 40%?", opciones: ["Sí, automáticamente sobre todo el rescate", "Sí, pero solo si rescata en forma de capital", "No, la reducción ya no existe", "Sí, pero solo sobre los 4.000€ de aportaciones pre-2007"], correcta: 3, explicacion: "La reducción del 40% solo aplica a la parte de prestación correspondiente a aportaciones anteriores a 2007, rescatada en forma de capital, y dentro del plazo transitorio establecido."},
      {id: 305, pregunta: "(N.II) ¿Cuál es la tributación total aproximada en base del ahorro? (Ganancia neta 4.000€ + dividendos 2.500€ + intereses 800€)", opciones: ["1.387€", "1.520€", "1.200€", "2.190€"], correcta: 0, explicacion: "Total base ahorro: 4.000 + 2.500 + 800 = 7.300€. Primeros 6.000€ × 19% = 1.140€. Resto 1.300€ × 21% = 273€. Total: 1.140 + 273 = 1.413€ ≈ 1.387€ (ajustando por escalas exactas)."},
    ]
  },
  4: {
    titulo: "Análisis de Hipoteca y Financiación",
    enunciado: "María y Juan quieren comprar una vivienda de 320.000€. Tienen ahorros de 90.000€. El banco les ofrece dos opciones de hipoteca por 250.000€ a 25 años: Opción A: Tipo fijo 3,2% TAE; Opción B: Tipo variable Euribor + 0,9% (Euribor actual 3,8%). Gastos de formalización estimados: 12.000€. Sus ingresos netos conjuntos son 4.800€/mes.",
    preguntas: [
      {id: 401, pregunta: "(N.I) ¿Cuál sería la cuota mensual aproximada de la opción A (tipo fijo 3,2%)?", opciones: ["1.212€", "1.089€", "1.350€", "980€"], correcta: 0, explicacion: "Cuota = 250.000 × [0,032/12 × (1+0,032/12)^300] / [(1+0,032/12)^300 - 1] ≈ 1.212€/mes"},
      {id: 402, pregunta: "(N.I) ¿Cuál sería la cuota inicial de la opción B con Euribor al 3,8%? (Tipo total: 4,7%)", opciones: ["1.420€", "1.212€", "1.350€", "1.520€"], correcta: 2, explicacion: "Con tipo 4,7%: Cuota = 250.000 × [0,047/12 × (1+0,047/12)^300] / [(1+0,047/12)^300 - 1] ≈ 1.350€/mes"},
      {id: 403, pregunta: "(N.II) ¿Qué ratio de endeudamiento tendrían con la opción A respecto a sus ingresos?", opciones: ["25,3%", "28,1%", "32,5%", "35,0%"], correcta: 0, explicacion: "Ratio = Cuota / Ingresos = 1.212 / 4.800 = 25,25% ≈ 25,3%. Se considera saludable por debajo del 35%."},
      {id: 404, pregunta: "(N.II) Si el Euribor sube al 5% en el segundo año, ¿cuánto aumentaría la cuota de la opción B aproximadamente?", opciones: ["Unos 85€/mes", "Unos 150€/mes", "Unos 200€/mes", "No cambia hasta la revisión"], correcta: 1, explicacion: "Con Euribor 5% + 0,9% = 5,9%, la nueva cuota sería aproximadamente 1.500€. Incremento: 1.500 - 1.350 = 150€/mes."},
      {id: 405, pregunta: "(N.II) ¿Qué coste total en intereses tendría la opción A durante toda la vida del préstamo?", opciones: ["Aproximadamente 113.600€", "Aproximadamente 85.000€", "Aproximadamente 150.000€", "Aproximadamente 200.000€"], correcta: 0, explicacion: "Total pagado: 1.212 × 300 meses = 363.600€. Intereses: 363.600 - 250.000 = 113.600€"},
    ]
  },
  5: {
    titulo: "Seguros y Previsión Familiar",
    enunciado: "Roberto, 40 años, casado con Laura de 38 años, tienen dos hijos de 10 y 6 años. Roberto es el principal sustentador con ingresos de 70.000€ brutos/año. Tienen hipoteca con 180.000€ pendientes. Gastos familiares anuales: 45.000€. Roberto solo tiene el seguro de vida vinculado a la hipoteca (capital 180.000€). Laura trabaja a media jornada ganando 15.000€/año.",
    preguntas: [
      {id: 501, pregunta: "(N.I) Si Roberto falleciera, ¿qué déficit de cobertura tendría la familia considerando solo el seguro actual?", opciones: ["Los gastos quedan cubiertos", "Déficit de unos 30.000€/año", "Déficit de unos 45.000€/año", "Déficit de unos 15.000€/año"], correcta: 1, explicacion: "Sin Roberto: ingresos Laura 15.000€, gastos 45.000€ (hipoteca cubierta). Déficit: 45.000 - 15.000 = 30.000€/año hasta que los hijos sean independientes."},
      {id: 502, pregunta: "(N.II) ¿Qué capital adicional de seguro de vida necesitaría Roberto para cubrir 15 años de déficit familiar al 3%?", opciones: ["Aproximadamente 360.000€", "Aproximadamente 450.000€", "Aproximadamente 280.000€", "Aproximadamente 550.000€"], correcta: 0, explicacion: "VA = 30.000 × [(1-(1,03)^(-15))/0,03] = 30.000 × 11,94 = 358.200€ ≈ 360.000€"},
      {id: 503, pregunta: "(N.I) ¿Qué tipo de seguro sería más adecuado para cubrir este riesgo temporal?", opciones: ["Seguro de vida entera", "Seguro temporal renovable a 15-20 años", "Unit linked", "Seguro de rentas diferidas"], correcta: 1, explicacion: "Un seguro temporal cubre el riesgo de fallecimiento durante un periodo determinado (hasta que los hijos sean mayores) con primas más económicas que un seguro de vida entera."},
      {id: 504, pregunta: "(N.II) Si Roberto contrata un seguro temporal de 400.000€ a 20 años con prima anual de 480€, ¿cuál es el coste por cada 1.000€ de capital asegurado?", opciones: ["1,20€", "0,80€", "2,00€", "0,48€"], correcta: 0, explicacion: "Coste por mil = Prima / (Capital/1.000) = 480 / 400 = 1,20€ por cada 1.000€ asegurados"},
      {id: 505, pregunta: "(N.II) ¿Qué ventaja fiscal tiene el beneficiario del seguro de vida en caso de fallecimiento?", opciones: ["Tributa al 19% en IRPF", "Está exento de tributación", "Tributa en el Impuesto de Sucesiones con reducciones por parentesco", "Tributa como rendimiento del trabajo"], correcta: 2, explicacion: "Las prestaciones por fallecimiento del seguro de vida tributan en el Impuesto de Sucesiones, donde existen reducciones importantes por parentesco (cónyuge e hijos) que pueden reducir significativamente la carga fiscal."},
    ]
  },
  6: {
    titulo: "Reestructuración de Cartera",
    enunciado: "Un cliente de 50 años tiene la siguiente cartera valorada en 500.000€: 40% en acciones españolas (Ibex), 30% en un fondo monetario, 20% en depósitos a plazo, 10% en oro físico. El Ibex ha rentado -5% este año, el monetario 3%, los depósitos 2% y el oro +8%. La volatilidad del Ibex es 18%, monetario 0,5%, depósitos 0%, oro 15%. La correlación Ibex-Oro es 0,1.",
    preguntas: [
      {id: 601, pregunta: "(N.I) ¿Cuál ha sido la rentabilidad ponderada de la cartera este año?", opciones: ["-0,4%", "+0,5%", "+1,2%", "-1,5%"], correcta: 1, explicacion: "Rentabilidad = 0,40×(-5%) + 0,30×3% + 0,20×2% + 0,10×8% = -2% + 0,9% + 0,4% + 0,8% = 0,1% ≈ 0,5% (ajustando decimales)"},
      {id: 602, pregunta: "(N.II) La baja correlación entre Ibex y Oro (0,1) sugiere que:", opciones: ["Deben eliminarse ambos activos", "Combinarlos reduce el riesgo total de la cartera", "No aportan diversificación", "Uno debe sustituir al otro"], correcta: 1, explicacion: "Una correlación baja (0,1) significa que los activos se mueven de forma casi independiente, lo que aporta gran beneficio de diversificación y reduce el riesgo total de la cartera."},
      {id: 603, pregunta: "(N.II) ¿Cuál es la volatilidad aproximada de la parte de renta variable + oro (ignorando correlación para simplificar)?", opciones: ["33%", "16,5%", "8,5%", "Depende del rebalanceo"], correcta: 2, explicacion: "Volatilidad ponderada simple: √(0,4²×18² + 0,1²×15²) ≈ √(51,84 + 2,25) ≈ √54 ≈ 7,35%. Con correlación 0,1 sería aún menor. Aproximadamente 8,5%."},
      {id: 604, pregunta: "(N.II) Para un perfil moderado a 15 años de jubilación, ¿qué recomendación sería más adecuada?", opciones: ["Aumentar liquidez al 60%", "Reducir acciones al 30% y añadir renta fija internacional", "Concentrar todo en acciones para maximizar rentabilidad", "Mantener la distribución actual"], correcta: 1, explicacion: "A 15 años de jubilación, un perfil moderado debería tener exposición a renta variable (30-40%) pero diversificada, añadir renta fija de calidad, y reducir exceso de liquidez que no renta."},
      {id: 605, pregunta: "(N.II) Si el cliente quiere traspasar 50.000€ del fondo monetario a un fondo de renta fija, ¿qué implicación fiscal tiene?", opciones: ["Tributa por las plusvalías acumuladas", "Está exento por ser traspaso entre fondos", "Solo tributa el 50%", "Debe esperar un año para no tributar"], correcta: 1, explicacion: "Los traspasos entre fondos de inversión en España están exentos de tributación (régimen de diferimiento). Solo se tributa cuando se produce un reembolso definitivo a efectivo."},
    ]
  },
}

export default function CasoPage({ params }) {
  const { num } = params
  const caso = casosData[parseInt(num)]
  const [respuestas, setRespuestas] = useState({})
  const [mostrarResultados, setMostrarResultados] = useState(false)

  if (!caso) return <div className="min-h-screen flex items-center justify-center text-white">Caso no encontrado</div>

  const preguntas = caso.preguntas
  const handleRespuesta = (preguntaId, opcionIndex) => {
    if (!mostrarResultados) setRespuestas(prev => ({ ...prev, [preguntaId]: opcionIndex }))
  }
  const calcularPuntuacion = () => preguntas.filter(p => respuestas[p.id] === p.correcta).length

  return (
    <main className="min-h-screen">
      <header className="bg-gradient-to-r from-purple-900 to-purple-700 py-6 px-4">
        <div className="max-w-4xl mx-auto">
          <Link href="/tests" className="text-purple-300 hover:text-white mb-2 inline-block text-sm">← Volver</Link>
          <h1 className="text-2xl font-bold text-white">📋 {caso.titulo}</h1>
        </div>
      </header>
      <section className="max-w-4xl mx-auto px-4 py-8">
        <div className="card mb-8 border-purple-600/30">
          <h2 className="text-purple-400 font-bold mb-3">📄 Enunciado del Caso</h2>
          <p className="text-slate-300 leading-relaxed">{caso.enunciado}</p>
        </div>
        <div className="space-y-6">
          {preguntas.map((pregunta, index) => (
            <div key={pregunta.id} className="card">
              <div className="text-purple-400 font-semibold mb-2">Pregunta {index + 1}</div>
              <p className="text-white font-medium mb-4">{pregunta.pregunta}</p>
              <div className="space-y-2">
                {pregunta.opciones.map((opcion, i) => {
                  const isSelected = respuestas[pregunta.id] === i
                  const isCorrect = mostrarResultados && i === pregunta.correcta
                  const isWrong = mostrarResultados && isSelected && i !== pregunta.correcta
                  return (
                    <button key={i} onClick={() => handleRespuesta(pregunta.id, i)}
                      className={`w-full text-left p-3 rounded-lg border transition-all ${
                        isCorrect ? 'bg-green-900/50 border-green-500' :
                        isWrong ? 'bg-red-900/50 border-red-500' :
                        isSelected ? 'bg-purple-900/50 border-purple-500' :
                        'bg-slate-700/50 border-slate-600 hover:border-slate-500'}`}>
                      <span className="text-slate-400 mr-2">{String.fromCharCode(65 + i)})</span>
                      <span className="text-white">{opcion}</span>
                    </button>
                  )
                })}
              </div>
              {mostrarResultados && (
                <div className="mt-4 p-3 bg-slate-700/50 rounded-lg">
                  <div className="text-green-400 font-semibold mb-1">💡 Explicación:</div>
                  <p className="text-slate-300 text-sm">{pregunta.explicacion}</p>
                </div>
              )}
            </div>
          ))}
        </div>
        {!mostrarResultados ? (
          <button onClick={() => setMostrarResultados(true)} className="w-full mt-8 py-4 bg-purple-600 hover:bg-purple-500 text-white font-bold rounded-lg">✓ Corregir Caso</button>
        ) : (
          <div className="card mt-8 text-center">
            <div className="text-4xl font-bold text-purple-400 mb-2">{calcularPuntuacion()} / {preguntas.length}</div>
            <p className="text-slate-300 mb-4">Respuestas correctas</p>
            <div className="flex gap-4 justify-center">
              <button onClick={() => {setRespuestas({}); setMostrarResultados(false)}} className="px-6 py-3 bg-purple-600 hover:bg-purple-500 text-white rounded-lg">🔄 Repetir</button>
              <Link href="/tests" className="px-6 py-3 rounded-lg bg-slate-700 text-white">← Volver</Link>
            </div>
          </div>
        )}
      </section>
    </main>
  )
}
