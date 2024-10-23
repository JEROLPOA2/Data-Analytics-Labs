
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("shipping-data.csv", index_col=0)

def gen_average_customer_rating():

    means = df.groupby('Mode_of_Shipment')['Customer_rating'].mean().reset_index()
    
    plt.barh(
        means['Mode_of_Shipment'], 
        means['Customer_rating'], 
        color='orange'
        )

    plt.xlim(0, 5)
    plt.title('Average Customer Rating')
    plt.ylabel('Shipment Mode')
    plt.xlabel('Average Rating')

    #plt.tight_layout()
    plt.savefig('average_customer_rating.png')


def gen_mode_of_shipment():

    percentage = df["Mode_of_Shipment"].value_counts(normalize=True).reset_index()
    
    
    plt.pie(
        percentage['proportion'], 
        labels=percentage["Mode_of_Shipment"], 
        autopct='%1.1f%%',
        wedgeprops=dict(width=0.3)
    )
    
    plt.title('Mode Of Shipment')
    plt.axis('equal')

    #plt.tight_layout()
    plt.savefig("mode_of_shipment.png")


def gen_weight_distribution():
    
    plt.hist(
        df['Weight_in_gms'], 
        bins=10,
        color='orange',
        rwidth=0.8,
        align="mid"
        )

    plt.title("Shipped Weight Distribution")
    plt.xlabel('Weights')
    plt.ylabel('Frequency')
    plt.xlim(0, 7000)
    plt.grid(False)

    #plt.tight_layout()
    plt.savefig("weight_distribution.png")


def gen_shipping_per_warehouse():

    ship_quant = df.groupby('Warehouse_block')['Mode_of_Shipment'].count().reset_index()

    plt.bar(
        ship_quant['Warehouse_block'], 
        ship_quant['Mode_of_Shipment'], 
        color='orange'
        )

    plt.title('Shipping Per Warehouse')
    plt.ylabel('Record Count')
    plt.xlabel('Warehouse Block')

    #plt.tight_layout()
    plt.savefig("shipping_per_warehouse.png")


gen_shipping_per_warehouse()
#gen_mode_of_shipment()
#gen_average_customer_rating()
#gen_weight_distribution()
