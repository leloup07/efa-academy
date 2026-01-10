import Link from 'next/link'

const manualesEIP = [
  { num: 1, nombre: 'Instrumentos y Mercados', slug: 'EIP_Nivel_I_Modulo_1_Instrumentos_y_Mercados_AMPLIADO' },
  { num: 2, nombre: 'Fondos y Sociedades de Inversión', slug: 'EIP_Nivel_I_Modulo_2_Fondos_y_Sociedades_de_Inversion_AMPLIADO' },
  { num: 3, nombre: 'Gestión de Carteras', slug: 'EIP_Nivel_I_Modulo_3_Gestion_de_Carteras_AMPLIADO' },
  { num: 4, nombre: 'Seguros', slug: 'EIP_Nivel_I_Modulo_4_Seguros_AMPLIADO' },
  { num: 5, nombre: 'Pensiones', slug: 'EIP_Nivel_I_Modulo_5_Pensiones_AMPLIADO' },
  { num: 6, nombre: 'Inversión Inmobiliaria', slug: 'EIP_Nivel_I_Modulo_6_Inversion_Inmobiliaria_AMPLIADO' },
  { num: 7, nombre: 'Crédito y Financiación', slug: 'EIP_Nivel_I_Modulo_7_Credito_Financiacion_AMPLIADO' },
  { num: 8, nombre: 'Fiscalidad', slug: 'EIP_Nivel_I_Modulo_8_Fiscalidad_AMPLIADO' },
  { num: 9, nombre: 'Cumplimiento Normativo', slug: 'EIP_Nivel_I_Modulo_9_Cumplimiento_Normativo_AMPLIADO' },
]

const manualesEFA = [
  { num: 1, nombre: 'Instrumentos y Mercados Avanzado', slug: 'EFA_Nivel_II_Modulo_1_Instrumentos_y_Mercados_Avanzado' },
  { num: 2, nombre: 'Gestión de Carteras Avanzado', slug: 'EFA_Nivel_II_Modulo_2_Gestion_de_Carteras_Avanzado' },
  { num: 3, nombre: 'Asesoramiento y Planificación Patrimonial', slug: 'EFA_Nivel_II_Modulo_3_Asesoramiento_y_Planificacion_Patrimonial' },
  { num: 4, nombre: 'Fiscalidad Avanzada', slug: 'EFA_Nivel_II_Modulo_4_Fiscalidad_Avanzada' },
  { num: 5, nombre: 'Seguros y Planificación del Riesgo', slug: 'EFA_Nivel_II_Modulo_5_Seguros_y_Planificacion_del_Riesgo' },
  { num: 6, nombre: 'Jubilación y Planificación Previsional', slug: 'EFA_Nivel_II_Modulo_6_Jubilacion_y_Planificacion_Previsional' },
  { num: 7, nombre: 'Inversión Inmobiliaria y Activos Reales', slug: 'EFA_Nivel_II_Modulo_7_Inversion_Inmobiliaria_y_Activos_Reales' },
  { num: 8, nombre: 'Legislación, Ética y Cumplimiento', slug: 'EFA_Nivel_II_Modulo_8_Legislacion_Etica_y_Cumplimiento' },
]

export default function ManualesPage() {
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
          
          <div className="grid md:grid-cols-3 gap-4">
            {manualesEIP.map((manual) => (
              <Link 
                key={manual.slug}
                href={`/manuales/${manual.slug}`}
                className="card hover:scale-105 transition-transform"
              >
                <div className="text-blue-400 font-bold text-lg mb-2">
                  Módulo {manual.num}
                </div>
                <div className="text-white">{manual.nombre}</div>
              </Link>
            ))}
          </div>
        </div>

        {/* EFA Nivel II */}
        <div>
          <h2 className="text-2xl font-bold text-blue-400 mb-6 flex items-center gap-2">
            <span>📘</span> EFA - Nivel II (8 módulos)
          </h2>
          <p className="text-slate-400 mb-6">European Financial Advisor - Módulos avanzados</p>
          
          <div className="grid md:grid-cols-3 gap-4">
            {manualesEFA.map((manual) => (
              <Link 
                key={manual.slug}
                href={`/manuales/${manual.slug}`}
                className="card hover:scale-105 transition-transform"
              >
                <div className="text-blue-400 font-bold text-lg mb-2">
                  Módulo {manual.num}
                </div>
                <div className="text-white">{manual.nombre}</div>
              </Link>
            ))}
          </div>
        </div>
      </section>
    </main>
  )
}
