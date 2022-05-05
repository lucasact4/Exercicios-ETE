// Faça um programa que leia um número. Se positivo armazene-o em A, se for negativo, em B. No final mostrar o resultado.
import java.util.Scanner;
public class Exercicio6 {

	public static void main(String[] args) {
		Scanner novo = new Scanner(System.in);
		System.out.print("Digite um número: ");
		double num = novo.nextDouble();
		if (num >= 0) {
			System.out.println("Número Positivo !\nArmazenando na variável 'A'.");
			double A = num;
			System.out.println("Número: " + A);
		}
		else {
			System.out.println("Número Negativo !\nArmazenando na variável 'B'.");
			double B = num;
			System.out.println("Número: " + B);
		}
		novo.close();
	}
}
