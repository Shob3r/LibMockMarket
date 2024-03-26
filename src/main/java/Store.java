
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.sql.SQLOutput;
import java.util.ArrayList;
import java.util.InputMismatchException;
import java.io.IOException;

public class Store
{
    // BufferedReader has replaced the scanner as it is simply superior to Scanner in every way
    BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
    
    // User data variables
    private BankAccount myBankAccount;
    private ArrayList<BuyableFood> boughtFood = new ArrayList<>();
    private ArrayList<BuyableClothing> boughtClothing = new ArrayList<>();
    private ArrayList<BuyableGame> boughtGames = new ArrayList<>();
    private ArrayList<BuyableSoftware> boughtSoftware = new ArrayList<>();
    private ArrayList<Buyable> myShoppingCart = new ArrayList<>();
    
    // Store data variables
    private StoreInventory storeInventory;
    
    public Store() throws IOException
    {
        System.out.println("Welcome to my storefront!");
        setupBankAccount();
        storeInventory = new StoreInventory();
        mainMenu();
    }

    private void setupBankAccount()
    {
        try
        {
            System.out.println("To begin, please set up a bank account.");
            System.out.println("How much money should your account contain?");
            double depositAmount = Double.parseDouble(reader.readLine());
            myBankAccount = new BankAccount(depositAmount);
        }
        catch(IOException | NumberFormatException e)
        {
            System.out.println("Error: " + e);
            setupBankAccount();
        }
    }
    
    private void mainMenu()
    {
        while(true)
        {
            try
            {
                System.out.println("\n------------------------------------------------------------- ");
                System.out.println("Please choose from one of the following menu options: ");
                System.out.println("1. View catalog of items to buy");
                System.out.println("2. Buy an item");
                System.out.println("3. View your cart of held items");
                System.out.println("4. Review the items you already own");
                System.out.println("5. View the status of your financials");
                System.out.println("6. Employee Access");
                System.out.println("7. Exit program");

                int input = Integer.parseInt(reader.readLine());

                switch(input)
                {
                    case 1:
                        itemMenu();
                        break;
                    case 2:
                        buyItem();
                        break;
                    case 3:
                        reviewMyShoppingCart();
                        break;
                    case 4:
                        reviewMyInventory();
                        break;
                    case 5:
                        reviewFinancials();
                        break;
                    case 6:
                        System.out.println("please enter the employee password (the password is not 'password' I swear)");
                        String inputPassword = reader.readLine();
                        if(inputPassword.equals("password"))
                        {
                            System.out.println("Congratulations! you are now logged into the employee panel");
                            adminPanel();
                        }
                        break;
                    case 7:
                        System.out.println("Thanks for shopping! Now exiting program ... ");
                        System.exit(0);
                        break;
                    default:
                        System.out.println("Incorrect input. Choose again!");
                        break;
                }
            }
            catch(IOException | NumberFormatException | InputMismatchException e)
            {
                System.out.println("Error: " + e + ". Returning you to the main menu.....");
            }

        }
    }
    private void itemMenu() throws IOException
    {
        System.out.println("Which products do you want to see?");
        System.out.println("1. All Products");
        System.out.println("2. Food");
        System.out.println("3. Clothing");
        System.out.println("4. Games");
        System.out.println("5. Software");
        System.out.println("6: Go back");
        System.out.println("--------------");
        System.out.print("(1-6) ");

        int choice = Integer.parseInt(reader.readLine());
        if(choice == 6)
        {
            System.out.println("Ok, returning to main menu.....");
            return;
        }

        switch(choice)
        {
            default:
                System.out.println("Please choose a valid number!");
                itemMenu();
                break;

            case 1:
                viewFullCatalog();
                break;
            case 2:
                viewFood();
                break;
            case 3:
                viewClothing();
                break;
            case 4:
                viewGames();
                break;
            case 5:
                viewSoftware();
                break;
        }
    }

