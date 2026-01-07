'use client'
import Link from 'next/link'
import { useState } from 'react'

const preguntasPorModulo = {
  eip: {
    1: [
      {id: 1, pregunta: "¿Qué describe mejor la diferencia entre mercado primario y secundario?", opciones: ["En primario se negocian activos ya emitidos", "En primario se produce la emisión inicial; en secundario intercambian activos", "En primario solo operan minoristas", "No existe diferencia"], correcta: 1, explicacion: "El mercado primario es donde el emisor capta fondos mediante la emisión inicial."},
      {id: 2, pregunta: "Si los tipos suben del 3% al 4%, un bono con duración 5:", opciones: ["Subirá un 5%", "Bajará un 5%", "No cambiará", "Subirá un 1%"], correcta: 1, explicacion: "Variación ≈ -Duración × Δtipos = -5 × 1% = -5%"},
      {id: 3, pregunta: "El riesgo específico se reduce mediante:", opciones: ["Apalancamiento", "Diversificación", "Alta beta", "Concentración"], correcta: 1, explicacion: "El riesgo específico se reduce diversificando."},
      {id: 4, pregunta: "Una opción call otorga:", opciones: ["Derecho a vender", "Derecho a comprar", "Obligación de comprar", "Obligación de vender"], correcta: 1, explicacion: "Call = derecho a comprar."},
      {id: 5, pregunta: "El spread bid-ask representa:", opciones: ["Tipo del banco central", "Coste de transacción", "Impuesto", "Dividendo"], correcta: 1, explicacion: "Es un coste implícito de liquidez."},
      {id: 6, pregunta: "La TIR de un bono es:", opciones: ["El cupón nominal", "La tasa que iguala precio y valor actual de flujos", "La inflación esperada", "La beta del bono"], correcta: 1, explicacion: "La TIR iguala el precio con el VA de los flujos."},
      {id: 7, pregunta: "Un índice por capitalización pondera según:", opciones: ["Mismo peso todos", "Capitalización bursátil", "Dividendo", "Volatilidad"], correcta: 1, explicacion: "Peso proporcional a capitalización."},
      {id: 8, pregunta: "La duración modificada mide:", opciones: ["Plazo", "Sensibilidad a tipos", "Cupón acumulado", "Rating"], correcta: 1, explicacion: "Variación % del precio ante 1% en TIR."},
      {id: 9, pregunta: "NO es riesgo de renta fija:", opciones: ["Tipo de interés", "Crédito", "Dilución", "Liquidez"], correcta: 2, explicacion: "Dilución es de renta variable."},
      {id: 10, pregunta: "El PER indica:", opciones: ["Precio/BPA", "BPA/Precio", "Dividendo/Precio", "Valor contable/Precio"], correcta: 0, explicacion: "PER = Precio / Beneficio por Acción."},
    ],
    2: [
      {id: 1, pregunta: "El valor liquidativo de un fondo se calcula:", opciones: ["Diariamente al cierre", "Semanalmente", "Mensualmente", "Al inicio del año"], correcta: 0, explicacion: "El VL se calcula diariamente."},
      {id: 2, pregunta: "Un fondo de inversión es:", opciones: ["Una sociedad anónima cotizada", "Un patrimonio colectivo sin personalidad jurídica", "Un depósito bancario", "Una póliza de seguro"], correcta: 1, explicacion: "El fondo es patrimonio colectivo gestionado por una SGIIC."},
      {id: 3, pregunta: "La comisión de gestión de un fondo:", opciones: ["Se cobra al suscribir", "Se descuenta diariamente del patrimonio", "Se cobra al reembolsar", "No existe en España"], correcta: 1, explicacion: "Se deduce del patrimonio diariamente."},
      {id: 4, pregunta: "Un ETF se diferencia de un fondo tradicional en:", opciones: ["No tiene comisiones", "Cotiza en bolsa en tiempo real", "No invierte en acciones", "Solo para institucionales"], correcta: 1, explicacion: "Los ETF cotizan como acciones."},
      {id: 5, pregunta: "El traspaso entre fondos en España:", opciones: ["Tributa siempre", "Está exento fiscalmente", "Solo tributa si hay pérdida", "No está permitido"], correcta: 1, explicacion: "Los traspasos entre fondos están exentos de tributación."},
      {id: 6, pregunta: "Una SICAV es:", opciones: ["Un fondo de pensiones", "Una sociedad de inversión de capital variable", "Un depósito estructurado", "Un seguro unit linked"], correcta: 1, explicacion: "SICAV = Sociedad de Inversión de Capital Variable."},
      {id: 7, pregunta: "El ratio de Sharpe mide:", opciones: ["Rentabilidad total", "Exceso de rentabilidad por unidad de riesgo", "Volatilidad", "Correlación"], correcta: 1, explicacion: "Sharpe = (Rent - Rf) / Volatilidad."},
      {id: 8, pregunta: "La frontera eficiente representa:", opciones: ["Carteras con máximo riesgo", "Carteras con máxima rentabilidad para cada nivel de riesgo", "Carteras sin riesgo", "El mercado total"], correcta: 1, explicacion: "Máxima rentabilidad esperada para cada nivel de riesgo."},
      {id: 9, pregunta: "Un fondo garantizado:", opciones: ["Garantiza siempre rentabilidad positiva", "Garantiza el capital a vencimiento bajo condiciones", "No tiene riesgo", "Es ilegal en España"], correcta: 1, explicacion: "Garantiza capital y/o rentabilidad a vencimiento."},
      {id: 10, pregunta: "La SGIIC es:", opciones: ["El banco custodio", "La sociedad gestora del fondo", "El supervisor", "El partícipe"], correcta: 1, explicacion: "Sociedad Gestora de Instituciones de Inversión Colectiva."},
    ],
    3: [
      {id: 1, pregunta: "La diversificación reduce:", opciones: ["El riesgo sistemático", "El riesgo específico", "Ambos riesgos", "Ningún riesgo"], correcta: 1, explicacion: "Solo reduce el riesgo específico (idiosincrático)."},
      {id: 2, pregunta: "Una beta de 1.5 significa:", opciones: ["Menos volátil que el mercado", "50% más volátil que el mercado", "Correlación negativa", "Sin riesgo"], correcta: 1, explicacion: "Beta > 1 indica mayor sensibilidad al mercado."},
      {id: 3, pregunta: "El CAPM establece que la rentabilidad esperada depende de:", opciones: ["La volatilidad total", "El riesgo sistemático (beta)", "El dividendo", "El PER"], correcta: 1, explicacion: "CAPM: E(R) = Rf + β(Rm - Rf)"},
      {id: 4, pregunta: "La correlación perfecta positiva (+1) implica:", opciones: ["Máximo beneficio de diversificación", "Ningún beneficio de diversificación", "Activos se mueven en dirección opuesta", "Activos independientes"], correcta: 1, explicacion: "Correlación +1 elimina el beneficio de diversificación."},
      {id: 5, pregunta: "El ratio de Treynor mide:", opciones: ["Rentabilidad total", "Exceso de rentabilidad por unidad de beta", "Volatilidad", "Correlación"], correcta: 1, explicacion: "Treynor = (Rent - Rf) / Beta"},
      {id: 6, pregunta: "La gestión activa busca:", opciones: ["Replicar un índice", "Batir al benchmark", "Minimizar costes", "Eliminar todo riesgo"], correcta: 1, explicacion: "Gestión activa intenta superar al índice de referencia."},
      {id: 7, pregunta: "El tracking error bajo indica:", opciones: ["Alta gestión activa", "Gestión muy cercana al índice", "Alto riesgo", "Mala gestión"], correcta: 1, explicacion: "Tracking error bajo = réplica cercana del benchmark."},
      {id: 8, pregunta: "El rebalanceo de cartera sirve para:", opciones: ["Aumentar el riesgo", "Mantener la asignación objetivo", "Eliminar activos", "Pagar menos impuestos"], correcta: 1, explicacion: "Reajusta pesos para mantener la estrategia."},
      {id: 9, pregunta: "Una cartera en la frontera eficiente:", opciones: ["Tiene el máximo riesgo posible", "No puede mejorar rentabilidad sin aumentar riesgo", "Está mal diversificada", "Solo tiene renta fija"], correcta: 1, explicacion: "Carteras óptimas en términos de rentabilidad-riesgo."},
      {id: 10, pregunta: "El alfa de Jensen mide:", opciones: ["El riesgo total", "La rentabilidad extra sobre la esperada por CAPM", "La volatilidad", "La correlación"], correcta: 1, explicacion: "Alfa positivo indica gestión que añade valor."},
    ],
    4: [
      {id: 1, pregunta: "Un seguro de vida-ahorro:", opciones: ["Solo cubre fallecimiento", "Combina ahorro e inversión con cobertura", "No tiene valor de rescate", "Es un producto bancario"], correcta: 1, explicacion: "Combina componente de ahorro con cobertura."},
      {id: 2, pregunta: "El tomador de un seguro es:", opciones: ["Quien recibe la indemnización", "Quien contrata y paga las primas", "El asegurado siempre", "La compañía de seguros"], correcta: 1, explicacion: "Tomador contrata y paga; puede coincidir o no con asegurado."},
      {id: 3, pregunta: "Un unit linked es:", opciones: ["Un fondo de inversión", "Un seguro donde el tomador asume el riesgo de inversión", "Un plan de pensiones", "Una cuenta corriente"], correcta: 1, explicacion: "Seguro donde las provisiones se invierten según elección del cliente."},
      {id: 4, pregunta: "El valor de rescate de un seguro es:", opciones: ["La prima pagada", "El importe que recibe si cancela anticipadamente", "El capital asegurado", "Los intereses"], correcta: 1, explicacion: "Cantidad recuperable al cancelar el contrato."},
      {id: 5, pregunta: "La prima de un seguro depende de:", opciones: ["Solo la edad", "Edad, capital, riesgo y gastos", "Solo el capital", "El banco"], correcta: 1, explicacion: "Múltiples factores determinan la prima."},
      {id: 6, pregunta: "Un seguro temporal cubre:", opciones: ["Toda la vida", "Un período determinado", "Solo invalidez", "Solo accidentes"], correcta: 1, explicacion: "Cobertura por plazo definido."},
      {id: 7, pregunta: "La provisión matemática representa:", opciones: ["Los gastos de gestión", "La reserva para obligaciones futuras", "El beneficio del asegurador", "La comisión del agente"], correcta: 1, explicacion: "Reserva técnica para pagar prestaciones."},
      {id: 8, pregunta: "El beneficiario de un seguro de vida:", opciones: ["Es siempre el tomador", "Es quien recibe la prestación", "Es la aseguradora", "No puede cambiarse"], correcta: 1, explicacion: "Designado por el tomador, recibe la prestación."},
      {id: 9, pregunta: "Un seguro de rentas:", opciones: ["Paga un capital único", "Paga prestaciones periódicas", "Solo cubre fallecimiento", "No existe en España"], correcta: 1, explicacion: "Rentas vitalicias o temporales."},
      {id: 10, pregunta: "La DGS supervisa:", opciones: ["Solo bancos", "Entidades aseguradoras", "Solo fondos", "El mercado de valores"], correcta: 1, explicacion: "Dirección General de Seguros y Fondos de Pensiones."},
    ],
    5: [
      {id: 1, pregunta: "Un plan de pensiones individual:", opciones: ["Permite rescate libre", "Tiene contingencias tasadas para el cobro", "No tiene ventajas fiscales", "Es un producto de renta fija"], correcta: 1, explicacion: "Solo se cobra por contingencias: jubilación, fallecimiento, etc."},
      {id: 2, pregunta: "Las aportaciones a planes de pensiones:", opciones: ["No desgravan", "Reducen la base imponible del IRPF", "Están exentas totalmente", "Tributan como ganancia patrimonial"], correcta: 1, explicacion: "Reducen la base imponible con límites."},
      {id: 3, pregunta: "El rescate de un plan tributa como:", opciones: ["Ganancia patrimonial", "Rendimiento del trabajo", "Renta exenta", "Rendimiento del capital"], correcta: 1, explicacion: "Las prestaciones tributan como rendimiento del trabajo."},
      {id: 4, pregunta: "La contingencia de jubilación permite:", opciones: ["Cobrar a cualquier edad", "Cobrar al acceder a la jubilación legal", "Solo cobrar en forma de renta", "No cobrar nunca"], correcta: 1, explicacion: "Se activa con la jubilación efectiva."},
      {id: 5, pregunta: "Los PPES (Planes de Pensiones de Empleo Simplificados):", opciones: ["Son solo para autónomos", "Permiten mayores aportaciones empresariales", "No tienen ventajas fiscales", "Son ilegales"], correcta: 1, explicacion: "Nuevo vehículo para pensiones de empleo con beneficios."},
      {id: 6, pregunta: "El límite actual de aportación a planes individuales es:", opciones: ["1.500€ anuales", "8.000€ anuales", "Sin límite", "10.000€ anuales"], correcta: 0, explicacion: "Desde 2022, el límite es 1.500€/año."},
      {id: 7, pregunta: "La regla de los 10 años de antigüedad permite:", opciones: ["Mayor desgravación", "Rescatar aportaciones con más de 10 años", "Cambiar de plan", "Menor tributación"], correcta: 1, explicacion: "Desde 2025 se pueden rescatar aportaciones con 10+ años."},
      {id: 8, pregunta: "Un plan de empleo es promovido por:", opciones: ["El partícipe", "La empresa para sus trabajadores", "El banco", "La CNMV"], correcta: 1, explicacion: "La empresa promueve el plan para sus empleados."},
      {id: 9, pregunta: "La movilización de planes permite:", opciones: ["Cambiar de banco", "Traspasar derechos a otro plan", "Retirar dinero libre", "Mayor rentabilidad"], correcta: 1, explicacion: "Se pueden mover derechos consolidados entre planes."},
      {id: 10, pregunta: "El déficit del sistema público de pensiones se debe a:", opciones: ["Demasiados cotizantes", "Envejecimiento demográfico y ratio cotizantes/pensionistas", "Pensiones muy bajas", "Exceso de ahorro privado"], correcta: 1, explicacion: "Menos cotizantes por pensionista y mayor longevidad."},
    ]
  }
}

