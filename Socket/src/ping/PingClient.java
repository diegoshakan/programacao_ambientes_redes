
package ping;

import java.io.IOException;
import java.net.DatagramPacket;
import java.net.DatagramSocket;
import java.net.InetAddress;
import java.util.Scanner;


public class PingClient {

 
    public static void main(String[] args) {
        
        
      InetAddress host;
      Scanner teclado = new Scanner(System.in);
      
      try {
          host = InetAddress.getByName("localhost");
          int porta = 3333;
          
          while(true) {
              System.out.println("Mensagem: ");
              String mensagem = teclado.nextLine();
              
              byte[] msg = mensagem.getBytes();
              DatagramPacket pack = new DatagramPacket(msg, msg.length, host, porta);
              DatagramSocket dataGramSocket = new DatagramSocket();
              dataGramSocket.send(pack);
              
              System.out.println("Mensagem enviada para: " + host.getHostAddress() + "porta: " + porta);
              System.out.println("Server " + new String(pack.getData()) + " alive");
              dataGramSocket.close();
          }
      }
      catch (IOException ex) {
            System.out.println("Erro: " + ex.getMessage());
       }
    }
    
}
