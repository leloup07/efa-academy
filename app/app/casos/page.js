import Link from 'next/link'

const casos = [
  {
    id: 1,
    titulo: 'Caso Práctico 1: Planificación Financiera Personal',
    descripcion: 'Cliente de 45 años con patrimonio diversificado. Análisis de situación, objetivos y propuesta de inversión.',
    temas: ['Análisis patrimonial', 'Perfil de riesgo', 'Asset allocation', 'Fiscalidad'],
  },
  {
    id: 2,
    titulo: 'Caso Práctico 2: Asesoramiento a Empresa Familiar',
    descripcion: 'Empresa familiar con necesidades de sucesión y planificación fiscal.',
    temas: ['Empresa familiar', 'Sucesión', 'Planificación fiscal', 'Inversiones'],
  },
]

export default function CasosPage() {
  return (
    <main className="min-h-screen">
      <header className="bg-gradient-to-r from-blue-900 to-blue-700 py-8 px-4">
        <div className="max-w-6xl mx-auto">
          <Link href="/" className="text-blue-300 hover:text-white mb-4 inline-block">
            ← Volver al inicio
          </Link>
          <h1 className="text-3xl font-bold text-white flex items-center gap-3">
            <span>📊</span> Casos Prácticos
          </h1>
          <p className="text-blue-200 mt-2">Ejercicios oficiales EFPA con soluciones detalladas</p>
        </div>
      </header>

      <section className="max-w-4xl mx-auto px-4 py-8">
        <div className="space-y-6">
          {casos.map((caso) => (
            <div key={caso.id} className="card">
              <h2 className="text-xl font-bold text-white mb-2">{caso.titulo}</h2>
              <p className="text-slate-400 mb-4">{caso.descripcion}</p>
              
              <div className="flex flex-wrap gap-2 mb-4">
                {caso.temas.map((tema, i) => (
                  <span key={i} className="bg-blue-900/50 text-blue-300 px-3 py-1 rounded-full text-sm">
                    {tema}
                  </span>
                ))}
              </div>
              
              <Link 
                href={`/casos/${caso.id}`}
                className="btn-primary inline-block"
              >
                Ver Caso Práctico
              </Link>
            </div>
          ))}
        </div>
      </section>
    </main>
  )
}
