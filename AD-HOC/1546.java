import java.util.HashMap;
import java.util.Map;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        int qtdCasos = scanner.nextInt();

        Map<Integer, String> dic = new HashMap<>();
        dic.put(1, "Rolien");
        dic.put(2, "Naej");
        dic.put(3, "Elehcim");
        dic.put(4, "Odranoel");

        for (int i = 0; i < qtdCasos; i++) {
            int qtdFeed = scanner.nextInt();
            for (int j = 0; j < qtdFeed; j++) {
                int chave = scanner.nextInt();
                System.out.println(dic.get(chave));
            }
        }

        scanner.close();
    }
}
