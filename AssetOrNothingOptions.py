# Derived Class from European Options
from Options import Options, OptionType
import GlobalFunctions as GF
import math
from EuropeanOptions import EuropeanOptions


class AssetOrNothing(EuropeanOptions):

    def __init__(self, S, K, r, T, vol, option_type: OptionType):
        super().__init__(S, K, r, T, vol, option_type)

    # Abstract Method for Option Price
    # Implemented in the Derived Class
    def OptionPrice(self):
        d1 = Options.d1(self.S, self.K, self.r, self.vol, self.T)
        if self.option_type == OptionType.Call:
            option_price = self.S * GF.N(d1)
        else:
            option_price = self.S * GF.N(-d1)
        return option_price

    def PutCallParityPrice(self):
        option_price = self.S - self.OptionPrice()
        return option_price

    # Abstract Methods for Option Greeks
    # Implemented in the Derived Class
    def Delta(self):
        d1 = Options.d1(self.S, self.K, self.r, self.vol, self.T)
        part_a = GF.n(d1) / (self.vol * math.sqrt(self.T))

        if self.option_type == OptionType.Call:
            delta = part_a + GF.N(d1)
        else:
            delta = -part_a + GF.N(-d1)
        return delta

    def Gamma(self):
        d1 = Options.d1(self.S, self.K, self.r, self.vol, self.T)
        d2 = Options.d2(self.S, self.K, self.r, self.vol, self.T)
        numerator = GF.n(d1) * d2
        denominator = self.S * (self.vol**2) * self.T
        if self.option_type == OptionType.Call:
            gamma = -numerator/denominator
        else:
            gamma = numerator / denominator
        return gamma

    def Vega(self):
        d1 = Options.d1(self.S, self.K, self.r, self.vol, self.T)
        d2 = Options.d2(self.S, self.K, self.r, self.vol, self.T)
        if self.option_type == OptionType.Call:
            vega = -self.S * d2 * GF.n(d1) /self.vol
        else:
            vega = self.S * d2 * GF.n(d1) / self.vol
        return vega

    def Rho(self):
        d1 = Options.d1(self.S, self.K, self.r, self.vol, self.T)
        if self.option_type == OptionType.Call:
            rho = self.S * math.sqrt(self.T) * GF.n(d1) / self.vol
        else:
            rho = -self.S * math.sqrt(self.T) * GF.n(d1) / self.vol
        return rho

    def Theta(self):
        d1 = Options.d1(self.S, self.K, self.r, self.vol, self.T)
        numerator = (math.log(self.K/self.S)/self.T) + (self.r + (self.vol*self.vol)/2)
        denominator =  2*self.vol*math.sqrt(self.T)
        partial_d1_with_T = numerator/denominator
        if self.option_type == OptionType.Call:
            theta = -self.S * GF.n(d1) * partial_d1_with_T
        else:
            theta = self.S * GF.n(d1) * partial_d1_with_T
        return theta
