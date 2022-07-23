// Escreva um programa que leia dois números inteiros e apresente as opções para usuário escolher o que deseja realizar:
// 1 – Verificar se os dois números lidos são pares 2 – Verificar se a média dos dois números é maior ou igual a 7. 3 – Sair
import java.util.Scanner;
public class Exercicio8 {

	public static void main(String[] args) {
		Scanner novo = new Scanner(System.in);
		System.out.print("Digite o 1° número: ");
		int num1 = novo.nextInt();
		System.out.print("Digite o 2° número: ");
		int num2 = novo.nextInt();
		System.out.print("1 - Verificar se os dois números lidos são pares\n2 - Verificar se a média dos dois números é maior ou igual a 7\n3 - Sair\nDigite a operação que deseja fazer: ");
		int escolha = novo.nextInt();
		while (escolha < 1 || escolha > 3) {
			System.out.print("Você digitou uma operação inexistente !\nTente novamente: ");
			escolha = novo.nextInt();
		}
		if (escolha == 1) {
			if (num1 % 2 == 0 && num2 % 2 == 0) {
				System.out.print("Os dois números são pares");
			}
			else {
				System.out.print("Os dois números não são pares");
			}
		}
		else if (escolha == 2) {
			double media = (num1 + num2) / 2;
			if (media >= 7) {
				System.out.print("A média dos números é maior que 7.0");
			}
			else {
				System.out.print("A média dos números não é maior que 7.0");
			}
		}
		else if (escolha == 3) {
			System.out.print("Você saiu do programa com sucesso !");
		    System.exit(0);
		}
		novo.close();
	}
}