    private void viewFullCatalog()
    {
        System.out.println("Here is a list of all the items currently for sale!");
        
        // Retrieve the master list from the store inventory and examine each entry individually
        for(Buyable item: storeInventory.getFullInventoryList()) 
        {
            System.out.println(item.getFullInfo(true));
        }
    }
    public void viewFood()
    {
        for(Buyable item: storeInventory.getFullInventoryList())
        {
            if(item instanceof BuyableFood)
            {
                System.out.println(item.getFullInfo(false));
            }
        }
    }

    public void viewClothing()
    {
        for(Buyable item: storeInventory.getFullInventoryList())
        {
            if(item instanceof BuyableClothing)
            {
                System.out.println(item.getFullInfo(false));
            }
        }
    }

    public void viewGames()
    {
        for(Buyable item: storeInventory.getFullInventoryList())
        {
            if(item instanceof BuyableGame)
            {
                System.out.println(item.getFullInfo(false));
            }
        }
    }

    public void viewSoftware()
    {
        for(Buyable item: storeInventory.getFullInventoryList())
        {
            if(item instanceof BuyableSoftware)
            {
                System.out.println(item.getFullInfo(false));
            }
        }
    }
    
    private void buyItem() throws IOException
    {
        System.out.println("Please type in the name of the item you wish to buy!");
        
        // Get user input
        String itemName = reader.readLine();
        
        // Holding variable for the desired item, if found
        Buyable itemToBuy = null;
        
        // Look through the full inventory to see if the item is present
        // Convert both item name and user input to lower case to prevent case issues!
        for(Buyable item: storeInventory.getFullInventoryList()) 
        {
            if(item.getItemName().equalsIgnoreCase(itemName))
            {
                itemToBuy = item;
                break;
            }
        }
        
        // If a suitable item was found, give them the option to buy it!
        if(itemToBuy != null)
        {
            System.out.println("We have " + itemToBuy.getItemName() + " in stock!");
            System.out.println("Type 1 to BUY NOW or 2 to PLACE IN YOUR SHOPPING CART.");
            
            int input = Integer.parseInt(reader.readLine());
            if(input == 1)
            {
                makePurchaseFromStore(itemToBuy);
            }
            else if(input == 2)
            {
                System.out.println("We'll hold onto this item for you.");
                moveItemToShoppingCart(itemToBuy);
            }
            else
            {
                System.out.println("Incorrect input. Purchase cancelled.");
            }
            
        }
        else // No suitable item found
        {
            System.out.println("The item you are looking for is sold out or does not exist, sorry!");
        }
    }

    private void reviewMyInventory() throws IOException
    {
        System.out.println("How many items would you like to see? type 'all' for all items");
        String items = reader.readLine().toLowerCase();

        System.out.println("Which types of items would you like to view? type 'all' if you want all item types to show");
        String itemType = reader.readLine().toLowerCase();
        if(items.equals("all"))
        {
            switch(itemType)
            {
                default:
                    System.out.println("please enter a valid item type! (case-insensitive)");
                    reviewMyInventory();
                    break;

                case "food":
                    System.out.println("Showing all food you have purchased:");
                    for(BuyableFood food : boughtFood)
                    {
                        // Do not include what item category the item comes from as the user literally just selected what item type they wanted to see
                        System.out.println(food.getFullInfo(false));
                    }
                    break;

                case "clothing":
                    System.out.println("Showing all clothing you have purchased:");
                    for(BuyableClothing clothing : boughtClothing)
                    {
                        System.out.println(clothing.getFullInfo(false));
                    }
                    break;

                case "games":
                    System.out.println("Showing all games you have purchased:");
                    for(BuyableGame games : boughtGames)
                    {
                        System.out.println(games.getFullInfo(false));
                    }
                    break;

                case "software":
                    System.out.println("Showing all software you have purchased:");
                    for(BuyableSoftware software : boughtSoftware)
                    {
                        System.out.println(software.getFullInfo(false));
                    }
                    break;
            }
        }
        else
        {
            int numItems = Integer.parseInt(items);
            switch(itemType)
            {
                default:
                    System.out.println("please enter a valid item type! (case-insensitive)");
                    reviewMyInventory();
                    break;

                case "food":
                    for(int i = 0; i < numItems; i++)
                    {
                        if(boughtFood.get(i) != null)
                        {
                            System.out.println(boughtFood.get(i).getFullInfo(false));
                        }
                        else break;
                    }
                    break;
                case "clothing":
                    for(int i = 0; i < numItems; i++)
                    {
                        if(boughtClothing.get(i) != null)
                        {
                            System.out.println(boughtFood.get(i).getFullInfo(false));
                        }
                        else break;
                    }
                    break;
                case "games":
                    for(int i = 0; i < numItems; i++)
                    {
                        if(boughtGames.get(i) != null)
                        {
                            System.out.println(boughtFood.get(i).getFullInfo(false));
                        }
                        else break;
                    }
                    break;
                case "software":
                    for(int i = 0; i < numItems; i++)
                    {
                        if(boughtSoftware.get(i) != null)
                        {
                            System.out.println(boughtFood.get(i).getFullInfo(false));
                        }
                        else break;
                    }
                    break;
            }
        }
    }

