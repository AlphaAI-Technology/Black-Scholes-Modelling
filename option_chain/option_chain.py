from scipy.stats import norm
import numpy


def option_chain(S=100.00, K=120.00, T=7, sigma=0.50, r=0.05):
    """Calculate the d1 component of the Black-Scholes PDE.

        :param S: Underlying Asset / Stock Price
        :type S: float
        :param K: Strike Price
        :type K: float
        :param T: time to expiration in days
        :type T: float
        :param sigma: Annualized Standard Deviation, or Volatility i.e. 50% is 0.50, or 30% is 0.30
        :type sigma: float
        :param r: risk-free interest rate
        :type r: float

        John C. Hull, "Options, Futures and Other Derivatives," 9th edition, Example 15.6, page 338

        Example : The stock price 6 months from the expiration of an option is $42, the exercise price
        of the option is $40, the risk-free interest rate is 10% per annum, and the volatility
        is 20% per annum. This means that S = 42, K = 40, r = 0.10, r = 0:2, T = 0.50

        S = 42
        K = 40
        r = .10
        sigma = .20
        t = 0.5
        calculated_d1 = _d1(S,K,t,r,sigma)
        text_book_d1 = 0.7693
        abs(calculated_d1 - text_book_d1) < 0.0001
        True
        """
    t = T / 365  # Converting the number of Days to Years

    d1 = (numpy.log(S / K) + (r + (sigma ** 2) / 2) * t) / (sigma * numpy.sqrt(t))
    """
        calculated_d1 = _d1(S,K,t,r,sigma)
        text_book_d1 = 0.7693
        abs(calculated_d1 - text_book_d1) < 0.0001
    """
    d2 = d1 - sigma * numpy.sqrt(t)

    """
    calculated_d2 = _d2(S,K,t,r,sigma) #0.627841271869
    text_book_d2 = 0.6278
    abs(calculated_d2 - text_book_d2) < 0.0001
    """

    call = S * norm.cdf(d1, 0, 1) - K * numpy.exp(-r * t) * norm.cdf(d2, 0, 1)

    """
    calculated_call = black_scholes('c', S, K, t, r, sigma)
    text_book_call = 4.76
    abs(calculated_call - text_book_call) < 0.01
    """

    put = - S * norm.cdf(-d1, 0, 1) + K * numpy.exp(-r * t) * norm.cdf(-d2, 0, 1)

    """
    calculated_put = black_scholes('p', S, K, t, r, sigma)
    text_book_put = 0.81
    abs(calculated_put - text_book_put) < 0.01
    """

    # Delta Computation
    put_delta = norm.cdf(d1) - 1.0
    call_delta = norm.cdf(d1)

    two_sqrt_t = 2 * numpy.sqrt(t)
    first_term = (-S * norm.pdf(d1) * sigma) / two_sqrt_t

    # Theta Computation
    call_second_term = r * K * numpy.exp(-r * t) * norm.cdf(d2)
    call_theta = (first_term - call_second_term) / 365.0

    put_second_term = r * K * numpy.exp(-r * t) * norm.cdf(-d2)
    put_theta = (first_term + put_second_term) / 365.0

    # Gamma Computation
    gamma = norm.pdf(d1) / (S * sigma * numpy.sqrt(t))

    # Vega Computation
    vega = S * norm.pdf(d1) * numpy.sqrt(t) * 0.01

    # Rho Computation
    e_to_the_minus_rt = numpy.exp(-r * t)
    call_rho = t * K * e_to_the_minus_rt * norm.cdf(d2) * .01
    put_rho = -t * K * e_to_the_minus_rt * norm.cdf(-d2) * .01

    return d1, d2, call, put, put_delta, call_delta, call_theta, put_theta, gamma, vega, call_rho, put_rho


"""
if __name__ == '__main__':

    # S, K, r, sigma, T = 42, 40, 0.10, 0.2, 365/2

    S, K, r, sigma, T = 49, 50, 0.05, 0.2, 140

    d1, d2, call, put, put_delta, call_delta, call_theta, \
        put_theta, gamma, vega, call_rho, put_rho = option_chain(S, K, T, sigma, r)

    print("Internal D1 Value : %2.5f & D2 Value : %2.5f" % (d1, d2))
    print("Call Value is : %2.5f" % call)
    print("Call Delta is : %2.5f" % call_delta)
    print("Call Theta is : %2.5f" % call_theta)
    print("Call Gamma is : %2.5f" % gamma)
    print("Call Vega is : %2.5f" % vega)
    print("Call Rho is : %2.5f" % call_rho)

    print("Put Value is : %2.5f" % put)
    print("Put Delta is : %2.5f" % put_delta)
    print("Put Theta is : %2.5f" % put_theta)
    print("Put Gamma is : %2.5f" % gamma)
    print("Put Vega is : %2.5f" % vega)
    print("Put Rho is : %2.5f" % put_rho)
"""



