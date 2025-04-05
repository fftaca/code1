### /*Comandos principales para subir y actualizar cambios a local*/ ###

git status        # Muestra los archivos modificados y el estado actual del repo

git add .         # Agrega todos los archivos modificados al área de preparación (stage)

git commit -m "Descripción de los cambios"  # Crea un commit con los cambios preparados

git push          # Sube los commits locales al repositorio remoto (GitHub)

git pull          # Trae y aplica los últimos cambios del repositorio remoto a tu carpeta local
-------------------------------------------------------------------------------------------------------------------

## Comandos Git Básicos

### 🔗 Configuración y conexión
- `git init` — Inicializa un repositorio Git local.
- `git clone <url>` — Clona un repositorio remoto a tu PC.
- `git remote add origin <url>` — Asocia el repositorio local con el remoto.

### 📥 Descargar (actualizar desde remoto)
- `git pull` — Descarga y fusiona los cambios del repositorio remoto.

### 📤 Subir archivos
1. `git add .` — Agrega todos los archivos al área de preparación (stage).
2. `git commit -m "Comentario"` — Crea un commit con los cambios.
3. `git push` — Sube los cambios al repositorio remoto.

### 🔄 Estado y sincronización
- `git status` — Muestra el estado actual del repositorio.
- `git log` — Muestra el historial de commits.
- `git fetch` — Descarga cambios del remoto sin fusionar.

### 🗑️ Borrar o deshacer
- `git rm <archivo>` — Elimina un archivo del repositorio y del disco.
- `git restore <archivo>` — Revierte cambios no confirmados.
- `git reset --hard HEAD` — Vuelve al último commit, descarta todo lo no guardado.



- 'git credential-manager clear' - Borrar Credenciales - Cerrar sesión

---