"""

Geometric Brownian Motion (GBM)
dX(t) = mu * X(t)dt + sigma * X(t) * dW(t)
X(t) = log ( S(t) )
S(t) = exp ( X(t) )

S(t+1) =

mu : long term mean
sigma > 0 : volatility coefficient
S(t) is the Stock Price


Ornstein-Uhlenbeck mean reverting processes (OU)
dX(t) = k ( theta - X(t) ) dt + sigma * dW(t);

The parameters are:

k > 0       : mean reversion coefficient
theta E R   : long term mean
sigma > 0   : volatility coefficient
and W(t) is a Wiener

"""