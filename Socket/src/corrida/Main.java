
package corrida;

import java.util.logging.Level;
import java.util.logging.Logger;


public class Main {
  
   
    public static void main(String[] args) {
        
        
        CorridaThreads massa = new CorridaThreads("Felipe Massa");
        CorridaThreads hamilton = new CorridaThreads("Lewis Hamilton");
        
        Thread th1 = new Thread(massa);
        Thread th2 = new Thread(hamilton);
        
        th1.start();
        th2.start(); 
        
          
        try {
            th1.join();
            th2.join();
        } catch (InterruptedException ex) {
            Logger.getLogger(Main.class.getName()).log(Level.SEVERE, null, ex);
        }
        
        
       
       if (CorridaThreads.ultimo == "Felipe Massa") {
           System.out.println("O Vencedor é Lewis Hamilton");
       }
       else {
           System.out.println("O Vencedor é Felipe Massa");
       }
        
        
        
          
    }

}
