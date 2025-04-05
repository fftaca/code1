#include <windows.h>  // Incluye las funciones necesarias para usar la API de Windows

int main() {
    // Muestra una ventana emergente (MessageBox)
    // Parámetros:
    // - NULL: sin ventana padre (ventana independiente)
    // - "Hola mundo": mensaje que se muestra
    // - "Mensaje": título de la ventana
    // - MB_OK: botón "OK" solamente
    MessageBox(NULL, "Hola mundo", "Ventana de prueba", MB_OK); //MB_OK solo genero un boton de OK y cierro la ventana = 1 y 0, si y no.

    // Devuelvo 0 al sistema operativo, indicando que todo terminó bien
    return 0;
}
/*
Constante
MB_OK	Solo un botón “OK”
MB_YESNO	Botones “Sí” y “No”
MB_OKCANCEL	Botones “OK” y “Cancelar”
MB_RETRYCANCEL	Botones “Reintentar” y “Cancelar”
MB_ICONERROR	Muestra un ícono de error (se puede combinar)
*/