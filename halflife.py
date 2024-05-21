def halflife(initial_quantity, decay_rate):
    half_life = 0
    if decay_rate <= 0:
        print("Decay rate should be positive.")
    else:
        half_life = 0.693 / decay_rate
    return half_life

# Example usage:
initial_quantity = float(input("Enter the initial quantity of the substance: "))
decay_rate = float(input("Enter the decay rate of the substance: "))

hl = calculate_halflife(initial_quantity, decay_rate)
if hl != 0:
    print("The half-life of the substance is:", hl)
