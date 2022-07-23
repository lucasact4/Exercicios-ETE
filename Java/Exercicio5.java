// Escreva um programa que leia quatro notas escolares de um aluno e apresentar uma mensagem que o
// aluno foi aprovado se o valor da média escolar for maior ou igual a 7. Se o valor da média for
// menor que 7, solicitar a notado recuperação, somar com o valor da média e obter a nova média.
// Se a nova média for maior ou igual a 7,apresentar uma mensagem informando que o aluno foi
// aprovado na recuperação. Se o aluno não foi aprovado, apresentar uma mensagem informando
// esta condição. Apresentar junto com as mensagens o valor da média do aluno.
import java.util.Scanner;
public class Exercicio5 {

	public static void main(String[] args) {
		System.out.println("Eae, vamos calcular a média do aluno ?");
		Scanner novo = new Scanner(System.in);
		System.out.print("Digite a 1° nota do aluno: ");
		double nota1 = novo.nextDouble();
		System.out.print("Digite a 2° nota do aluno: ");
		double nota2 = novo.nextDouble();
		System.out.print("Digite a 3° nota do aluno: ");
		double nota3 = novo.nextDouble();
		System.out.print("Digite a 4° nota do aluno: ");
		double nota4 = novo.nextDouble();
		double media1 = (nota1 + nota2 + nota3 + nota4) / 4;
		if (media1 >= 7) {
			System.out.println("Aluno Aprovado !\nSua média: " + media1);
		}
		if (media1 < 7) {
			System.out.print("Você não atingiu uma nota maior ou igual a 7.0.\nPor favor, digite a sua nota de recuperação: ");
			double rec = novo.nextDouble();
			double media2 = media1 + rec;
			if (media2 >= 7) {
				System.out.println("Aluno Aprovado !\nSua média: " + media2);
			}
			else {
				System.out.println("Aluno Reprovado !\nSua média: " + media2);
			}
				
		}
		novo.close();
	}
}
