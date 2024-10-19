# 6. Calculate simple interest
def simple_interest():
    principal = float(input("Enter the principal amount: "))
    rate_of_interest = float(input("Enter the rate of interest: "))
    time_period = float(input("Enter the time period (in years): "))
    
    interest = (principal * rate_of_interest * time_period) / 100
    print(f"Simple Interest: {interest}")

simple_interest()