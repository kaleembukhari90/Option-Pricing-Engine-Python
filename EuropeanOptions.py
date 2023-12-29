# Derived Class for Plain Vanilla European Call Options

from Options import Options, OptionType
import GlobalFunctions as GF
import math

class EuropeanOptions(Options):

    # Initializing Private Data Members and Calling the Constructor for the Base Class
    def __init__(self, S, K, r, T, vol, option_type: OptionType):
        super().__init__(S, K, r, vol, option_type)
        self.__T = T    # Time to Expiry

    # Getter for Time to Expiry
    @property
    def T(self):
        return self.__T
    # Setter for Time to Expiry
    @T.setter
    def T(self, T_new):
        self.__T = T_new

    # Method to Toggle between Options
    # Change Call to Put and Put to Call
    def ToggleOption(self):
        if self.option_type == OptionType.Call:
            self.option_type = OptionType.Put
        else:
            self.option_type = OptionType.Call

    # Abstract Method for Option Price
    # Implemented in the Derived Class
    def OptionPrice(self):
        d1 = Options.d1(self.S, self.K, self.r, self.vol, self.T)
        d2 = Options.d2(self.S, self.K, self.r, self.vol, self.T)
        if self.option_type == OptionType.Call:
            option_price = self.S * GF.N(d1) - self.K * math.exp(-self.r * self.T) * GF.N(d2)
        else:
            option_price = self.K * math.exp(-self.r * self.T) * GF.N(-d2) - self.S * GF.N(-d1)
        return option_price

    def PutCallParityPrice(self):
        if self.option_type == OptionType.Call:
            option_price = self.OptionPrice() + self.K * math.exp(-self.r * self.T) - self.S
        else:
            option_price = self.OptionPrice() + self.S - self.K * math.exp(-self.r * self.T)
        return option_price

    # Abstract Methods for Option Greeks
    # Implemented in the Derived Class
    def Delta(self):
        d1 = Options.d1(self.S, self.K, self.r, self.vol, self.T)
        if self.option_type == OptionType.Call:
            delta = GF.N(d1)
        else:
            delta = -GF.N(-d1)
        return delta

    def Gamma(self):
        d1 = Options.d1(self.S, self.K, self.r, self.vol, self.T)
        numerator = GF.n(d1)
        denominator = self.S * self.vol * math.sqrt(self.T)
        gamma = numerator/denominator
        return gamma

    def Vega(self):
        d1 = Options.d1(self.S, self.K, self.r, self.vol, self.T)
        vega = self.S * math.sqrt(self.T) * GF.n(d1)
        return vega

    def Rho(self):
        d2 = Options.d2(self.S, self.K, self.r, self.vol, self.T)
        if self.option_type == OptionType.Call:
            rho = self.K * math.exp(-self.r * self.T) * self.T * GF.N(d2)
        else:
            rho = -self.K * math.exp(-self.r * self.T) * self.T * GF.N(-d2)
        return rho

    def Theta(self):
        d1 = Options.d1(self.S, self.K, self.r, self.vol, self.T)
        d2 = Options.d2(self.S, self.K, self.r, self.vol, self.T)
        if self.option_type == OptionType.Call:
            theta = (-self.S * GF.n(d1) * self.vol)/(2 * math.sqrt(self.T)) - self.r * self.K * math.exp(-self.r * self.T) * GF.N(d2)
        else:
            theta = (-self.S * GF.n(d1) * self.vol) / (2 * math.sqrt(self.T)) + self.r * self.K * math.exp(-self.r * self.T) * GF.N(-d2)
        return theta
