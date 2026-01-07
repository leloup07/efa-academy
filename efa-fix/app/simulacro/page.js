'use client'
import Link from 'next/link'
import { useState, useEffect } from 'react'

const preguntas = [
  {id: 1, pregunta: "¿Qué describe mejor la diferencia entre mercado primario y secundario?", opciones: ["En primario se negocian activos ya emitidos", "En primario se produce la emisión inicial; en secundario los inversores intercambian activos", "En primario solo operan minoristas", "No existe diferencia"], correcta: 1},
  {id: 2, pregunta: "Si los tipos suben del 3% al 4%, un bono con duración 5:", opciones: ["Subirá un 5%", "Bajará un 5%", "No cambiará", "Subirá un 1%"], correcta: 1},
  {id: 3, pregunta: "El riesgo específico se reduce mediante:", opciones: ["Apalancamiento", "Diversificación", "Alta beta", "Concentración"], correcta: 1},
  {id: 4, pregunta: "Una opción call otorga:", opciones: ["Derecho a vender", "Derecho a comprar", "Obligación de comprar", "Obligación de vender"], correcta: 1},
  {id: 5, pregunta: "El spread bid-ask representa:", opciones: ["Tipo del banco central", "Coste de transacción", "Impuesto", "Dividendo"], correcta: 1},
  {id: 6, pregunta: "La TIR de un bono es:", opciones: ["El cupón nominal", "La tasa que iguala precio y valor actual de flujos", "La inflación esperada", "La beta del bono"], correcta: 1},
  {id: 7, pregunta: "Un índice por capitalización pondera según:", opciones: ["Mismo peso todos", "Capitalización bursátil", "Dividendo", "Volatilidad"], correcta: 1},
  {id: 8, pregunta: "El riesgo de reinversión es:", opciones: ["Variación de precio", "Impago", "Reinvertir cupones a tipos menores", "Tipo de cambio"], correcta: 2},
  {id: 9, pregunta: "Correlación baja entre activos:", opciones: ["Aumenta riesgo", "No afecta", "Reduce riesgo conjunto", "Elimina volatilidad"], correcta: 2},
  {id: 10, pregunta: "Un forward de divisa es:", opciones: ["Contrato organizado", "Contrato OTC para intercambio futuro", "ETF de divisa", "Depósito a plazo"], correcta: 1},
  {id: 11, pregunta: "Si BCE sube tipos, el euro:", opciones: ["Se deprecia", "Se aprecia", "No cambia", "Desaparece"], correcta: 1},
  {id: 12, pregunta: "La duración modificada mide:", opciones: ["Plazo", "Sensibilidad a tipos", "Cupón acumulado", "Rating"], correcta: 1},
  {id: 13, pregunta: "NO es riesgo de renta fija:", opciones: ["Tipo de interés", "Crédito", "Dilución", "Liquidez"], correcta: 2},
  {id: 14, pregunta: "Bono callable significa:", opciones: ["Tenedor exige reembolso", "Emisor amortiza anticipado", "Cupón variable", "Indexado inflación"], correcta: 1},
  {id: 15, pregunta: "El PER indica:", opciones: ["Precio/BPA", "BPA/Precio", "Dividendo/Precio", "Valor contable/Precio"], correcta: 0},
  {id: 16, pregunta: "En CAPM, beta mide:", opciones: ["Volatilidad total", "Riesgo sistemático", "Dividendos", "Riesgo crédito"], correcta: 1},
  {id: 17, pregunta: "Diferencia futuro vs opción:", opciones: ["Futuro OTC, opción organizada", "Futuro obligación, opción derecho para comprador", "Opciones más líquidas", "Futuros sin vencimiento"], correcta: 1},
  {id: 18, pregunta: "Nocional de swap 10M€ significa:", opciones: ["Se intercambian 10M", "Base de cálculo de intereses", "Pérdida máxima 10M", "Coste 10M"], correcta: 1},
  {id: 19, pregunta: "Tracking error mide:", opciones: ["Errores del broker", "Desviación vs benchmark", "Error del VL", "Bid-ask"], correcta: 1},
  {id: 20, pregunta: "Inversor conservador 2 años debe evitar:", opciones: ["Letras Tesoro", "Depósitos", "Fondos monetarios", "Acciones volátiles"], correcta: 3},
  {id: 21, pregunta: "El valor liquidativo de un fondo se calcula:", opciones: ["Diariamente al cierre", "Semanalmente", "Mensualmente", "Al inicio del año"], correcta: 0},
  {id: 22, pregunta: "Un fondo de inversión es:", opciones: ["Una sociedad anónima cotizada", "Un patrimonio colectivo sin personalidad jurídica", "Un depósito bancario", "Una póliza de seguro"], correcta: 1},
  {id: 23, pregunta: "La comisión de gestión de un fondo:", opciones: ["Se cobra al suscribir", "Se descuenta diariamente del patrimonio", "Se cobra al reembolsar", "No existe en España"], correcta: 1},
  {id: 24, pregunta: "Un ETF se diferencia de un fondo tradicional en:", opciones: ["No tiene comisiones", "Cotiza en bolsa en tiempo real", "No invierte en acciones", "Solo para institucionales"], correcta: 1},
  {id: 25, pregunta: "El traspaso entre fondos en España:", opciones: ["Tributa siempre", "Está exento fiscalmente", "Solo tributa si hay pérdida", "No está permitido"], correcta: 1},
  {id: 26, pregunta: "Una SICAV es:", opciones: ["Un fondo de pensiones", "Una sociedad de inversión de capital variable", "Un depósito estructurado", "Un seguro unit linked"], correcta: 1},
  {id: 27, pregunta: "El ratio de Sharpe mide:", opciones: ["Rentabilidad total", "Exceso de rentabilidad por unidad de riesgo", "Volatilidad", "Correlación"], correcta: 1},
  {id: 28, pregunta: "La frontera eficiente representa:", opciones: ["Carteras con máximo riesgo", "Carteras con máxima rentabilidad para cada nivel de riesgo", "Carteras sin riesgo", "El mercado total"], correcta: 1},
  {id: 29, pregunta: "Un seguro de vida-ahorro:", opciones: ["Solo cubre fallecimiento", "Combina ahorro e inversión con cobertura", "No tiene valor de rescate", "Es un producto bancario"], correcta: 1},
  {id: 30, pregunta: "El tomador de un seguro es:", opciones: ["Quien recibe la indemnización", "Quien contrata y paga las primas", "El asegurado siempre", "La compañía de seguros"], correcta: 1},
  {id: 31, pregunta: "Un plan de pensiones individual:", opciones: ["Permite rescate libre", "Tiene contingencias tasadas para el cobro", "No tiene ventajas fiscales", "Es un producto de renta fija"], correcta: 1},
  {id: 32, pregunta: "Las aportaciones a planes de pensiones:", opciones: ["No desgravan", "Reducen la base imponible del IRPF", "Están exentas totalmente", "Tributan como ganancia patrimonial"], correcta: 1},
  {id: 33, pregunta: "Una hipoteca a tipo variable:", opciones: ["Tiene cuota fija toda la vida", "Se revisa periódicamente según un índice de referencia", "No tiene intereses", "Solo la ofrecen bancos públicos"], correcta: 1},
  {id: 34, pregunta: "La TAE de un préstamo incluye:", opciones: ["Solo el tipo nominal", "Tipo nominal más comisiones y gastos", "Solo comisiones", "El IVA"], correcta: 1},
  {id: 35, pregunta: "En una amortización francesa:", opciones: ["Las cuotas son crecientes", "Las cuotas son constantes", "Solo se pagan intereses", "No hay intereses"], correcta: 1},
  {id: 36, pregunta: "Los rendimientos de un depósito tributan como:", opciones: ["Rendimiento del trabajo", "Rendimiento del capital mobiliario", "Ganancia patrimonial", "No tributan"], correcta: 1},
  {id: 37, pregunta: "La venta de acciones con beneficio tributa como:", opciones: ["Rendimiento del trabajo", "Rendimiento del capital mobiliario", "Ganancia patrimonial", "Renta exenta"], correcta: 2},
  {id: 38, pregunta: "El diferimiento fiscal de los fondos permite:", opciones: ["No pagar nunca impuestos", "Aplazar la tributación hasta el reembolso", "Deducir pérdidas ilimitadamente", "Tributar al 0%"], correcta: 1},
  {id: 39, pregunta: "MiFID II obliga a:", opciones: ["Eliminar todas las comisiones", "Evaluar idoneidad y conveniencia del cliente", "Garantizar rentabilidades", "Prohibir la renta variable"], correcta: 1},
  {id: 40, pregunta: "El test de conveniencia evalúa:", opciones: ["La situación financiera completa", "Conocimientos y experiencia del cliente", "Solo los objetivos de inversión", "La edad del cliente"], correcta: 1},
  {id: 41, pregunta: "Un producto complejo según MiFID II incluye:", opciones: ["Depósitos a plazo", "Letras del Tesoro", "Derivados y estructurados", "Acciones del IBEX"], correcta: 2},
  {id: 42, pregunta: "El blanqueo de capitales se previene con:", opciones: ["Ignorar operaciones sospechosas", "Identificación del cliente y comunicación de operaciones", "Aceptar efectivo ilimitado", "No preguntar origen de fondos"], correcta: 1},
  {id: 43, pregunta: "La CNMV supervisa:", opciones: ["Solo bancos", "Mercados de valores y ESIs", "Solo seguros", "El Banco de España"], correcta: 1},
  {id: 44, pregunta: "Un conflicto de intereses debe:", opciones: ["Ocultarse al cliente", "Identificarse, gestionarse y comunicarse", "Ignorarse si es pequeño", "Aprovecharse para la entidad"], correcta: 1},
  {id: 45, pregunta: "Las SOCIMIs invierten principalmente en:", opciones: ["Acciones tecnológicas", "Inmuebles para alquiler", "Materias primas", "Criptomonedas"], correcta: 1},
  {id: 46, pregunta: "El IBI es un impuesto:", opciones: ["Estatal sobre la renta", "Municipal sobre bienes inmuebles", "Autonómico sobre vehículos", "No existe"], correcta: 1},
  {id: 47, pregunta: "La plusvalía municipal grava:", opciones: ["La renta del alquiler", "El incremento de valor del suelo al transmitir", "Los intereses hipotecarios", "El IVA de la compra"], correcta: 1},
  {id: 48, pregunta: "Un unit linked es:", opciones: ["Un fondo de inversión", "Un seguro de vida donde el tomador asume el riesgo de inversión", "Un plan de pensiones", "Una cuenta corriente"], correcta: 1},
  {id: 49, pregunta: "El Euribor es:", opciones: ["Un índice bursátil", "Un tipo de referencia interbancario europeo", "Una acción del IBEX", "Un fondo de inversión"], correcta: 1},
  {id: 50, pregunta: "La educación financiera busca:", opciones: ["Vender más productos", "Mejorar la capacidad de decisión financiera del ciudadano", "Eliminar la regulación", "Aumentar el riesgo"], correcta: 1}
]

