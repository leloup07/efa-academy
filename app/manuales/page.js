import Link from 'next/link'
import { getAllManuales } from '@/lib/manuales'

export default function ManualesPage() {
  const { eip, efa } = getAllManuales()

  return (
    <main className="min-h-screen">
      <header className="bg-gradient-to-r from-blue-900 to-blue-700 py-8 px-4">
        <div className="max-w-6xl mx-auto">
          <Link href="/" className="text-blue-300 hover:text-white mb-4 inline-block">
            ← Volver al inicio
          </Link>
          <h1 className="text-3xl font-bold text-white flex items-center gap-3">
            <span>📚</span> Manuales de Estudio
          </h1>
          <p className="text-blue-200 mt-2">Contenido completo alineado con EFPA España</p>
        </div>
      </header>

      <section className="max-w-6xl mx-auto px-4 py-8">
        {/* EIP Nivel I */}
        <div className="mb-12">
          <h2 className="text-2xl font-bold text-blue-400 mb-6 flex items-center gap-2">
            <span>📗</span> EIP - Nivel I (9 módulos)
          </h2>
          <p className="text-slate-400 mb-6">European Investment Practitioner - Módulos fundamentales</p>
          
          {eip.length > 0 ? (
            <div className="grid md:grid-cols-3 gap-4">
              {eip.map((manual) => (
                <Link 
                  key={manual.slug}
                  href={`/manuales/${manual.slug}`}
                  className="card hover:scale-105"
                >
                  <div className="text-blue-400 font-bold text-lg mb-2">
                    Módulo {manual.numero}
                  </div>
                  <div className="text-white">{manual.nombre}</div>
                </Link>
              ))}
            </div>
          ) : (
            <p className="text-slate-400">No hay módulos EIP disponibles</p>
          )}
        </div>

        {/* EFA Nivel II */}
        <div>
          <h2 className="text-2xl font-bold text-blue-400 mb-6 flex items-center gap-2">
            <span>📘</span> EFA - Nivel II (8 módulos)
          </h2>
          <p className="text-slate-400 mb-6">European Financial Advisor - Módulos avanzados</p>
          
          {efa.length > 0 ? (
            <div className="grid md:grid-cols-3 gap-4">
              {efa.map((manual) => (
                <Link 
                  key={manual.slug}
                  href={`/manuales/${manual.slug}`}
                  className="card hover:scale-105"
                >
                  <div className="text-blue-400 font-bold text-lg mb-2">
                    Módulo {manual.numero}
                  </div>
                  <div className="text-white">{manual.nombre}</div>
                </Link>
              ))}
            </div>
          ) : (
            <p className="text-slate-400">No hay módulos EFA disponibles</p>
          )}
        </div>
      </section>
    </main>
  )
}
