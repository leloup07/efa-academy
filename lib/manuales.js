import fs from 'fs'
import path from 'path'
import matter from 'gray-matter'

const manualesDir = path.join(process.cwd(), 'data/manuales')

export function getAllManuales() {
  if (!fs.existsSync(manualesDir)) {
    return { eip: [], efa: [] }
  }
  
  const files = fs.readdirSync(manualesDir).filter(f => f.endsWith('.md'))
  
  const manuales = files.map(filename => {
    const slug = filename.replace('.md', '')
    const filePath = path.join(manualesDir, filename)
    const content = fs.readFileSync(filePath, 'utf-8')
    
    // Extraer número de módulo - buscar "Modulo_X_"
    const matchNumero = slug.match(/Modulo_(\d+)_/)
    const numero = matchNumero ? parseInt(matchNumero[1]) : 0
    
    // Extraer nombre - todo después de "Modulo_X_" hasta el sufijo
    const matchNombre = slug.match(/Modulo_\d+_(.+?)(?:_AMPLIADO|_COMPLETO|_Avanzado)?$/)
    const nombre = matchNombre ? matchNombre[1].replace(/_/g, ' ') : slug
    
    // Determinar nivel
    const nivel = slug.includes('EIP_Nivel_I') ? 'EIP' : slug.includes('EFA_Nivel_II') ? 'EFA' : 'Otro'
    
    return { slug, filename, numero, nombre, nivel }
  })
  
  const eip = manuales.filter(m => m.nivel === 'EIP').sort((a, b) => a.numero - b.numero)
  const efa = manuales.filter(m => m.nivel === 'EFA').sort((a, b) => a.numero - b.numero)
  
  return { eip, efa }
}

export function getManualBySlug(slug) {
  const filePath = path.join(manualesDir, `${slug}.md`)
  
  if (!fs.existsSync(filePath)) {
    return null
  }
  
  const content = fs.readFileSync(filePath, 'utf-8')
  
  const matchNumero = slug.match(/Modulo_(\d+)_/)
  const numero = matchNumero ? parseInt(matchNumero[1]) : 0
  
  const matchNombre = slug.match(/Modulo_\d+_(.+?)(?:_AMPLIADO|_COMPLETO|_Avanzado)?$/)
  const nombre = matchNombre ? matchNombre[1].replace(/_/g, ' ') : slug
  
  const nivel = slug.includes('EIP_Nivel_I') ? 'EIP Nivel I' : slug.includes('EFA_Nivel_II') ? 'EFA Nivel II' : 'Manual'
  
  return { slug, content, numero, nombre, nivel }
}
