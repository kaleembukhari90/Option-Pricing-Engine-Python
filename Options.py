# Abstract Base Class for Options
# All specific Options Classes:
# 1. Plan Vanilla European Options
# 2. Digital European Options

from abc import ABC, abstractmethod
from enum import Enum
import GlobalFunctions as GF
import math

class OptionType(Enum):
    Call = 1
    Put = 2

class Options(ABC):

    # Initializing private data members
    def __init__(self, S, K, r, vol, option_type: OptionType):
        self.__S = S        # Stock Price at time Zero
        self.__K = K        # Strike Price
        self.__r = r        # Risk Free Rate
        self.__vol = vol    # Volatility
        self.__option_type = option_type    # Option Type: Call or Put

    # Getter for Stock Price
    @property
    def S(self):
        return self.__S
    # Setter for Stock Price
    @S.setter
    def S(self, S_new):
        self.__S = S_new

    # Getter for Strike
    @property
    def K(self):
        return self.__K
    # Setter for Strike
    @K.setter
    def K(self, K_new):
        self.__K = K_new

    # Getter for Risk Free Rate
    @property
    def r(self):
        return self.__r
    # Setter for Risk Free Rate
    @r.setter
    def r(self, r_new):
        self.__r = r_new

    # Getter for Volatility
    @property
    def vol(self):
        return self.__vol

    # Setter for Volatility
    @vol.setter
    def vol(self, vol_new):
        self.__vol = vol_new

    # Getter for Option Type
    @property
    def option_type(self):
        return self.__option_type

    # Setter for Option Type
    @option_type.setter
    def option_type (self, optionType_new):
        self.__option_type = optionType_new

    # Static Method to compute the value for d1
    @staticmethod
    def d1(S, K, r, vol, T):
        numerator = math.log(S/K) + (r + (vol**2)/2)*T
        denominator = vol*math.sqrt(T)
        return numerator/denominator

    # Static Method to compute the value for d2
    @staticmethod
    def d2(S, K, r, vol, T):
        return Options.d1(S, K, r, vol, T) - (vol * math.sqrt(T))

    # Abstract Method to Toggle between Options
    # Change Call to Put and Put to Call
    # Implemented in the Derived Class
    @abstractmethod
    def ToggleOption(self):
        pass

    # Abstract Method for Option Price
    # Implemented in the Derived Class
    @abstractmethod
    def OptionPrice(self):
        pass

    # Abstract Method for Option Price using Put Call Parity
    # Implemented in the Derived Class
    @abstractmethod
    def PutCallParityPrice(self):
        pass

    # Abstract Methods for Option Greeks
    # Implemented in the Derived Class
    @abstractmethod
    def Delta(self):
        pass

    @abstractmethod
    def Gamma(self):
        pass

    @abstractmethod
    def Vega(self):
        pass

    @abstractmethod
    def Rho(self):
        pass

    @abstractmethod
    def Theta(self):
        pass
