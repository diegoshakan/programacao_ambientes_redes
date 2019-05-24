
package caracoroa;

import java.util.Scanner;
import java.util.logging.Level;
import java.util.logging.Logger;


public class Main {

 
    public static void main(String[] args) {
        
        CaraCoroa cara = new CaraCoroa("cara");
        CaraCoroa coroa = new CaraCoroa("coroa");
        
        Thread th1 = new Thread(cara);
        Thread th2 = new Thread(coroa);
        
        Scanner entrada = new Scanner(System.in);
        
        System.out.print("Digite seu Palpite: ");
        String palpite = entrada.nextLine();
        System.out.println("");
        System.out.println("");
        
        th1.start();
        th2.start();
        
        
        try {
            th1.join();
            th2.join();
            
        } catch (InterruptedException ex) {
            Logger.getLogger(Main.class.getName()).log(Level.SEVERE, null, ex);
        }
        
   
        if (CaraCoroa.resposta.toLowerCase().equals(palpite.toLowerCase())) {
            System.out.println("");
            System.out.println("Meu palpite: " + palpite);
            System.out.println("Valor da Thread: " + CaraCoroa.resposta);
            System.out.println("");
            System.out.println("Você acertou");
        }
        else {
            System.out.println("");
            System.out.println("Meu palpite: " + palpite);
            System.out.println("Valor da Thread: " + CaraCoroa.resposta);
            System.out.println("");
            System.out.println("Você errou");
        }
        
        
    }
    
}
