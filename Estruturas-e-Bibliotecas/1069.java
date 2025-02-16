import java.util.Scanner;

public class Main {

    public static int contarDiamantes(String sequencia) {
        int pilha = 0;
        int diamantes = 0;

        for (char caractere : sequencia.toCharArray()) {
            if (caractere == '<') {
                pilha++;
            } else if (caractere == '>' && pilha > 0) {
                pilha--;
                diamantes++;
            }
        }

        return diamantes;
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        int N = scanner.nextInt();
        scanner.nextLine();

        for (int i = 0; i < N; i++) {
            String sequencia = scanner.nextLine().trim();
            System.out.println(contarDiamantes(sequencia));
        }

        scanner.close();
    }
}