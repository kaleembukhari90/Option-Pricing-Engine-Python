# Derived Class from European Options
from Options import Options, OptionType
import GlobalFunctions as GF
import math
from EuropeanOptions import EuropeanOptions


class CashOrNothing(EuropeanOptions):

    def __init__(self, S, K, r, T, vol, option_type: OptionType):
        super().__init__(S, K, r, T, vol, option_type)

    # Abstract Method for Option Price
    # Implemented in the Derived Class
    def OptionPrice(self):
        d2 = Options.d2(self.S, self.K, self.r, self.vol, self.T)
        if self.option_type == OptionType.Call:
            option_price = math.exp(-self.r * self.T) * GF.N(d2)
        else:
            option_price = math.exp(-self.r * self.T) * GF.N(-d2)
        return option_price

    def PutCallParityPrice(self):
        option_price = math.exp(-self.r * self.T) - self.OptionPrice()
        return option_price

    # Abstract Methods for Option Greeks
    # Implemented in the Derived Class
    def Delta(self):
        d2 = Options.d2(self.S, self.K, self.r, self.vol, self.T)

        if self.option_type == OptionType.Call:
            delta = math.exp(-self.r * self.T) * GF.n(d2) / (self.S * self.vol * math.sqrt(self.T))
        else:
            delta = -math.exp(-self.r * self.T) * GF.n(d2) / (self.S * self.vol * math.sqrt(self.T))
        return delta

    def Gamma(self):
        d1 = Options.d1(self.S, self.K, self.r, self.vol, self.T)
        d2 = Options.d2(self.S, self.K, self.r, self.vol, self.T)
        numerator = GF.n(d2) * d1
        denominator = self.S**2 * (self.vol**2) * self.T
        if self.option_type == OptionType.Call:
            gamma = -numerator/denominator
        else:
            gamma = numerator / denominator
        return gamma

    def Vega(self):
        d1 = Options.d1(self.S, self.K, self.r, self.vol, self.T)
        d2 = Options.d2(self.S, self.K, self.r, self.vol, self.T)
        if self.option_type == OptionType.Call:
            vega = -math.exp(-self.r * self.T) * d1 * GF.n(d2) /self.vol
        else:
            vega = math.exp(-self.r * self.T) * d1 * GF.n(d2) /self.vol
        return vega

    def Rho(self):
        d2 = Options.d2(self.S, self.K, self.r, self.vol, self.T)
        if self.option_type == OptionType.Call:
            rho = math.exp(-self.r * self.T) * ((math.sqrt(self.T) * GF.n(d2) / self.vol) - (self.T * GF.N(d2)))
        else:
            rho = math.exp(-self.r * self.T) * ((-math.sqrt(self.T) * GF.n(d2) / self.vol) - (self.T * GF.N(-d2)))
        return rho

    def Theta(self):
        d2 = Options.d2(self.S, self.K, self.r, self.vol, self.T)

        numerator = (math.log(self.K/self.S)/self.T) + (self.r - (self.vol*self.vol)/2)
        denominator =  2 * self.vol * math.sqrt(self.T)
        partial_d2_with_T = numerator/denominator

        part_a = -self.r * math.exp(-self.r*self.T) * GF.N(d2)
        part_b = math.exp(-self.r * self.T) * GF.n(d2) * partial_d2_with_T

        if self.option_type == OptionType.Call:
            theta = -(part_a + part_b)
        else:
            theta = self.r * math.exp(-self.r * self.T) + part_a + part_b
        return theta
