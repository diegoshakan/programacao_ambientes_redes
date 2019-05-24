
package corrida;

import java.util.Random;
import java.util.logging.Level;
import java.util.logging.Logger;


public class CorridaThreads implements Runnable {

    private String nome;
    private int tempo;
    public static String ultimo;
    
    
    public CorridaThreads(String nome) {
        this.nome = nome;
        Random random = new Random();
        this.tempo = random.nextInt(700);
    }
    
    public String getNome() {
        return this.nome;
    }
    
    public void run() {
        try {
            
            for(int i = 1; i < 66; i++) {
                Thread.sleep(this.tempo);
                System.out.println(this.nome + ", volta " + i);
         
            } 
            
        }catch (InterruptedException ex) {
           Logger.getLogger(CorridaThreads.class.getName()).log(Level.SEVERE, null, ex);
        }
        
        
        CorridaThreads.ultimo = this.getNome();
        
               
    }
 }
    

