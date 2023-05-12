def calculate_interest_rate2(amount: int, year: int):
    years_count = 1
    while years_count <= year:
        compound_interest = amount * (1 + 0.05) ** years_count
        print(f"Year {years_count} the total return is {compound_interest:,.2f} ")
        years_count += 1


amount = int(input("Enter your amount: \n"))
year = int(input("Enter the number of years: \n"))

calculate_interest_rate2(amount, year)
