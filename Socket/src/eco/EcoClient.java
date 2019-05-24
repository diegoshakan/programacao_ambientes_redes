package eco;

import java.io.IOException;
import java.io.PrintStream;
import java.net.Socket;
import java.net.UnknownHostException;
import java.util.Scanner;

public class EcoClient {
	public static void main(String[] args) {

		int porta = 3333;
		String ip = "localhost";

		try {
			Socket cliente = new Socket(ip, porta);

			System.out.printf("O cliente se conectou ao servidor %s.\n\n", ip);

			Scanner teclado = new Scanner(System.in);
                        
                        //Pegando o que o servidor envia
                        Scanner entrada = new Scanner(cliente.getInputStream());

			// stream para enviar dados para o servidor
			PrintStream saida = new PrintStream(cliente.getOutputStream());

			System.out.print("texto para enviar: ");
			while (teclado.hasNextLine()) {
				saida.println(teclado.nextLine());
                                System.out.println(entrada.nextLine());
				System.out.print("texto para enviar: ");
                                
			}

			saida.close();
			teclado.close();
			cliente.close();
		} catch (UnknownHostException e) {
			System.out.println("Erro de conexão: " + e.getMessage());
		} catch (IOException e) {
			System.out.println("Erro de I/O: " + e.getMessage());
		}
	}
}