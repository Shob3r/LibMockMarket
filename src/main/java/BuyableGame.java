
public class BuyableGame extends Buyable
{
    private final int numPlayers;
    private final String genre;
    
    public BuyableGame(double price, String name, int numPlayers, String genre) {
        super(price, name, "Game");
        this.numPlayers = numPlayers;
        this.genre = genre;
    }

    public int getNumPlayers()
    {
        return numPlayers;
    }
    
    public String getGenre()
    {
        return genre;
    }

    @Override
    public String getFullInfo(boolean includeItemCategory)
    {
        return super.getFullInfo(includeItemCategory) + " | Genre: " + getGenre() + " | Player Count: " + getNumPlayers();
    }
}
