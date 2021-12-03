

# def run_metrics():


def cashflow(price, rent_income):
    percent = rent_income/price*100
    if percent >= 1:
        return True


def main():
    price = int(input("Enter property purchase price: "))
    rent_income = int(input("Enter total rental income: "))
    if cashflow(price, rent_income):
        print("This property will cash flow")
    else:
        print("This property will not cash flow")


main()
