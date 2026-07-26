def future_value(current_value, growth_rate, years):
    # Base case
    if years == 0:
        return current_value

    # Recursive case
    return future_value(current_value * (1 + growth_rate), growth_rate, years - 1)


# User Input
current_value = float(input("Enter current value: $"))
growth_rate = float(input("Enter annual growth rate (%): ")) / 100
years = int(input("Enter number of years: "))

# Calculate Future Value
predicted_value = future_value(current_value, growth_rate, years)

print(f"\nPredicted Future Value after {years} years: ${predicted_value:.2f}")