    private void reviewFinancials() throws IOException
    {
        System.out.println("You have $" + myBankAccount.getBalance() + " left in your account");
        System.out.println("What would you like to do?");
        System.out.println("1. View recent purchases");
        System.out.println("2. Add money to your account");
        System.out.println("3. Go back to the main menu");
        int choice = Integer.parseInt(reader.readLine());
        switch (choice)
        {
            default:
                System.out.println("Please enter a valid number!");
                break;
            case 1:

                if(!storeInventory.soldItems.isEmpty())
                {
                    System.out.println("Here are the 3 most recent purchases you have made:");
                    System.out.println("-------------------------------------------------");
                    for(int i = 0; i < 3; i++)
                    {
                        if(storeInventory.soldItems.get(i) != null)
                        {
                            System.out.println(storeInventory.soldItems.get(i).getFullInfo(true));
                        }
                        else break;
                    }
                }
                else System.out.println("You have not purchased any items recently!");
                break;
            case 2:
                System.out.println("How much money would you like to add to your account?");
                double moneyToAdd = Double.parseDouble(reader.readLine());
                myBankAccount.addBalance(moneyToAdd);
                break;
            case 3:
                System.out.println("Ok, returning to main menu");
        }
    }

    // SHOPPING CART METHODS
    private void reviewMyShoppingCart() throws IOException
    {
        if(!myShoppingCart.isEmpty())
        {
             System.out.println("Here are all of the items being held in your shopping cart: ");
             for(Buyable item: myShoppingCart)
             {
                 System.out.println(item.getItemName());
             }

             System.out.println("Would you like to purchase any held items now? 1 for YES or any other key for NO");

             String userInput = reader.readLine();

             if(userInput.equals("1"))
             {
                 buyItemInShoppingCart();
             }
             else
             {
                 System.out.println("Leaving shopping cart as is and returning to the storefront ... ");
             } 
        }
        else
        {
            System.out.println("Your shopping cart is empty! Nothing to see here ... ");
        }
    }
    
    private void buyItemInShoppingCart() throws IOException
    {
        System.out.println("Type in the name of the item you want to buy from the shopping cart: ");
        String userChoice = reader.readLine();
        
        for(Buyable itemInCart: myShoppingCart)
        {
            if(itemInCart.getItemName().equalsIgnoreCase(userChoice))
            {
                makePurchaseFromShoppingCart(itemInCart);
                break;
            }
            else
            {
                System.out.println("Item could not be found in shopping cart.");
            }
        }
    }
    
    private void removeItemFromShoppingCart(Buyable item) throws IOException
    {
        System.out.println("Which item would you like to remove from your shopping cart?");
        String userChoice = reader.readLine();
        
        for(Buyable cartItem: myShoppingCart)
        {
            if(cartItem.getItemName().equalsIgnoreCase(userChoice))
            {
                System.out.println("You have removed " + cartItem.getItemName() + " from your shopping cart.");
                moveItemFromShoppingCartToInventory(item);
            }
            else
            {
                System.out.println("Item could not be found in your shopping cart.");
            }
        }
    }
    
