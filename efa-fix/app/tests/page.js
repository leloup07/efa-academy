'use client'
import Link from 'next/link'
import { useState } from 'react'

const modulosEIP = [
  { num: 1, nombre: 'Instrumentos y Mercados', preguntas: 10 },
  { num: 2, nombre: 'Fondos y Sociedades de Inversión', preguntas: 10 },
  { num: 3, nombre: 'Gestión de Carteras', preguntas: 10 },
  { num: 4, nombre: 'Seguros', preguntas: 10 },
  { num: 5, nombre: 'Pensiones', preguntas: 10 },
  { num: 6, nombre: 'Inversión Inmobiliaria', preguntas: 10 },
  { num: 7, nombre: 'Crédito y Financiación', preguntas: 10 },
  { num: 8, nombre: 'Fiscalidad', preguntas: 10 },
  { num: 9, nombre: 'Cumplimiento Normativo', preguntas: 10 },
]

export default function TestsPage() {
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
        <h2 className="text-xl font-bold text-white mb-6">📗 EIP - Nivel I</h2>
        <div className="grid md:grid-cols-3 gap-4">
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
              <div className="text-slate-400 text-sm">{modulo.preguntas} preguntas</div>
            </Link>
          ))}
        </div>
      </section>
    </main>
  )
}
