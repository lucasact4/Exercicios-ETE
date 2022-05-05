// Ler uma temperatura em graus Fahrenheit e apresentá-Ia convertida em graus Celsius. A fórmula de conversão de temperatura
// a ser utilizada é C = (F - 32) * 5 / 9, em que a variável F é a temperatura em graus Fahrenheit e a variável C é a
// temperatura em graus Celsius.
import java.util.Scanner;
public class Exercicio4 {

	public static void main(String[] args) {
		System.out.println("Eae, vamos converter Graus Fahrenheit para Graus Celcius ?");
		Scanner novo = new Scanner(System.in);
		System.out.print("Digite a temperatura em Graus Farenheit: F°");
		double faren = novo.nextDouble();
		System.out.print("A temeratura F°" + faren + "em Graus Celcius é: C°" + (faren - 32) * 5 / 9);
		novo.close();
	}
}
