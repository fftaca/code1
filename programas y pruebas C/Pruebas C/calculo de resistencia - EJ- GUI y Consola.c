#include <windows.h>
#include <stdio.h>

/*PARA GUI*/
int main() {
    double V = 9.0;
    double I = 0.03;
    double R = V / I;

    char mensaje[100];
    sprintf(mensaje, "Ley de Ohm:\nR = V / I\nR = %.2f / %.2f = %.2f Ohm", V, I, R);

    MessageBox(NULL, mensaje, "Calculo de Resistencia", MB_OK);
    return 0;
}

/*PARA CONSOLA*/

#include <stdio.h>

int main() {
    double V = 9.0;
    double I = 0.03;
    double R = V / I;

    printf("Ley de Ohm:\n");
    printf("R = V / I\n");
    printf("R = %.2f / %.2f = %.2f Ohm\n", V, I, R);

    return 0;
}
