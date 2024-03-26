/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

import java.io.IOException;

/**
 *
 * @author rowell_w
 */
public class Runner
{
    public static void main(String[] args)
    {
        try
        {
            Store store = new Store();
        }
        // Catch EVERY error in this one statement (peak of my programming career)
        catch(IOException | NumberFormatException e)
        {
            System.out.println("Error: " + e);
            main(args);
        }
    }
}