const preguntasDefault = [
  {id: 1, pregunta: "Pregunta de ejemplo para este módulo", opciones: ["Opción A", "Opción B (correcta)", "Opción C", "Opción D"], correcta: 1, explicacion: "Contenido en desarrollo. Próximamente más preguntas."},
]

const nombreModulo = {
  1: 'Instrumentos y Mercados',
  2: 'Fondos y Sociedades',
  3: 'Gestión de Carteras',
  4: 'Seguros',
  5: 'Pensiones',
  6: 'Inversión Inmobiliaria',
  7: 'Crédito y Financiación',
  8: 'Fiscalidad',
  9: 'Cumplimiento Normativo'
}

export default function TestModuloPage({ params }) {
  const { nivel, modulo } = params
  const [respuestas, setRespuestas] = useState({})
  const [mostrarResultados, setMostrarResultados] = useState(false)

  const preguntas = preguntasPorModulo[nivel]?.[parseInt(modulo)] || preguntasDefault

  const handleRespuesta = (preguntaId, opcionIndex) => {
    if (!mostrarResultados) {
      setRespuestas(prev => ({ ...prev, [preguntaId]: opcionIndex }))
    }
  }

  const calcularPuntuacion = () => {
    let correctas = 0
    preguntas.forEach(p => {
      if (respuestas[p.id] === p.correcta) correctas++
    })
    return correctas
  }

  const reiniciar = () => {
    setRespuestas({})
    setMostrarResultados(false)
  }

  return (
    <main className="min-h-screen">
      <header className="bg-gradient-to-r from-blue-900 to-blue-700 py-6 px-4 sticky top-0 z-10">
        <div className="max-w-4xl mx-auto">
          <Link href="/tests" className="text-blue-300 hover:text-white mb-2 inline-block text-sm">
            ← Volver a Tests
          </Link>
          <h1 className="text-2xl font-bold text-white">
            {nivel.toUpperCase()} - Módulo {modulo}: {nombreModulo[modulo] || 'Test'}
          </h1>
        </div>
      </header>

      <section className="max-w-4xl mx-auto px-4 py-8">
        <div className="space-y-6">
          {preguntas.map((pregunta, index) => (
            <div key={pregunta.id} className="card">
              <div className="text-blue-400 font-semibold mb-2">Pregunta {index + 1}</div>
              <p className="text-white font-medium mb-4">{pregunta.pregunta}</p>
              
              <div className="space-y-2">
                {pregunta.opciones.map((opcion, i) => {
                  const isSelected = respuestas[pregunta.id] === i
                  const isCorrect = mostrarResultados && i === pregunta.correcta
                  const isWrong = mostrarResultados && isSelected && i !== pregunta.correcta
                  
                  return (
                    <button
                      key={i}
                      onClick={() => handleRespuesta(pregunta.id, i)}
                      className={`w-full text-left p-3 rounded-lg border transition-all ${
                        isCorrect ? 'bg-green-900/50 border-green-500' :
                        isWrong ? 'bg-red-900/50 border-red-500' :
                        isSelected ? 'bg-blue-900/50 border-blue-500' :
                        'bg-slate-700/50 border-slate-600 hover:border-slate-500'
                      }`}
                    >
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
          <button
            onClick={() => setMostrarResultados(true)}
            className="btn-primary w-full mt-8"
          >
            ✓ Corregir Test
          </button>
        ) : (
          <div className="card mt-8 text-center">
            <div className="text-4xl font-bold text-blue-400 mb-2">
              {calcularPuntuacion()} / {preguntas.length}
            </div>
            <p className="text-slate-300 mb-4">Respuestas correctas</p>
            <div className="flex gap-4 justify-center">
              <button onClick={reiniciar} className="btn-primary">
                🔄 Repetir Test
              </button>
              <Link href="/tests" className="px-6 py-3 rounded-lg bg-slate-700 text-white">
                ← Volver a Tests
              </Link>
            </div>
          </div>
        )}
      </section>
    </main>
  )
}
