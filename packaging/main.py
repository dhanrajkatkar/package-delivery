from packer import Packer
from bin import Bin
from item import Item
from pandas import read_csv

df = read_csv("/home/pega/Downloads/Ship_InventSum.csv")
df.columns = ["sales_id", "item_id", "shipment_quantity", "width", "height", "depth", "lat", "lon",
              "customer_delivery_date"]
df['width'] = df['width'] * 2.5
df['height'] = df['height'] * 2.5
df['depth'] = df['depth'] * 2.5
df['volume'] = df['width'] * df['height'] * df['depth']
df = df.drop(['customer_delivery_date'], axis=1)
df_prod = df.sample(500)


pkr = Packer()
# name, length, width, height, capacity(weight)
pkr.add_bin(Bin('20-ft container', 589, 235, 236, 25000))

for i, r in df_prod.iterrows():
    pkr.add_item(Item(r['item_id'], r['depth'], r['width'], r['height'], 1))

for i in range(10):
    fitted, unfitted = pkr.pack()
    pkr.unplaced_items = unfitted
    pkr.bins = []
    pkr.add_bin(Bin('20-ft container', 589, 235, 236, 25000))

    pkr.placed_items = []
    pkr.unfit_items = []
    pkr.total_items = len(unfitted)

    print(len(fitted), "fitted", fitted)
    print('*'*40)
    print(len(unfitted), "unfitted", unfitted)

# fitted, unfitted = pkr.pack()
#
#
# print(len(fitted), "fitted", fitted)
# print('*'*40)
# print(len(unfitted), "unfitted", unfitted)
