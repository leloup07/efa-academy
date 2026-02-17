# EFA Academy

Plataforma de preparación para certificaciones EFPA España.

## Instalación

```bash
npm install
npm run dev
```

## Despliegue en Railway

```bash
npm install
git add .
git commit -m "Deploy EFA Academy"
git push
```

## Estructura

```
├── app/                    # Páginas Next.js (App Router)
│   ├── page.js            # Página principal
│   ├── manuales/          # Manuales de estudio
│   ├── tests/             # Tests de práctica
│   ├── simulacro/         # Simulacro oficial
│   └── casos/             # Casos prácticos
├── data/
│   ├── manuales/          # Archivos .md de manuales
│   └── tests/             # Archivos .json de preguntas
├── lib/                   # Utilidades
└── components/            # Componentes React
```

## Añadir nuevos módulos

1. Añadir archivo .md en `data/manuales/`
2. Seguir nomenclatura: `EIP_Nivel_I_Modulo_X_Nombre_AMPLIADO.md` o `EFA_Nivel_II_Modulo_X_Nombre_AMPLIADO.md`
3. Hacer commit y push

## Tecnologías

- Next.js 14
- React 18
- Tailwind CSS
- Markdown (react-markdown)
