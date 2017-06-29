print 'Restaurant Search System'

# restaurant dictionary
restaurant_dict = {
    'Pizza Hut': {
        'Owner': 'Dan and Frank Carney',
        'Restaurant Rating': '4.1/5',
        'Food List': {
            'Veggie Supreme': 490,
            'Chicken Supreme': 570,
            'Tandoori Paneer': 460,
            'Chicken Tikka': 490,
            'Double Cheese': 370,
            'Chicken N Spicy': 460,
            'Margherita': 250,
            'Paneer Overloaded': 269,
            'Spicy Chicken Overloaded': 299
        }
    },
    "Domino's": {
        'Owner': 'Tom Monaghan',
        'Restaurant Rating': '4.3/5',
        'Food List': {
            'Chicken Fajita': 390,
            'Margherita': 420,
            'Cheese & Tomato': 290,
            'Cheese & Bbq Chicken': 430,
            'Chicken Fiest': 380,
            'Spicy Chicken': 475,
            'Keema do Pyaaza': 510,
            'Zesty Chicken ': 510,
            'Non Veg Extravaganza': 575,
            'Meatzaa': 575
        }
    },
    "McDonald's": {
        'Owner': 'Ray Kroc',
        'Restaurant Rating': '4.0/5',
        'Food List': {
            'McAloo Tikki': 109,
            'Chicken McGrill': 119,
            'McAloo Wrap with Chipotle Sauce': 132,
            'Grill Chicken Wrap with Chipotle Sauce ': 150,
            'Filet-O-Fish': 189,
            'Chicken Maharaja Mac': 204,
            'Chicken McNuggets': 265,
            'Big Spicy Chicken Wrap': 244,
            'Grilled Chicken Royale': 231,
            'Hot Cakes (with Syrup & Butter) ': 114
        }
    },
    'KFC': {
        'Owner': ' Colonel Harland Sanders',
        'Restaurant Rating': '4.7/5',
        'Food List': {
            'Smoky Grilled or Hot and Crispy': 295,
            'Duo Bucket Meal': 399,
            'Zinger Delux': 230,
            'Cheezy Crunch': 154,
            "Chicken Rockin'": 160,
            'Veg Zinger': 174,
            'Chicken Zinger': 194,
            'Mingles Bucket': 199,
            'Longer': 120,
            'Rice Bowlz': 159
        }
    }
}

print 'Please Select From The Following \n1. Restaurant Owner. \n2. Customer.'

selection = raw_input ('Enter Your Choice: \n')
if selection == '1':

    # Owner panel

    print 'Do You Want to Update any Information: \n1. Yes! \n2. No!'
    update_info = raw_input ('Enter Your Choice: \n')
    if update_info == '2':
        print 'Thanks! Good Luck'
    elif update_info == '1':
        print 'What You Want to Update? \n1. Add Item. \n2. Delete Item. \n3. Price Change. \n4. Exit'
        update_what = raw_input ('Enter Your Choice!\n')
        if update_what == '4':
            print 'You Choose to Exit, Thanks!'
        # Adding New Item to Menu with its Price
        elif update_what == '1':
            restaurant_name = raw_input ('Enter Your Restaurant Name \n')
            enter_food_name = raw_input ('Enter Item Name: \n')
            if enter_food_name in (restaurant_dict[restaurant_name]['Food List'].keys ()):
                print enter_food_name + ' Already Present in the Menu'
            else:
                food_price = int (raw_input ('Enter the Price of ' + enter_food_name + ' in INR\n'))
                restaurant_dict[restaurant_name]['Food List'][enter_food_name] = food_price
                print 'Food Item ' + enter_food_name + ' Added to Menu'
                # print restaurant_dict[restaurant_name]['Food List']
        elif update_what == '2':
            restaurant_name = raw_input ('Enter Restaurant Name\n')
            # deleting item from existing menu
            delete_item = raw_input ('Enter Item Name to be Deleted\n')
            del restaurant_dict[restaurant_name]['Food List'][delete_item]
            print delete_item + ' Deleted from Menu'
            # print restaurant_dict[restaurant_name]['Food List']
        elif update_what == '3':
            restaurant_name = raw_input ('Enter Restaurant Name\n')
            # changing price of any item in menu
            change_price_item = raw_input ('Enter Item whose Price you want to change\n')
            new_price = int (raw_input ('Enter new price of the ' + change_price_item + ' in INR \n'))
            restaurant_dict[restaurant_name]['Food List'][change_price_item] = new_price
            print change_price_item + ' Price changed '
            print  restaurant_dict[restaurant_name]['Food List']

if selection == '2':
    print '\nRestaurant List:'

    # Customer panel

    index = 0
    for restaurant_name in restaurant_dict.keys ():
        print str (index + 1) + ". " + restaurant_name
        index += 1

    customer_choice = raw_input (
        '\nSelect from the following \n1. Order Food. \n2. Rate a Restaurant \n3. Exit \nEnter your choice\n')
    if customer_choice == '3':
        print 'You choose to Exit. Thank You'
    elif customer_choice == '2':
        print '\nPlease select a restaurant from the following:'
        index = 0
        for restaurant_name in restaurant_dict.keys ():
            print str (index + 1) + ". " + restaurant_name
            index += 1
        restaurant_choice = raw_input ('Your Choice:\n')
        if restaurant_choice == '1' or '2' or '3' or '4':
            print 'Rate the Chosen Restaurant'
            rate = raw_input ('Enter rating between 0-10\n')
            print 'You rated ' + rate + ' stars'
    elif customer_choice == '1':
        print '\nChoose the Restaurant of your choice:'
        index = 0
        for restaurant_name in restaurant_dict.keys ():
            print str (index + 1) + ". " + restaurant_name
            index += 1
        restaurant_choice = raw_input ('Your Choice:\n')
        if restaurant_choice == '1' or '2' or '3' or '4':
            delivery_order = raw_input ('What you want to:\n1. Home Delivery \n2. Walk In\n')
            if delivery_order == '1':
                print 'You Choose Home Delivery\n'
                order_food = raw_input ('Enter Food Item\n')
                if (order_food in restaurant_dict[restaurant_name]['Food List']) == True:
                    print 'Order Placed'
                    bill = (restaurant_dict[restaurant_name]['Food List'][order_food])*2.1
                    print 'Your Total bill is ' + str(bill)
                else:
                    print 'Food Item not Found, Order Something Else'
            elif delivery_order == '2':
                print 'You Choose Walk In\n'
                order_food = raw_input ('Enter Food Item\n')
                if (order_food in restaurant_dict[restaurant_name]['Food List']) == True:
                    print 'Order Placed'
                    bill = (restaurant_dict[restaurant_name]['Food List'][order_food]) * 2.1
                    print 'Your Total bill is ' + str (bill)
                else:
                    print 'Food Item not Found, Order Something Else'