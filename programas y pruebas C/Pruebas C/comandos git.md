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