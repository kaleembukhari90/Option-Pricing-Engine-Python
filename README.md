# Option Pricing Engine
Disclaimer: This repository is not intended to be a financial advisory or actionable tool. It is purely a programming project for Financial Engineering.

This repository contains Python code for an Option Pricing Engine. The Engine is designed to price Plain-Vanilla European Options using the Black-Scholes Formula and Binary Options (Asset or Nothing and Cash or Nothing). The repository also contains codes for Option Greeks.

## European Options
The code contains implementation for the Exact Formula for Black-Scholes Model along with the fundamental Option Greeks namely Delta, Gamma, Vega, Theta, and Rho. Moreover, a pricing mechanism using Put-Call Parity has also been setup.

Call Option Formula:

$$C = S_0N(d_1) - Ke^{-rT}N(d_2)$$

Put Option Formula:

$$P = Ke^{-rT}N(-d_2) - S_0N(-d_1)$$

### Option Greeks
<b> Note </b>: Formulae given below are just for Call Options.

$$Delta (\Delta C) = \frac{\partial C}{\partial S} = N(d_1)$$
$$ Gamma(\Gamma C) = \frac{\partial^2 C}{\partial S^2} = \frac{\partial \Delta C}{\partial S} = \frac{n(d_1)}{S_0 \sigma \sqrt{T}}$$
$$Vega C = \frac{\partial C}{\partial \sigma} = S_0\sqrt{T}n(d_1)$$
$$Rho(\rho C) = \frac{\partial C}{\partial r} = Ke^{-rT}TN(d_2)$$
$$Theta(\theta C) = \frac{\partial C}{\partial T} = S_0rN(d_1) - Ke^{-rT}rN(d2) - S_0\frac{\sigma}{2\sqrt T}n(d_1)$$


## Binary Options
### Asset or Nothing (AON)
The code contains implementation of the Exact Formula for pricing Asset or Nothing Call and Put Options.

Call Option Formula:
$$C_{AON} = S_0N(d_1)$$

Put Option Formula:
$$P_{AON} = S_0N(-d_1)$$


### AON Option Greeks
<b> Note </b>: Formulae given below are just for Call Options.

$$Delta (\Delta C_{AON}) = \frac{\partial C}{\partial S} = \frac{n(d_1)}{\sigma \sqrt T} + N(d_1)$$
$$Gamma(\Gamma C_{AON}) = \frac{\partial^2 C}{\partial S^2} = \frac{\partial \Delta C}{\partial S} = -\frac{n(d_1)d_2}{S_0\sigma^2T}$$
$$Vega (C_{AON}) = \frac{\partial C}{\partial \sigma} = -\frac{S_0d_2n(d_1)}{\sigma}$$
$$Rho(\rho C_{AON}) = \frac{\partial C}{\partial r} = \frac{S_0\sqrt T n(d_1)}{\sigma}$$
$$Theta(\theta C_{AON}) = \frac{\partial C}{\partial T} = S_0rN(d_1) - Ke^{-rT}rN(d2) - S_0\frac{\sigma}{2\sqrt T}n(d_1)$$


### Cash or Nothing (CON)
The code contains implementation of the Exact Formula for pricing Cash or Nothing Call and Put Options.

Call Option Formula:
$$C_{CON} = e^{-rT}N(d_2)$$

Put Option Formula:
$$P_{CON} = e^{-rT}N(-d_2)$$


### CON Option Greeks
<b> Note </b>: Formulae given below are just for Call Options.

$$Delta (\Delta C_{CON}) = \frac{\partial C}{\partial S} = \frac{e^{-rT}n(d_2)}{S_0\sigma \sqrt T}$$
$$Gamma(\Gamma C_{CON}) = \frac{\partial^2 C}{\partial S^2} = \frac{\partial \Delta C}{\partial S} = -\frac{e^{-rT}n(d_2)d_1}{S_0^2\sigma^2T}$$
$$Vega (C_{CON}) = \frac{\partial C}{\partial \sigma} = -\frac{e^{-rT}d_1n(d_2)}{\sigma}$$
$$Rho(\rho C_{CON}) = \frac{\partial C}{\partial r} = e^{-rT}\left(\frac{\sqrt T n(d_2)}{\sigma} - TN(d_2)\right)$$
$$Theta(\theta C_{CON}) = \frac{\partial C}{\partial T} = -re^{-rT}N(d_2) + e^{-rT}n(d_2)\frac{\partial d_2}{\partial T}$$


### General Notations for Plain Vanilla European and Binary Options

$N(x)$ = Cummulative Distribution Function (CDF) of a Standard Normal Random Variable

$n(x)$ = Probability Density Function (PDF) of a Standard Normal Random Variable

$$N(x) = \frac{1}{\sqrt{2\pi}} \int_{-\infty}^{x} e^{-x^2/2} \, dx$$

$$n(x) = \frac{dN(x)}{dx} = \frac{1}{\sqrt{2\pi}} e^{-\frac{x^2}{2}}$$

$$d_1 = \frac{\ln(S/K) + (r+\frac{\sigma^2}{2})T}{\sigma \sqrt{T}}$$

$$d_2 = \frac{\ln(S/K) + (r-\frac{\sigma^2}{2})T}{\sigma \sqrt{T}}$$

#### Option Paramters in use
$S_0$ = Asset Price at Time Zero

$K$ = Strike

$T$ = Time to Expiry

$r$ = Risk-Free Rate

$\sigma$ = Volatility (Constant)

$AON$ = Asset or Nothing Option

$CON$ = Cash or Nothing Option