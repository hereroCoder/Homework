#greet customer in and show items
def welcoming_customer(items):
  print("Welcome to Wame Retail")
  for item in items:
      print("{}: £{}".format(item, items[item]))


def can_afford(price, customer_money):
  if price <= customer_money:
    return True
  return False


def buying_if_has_extra_money(customer_money,option,price):

  extra_money = input(
      "Sorry you cant afford that. Do you have extra money? y/n ")
  if extra_money == "y":
      money = int(input("How much? "))
      customer_money += money
      #check if the customer can now afford item
      if can_afford(price, customer_money):
          print("Here is your {}!".format(option))
          print("press e to exit")
          return

      print("Still not enough. {} cost  £{} and you have  £{}".format(
          option, price, customer_money))
      print("lets try to get you an item again")

  elif extra_money == "n":
      print("Ok no problem, you can try to buy a different item")
  else:
      print("That was an invalid input. You had to select y or n")


class NoEnoughIncomeError (Exception):
  # When the customer money is less than item price
  pass


def shopping_attempts(items,customer_money,attempt):
  while attempt < 3:

    option = input("press e to exit or enter the item name: ")

    if option == "e":
        print("Leaving soo soon.")
        return

    elif option in items:
        if can_afford(items[option], customer_money):
            print("Here is your {}!".format(option))
            return
        else:
          buying_if_has_extra_money(customer_money, option, items[option])

    else:
      # if option is invalid
      raise ValueError(
          "Was expecting e for exit or name of item available")
    attempt += 1
  else:
    raise NoEnoughIncomeError("Failed to purchase after 3 trials") #custom error after 3 times



def purchasing():
 
  try:
    items = {
        "shirt": 19.99,
        "jean": 21.80,
        "sneakers": 200,
        "cap": 9.50
    }
    customer_money = 100
    attempt= 0

    welcoming_customer(items)
    shopping_attempts(items, customer_money,attempt)
   
  except ValueError as exc:
    print("Invalid input: {}".format(exc))

  except NoEnoughIncomeError as exc:
    print("Couldn't get the item {}".format(exc))

  except:
    print("Something else went wrong")

  finally:
    print("Bye, hope to see you soon.")

# to be commented out to run the shop.py
# def main():
#   purchasing()

# if __name__ == main():
#    main()