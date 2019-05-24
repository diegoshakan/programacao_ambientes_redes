/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package caracoroa;

import java.util.Random;
import java.util.logging.Level;
import java.util.logging.Logger;


public class CaraCoroa implements Runnable {
    
    public static String resposta;
    private String respostaThread;
    private int tempo;
    
    
    public CaraCoroa(String respostaThread) {
        this.respostaThread = respostaThread;
        Random random = new Random();
        this.tempo = random.nextInt(30);
    }
    
    public String getRespostaThread() {
        return this.respostaThread;
    }
  
    public void run() {
        try {
            Thread.sleep(this.tempo);
            System.out.println(this.respostaThread);
            
        } catch (InterruptedException ex) {
            Logger.getLogger(CaraCoroa.class.getName()).log(Level.SEVERE, null, ex);
        }
        
        CaraCoroa.resposta = this.getRespostaThread();
    }
    
   
    
    
    
}
