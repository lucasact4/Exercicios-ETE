import java.util.Scanner;


public class Ex2 {
	public static void main(String [] args) {
		Scanner novo = new Scanner(System.in);
		System.out.println("Esolha um refri <3\n1 - Coca-Cola\n2 - Índaia\n3 - Guarana\n4 - Fanta\n5 - Frevo-Uva");
		int num = novo.nextInt();
		switch (num) {
		case 1:
			System.out.print("=-=-=-=\nVocê selecionou Coca-Cola\n=-=-=-=");
			break;
		case 2:
			System.out.print("=-=-=-=\nVocê selecionou Índaia\n=-=-=-=");
			break;
		case 3:
			System.out.print("=-=-=-=\nVocê selecionou Guarana\n=-=-=-=");
			break;
		case 4:
			System.out.print("=-=-=-=\nVocê selecionou Fanta\n=-=-=-=");
			break;
		case 5:
			System.out.print("=-=-=-=\nVocê selecionou Fanta-Uva\n=-=-=-=");
			break;
		default:
			System.out.print("Opçãoo Inválida !");
			break;
		}
		novo.close();
	}

}
