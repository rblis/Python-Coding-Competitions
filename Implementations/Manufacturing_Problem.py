'''
Manufacturing Problem
Programming challenge description:
Background

You are working for a manufacturing company, and are trying to make your product as cheaply as possible. Let's say you're making teddy bears. You can potentially buy painted glass eyeballs, tiny shirts, fake bear cloth, and sewing thread, and put them all together in your factory to produce the teddy bear. But to save money, maybe you can build the painted glass eyeballs yourself by buying glass and paint. And so on and so forth. You could even build your own paint if it's cheaper than purchasing paint directly! Your goal is to figure out the cheapest way to make your product. There are no costs associated with combining inputs into a product. The first part of the input will be the product you are trying to obtain (the "target product"). The second part will be data representing how to build and/or purchase various products. Your code should output the cheapest way to obtain the target product (either via building it yourself or purchasing it).
Input Description

    A target product (target_product)
    For each Product:
        The name of the product (product_name)
        The price to purchase the product directly (price_to_purchase)
        The number of materials required as inputs to build the product (input_products_size)
        A list of materials required as inputs to build the product (input_products)

If price_to_purchase is null, it is impossible to purchase that product. If input_products is empty, it is impossible to build that product

These inputs will be formatted like this:

<target_product>
<product_name>,<price_to_purchase>,<input_products_size>,<input_products>
<product_name>,<price_to_purchase>,<input_products_size>,<input_products>
<product_name>,<price_to_purchase>,<input_products_size>,<input_products>
<product_name>,<price_to_purchase>,<input_products_size>,<input_products>

Example

teddy bear
painted glass eyeball,10.5,2,glass;paint
glass,5,0,
paint,4,0,
teddy bear,null,4,painted glass eyeball;tiny shirt;faux bear fur fabric;sewing thread
faux bear fur fabric,15,2,bear;yarn
bear,100,0,
yarn,2,0,
sewing thread,13,0,
tiny shirt,24,0,

In the above example, we are making teddy bears, since that is in the first row of the input. Teddy bears are not able to be purchased on the market ("null" in the second column of the input), thus you'll have to build the teddy bear yourself.

It is cheaper to build the "painted glass eyeball" yourself out of glass and paint, instead of purchasing the eyeballs ($5 + $4 < $10.5). However, it is cheaper to purchase the "faux bear fur fabric", rather than make it yourself out of bear and yarn ($15 < $100 + $2). Since the list of inputs is empty for sewing threads and tiny shirts, that means they must be purchased for $13 and $24, repectively. So the cheapest price to produce teddy bears would be calculated below:

  5  (glass)
+ 4  (paint)
+ 15 (faux bear fur fabric)
+ 24 (tiny shirt)
+ 13 (sewing thread)
--------
 $61

To format this properly, you should write 61.00 to stdout.
Notes

    The target product will always be possible to build and/or purchase
    There are no "cycles" of inputs. For example, it would never be the case that product A is an input to product B, but product B is also an input to product A
    Some products are "raw inputs", and are unable to be produced. They must be purchased. They have an empty list of input products (in the above example, bear, yarn, sewing thread, and tiny shirt are all "raw inputs")
    Since the output is simply the cheapest price to produce the target product, it does not matter if there is a tie between the price to purchase the target product and the price to produce it
    It is possible to for a product to be an input to multiple other products
    If a product is in input_products, it is guaranteed to be listed as a product

Input:

    A target product
    For each Product:
        The name of the product
        The price to purchase the product directly
        The number of products required as inputs to build the product
        A list of products required as inputs to build the product

teddy bear
painted glass eyeball,10.5,2,glass;paint
glass,5,0,
paint,4,0,
teddy bear,null,4,painted glass eyeball;tiny shirt;faux bear fur fabric;sewing thread
faux bear fur fabric,15,2,bear;yarn
bear,100,0,
yarn,2,0,
sewing thread,13,0,
tiny shirt,24,0,

NOTE: You have been given skeleton code to help parse this input. You may alter this code as you wish, including not using it at all.
Output:

A number, formatted with two decimal places, that is the cheapest possible price to manufacture the target product

61.00
Test 1
Test Input
car
car,30000,5,seat;steering wheel;carpet;windshield;radio
radio,200,0,
steering wheel,null,3,leather;plastic;foam
seat,null,3,leather;foam;plastic
plastic,1300,0,
foam,7000,0,
leather,4000,0,
carpet,1000,1,plastic
windshield,5000,1,glass
glass,2000,1,sand
sand,0,0,
Expected Output
25800.00
Test 2
Test Input
office chair
wheels,3.5,2,plastic;metal
cushioned seat,7.5,3,screws;padding;leather
screws,1.5,1,metal
arm rests,5,3,padding;plastic;leather
lumbar support,15,4,plastic;padding;leather;screws
plastic,2,0,
padding,3,0,
leather,4,0,
metal,1,0,
office chair,26.25,5,wheels;cushioned seat;screws;arm rests;lumbar support
Expected Output
26.25
Test 3
Test Input
sandwich
mayonnaise,1,0,
sand,0,0,
bread,3,3,yeast;water;flour
flour,1,0,
water,1,0,
yeast,1,0,
sandwich,10,6,mayonnaise;sand;bread;mozzarella;bacon;salt
bacon,3,1,pig
pig,1000,0,
salt,1,2,sea salt;iodine
iodine,40,0,
sea salt,.5,0,
mozzarella,3,0,
Expected Output
10.00
Test 4
Test Input
teddy bear
painted glass eyeball,10.5,2,glass;paint
glass,5,0,
paint,4,0,
teddy bear,null,4,painted glass eyeball;tiny shirt;faux bear fur fabric;sewing thread
faux bear fur fabric,15,2,bear;yarn
bear,100,0,
yarn,2,0,
sewing thread,13,0,
tiny shirt,24,0,
Expected Output
61.00
'''