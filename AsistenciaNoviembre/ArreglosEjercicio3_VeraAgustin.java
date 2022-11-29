/*
Leer 5 numeros por teclado, almacenarlos en un arreglo y realizar la media de los numeros positivos, la media de los negativos y contar los 
0*/
package ejercicios;

import java.util.Scanner;

public class Arreglos_Ejercicio_3 {
    public static void main(String[] args) {
        Scanner input  = new Scanner(System.in);
        float numeros[] = new float[5];
        float neg=0, pos=0, mediaPos=0, mediaNeg=0;
        int ceros=0, positivos=0, negativos = 0;
        
        
        for (int i = 0; i < numeros.length; i++) {
            System.out.println("Ingrese un numero: ");
            numeros[i] = input.nextFloat();
        }
        
        for (int i = 0; i < numeros.length; i++) {
            if(numeros[i] > 0){
                positivos++;
                pos += numeros[i];
            }else if(numeros[i] < 0){
                negativos++;
                neg += numeros[i];
            }else{
                ceros++;
            }
        }
        System.out.println("Cantidad de 0: "+ ceros);
        System.out.println("Media de positivos: "+ pos / positivos);
        System.out.println("Media de negativos: "+ neg / negativos);
    }
   
}
