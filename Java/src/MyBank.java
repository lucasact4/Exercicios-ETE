import java.util.Scanner;
import java.io.IOException;

public class MyBank {
	public static void main(String[] args) throws InterruptedException, IOException{
		int esc;
		final float SALDOIN = 150f;
		float saldo = SALDOIN;
		float deposit;
		float saque;
		do {
			Scanner in = new Scanner(System.in);
			System.out.println("====================");
			System.out.println("1 - Depositar");
			System.out.println("2 - Sacar");
			System.out.println("3 - Ver Extrato");
			System.out.println("4 - Sair");
			System.out.println("====================");

			System.out.print("Digite sua operação: ");
			esc = in.nextInt(); 
			System.out.println("====================");

			
			switch(esc) {
				case 1:
					do {
						System.out.print("Digite o valor a ser depositado: ");
						deposit = in.nextFloat();
						if (deposit>=0) {
						saldo += deposit;
						} else {
							System.out.print("Valor inválido\n");
						}
					} while(deposit<0);
					
					break;
				case 2:
					do {
						System.out.print("Digite o valor a ser sacado: ");
						saque = in.nextFloat();
						if(saque<=saldo) {
							saldo -= saque;
						} else {
							System.out.println("Saldo Inválido!");
						}
						break;
					} while(saque>saldo);
				case 3:
					System.out.println("O seu saldo é de R$" + saldo + " reais");
					break;
				case 4:
					System.out.print("Saindo do sistema...");
					break;
				default:
					System.out.print("Opção Inválida! Tente novamente!");
			}
			

		} while(esc!=4);
	}
}