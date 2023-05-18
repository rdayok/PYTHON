def calculate_interest_rate2(amount: int, inputted_years: int):
    try:
        inputted_years += 1
        for years in range(1, inputted_years):
            compound_interest = amount * (1 + 0.05) ** years
            print(f"Year {years} total capital and interest of {compound_interest:,.2f} ")
    except ValueError:
        return f"u dey mad, put number jareh"


amount = int(input("Enter your amount: \n"))
inputted_years = int(input("Enter the number of years: \n"))
calculate_interest_rate2(amount, inputted_years)
