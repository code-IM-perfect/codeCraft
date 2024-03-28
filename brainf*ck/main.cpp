#include <iostream>
using namespace std;

char cells[30000] = {0};

int current = 0;

void handleValue(char k) {
    if (k == '>') {
        // current++;
        // current %= 30000;
        if (current == 30000) {
            current = 0;
        } else {
            current++;
        }

    } else if (k == '<') {
        // current--;
        // current %= 30000;
        if (current == 0) {
            current = 30000;
        } else {
            current--;
        }
    } else if (k == '+') {
        cells[current]++;
    } else if (k == '-') {
        cells[current]--;
    } else if (k == '.') {
        cout << +cells[current] << endl;
    } else if (k == '[') {
        int loop = 1;
        string loopingSeries = "";
        k = cin.get();
        while ((k != ']') && (loop)) {
            loopingSeries = loopingSeries + k;
            k = cin.get();
            if (k == '[') {
                loop++;
            } else if (k == ']') {
                loop--;
            }
        }
        int n = loopingSeries.length();
        while (cells[current]) {
            for (int i = 0; i < n; i++) {
                handleValue(loopingSeries[i]);
            }
        }
        loop--;
    }
}

int main() {
    char k;

    while (cin.get(k)) {
        handleValue(k);
    }

    return 0;
}
