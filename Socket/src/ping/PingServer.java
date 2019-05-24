
package ping;

import java.io.IOException;
import java.net.DatagramPacket;
import java.net.DatagramSocket;
import java.net.InetAddress;
import java.util.Scanner;




public class PingServer {

    
    public static void main(String[] args) {
        
        DatagramSocket dataGramsocket;
        DatagramPacket pack;
        int porta = 3333;

        while (true) {
                try {
                        System.out.println("Servidor UDP. Aguardando requisição...");
                        //Porta do servidor
                        dataGramsocket = new DatagramSocket(porta);
                        //Tamanho da mensagem
                        byte[] msg = new byte[256];
                        //Pegando a mensagem
                        pack = new DatagramPacket(msg, msg.length);
                        dataGramsocket.receive(pack);
                        
                        //Imprimindo a mensagem
                        System.out.println("Mensagem: " + new String(pack.getData()));
                        byte[] req = pack.getData();
                        
                        //Pegando IP e Porta do cliente
                        InetAddress ipClient = pack.getAddress();
                        int portClient = pack.getPort();
                        
                        //Enviando a mensagem para o cliente
                        pack = new DatagramPacket(req, req.length, ipClient, portClient);
                        dataGramsocket.send(pack);
                        
                        //dataGramsocket.send(dataGramPack.getData());
                        dataGramsocket.close();
                        
                        
                        
                } catch (IOException ex) {
                        System.out.println("Erro: " + ex.getMessage());
                }
        }

        }
    
}
