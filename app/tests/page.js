'use client'
import Link from 'next/link'
import { useState } from 'react'

const modulosEIP = [
  { num: 1, nombre: 'Instrumentos y Mercados', preguntas: 50 },
  { num: 2, nombre: 'Fondos y Sociedades de Inversión', preguntas: 50 },
  { num: 3, nombre: 'Gestión de Carteras', preguntas: 50 },
  { num: 4, nombre: 'Seguros', preguntas: 50 },
  { num: 5, nombre: 'Pensiones', preguntas: 50 },
  { num: 6, nombre: 'Inversión Inmobiliaria', preguntas: 50 },
  { num: 7, nombre: 'Crédito y Financiación', preguntas: 50 },
  { num: 8, nombre: 'Fiscalidad', preguntas: 50 },
  { num: 9, nombre: 'Cumplimiento Normativo', preguntas: 50 },
]

const modulosEFA = [
  { num: 1, nombre: 'Instrumentos y Mercados Avanzado', preguntas: 40 },
  { num: 2, nombre: 'Gestión de Carteras Avanzada', preguntas: 40 },
  { num: 3, nombre: 'Asesoramiento y Planificación', preguntas: 40 },
  { num: 4, nombre: 'Fiscalidad Avanzada', preguntas: 40 },
  { num: 5, nombre: 'Seguros Avanzado', preguntas: 40 },
  { num: 6, nombre: 'Jubilación y Planificación', preguntas: 40 },
  { num: 7, nombre: 'Inversión Inmobiliaria Avanzada', preguntas: 40 },
  { num: 8, nombre: 'Legislación y Ética', preguntas: 40 },
]

export default function TestsPage() {
  const [nivel, setNivel] = useState('eip')
  const modulos = nivel === 'eip' ? modulosEIP : modulosEFA

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
          <p className="text-blue-200 mt-2">Practica por módulos con explicaciones detalladas</p>
        </div>
      </header>

      <section className="max-w-6xl mx-auto px-4 py-8">
        {/* Selector de nivel */}
        <div className="flex gap-4 mb-8">
          <button
            onClick={() => setNivel('eip')}
            className={`px-6 py-3 rounded-lg font-semibold transition-all ${
              nivel === 'eip' 
                ? 'bg-blue-600 text-white' 
                : 'bg-slate-700 text-slate-300 hover:bg-slate-600'
            }`}
          >
            📗 EIP - Nivel I
          </button>
          <button
            onClick={() => setNivel('efa')}
            className={`px-6 py-3 rounded-lg font-semibold transition-all ${
              nivel === 'efa' 
                ? 'bg-blue-600 text-white' 
                : 'bg-slate-700 text-slate-300 hover:bg-slate-600'
            }`}
          >
            📘 EFA - Nivel II
          </button>
        </div>

        {/* Grid de módulos */}
        <div className="grid md:grid-cols-3 gap-4">
          {modulos.map((modulo) => (
            <Link
              key={modulo.num}
              href={`/tests/${nivel}/${modulo.num}`}
              className="card hover:scale-105"
            >
              <div className="text-blue-400 font-bold text-lg mb-2">
                Módulo {modulo.num}
              </div>
              <div className="text-white mb-2">{modulo.nombre}</div>
              <div className="text-slate-400 text-sm">{modulo.preguntas} preguntas</div>
            </Link>
          ))}
        </div>
      </section>
    </main>
  )
}
