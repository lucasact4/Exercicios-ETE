// Ler uma temperatura em graus Celsius e apresentá-Ia convertida em graus Fahrenheit. A fórmula de conversão de
// temperatura a ser utilizada é F = (9 * C + 160) / 5, em que a variável F representa é a temperatura
// em graus Fahrenheit e a variável C representa é a temperatura em graus Celsius.
import java.util.Scanner;
public class Exercicio3 {

	public static void main(String[] args) {
		System.out.println("Eae, vamos converter Graus Celcius para Graus Fahrenheit ?");
		Scanner novo = new Scanner(System.in);
		System.out.print("Digite a temperatura em Graus Celcius: C°");
		double celcius = novo.nextDouble();
		System.out.print("A temeratura C°" + celcius + "em Graus Farenheit é: F°" + (9 * celcius + 160) / 5);
		novo.close();
	}
}
