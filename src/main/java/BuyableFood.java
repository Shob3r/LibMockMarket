
public class BuyableFood extends Buyable
{

    private final double weight;
    
    public BuyableFood(double price, String name, double weight) {
        super(price, name, "Food");
        this.weight = weight;
    }

    public double getWeight()
    {
        return weight;
    }

    @Override
    public String getFullInfo(boolean includeItemCategory)
    {
        return super.getFullInfo(includeItemCategory) + " | " + getWeight() + "g";
    }
}
