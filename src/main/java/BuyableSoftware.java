public class BuyableSoftware extends Buyable
{
    private final String softwareType;

    public BuyableSoftware(double price, String name, String type)
    {
        super(price, name, "Software");
        softwareType = type;
    }

    public String getSoftwareType()
    {
        return softwareType;
    }

    @Override
    public String getFullInfo(boolean includeItemCategory)
    {
        return super.getFullInfo(includeItemCategory) + " | Software Type: " + getSoftwareType();
    }
}
