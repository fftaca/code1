## 🚀 Comandos principales para subir y actualizar cambios entre GitHub y tu PC

git status                       # Verifica archivos modificados y el estado del repositorio  
git add .                        # Agrega todos los cambios al área de preparación (stage)  
git commit -m "Comentario"       # Crea un commit con los cambios preparados  
git push                         # Sube los commits al repositorio remoto (GitHub)  
git pull                         # Descarga y aplica los cambios del remoto a tu carpeta local  

---

## 🔧 Configuración y conexión

git init                         # Inicializa un repositorio Git local  
git clone <url>                  # Clona un repositorio remoto a tu PC  
git remote add origin <url>      # Conecta el repo local con el remoto en GitHub  
git remote -v                    # Muestra la URL del repositorio remoto conectado  
git credential-manager clear     # Cierra sesión borrando las credenciales guardadas  

---

## 📥 Descargar (actualizar desde remoto)

git pull                         # Descarga y fusiona cambios del remoto  
git fetch                        # Descarga cambios sin fusionarlos automáticamente  

---

## 📤 Subir archivos (pasos típicos)

git add .                        # Agrega todos los archivos modificados  
git commit -m "Comentario"       # Confirma los cambios preparados  
git push                         # Sube los commits al repositorio remoto  
git push origin main             # Sube los cambios específicamente a la rama `main`  

---

## 🔄 Estado y sincronización

git status                       # Muestra el estado actual del repositorio  
git log                          # Muestra historial completo de commits  
git log --oneline                # Muestra historial resumido  

---

## 🗑️ Borrar, deshacer y restaurar

git rm <archivo>                # Elimina un archivo del repo y del disco  
git restore <archivo>           # Revierte los cambios no guardados del archivo  
git reset --hard HEAD           # Revierte todo al último commit confirmado  

---