    // Move item from inventory to shopping cart
    private void moveItemToShoppingCart(Buyable item)
    {
        myShoppingCart.add(item);
        storeInventory.removeItemFromInventory(item);
    }
    
    private void moveItemFromShoppingCartToInventory(Buyable item)
    {
        storeInventory.restockItemToInventory(item);
        myShoppingCart.remove(item);
    }

    private void makePurchaseFromStore(Buyable item)
    {
        // If you can afford the item, buy it and remove it from the store
        if(myBankAccount.canAfford(item.getPrice()))
        {
            myBankAccount.makePurchase(item.getPrice());
            System.out.println("Purchase complete! You now own " + item.getItemName());
            addBoughtItemToCorrectPurchaseList(item);
            storeInventory.removeItemFromInventory(item);
            storeInventory.soldItems.add(item);
        }
        else
        {
            System.out.println("You can't afford that item ... ");
        }
    }

    private void addBoughtItemToCorrectPurchaseList(Buyable boughtItem)
    {
        if(boughtItem instanceof BuyableFood)
        {
            boughtFood.add((BuyableFood) boughtItem);
        }
        else if (boughtItem instanceof BuyableClothing)
        {
            boughtClothing.add((BuyableClothing) boughtItem);
        }
        else if (boughtItem instanceof BuyableGame)
        {
            boughtGames.add((BuyableGame) boughtItem);
        }
        else if (boughtItem instanceof BuyableSoftware)
        {
            boughtSoftware.add((BuyableSoftware) boughtItem);
        }
    }

    private void makePurchaseFromShoppingCart(Buyable item)
    {
        // If you can afford the item, buy it and remove it from the store
        if(myBankAccount.canAfford(item.getPrice()))
        {
            myBankAccount.makePurchase(item.getPrice());
            System.out.println("Purchase complete! You now own " + item.getItemName());
            addBoughtItemToCorrectPurchaseList(item);
            myShoppingCart.remove(item);
        }
        else
        {
            System.out.println("You can't afford that item ... ");
        }        
    }


    private void adminPanel() throws IOException
    {
        System.out.println("Welcome to the employee menu");
        while (true)
        {
            System.out.println("----------------------------------");
            System.out.println("What would you like to do?");
            System.out.println("1. Add item to stock");
            System.out.println("2. Go back");

            int choice = Integer.parseInt(reader.readLine());

            if(choice == 1)
            {
                addCustomItemToStock();
            }
            else if (choice == 2)
            {
                System.out.println("Returning to main menu....");
                break;
            }
        }

    }
    private void addCustomItemToStock() throws IOException
    {
        System.out.println("What item type would you like to add?");
        System.out.println("1. Food");
        System.out.println("2. Clothing");
        System.out.println("3. Games");
        System.out.println("4. Software");
        int itemType = Integer.parseInt(reader.readLine());

        System.out.println("What is the name of the item?");
        String itemName = reader.readLine();

        System.out.println("How much does this item cost?");
        double price = Double.parseDouble(reader.readLine());

        switch(itemType)
        {
            default:
                System.out.println("Please input a valid choice!");
                break;
            case 1:     // Food
                System.out.println("How much does this food product weigh?");
                double weight = Double.parseDouble(reader.readLine());
                storeInventory.foodForSale.add(new BuyableFood(price, itemName, weight));
                break;
            case 2:     // Clothing
                System.out.println("What size is this clothing?");
                String size = reader.readLine();
                storeInventory.clothesForSale.add(new BuyableClothing(price, itemName, size));
                break;
            case 3:     // Games
                System.out.println("What type of game is this?");
                String gameGenre = reader.readLine();
                System.out.println("How many players can play this game?");
                int numPlayers = Integer.parseInt(reader.readLine());

                storeInventory.gamesForSale.add(new BuyableGame(price, itemName, numPlayers, gameGenre));
                break;
            case 4:     // Software
                System.out.println("What type of software is this?");
                String softwareType = reader.readLine();

                storeInventory.softwareForSale.add(new BuyableSoftware(price, itemName, softwareType));
                break;
        }
    }
}
