from Options import OptionType
from EuropeanOptions import EuropeanOptions as E

if __name__ == '__main__':
    Euro1 = E(100, 105, 0.01, 3, 0.05, OptionType.Call)
    for i in range (0, 2):
        EuroOptionType = Euro1.option_type.name
        print(f"{EuroOptionType} Option Price: {Euro1.OptionPrice(): .6f}")
        list_methods = ['Delta', 'Gamma', 'Vega', 'Theta', 'Rho']
        print(f"{EuroOptionType} Option Greeks")
        for method in list_methods:
            option_greek = getattr(Euro1, method)()
            print(f"{method}: {option_greek: .4f}")
        if EuroOptionType == "Call":
            EuroOptionType = "Put"
        elif EuroOptionType == "Put":
            EuroOptionType = "Call"
        print(f"\nPrices Using Put Call Parity")
        print(f"{EuroOptionType} Option Price: {Euro1.PutCallParityPrice(): .6f} \n")
        Euro1.ToggleOption()
