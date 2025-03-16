//           EJERCICIO #1 - Numeros Primos
// Determinar si un número ingresado por el usuario es primo.

import java.util.Scanner;

public class E1_numerosPrimos {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.println("Ingrese un numero: ");
        int numero = scanner.nextInt();
        boolean esPrimo = true;

        for (int i = 2; i <= numero / 2 ; i++){
            if (numero % i == 0){
                esPrimo = false;
                break;
            }
        }

        if(esPrimo){
            System.out.println(numero + " es un numero primo");
        } else {
            System.out.println(numero + " no es un numero primo");
        }
    }

}
