def halflife(initial_quantity, decay_rate):
    half_life = 0
    if decay_rate <= 0:
        print("Decay rate should be positive.")
    else:
        half_life = 0.693 / decay_rate
    return half_life

def hldo():
    initial_quantity = float(input("Enter the initial quantity of the substance: "))
    decay_rate = float(input("Enter the decay rate of the substance: "))

    hl = halflife(initial_quantity, decay_rate)
    if hl != 0:
        print("The half-life of the substance is:", hl)
##comment from kole: why does this smell like chatGPT... the "#example usage" was a dead givaway
##also, it did not use a function properly, and overrode the mainline code with itself at execution time     it also called a non-existant function
##anyways, i made it work

## please do not use chatGTP. it's code is hard to maintain/implement