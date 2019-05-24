
package eco;

import java.io.IOException;
import java.io.PrintStream;
import java.net.InetAddress;
import java.net.ServerSocket;
import java.net.Socket;
import java.util.Scanner;
import java.util.logging.Level;
import java.util.logging.Logger;


public class EcoServer {


    public static void main(String[] args) {
        
        try {
            //Iniciando o servidor
            ServerSocket server = new ServerSocket(3333);
    
            
            String ip = InetAddress.getByName("localhost").getHostAddress();
            byte[] ipVec = InetAddress.getByName("localhost").getAddress();
            String host = InetAddress.getByAddress(ipVec).getHostName();  
            
            System.out.printf("Servidor %s (%s) aguardando conexão na porta 3333\n", host, ip);
            
            //Aguandando conexão
            Socket cliente = server.accept();
            System.out.println("Cliente conectado do IP" + cliente.getInetAddress().getHostAddress());
            
            //Recebe dados
            Scanner entrada = new Scanner(cliente.getInputStream());
            
            //Envia dados
            PrintStream saida = new PrintStream(cliente.getOutputStream());
            
            //Pegando o que o cliente enviou e reenviando tudo em maiúsculo
            while(entrada.hasNextLine()) {
                String texto = entrada.nextLine();
                System.out.println("Mensagem " + texto); 
                saida.println("Server: " + texto.toUpperCase());
            }
            
            entrada.close();
            server.close();
   
            
            
            //Socket client = server.accept();
        } catch (IOException ex) {
            Logger.getLogger(ServerSocket.class.getName()).log(Level.SEVERE, null, ex);
        }
    }
    
}
