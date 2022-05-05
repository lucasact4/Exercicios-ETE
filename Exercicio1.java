// Faça um programa para calcular o estoque médio de uma peça, sendo que: ESTOQUE MÉDIO = (QUANTIDADE_MÍNIMA + QUANTIDADE_MÁXIMA) / 2.
import java.util.Scanner;
public class Exercicio1 {

	public static void main(String[] args) {
		System.out.println("Eae, vamos calcular o estoque médio de uma peça ?");
		Scanner novo = new Scanner(System.in);
		System.out.print("Digite a quantidade mínima: ");
		int Qminima = novo.nextInt();
		System.out.print("Digite a quantidade máxima: ");
		int Qmaximo = novo.nextInt();
		System.out.println("Estoque médio: " + (Qminima+Qmaximo)/2);
		novo.close();
	}
}
