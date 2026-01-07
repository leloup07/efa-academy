# Despliegue en Railway - EFA Academy

## Opción 1: Nuevo proyecto (recomendado)

```bash
# 1. Extrae el ZIP en una carpeta nueva
unzip EFA_Academy_NextJS_Completo.zip
cd efa-academy-next

# 2. Instala dependencias
npm install

# 3. Inicializa git y sube a GitHub
git init
git add .
git commit -m "EFA Academy v3.0"
git remote add origin https://github.com/TU_USUARIO/efa-academy.git
git push -u origin main

# 4. En Railway: New Project → Deploy from GitHub
```

## Opción 2: Reemplazar proyecto existente

```bash
# 1. Extrae el ZIP
unzip EFA_Academy_NextJS_Completo.zip

# 2. Ve a tu proyecto existente
cd ~/Projects/efa_academy

# 3. Borra todo excepto .git
find . -maxdepth 1 ! -name '.git' ! -name '.' -exec rm -rf {} +

# 4. Copia todo del nuevo proyecto
cp -r /ruta/a/efa-academy-next/* .
cp -r /ruta/a/efa-academy-next/.gitignore .

# 5. Instala y sube
npm install
git add .
git commit -m "EFA Academy v3.0 - Rediseño completo"
git push --force
```

## Añadir nuevos módulos

Para EIP Nivel I:
```
data/manuales/EIP_Nivel_I_Modulo_X_Nombre_AMPLIADO.md
```

Para EFA Nivel II:
```
data/manuales/EFA_Nivel_II_Modulo_X_Nombre_AMPLIADO.md
```

La app detecta automáticamente los archivos .md.
