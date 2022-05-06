// Escreva um programa que exiba as seguintes opções e realize os que se pede em cada uma delas:
// 1 – Adição, 2 – Subtração, 3 – Multiplicação, 4 – Divisão
import java.util.Scanner;
public class Exercicio7 {

	public static void main(String[] args) {
		System.out.println("Eae, vamos calcular ? Digite o número da função que deseja:\n1 - Adição, 2 - Subtração, 3 - Mutiplicação, 4 - Divisão");
		Scanner novo = new Scanner(System.in);
		int num = novo.nextInt();
		while (num < 1 || num > 4) {
			System.out.print("Você digitou uma operação inexistente !\nTente novamente: ");
			num = novo.nextInt();
		}
		if (num == 1) {
			System.out.print("Você escolheu Adição !\nDigite o 1° número: ");
			double n1 = novo.nextDouble();
			System.out.print("Digite o 2° número: ");
			double n2 = novo.nextDouble();
			double soma = n1 + n2;
			System.out.println("A Adição de " + n1 + " + " + n2 + " é " + soma + "!");
		}
		else if (num == 2) {
			System.out.print("Você escolheu Subtração !\nDigite o 1° número que deseja subtrair: ");
			double m1 = novo.nextDouble();
			System.out.print("Digite o 2° número que deseja subtrair do número anterior: ");
			double m2 = novo.nextDouble();
			double subtracao = m1 - m2;
			System.out.println("A Subtração de " + m1 + " - " + m2 + " é " + subtracao + "!");
		}
		else if(num == 3) {
			System.out.print("Você escolheu Multiplicação !\nDigite o 1° número que deseja multiplicar: ");
			double b1 = novo.nextDouble();
			System.out.print("Digite o 2° número que deseja multiplicar: ");
			double b2 = novo.nextDouble();
			double mult = b1 * b2;
			System.out.println("A Multiplicação de " + b1 + " x " + b2 + " é " + mult + "!");
		}
		else if (num == 4) {
			System.out.print("Você escolheu Divisão !\nDigite o 1° número que deseja dividir: ");
			double v1 = novo.nextDouble();
			System.out.print("Digite o 2° número por quanto quer dividir: ");
			double v2 = novo.nextDouble();
			double div = v1 / v2;
			System.out.println("A Divisão de " + v1 + " ÷ " + v2 + " é " + div + "!");
		}
		novo.close();
	}
}
