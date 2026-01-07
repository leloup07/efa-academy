import fs from 'fs'
import path from 'path'

const testsDir = path.join(process.cwd(), 'data/tests')

export function getAllTests() {
  if (!fs.existsSync(testsDir)) {
    return []
  }
  
  const files = fs.readdirSync(testsDir).filter(f => f.endsWith('.json'))
  
  return files.map(filename => {
    const filePath = path.join(testsDir, filename)
    const content = JSON.parse(fs.readFileSync(filePath, 'utf-8'))
    return content
  })
}

export function getTestByModulo(nivel, modulo) {
  const filename = `${nivel}_modulo_${modulo}.json`
  const filePath = path.join(testsDir, filename)
  
  if (!fs.existsSync(filePath)) {
    return null
  }
  
  return JSON.parse(fs.readFileSync(filePath, 'utf-8'))
}

// Preguntas de ejemplo hardcodeadas para cuando no hay JSON
export const preguntasEjemplo = {
  eip: [
    {
      modulo: 1,
      titulo: "Instrumentos y Mercados",
      preguntas: [
        {
          id: 1,
          pregunta: "¿Qué describe mejor la diferencia entre mercado primario y secundario?",
          opciones: [
            "En primario se negocian activos ya emitidos y en secundario se emiten nuevos",
            "En primario se produce la emisión y captación inicial de fondos por el emisor; en secundario los inversores intercambian los activos",
            "En primario solo operan minoristas y en secundario solo institucionales",
            "No existe diferencia relevante entre ambos"
          ],
          correcta: 1,
          explicacion: "El mercado primario es donde el emisor capta fondos mediante la emisión inicial de valores. En el secundario, los inversores compran y venden entre sí valores ya emitidos."
        },
        {
          id: 2,
          pregunta: "Si los tipos de interés de mercado suben del 3% al 4%, el precio de un bono existente con cupón fijo del 3% y duración modificada de 5 años:",
          opciones: [
            "Subirá aproximadamente un 5%",
            "Bajará aproximadamente un 5%",
            "Permanecerá invariable",
            "Subirá exactamente un 1%"
          ],
          correcta: 1,
          explicacion: "Variación precio ≈ -Duración × Δtipos = -5 × 1% = -5%. Los bonos tienen relación inversa con los tipos."
        }
      ]
    }
  ]
}
