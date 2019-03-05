import java.util.Scanner; 

public class q3 { 
    public static void main(String[] args) 
                           throws InterruptedException { 
        final PC pc = new PC(); 
  
        Thread t1 = new Thread(new Runnable() { 
            @Override
            public void run(){ 
                try{ 
                    pc.odd(); 
                } 
                catch(InterruptedException e){ 
                    e.printStackTrace(); 
                } 
            } 
        }); 

        Thread t2 = new Thread(new Runnable() { 
            @Override
            public void run(){ 
                try{ 
                    pc.even(); 
                } 
                catch(InterruptedException e){ 
                    e.printStackTrace(); 
                } 
            } 
        }); 
  
        t1.start(); 
        t2.start(); 
  
        t1.join(); 
        t2.join(); 
    } 

    public static class PC { 
        public void odd()throws InterruptedException { 
            synchronized(this) { 
                for(int i=1; i<1000; i=i+2){
                    System.out.println(i); 
                    
                    notify();
                    wait(); 
                    
                }
            } 
        } 
        
        public void even()throws InterruptedException { 
            Thread.sleep(100);
            synchronized(this){ 
                for(int i=2; i<1000; i=i+2){
                    System.out.println(i); 
                    
                    notify();
                    wait(); 
                }
                notify();
            } 
        } 
    } 
} 
