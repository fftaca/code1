#include <windows.h>
#include <stdio.h>

int WINAPI WinMain(HINSTANCE hInst, HINSTANCE hPrev, LPSTR lpCmd, int nShow) {
    double V = 9.0;   // Voltaje en volts
    double I = 0.03;  // Corriente en amperes
    double R = V / I;

    char mensaje[100];
    sprintf(mensaje, "Ley de Ohm:\nR = V / I\nR = %.2f / %.2f = %.2f Ohm", V, I, R);

    MessageBox(NULL, mensaje, "Calculo de Resistencia", MB_OK);
    return 0;
}
