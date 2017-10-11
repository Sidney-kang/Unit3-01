/****************************************************************************
 *
 * Created on : 5 Oct. 2017
 * Created for : ICS3UR
 * Daily Assignment - Unit 3-01 
 * This program shows how to use an if statement  
 *
 ****************************************************************************/

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class guessingGame 
{
 
  static int NUMBERCOMPUTERISTHINKINGABOUT = 5;
  
  public static void main(String[] args)
    {  
       try 
       {
         double numberEntered;
         BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
         System.out.println("Enter the number that you think the computer is thinking about.");
        
         numberEntered = Double.parseDouble(br.readLine());  

         if (numberEntered == NUMBERCOMPUTERISTHINKINGABOUT)
            {
             System.out.println("Correct!");
            }
         else 
            {
             System.out.println("Try again!");
            }    
        }                
            
         catch(Exception nfe)       
            {
             System.err.println("Invalid input!");
            }  
    }      
}