export default function SimulacroPage() {
  const [started, setStarted] = useState(false)
  const [finished, setFinished] = useState(false)
  const [currentQ, setCurrentQ] = useState(0)
  const [respuestas, setRespuestas] = useState({})
  const [timeLeft, setTimeLeft] = useState(90 * 60)

  useEffect(() => {
    if (started && !finished && timeLeft > 0) {
      const timer = setTimeout(() => setTimeLeft(timeLeft - 1), 1000)
      return () => clearTimeout(timer)
    }
    if (timeLeft === 0) setFinished(true)
  }, [started, finished, timeLeft])

  const formatTime = (s) => `${Math.floor(s/60)}:${(s%60).toString().padStart(2,'0')}`

  const handleRespuesta = (idx) => {
    setRespuestas({...respuestas, [currentQ]: idx})
  }

  const calcularNota = () => {
    let correctas = 0, incorrectas = 0
    preguntas.forEach((p, i) => {
      if (respuestas[i] === p.correcta) correctas++
      else if (respuestas[i] !== undefined) incorrectas++
    })
    return Math.max(0, correctas - incorrectas * 0.25)
  }

  if (!started) {
    return (
      <main className="min-h-screen">
        <header className="bg-gradient-to-r from-blue-900 to-blue-700 py-8 px-4">
          <div className="max-w-6xl mx-auto">
            <Link href="/" className="text-blue-300 hover:text-white mb-4 inline-block">← Volver</Link>
            <h1 className="text-3xl font-bold text-white">🎯 Simulacro Oficial EIP</h1>
          </div>
        </header>
        <section className="max-w-2xl mx-auto px-4 py-12">
          <div className="card text-center">
            <div className="text-6xl mb-6">🎯</div>
            <h2 className="text-2xl font-bold text-white mb-4">Simulacro de Examen</h2>
            <div className="grid grid-cols-3 gap-4 mb-8">
              <div className="bg-slate-700/50 rounded-lg p-4">
                <div className="text-2xl font-bold text-blue-400">50</div>
                <div className="text-slate-300 text-sm">Preguntas</div>
              </div>
              <div className="bg-slate-700/50 rounded-lg p-4">
                <div className="text-2xl font-bold text-blue-400">90</div>
                <div className="text-slate-300 text-sm">Minutos</div>
              </div>
              <div className="bg-slate-700/50 rounded-lg p-4">
                <div className="text-2xl font-bold text-blue-400">70%</div>
                <div className="text-slate-300 text-sm">Para aprobar</div>
              </div>
            </div>
            <div className="bg-slate-700/30 rounded-lg p-4 mb-6 text-left text-sm">
              <p className="text-white font-semibold mb-2">⚠️ Instrucciones:</p>
              <ul className="text-slate-300 space-y-1">
                <li>• Correctas: +1 punto | Incorrectas: -0,25 | En blanco: 0</li>
                <li>• Puedes navegar entre preguntas</li>
                <li>• El examen termina al acabar el tiempo o al enviarlo</li>
              </ul>
            </div>
            <button onClick={() => setStarted(true)} className="btn-primary text-lg px-8 py-4">
              Comenzar Simulacro
            </button>
          </div>
        </section>
      </main>
    )
  }

  if (finished) {
    const nota = calcularNota()
    const aprobado = nota >= 35
    return (
      <main className="min-h-screen">
        <header className="bg-gradient-to-r from-blue-900 to-blue-700 py-8 px-4">
          <div className="max-w-6xl mx-auto">
            <h1 className="text-3xl font-bold text-white">📊 Resultado del Simulacro</h1>
          </div>
        </header>
        <section className="max-w-2xl mx-auto px-4 py-12">
          <div className="card text-center">
            <div className={`text-6xl mb-4 ${aprobado ? 'text-green-400' : 'text-red-400'}`}>
              {aprobado ? '✅' : '❌'}
            </div>
            <div className="text-4xl font-bold text-white mb-2">{nota.toFixed(2)} / 50</div>
            <div className={`text-xl ${aprobado ? 'text-green-400' : 'text-red-400'}`}>
              {aprobado ? '¡APROBADO!' : 'NO APROBADO'}
            </div>
            <div className="text-slate-400 mt-2">Necesitas 35 puntos (70%) para aprobar</div>
            <Link href="/" className="btn-primary inline-block mt-8">Volver al Inicio</Link>
          </div>
        </section>
      </main>
    )
  }

  const p = preguntas[currentQ]

  return (
    <main className="min-h-screen">
      <header className="bg-gradient-to-r from-blue-900 to-blue-700 py-4 px-4 sticky top-0 z-10">
        <div className="max-w-4xl mx-auto flex justify-between items-center">
          <div className="text-white font-bold">Pregunta {currentQ + 1} / 50</div>
          <div className={`font-mono text-xl ${timeLeft < 300 ? 'text-red-400' : 'text-white'}`}>
            ⏱️ {formatTime(timeLeft)}
          </div>
        </div>
      </header>

      <section className="max-w-4xl mx-auto px-4 py-6">
        <div className="card mb-6">
          <p className="text-white text-lg mb-6">{p.pregunta}</p>
          <div className="space-y-3">
            {p.opciones.map((op, i) => (
              <button
                key={i}
                onClick={() => handleRespuesta(i)}
                className={`w-full text-left p-4 rounded-lg border transition-all ${
                  respuestas[currentQ] === i 
                    ? 'bg-blue-900/50 border-blue-500' 
                    : 'bg-slate-700/50 border-slate-600 hover:border-slate-500'
                }`}
              >
                <span className="text-blue-400 font-bold mr-2">{String.fromCharCode(65+i)})</span>
                <span className="text-white">{op}</span>
              </button>
            ))}
          </div>
        </div>

        <div className="flex justify-between items-center">
          <button
            onClick={() => setCurrentQ(Math.max(0, currentQ - 1))}
            disabled={currentQ === 0}
            className="px-6 py-3 rounded-lg bg-slate-700 text-white disabled:opacity-50"
          >
            ← Anterior
          </button>
          
          {currentQ < 49 ? (
            <button
              onClick={() => setCurrentQ(currentQ + 1)}
              className="px-6 py-3 rounded-lg bg-blue-600 text-white"
            >
              Siguiente →
            </button>
          ) : (
            <button
              onClick={() => setFinished(true)}
              className="px-6 py-3 rounded-lg bg-green-600 text-white"
            >
              Finalizar Examen
            </button>
          )}
        </div>

        <div className="mt-8 flex flex-wrap gap-2 justify-center">
          {preguntas.map((_, i) => (
            <button
              key={i}
              onClick={() => setCurrentQ(i)}
              className={`w-8 h-8 rounded text-sm font-bold ${
                i === currentQ ? 'bg-blue-600 text-white' :
                respuestas[i] !== undefined ? 'bg-green-700 text-white' : 'bg-slate-700 text-slate-400'
              }`}
            >
              {i + 1}
            </button>
          ))}
        </div>
      </section>
    </main>
  )
}
