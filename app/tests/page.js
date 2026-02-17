'use client'
import Link from 'next/link'

const modulosEFA = [
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

const simulacrosOriginales = [
  { num: 1, titulo: 'Simulacro #1', preguntas: 50, tiempo: 90 },
  { num: 2, titulo: 'Simulacro #2', preguntas: 50, tiempo: 90 },
  { num: 3, titulo: 'Simulacro #3', preguntas: 50, tiempo: 90 },
  { num: 4, titulo: 'Simulacro #4', preguntas: 50, tiempo: 90 },
  { num: 5, titulo: 'Simulacro #5', preguntas: 50, tiempo: 90 },
  { num: 6, titulo: 'Simulacro #6', preguntas: 50, tiempo: 90 },
]

const simulacrosNuevos = [
  { id: 'A', titulo: 'Simulacro A (Jesús Pérez)', preguntas: 50, tiempo: 90, archivo: 'simulacro_A' },
  { id: 'B', titulo: 'Simulacro B (Jesús Pérez)', preguntas: 50, tiempo: 90, archivo: 'simulacro_B' },
  { id: 'C', titulo: 'Simulacro C', preguntas: 51, tiempo: 90, archivo: 'simulacro_C' },
  { id: 'D', titulo: 'Simulacro D', preguntas: 52, tiempo: 90, archivo: 'simulacro_D' },
  { id: 'E', titulo: 'Simulacro E', preguntas: 100, tiempo: 120, archivo: 'simulacro_E' },
  { id: 'G', titulo: 'Simulacro G', preguntas: 40, tiempo: 90, archivo: 'simulacro_G' },
  { id: 'H', titulo: 'Simulacro H (Jesús Pérez)', preguntas: 50, tiempo: 90, archivo: 'simulacro_H' },
  { id: 'J22', titulo: 'Examen Junio 2022', preguntas: 50, tiempo: 90, archivo: 'simulacro_junio2022' },
  { id: 'EFA', titulo: 'Simulacro EFA Completo', preguntas: 50, tiempo: 90, archivo: 'simulacro_efa_completo' },
]

const repasos = [
  { id: 'final', titulo: 'Repaso Final', preguntas: 87, tiempo: 120, archivo: 'repaso_final' },
  { id: 'intermedio', titulo: 'Repaso Intermedio', preguntas: 12, tiempo: 30, archivo: 'repaso_intermedio' },
]

const examenesCarteras = [
  { num: 1, titulo: 'Examen Carteras 1', preguntas: 28, tiempo: 60, archivo: 'examen_carteras_1' },
  { num: 2, titulo: 'Examen Carteras 2', preguntas: 45, tiempo: 60, archivo: 'examen_carteras_2' },
  { num: 3, titulo: 'Examen Carteras 3', preguntas: 28, tiempo: 60, archivo: 'examen_carteras_3' },
  { num: 4, titulo: 'Examen Carteras 4', preguntas: 45, tiempo: 60, archivo: 'examen_carteras_4' },
]

const casosPracticos = [
  { num: 1, titulo: 'Planificación de Jubilación', preguntas: 5 },
  { num: 2, titulo: 'Gestión de Cartera', preguntas: 5 },
  { num: 3, titulo: 'Fiscalidad de Operaciones', preguntas: 5 },
  { num: 4, titulo: 'Análisis de Hipoteca', preguntas: 5 },
  { num: 5, titulo: 'Seguros y Previsión', preguntas: 5 },
  { num: 6, titulo: 'Reestructuración de Cartera', preguntas: 5 },
]

export default function TestsPage() {
  const totalModulos = modulosEFA.reduce((s, m) => s + m.preguntas, 0)

  return (
    <main className="min-h-screen">
      <header className="bg-gradient-to-r from-blue-900 to-blue-700 py-8 px-4">
        <div className="max-w-6xl mx-auto">
          <Link href="/" className="text-blue-300 hover:text-white mb-4 inline-block">&larr; Volver al inicio</Link>
          <h1 className="text-3xl font-bold text-white flex items-center gap-3">📝 Tests de Práctica EFA</h1>
          <p className="text-blue-200 mt-2">1.888 preguntas + 15 simulacros + 4 exámenes de carteras + 6 casos prácticos</p>
          <p className="text-blue-300 text-sm mt-1">(N.I) = Nivel I EIP &bull; (N.II) = Nivel II EFA</p>
        </div>
      </header>

      <section className="max-w-6xl mx-auto px-4 py-8">
        {/* Tests por Módulo */}
        <h2 className="text-xl font-bold text-white mb-4">📚 Tests por Módulo</h2>
        <div className="grid md:grid-cols-3 lg:grid-cols-5 gap-3 mb-10">
          {modulosEFA.map((m) => (
            <Link key={m.num} href={`/tests/eip/${m.num}`} className="card hover:scale-105 transition-transform p-4">
              <div className="text-blue-400 font-bold">Módulo {m.num}</div>
              <div className="text-white text-sm mb-1">{m.nombre}</div>
              <div className="text-green-400 text-xs">{m.preguntas} preguntas</div>
            </Link>
          ))}
        </div>

        {/* Simulacros Originales */}
        <h2 className="text-xl font-bold text-white mb-4">🎯 Simulacros de Examen (Generados)</h2>
        <div className="grid md:grid-cols-3 lg:grid-cols-6 gap-3 mb-10">
          {simulacrosOriginales.map((s) => (
            <Link key={s.num} href={`/tests/simulacro/${s.num}`} className="card hover:scale-105 transition-transform p-4 border-yellow-600/30">
              <div className="text-yellow-400 font-bold">{s.titulo}</div>
              <div className="text-slate-300 text-sm">{s.preguntas} preguntas</div>
              <div className="text-slate-400 text-xs">{s.tiempo} min</div>
            </Link>
          ))}
        </div>

        {/* Simulacros Nuevos (de los PDFs) */}
        <h2 className="text-xl font-bold text-white mb-2">🏆 Simulacros Oficiales (Material de Clase)</h2>
        <p className="text-slate-400 text-sm mb-4">Simulacros reales de preparación EFA con soluciones detalladas</p>
        <div className="grid md:grid-cols-3 lg:grid-cols-4 gap-3 mb-10">
          {simulacrosNuevos.map((s) => (
            <Link key={s.id} href={`/tests/simulacro/${s.archivo}`} className="card hover:scale-105 transition-transform p-4 border-green-600/30">
              <div className="text-green-400 font-bold text-sm">{s.titulo}</div>
              <div className="text-slate-300 text-sm">{s.preguntas} preguntas</div>
              <div className="text-slate-400 text-xs">{s.tiempo} min</div>
            </Link>
          ))}
        </div>

        {/* Repasos */}
        <h2 className="text-xl font-bold text-white mb-4">📖 Repasos</h2>
        <div className="grid md:grid-cols-2 gap-3 mb-10">
          {repasos.map((r) => (
            <Link key={r.id} href={`/tests/simulacro/${r.archivo}`} className="card hover:scale-105 transition-transform p-4 border-cyan-600/30">
              <div className="text-cyan-400 font-bold">{r.titulo}</div>
              <div className="text-slate-300 text-sm">{r.preguntas} preguntas</div>
              <div className="text-slate-400 text-xs">{r.tiempo} min</div>
            </Link>
          ))}
        </div>

        {/* Exámenes de Carteras */}
        <h2 className="text-xl font-bold text-white mb-4">📈 Exámenes de Gestión de Carteras</h2>
        <div className="grid md:grid-cols-2 lg:grid-cols-4 gap-3 mb-10">
          {examenesCarteras.map((e) => (
            <Link key={e.num} href={`/tests/simulacro/${e.archivo}`} className="card hover:scale-105 transition-transform p-4 border-orange-600/30">
              <div className="text-orange-400 font-bold">{e.titulo}</div>
              <div className="text-slate-300 text-sm">{e.preguntas} preguntas</div>
              <div className="text-slate-400 text-xs">{e.tiempo} min</div>
            </Link>
          ))}
        </div>

        {/* Casos Prácticos */}
        <h2 className="text-xl font-bold text-white mb-4">📋 Casos Prácticos</h2>
        <div className="grid md:grid-cols-2 lg:grid-cols-3 gap-3">
          {casosPracticos.map((c) => (
            <Link key={c.num} href={`/tests/caso/${c.num}`} className="card hover:scale-105 transition-transform p-4 border-purple-600/30">
              <div className="text-purple-400 font-bold">Caso {c.num}</div>
              <div className="text-white text-sm mb-1">{c.titulo}</div>
              <div className="text-slate-400 text-xs">{c.preguntas} preguntas</div>
            </Link>
          ))}
        </div>
      </section>
    </main>
  )
}
