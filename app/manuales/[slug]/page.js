import Link from 'next/link'
import { getManualBySlug, getAllManuales } from '@/lib/manuales'
import ReactMarkdown from 'react-markdown'
import remarkGfm from 'remark-gfm'
import { notFound } from 'next/navigation'

export async function generateStaticParams() {
  const { eip, efa } = getAllManuales()
  return [...eip, ...efa].map((manual) => ({
    slug: manual.slug,
  }))
}

export default function ManualPage({ params }) {
  const manual = getManualBySlug(params.slug)
  
  if (!manual) {
    notFound()
  }

  return (
    <main className="min-h-screen">
      <header className="bg-gradient-to-r from-blue-900 to-blue-700 py-6 px-4 sticky top-0 z-10">
        <div className="max-w-4xl mx-auto">
          <Link href="/manuales" className="text-blue-300 hover:text-white mb-2 inline-block text-sm">
            ← Volver a Manuales
          </Link>
          <h1 className="text-2xl font-bold text-white">
            {manual.nivel} - Módulo {manual.numero}: {manual.nombre}
          </h1>
        </div>
      </header>

      <article className="max-w-4xl mx-auto px-4 py-8">
        <div className="bg-slate-800/50 rounded-xl p-8 border border-slate-700">
          <div className="markdown-content prose prose-invert max-w-none">
            <ReactMarkdown remarkPlugins={[remarkGfm]}>{manual.content}</ReactMarkdown>
          </div>
        </div>
      </article>
    </main>
  )
}
