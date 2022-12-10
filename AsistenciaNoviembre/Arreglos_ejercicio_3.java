/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package Arreglos_Ejercicio_3;
import java.util.Scanner
        
public class Arreglos_ejercicio_3 {
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        float numeros[] = new float[5];
        float negativos=0, positivos=0,mediaNegativos,mediaPositivos;
        int conteo0=0,conteo_negativos=0,conteo_positivos=0;
        
        System.out.println("Guardamos los elementos del arreglo: ");
        para(int i=0;i<5;i++){
            System.out.println((i+1)+".Digite un numero: ");
            numeros[i] = entrada.nextFloat();
            if(numeros[i]>0){
                conteo_positivos++;
            }
            else if(numeros[i]<0){
                negativos += numeros[i];
                conteo_negativos++;
            }
            más{
                conteo0++;
            }
        }
            
       si(conteo_positivos == 0){
           System.out.println("\nNo se puede sacar los medios de los numeros");
        }
        
        System.out.println("La cantidad de ceros es: "+conteo0);
    }
}
}
