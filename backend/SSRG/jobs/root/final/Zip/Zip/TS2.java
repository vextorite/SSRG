import java.util.Scanner;

public class TestSeller {

   public static void main(String[] args){
   Scanner in = new Scanner(System.in);
   Seller sellerObj1 = new Seller();
   System.out.println("Please enter the details of the seller.");
   System.out.print("ID: ");
   sellerObj1.ID = in.nextLine();
   System.out.print("Name: ");
   sellerObj1.name = in.nextLine();
   System.out.print("Location: ");
   sellerObj1.location = in.nextLine();
   System.out.print("Product: ");
   sellerObj1.product = in.nextLine();
   System.out.print("Price: ");
   String word = in.nextLine();
   Currency rand = new Currency("R", "ZAR", 100);
   Money unitpriceVar = new Money(word, rand);
   sellerObj1.unit_price = unitpriceVar;
   System.out.print("Units: ");
   sellerObj1.number_of_units =Integer.valueOf(in.nextLine());
   System.out.println("The seller has been successfully created:");
   System.out.println("ID of the seller: "+sellerObj1.ID);
   System.out.println("Name of the seller: "+sellerObj1.name);
   System.out.println("Location of the seller: "+sellerObj1.location);
   System.out.println("The product to sell: "+sellerObj1.product);
   System.out.println("Product unit price: "+sellerObj1.unit_price);
   System.out.println("The number of available units: "+sellerObj1.number_of_units);

   




   
   

   
   }
   
}