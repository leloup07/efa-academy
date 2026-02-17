import Link from 'next/link'

const casos = [
  {
    id: 1,
    titulo: 'Caso Práctico 1: Planificación Financiera Personal',
    descripcion: 'Cliente de 45 años, casado, con 2 hijos. Patrimonio: 500.000€ (vivienda habitual 300.000€, fondos de inversión 150.000€, depósitos 50.000€). Ingresos netos familiares: 80.000€/año. Objetivo: jubilación a los 65 años manteniendo nivel de vida.',
    temas: ['Análisis patrimonial', 'Perfil de riesgo', 'Asset allocation', 'Fiscalidad', 'Planificación jubilación'],
    solucion: [
      '1. Análisis de situación: Ratio ahorro actual 15%, horizonte 20 años.',
      '2. Perfil inversor: Moderado (test de idoneidad 55/100 puntos).',
      '3. Propuesta asset allocation: 60% RV / 30% RF / 10% liquidez.',
      '4. Optimización fiscal: Maximizar aportaciones PP (1.500€/año), traspasos entre fondos.',
      '5. Objetivo jubilación: Necesidad 40.000€/año × 25 años = 1M€. Con rentabilidad 5% anual y ahorro sistemático, objetivo alcanzable.'
    ]
  },
  {
    id: 2,
    titulo: 'Caso Práctico 2: Asesoramiento a Empresa Familiar',
    descripcion: 'Empresa familiar, facturación 2M€, 15 empleados. Propietario 60 años, quiere planificar sucesión a sus 2 hijos (35 y 32 años). Patrimonio empresarial: 1.5M€. Patrimonio personal: 800.000€.',
    temas: ['Empresa familiar', 'Sucesión', 'Planificación fiscal', 'Protocolo familiar', 'Inversiones'],
    solucion: [
      '1. Protocolo familiar: Establecer reglas de gobierno, acceso y salida.',
      '2. Valoración empresa: Múltiplo EBITDA (6x) = 1.8M€ valor estimado.',
      '3. Planificación sucesión: Donación progresiva vs. herencia (análisis fiscal).',
      '4. Reducción 95% ISD empresa familiar: Requisitos y planificación.',
      '5. Diversificación patrimonio personal: Reducir concentración en la empresa.',
      '6. Seguro de vida key-man: Protección ante contingencias del fundador.'
    ]
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
        <div className="space-y-8">
          {casos.map((caso) => (
            <div key={caso.id} className="card">
              <h2 className="text-xl font-bold text-white mb-3">{caso.titulo}</h2>
              
              <div className="bg-slate-700/50 rounded-lg p-4 mb-4">
                <h3 className="text-blue-400 font-semibold mb-2">📋 Enunciado:</h3>
                <p className="text-slate-300">{caso.descripcion}</p>
              </div>
              
              <div className="flex flex-wrap gap-2 mb-4">
                {caso.temas.map((tema, i) => (
                  <span key={i} className="bg-blue-900/50 text-blue-300 px-3 py-1 rounded-full text-sm">
                    {tema}
                  </span>
                ))}
              </div>
              
              <details className="group">
                <summary className="btn-primary cursor-pointer inline-block">
                  Ver Solución Propuesta
                </summary>
                <div className="mt-4 bg-green-900/20 border border-green-800 rounded-lg p-4">
                  <h3 className="text-green-400 font-semibold mb-3">✅ Solución:</h3>
                  <ul className="space-y-2">
                    {caso.solucion.map((paso, i) => (
                      <li key={i} className="text-slate-300">{paso}</li>
                    ))}
                  </ul>
                </div>
              </details>
            </div>
          ))}
        </div>
        
        <div className="card mt-8 text-center">
          <div className="text-4xl mb-4">📚</div>
          <h3 className="text-xl font-bold text-white mb-2">Más casos próximamente</h3>
          <p className="text-slate-400">Se añadirán nuevos casos prácticos de exámenes anteriores.</p>
        </div>
      </section>
    </main>
  )
}
