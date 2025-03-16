//              Ejercicio #2 - Serie Fibonacci
// Generar la serie de Fibonacci hasta un número específico.

// 0, 1, 1, 2, 3, 5, 8, 13, 21...

import java.util.Scanner;

public class E2_serieFibonacci {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.println("Ingrese el numero de terminos: ");
        int n = scanner.nextInt();
        int primero = 0, segundo = 1;

        //
        System.out.println("Serie Fibonacci");
        for (int i = 1; i <= n; i++){
            System.out.println(primero + " "); // 0, 1,
            int siguiente = primero + segundo; // 1, 2,
            primero = segundo; // 0 -> 1, 1 -> 1,
            segundo = siguiente;// 1 -> 1, 1 -> 2,
        }



    }
}
