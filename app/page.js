import Link from 'next/link'

export default function Home() {
  const stats = [
    { number: '10', label: 'Módulos Completos', sublabel: 'N.I (EIP) + N.II (EFA)' },
    { number: '1.888', label: 'Preguntas de Práctica', sublabel: 'Con explicaciones' },
    { number: '15', label: 'Simulacros de Examen', sublabel: 'Hasta 100 preguntas / 90 min' },
    { number: '4', label: 'Exámenes de Carteras', sublabel: 'Gestión de Carteras' },
  ]

  const sections = [
    {
      title: 'Manuales de Estudio',
      description: 'Contenido ampliado de 15-30 páginas por módulo. Incluye teoría completa, ejemplos prácticos, casos de estudio y preguntas de autoevaluación.',
      icon: '📚',
      href: '/manuales',
      features: ['10 módulos completos', 'Nivel I y Nivel II integrados', 'Formato Markdown navegable'],
    },
    {
      title: 'Tests de Práctica',
      description: '1.888 preguntas organizadas por módulo con indicador de nivel (N.I o N.II) y explicaciones detalladas.',
      icon: '📝',
      href: '/tests',
      features: ['1.888 preguntas con explicaciones', '10 módulos temáticos', 'Corrección instantánea'],
    },
    {
      title: 'Simulacros de Examen',
      description: '15 simulacros completos incluyendo exámenes reales (Junio 2022, Marzo 2020) con cronómetro y penalización de 0.25 por error.',
      icon: '🎯',
      href: '/tests',
      features: ['15 simulacros (A-H + oficiales)', 'Cronómetro de 90 min', 'Nota con penalización'],
    },
    {
      title: 'Exámenes de Carteras',
      description: '4 exámenes específicos de Gestión de Carteras con preguntas de cálculo avanzado: Sharpe, VaR, CAPM, tracking error.',
      icon: '📊',
      href: '/tests',
      features: ['4 exámenes especializados', 'Cálculos avanzados', 'Metodología EFPA'],
    },
  ]

  return (
    <main className="min-h-screen">
      {/* Header */}
      <header className="bg-gradient-to-r from-blue-900 to-blue-700 py-8 px-4">
        <div className="max-w-6xl mx-auto">
          <div className="flex items-center gap-3 mb-2">
            <span className="text-4xl">📚</span>
            <h1 className="text-4xl font-bold text-white">EFA Academy</h1>
          </div>
          <p className="text-blue-200 text-lg">Preparación completa para tu certificación EFPA</p>
        </div>
      </header>

      {/* Stats */}
      <section className="max-w-6xl mx-auto px-4 -mt-6">
        <div className="grid grid-cols-2 md:grid-cols-4 gap-4">
          {stats.map((stat, i) => (
            <div key={i} className="bg-slate-800 rounded-xl p-4 border border-slate-700">
              <div className="text-3xl font-bold text-blue-400">{stat.number}</div>
              <div className="text-white font-medium">{stat.label}</div>
              <div className="text-slate-400 text-sm">{stat.sublabel}</div>
            </div>
          ))}
        </div>
      </section>

      {/* Main Sections */}
      <section className="max-w-6xl mx-auto px-4 py-12">
        <div className="grid md:grid-cols-2 gap-6">
          {sections.map((section, i) => (
            <Link key={i} href={section.href} className="card group cursor-pointer">
              <div className="flex items-start gap-4">
                <span className="text-4xl">{section.icon}</span>
                <div className="flex-1">
                  <h2 className="text-xl font-bold text-white group-hover:text-blue-400 transition-colors">
                    {section.title}
                  </h2>
                  <p className="text-slate-400 mt-2 text-sm">{section.description}</p>
                  <ul className="mt-4 space-y-1">
                    {section.features.map((feature, j) => (
                      <li key={j} className="text-slate-300 text-sm flex items-center gap-2">
                        <span className="text-green-400">✓</span> {feature}
                      </li>
                    ))}
                  </ul>
                </div>
              </div>
            </Link>
          ))}
        </div>
      </section>

      {/* Footer */}
      <footer className="border-t border-slate-700 py-6 px-4">
        <div className="max-w-6xl mx-auto text-center text-slate-400">
          <p>📚 EFA Academy | Preparación completa para certificaciones EFPA España</p>
        </div>
      </footer>
    </main>
  )
}
