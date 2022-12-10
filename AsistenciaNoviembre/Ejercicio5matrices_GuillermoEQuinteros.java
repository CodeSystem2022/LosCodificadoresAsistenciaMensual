/*
  Ejercicio 5 de matrices: Crear una matriz de mxn que pueda ser llenada por el usuario.
Moatrar la matriz resultante y mostrar la suma de cada fila y cada columna.
 */
package ejercicio5matrices_guillermoequinteros;

import java.util.Scanner;
import javax.swing.JOptionPane;

public class Ejercicio5matrices_GuillermoEQuinteros {
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        
        int matriz [][],nFilas,nColumnas,sumaFilas,sumaColumnas;
        int posFila,posColumna;
        
        nFilas = Integer.parseInt(JOptionPane.showInputDialog("Ingrese el n° de filas: "));
        nColumnas = Integer.parseInt(JOptionPane.showInputDialog("Ingrese el n° de columnas: "));
        
        matriz = new int [nFilas][nColumnas];
        int filas[] = new int[nFilas];
        int columnas[] = new int[nColumnas];
        
        System.out.println("Completar la matriz: ");
        for(int i=0;i<nFilas;i++){
            for(int j=0;j<nColumnas;j++){
                System.out.print("Matriz ["+i+"]["+j+"]: ");
                matriz[i][j] = entrada.nextInt();
            }
        }
        System.out.println("\nLa Matriz: ");
        for(int i=0;i<nFilas;i++){
            for(int j=0;j<nColumnas;j++){
                System.out.print(matriz[i][j]+" ");
            }
            System.out.println("");
        }
        //Suma de filas
        posFila = 0;
        for(int i=0;i<nFilas;i++){
            sumaFilas=0;
            for(int j=0;j<nColumnas;j++){
                sumaFilas += matriz[i][j];
            }
            filas[posFila] = sumaFilas;
            posFila++;
        }
        //Suma de columnas
        posColumna = 0;
        for(int j=0;j<nColumnas;j++){
            sumaColumnas=0;
            for(int i=0;i<nFilas;i++){
                sumaColumnas += matriz[i][j];
            }
            columnas[posColumna] = sumaColumnas;
            posColumna++;
        }
        System.out.println("\nLa suma de las filas es: ");
        for(int i=0;i<nFilas;i++){
            System.out.print(filas[i]+" - ");
        }
        System.out.println("");
        System.out.println("\nLa suma de las columnas es: ");
        for(int i=0;i<nColumnas;i++){
            System.out.print(columnas[i]+" - ");
        }
        System.out.println("");
    }
    
}
