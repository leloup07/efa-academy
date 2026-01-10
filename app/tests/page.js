'use client'
import Link from 'next/link'

const modulosEIP = [
  { num: 1, nombre: 'Instrumentos y Mercados', preguntas: 100 },
  { num: 2, nombre: 'Fondos y Sociedades de Inversión', preguntas: 75 },
  { num: 3, nombre: 'Gestión de Carteras', preguntas: 100 },
  { num: 4, nombre: 'Seguros', preguntas: 75 },
  { num: 5, nombre: 'Pensiones', preguntas: 60 },
  { num: 6, nombre: 'Inversión Inmobiliaria', preguntas: 60 },
  { num: 7, nombre: 'Crédito y Financiación', preguntas: 60 },
  { num: 8, nombre: 'Fiscalidad', preguntas: 100 },
  { num: 9, nombre: 'Cumplimiento Normativo', preguntas: 75 },
  { num: 10, nombre: 'Asesoramiento Financiero', preguntas: 75 },
]

export default function TestsPage() {
  const totalPreguntas = modulosEIP.reduce((sum, m) => sum + m.preguntas, 0)
  
  return (
    <main className="min-h-screen">
      <header className="bg-gradient-to-r from-blue-900 to-blue-700 py-8 px-4">
        <div className="max-w-6xl mx-auto">
          <Link href="/" className="text-blue-300 hover:text-white mb-4 inline-block">
            ← Volver al inicio
          </Link>
          <h1 className="text-3xl font-bold text-white flex items-center gap-3">
            <span>📝</span> Tests de Práctica
          </h1>
          <p className="text-blue-200 mt-2">
            {totalPreguntas} preguntas con explicaciones detalladas
          </p>
        </div>
      </header>

      <section className="max-w-6xl mx-auto px-4 py-8">
        <h2 className="text-xl font-bold text-white mb-6">📗 EIP/EFA - Todos los Módulos</h2>
        <div className="grid md:grid-cols-3 lg:grid-cols-4 gap-4">
          {modulosEIP.map((modulo) => (
            <Link
              key={modulo.num}
              href={`/tests/eip/${modulo.num}`}
              className="card hover:scale-105 transition-transform"
            >
              <div className="text-blue-400 font-bold text-lg mb-2">
                Módulo {modulo.num}
              </div>
              <div className="text-white mb-2">{modulo.nombre}</div>
              <div className="text-green-400 text-sm font-semibold">{modulo.preguntas} preguntas</div>
            </Link>
          ))}
        </div>
        
        <div className="mt-8 p-4 bg-slate-800/50 rounded-xl border border-slate-700">
          <h3 className="text-white font-bold mb-2">📊 Resumen del banco de preguntas</h3>
          <p className="text-slate-300">
            Total: <span className="text-green-400 font-bold">{totalPreguntas}</span> preguntas distribuidas en 10 módulos, 
            cubriendo todo el temario EFA.
          </p>
        </div>
      </section>
    </main>
  )
}
