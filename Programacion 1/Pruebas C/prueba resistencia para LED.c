#include <windows.h>
#include <stdio.h>

#define ID_EDIT1 101
#define ID_EDIT2 102
#define ID_EDIT3 103
#define ID_BUTTON_CALC 104
#define ID_BUTTON_EXIT 105
#define ID_STATIC_RESULT 106

LRESULT CALLBACK WindowProc(HWND hwnd, UINT msg, WPARAM wParam, LPARAM lParam) {
    static HWND hEditV, hEditLed, hEditI, hStaticResult;

    switch (msg) {
    case WM_CREATE:
        CreateWindow("STATIC", "Voltaje de fuente (V):", WS_VISIBLE | WS_CHILD, 20, 20, 150, 20, hwnd, NULL, NULL, NULL);
        hEditV = CreateWindow("EDIT", "", WS_VISIBLE | WS_CHILD | WS_BORDER, 180, 20, 100, 20, hwnd, (HMENU)ID_EDIT1, NULL, NULL);

        CreateWindow("STATIC", "Caida LED (V):", WS_VISIBLE | WS_CHILD, 20, 50, 150, 20, hwnd, NULL, NULL, NULL);
        hEditLed = CreateWindow("EDIT", "", WS_VISIBLE | WS_CHILD | WS_BORDER, 180, 50, 100, 20, hwnd, (HMENU)ID_EDIT2, NULL, NULL);

        CreateWindow("STATIC", "Corriente (mA):", WS_VISIBLE | WS_CHILD, 20, 80, 150, 20, hwnd, NULL, NULL, NULL);
        hEditI = CreateWindow("EDIT", "", WS_VISIBLE | WS_CHILD | WS_BORDER, 180, 80, 100, 20, hwnd, (HMENU)ID_EDIT3, NULL, NULL);

        CreateWindow("BUTTON", "Calcular", WS_VISIBLE | WS_CHILD, 50, 120, 100, 30, hwnd, (HMENU)ID_BUTTON_CALC, NULL, NULL);
        CreateWindow("BUTTON", "Cerrar", WS_VISIBLE | WS_CHILD, 180, 120, 100, 30, hwnd, (HMENU)ID_BUTTON_EXIT, NULL, NULL);

        hStaticResult = CreateWindow("STATIC", "", WS_VISIBLE | WS_CHILD, 20, 170, 350, 60, hwnd, (HMENU)ID_STATIC_RESULT, NULL, NULL);
        break;

    case WM_COMMAND:
        if (LOWORD(wParam) == ID_BUTTON_CALC) {
            char bufV[20], bufLed[20], bufI[20];
            double Vfuente, Vled, I, R;
            char resultado[256];

            GetWindowText(hEditV, bufV, sizeof(bufV));
            GetWindowText(hEditLed, bufLed, sizeof(bufLed));
            GetWindowText(hEditI, bufI, sizeof(bufI));

            Vfuente = atof(bufV);
            Vled = atof(bufLed);
            I = atof(bufI) / 1000.0; // Convertimos mA a A

            if (I > 0 && Vfuente > Vled) {
                R = (Vfuente - Vled) / I;
                snprintf(resultado, sizeof(resultado),
                    "Formula: R = (Vf - Vled) / I\n"
                    "R = (%.2f - %.2f) / %.3f = %.2f ohms",
                    Vfuente, Vled, I, R);
            } else {
                snprintf(resultado, sizeof(resultado),
                    "⚠️ Datos invalidos.\nVerifique que Vfuente > Vled y I > 0.");
            }

            SetWindowText(hStaticResult, resultado);
        }
        if (LOWORD(wParam) == ID_BUTTON_EXIT) {
            PostQuitMessage(0);
        }
        break;

    case WM_DESTROY:
        PostQuitMessage(0);
        break;

    default:
        return DefWindowProc(hwnd, msg, wParam, lParam);
    }
    return 0;
}

int WINAPI WinMain(HINSTANCE hInstance, HINSTANCE hPrevInstance,
    LPSTR lpCmdLine, int nCmdShow) {

    const char CLASS_NAME[] = "CalculadoraLED";

    WNDCLASS wc = { };
    wc.lpfnWndProc = WindowProc;
    wc.hInstance = hInstance;
    wc.lpszClassName = CLASS_NAME;
    wc.hbrBackground = (HBRUSH)(COLOR_WINDOW + 1);

    RegisterClass(&wc);

    HWND hwnd = CreateWindowEx(0, CLASS_NAME, "Calculadora de R para LED",
        WS_OVERLAPPEDWINDOW ^ WS_THICKFRAME ^ WS_MAXIMIZEBOX,
        CW_USEDEFAULT, CW_USEDEFAULT, 400, 280,
        NULL, NULL, hInstance, NULL);

    ShowWindow(hwnd, nCmdShow);

    MSG msg = { };
    while (GetMessage(&msg, NULL, 0, 0)) {
        TranslateMessage(&msg);
        DispatchMessage(&msg);
    }

    return 0;
}
