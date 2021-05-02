#constants:
gs_flat = 20.00
gsp_price = 125.00

#input:
weight = 4.8
print("Your item's weight is: " + str(weight) + " lb")

#ground shipping calculation:
if weight <= 2:
  gs_price = weight * 1.50 + gs_flat
elif weight > 2 and weight <= 6:
  gs_price = weight * 3.00 + gs_flat
elif weight > 6 and weight <= 10:
  gs_price = weight * 4.00 + gs_flat
elif weight > 10:
  gs_price = weight * 4.75 + gs_flat
print("Price for Ground Shipping is: $" + str(gs_price))

#ground shipping premium "calculation":
print("Price for Ground Shipping Premium is: $" + str(gsp_price))

#drone shipping calculation:
if weight <= 2:
  ds_price = weight * 4.50
elif weight > 2 and weight <= 6:
  ds_price = weight * 9.00
elif weight > 6 and weight <= 10:
  ds_price = weight * 12.00
elif weight > 10:
  ds_price = weight * 14.25
print("Price for Drone Shipping is: $" + str(ds_price))

#solution:
final_price = gs_price
choice = "Ground Shipping"
if final_price > gsp_price:
  final_price = gsp_price
  choice = "Ground Shipping Premium"
if final_price > ds_price:
  final_price = ds_price
  choice = "Drone Shipping"
print("Therefore, we recommend " + choice + "!")