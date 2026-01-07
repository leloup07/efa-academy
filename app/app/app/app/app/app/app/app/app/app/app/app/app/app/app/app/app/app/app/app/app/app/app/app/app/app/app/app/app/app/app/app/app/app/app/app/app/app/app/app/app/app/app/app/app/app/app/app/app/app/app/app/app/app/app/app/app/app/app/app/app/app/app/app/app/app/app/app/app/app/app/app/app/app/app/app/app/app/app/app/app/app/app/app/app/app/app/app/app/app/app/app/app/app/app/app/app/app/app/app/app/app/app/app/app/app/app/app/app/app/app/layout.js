import './globals.css'

export const metadata = {
  title: 'EFA Academy - Preparación EFPA',
  description: 'Plataforma de preparación para certificaciones EFPA España',
}

export default function RootLayout({ children }) {
  return (
    <html lang="es">
      <body className="antialiased">
        {children}
      </body>
    </html>
  )
}
