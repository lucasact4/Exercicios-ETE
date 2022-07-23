// Faça um programa que: Leia a cotação do dólar, Leia um valor em dólares, Converta esse valor para Real, Mostre o resultado.
import java.util.Scanner;
public class Exercicio2 {

	public static void main(String[] args) {
		System.out.println("Eae, vamos calcular a cotação do dólar e converte-lo em real ?");
		Scanner novo = new Scanner(System.in);
		System.out.print("Digite a cotação do dólar: ");
		double cotacao = novo.nextDouble();
		System.out.print("Digite o valor em dólar que deseja converter para real: ");
		double dolar = novo.nextDouble();
		System.out.println("Com " + dolar + " Dólares você consegue comprar R$" + dolar/cotacao);
		novo.close();
	}
}
