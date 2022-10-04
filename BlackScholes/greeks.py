import numpy
from scipy.stats import norm


def _d1(S, K, t, r, sigma):  # see Hull 9th Edition , page 338
    """Calculate the d1 component of the Black-Scholes PDE.

    :param S: Underlying Asset / Stock Price
    :type S: float
    :param K: Strike Price
    :type K: float
    :param sigma: Annualized Standard Deviation, or Volatility i.e. 50% is 0.50, or 30% is 0.30
    :type sigma: float
    :param t: time to expiration in years
    :type t: float
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

    sigma_squared = sigma * sigma
    numerator = numpy.log(S / float(K)) + (r + sigma_squared / 2.) * t
    denominator = sigma * numpy.sqrt(t)

    if not denominator:
        print('')
    return numerator / denominator


def _d2(S, K, t, r, sigma):  # see Hull 9th Edition , page 338
    """Calculate the d2 component of the Black-Scholes PDE.

    :param S: underlying asset price
    :type S: float
    :param K: strike price
    :type K: float
    :param sigma: annualized standard deviation, or volatility
    :type sigma: float
    :param t: time to expiration in years
    :type t: float
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
    calculated_d2 = _d2(S,K,t,r,sigma) #0.627841271869
    text_book_d2 = 0.6278
    abs(calculated_d2 - text_book_d2) < 0.0001
    True
    """

    return _d1(S, K, t, r, sigma) - sigma * numpy.sqrt(t)


def black_scholes(flag, S, K, t, r, sigma):
    """Return the Black-Scholes option price implemented in
        python (for reference).

    :param S: underlying asset price
    :type S: float
    :param K: strike price
    :type K: float
    :param sigma: annualized standard deviation, or volatility
    :type sigma: float
    :param t: time to expiration in years
    :type t: float
    :param r: risk-free interest rate
    :type r: float
    :param flag: 'c' or 'p' for call or put.
    :type flag: str

    John C. Hull, "Options, Futures and Other Derivatives," 9th edition, Example 15.6, page 338

    Example : The stock price 6 months from the expiration of an option is $42, the exercise price
    of the option is $40, the risk-free interest rate is 10% per annum, and the volatility
    is 20% per annum. This means that S = 42, K = 40, r = 0.10, sigma = 0.2, T = 0.50

    S, K, r, sigma, t = 42, 40, 0.10, 0.2, 0.50

    calculated_call = black_scholes('c', S, K, t, r, sigma)
    text_book_call = 4.76
    abs(calculated_call - text_book_call) < 0.01

    calculated_put = black_scholes('p', S, K, t, r, sigma)
    text_book_put = 0.81
    abs(calculated_put - text_book_put) < 0.01

    """

    e_to_the_minus_rt = numpy.exp(-r * t)
    d1 = _d1(S, K, t, r, sigma)
    d2 = _d2(S, K, t, r, sigma)
    if flag == 'c':
        return S * norm.cdf(d1) - K * e_to_the_minus_rt * norm.cdf(d2)
    else:
        return - S * norm.cdf(-d1) + K * e_to_the_minus_rt * norm.cdf(-d2)


def delta(flag, S, K, t, r, sigma):
    """Return Black-Scholes delta of an option.

    :param S: underlying asset price
    :type S: float
    :param K: strike price
    :type K: float
    :param sigma: annualized standard deviation, or volatility
    :type sigma: float
    :param t: time to expiration in years
    :type t: float
    :param r: risk-free interest rate
    :type r: float
    :param flag: 'c' or 'p' for call or put.
    :type flag: str

    John C. Hull, "Options, Futures and Other Derivatives," 9th edition, Example 19.1, page 405

    Example 19.1, page 405, Hull:
    Consider again the call option on a non-dividend-paying stock in Section 19.1
    where the stock price is $49, the strike price is $50, the risk-free rate is 5%, the
    time to maturity is 20 weeks ( 0.3846 years), and the volatility is 20%.

    S = 49
    K = 50
    r = .05
    t = 0.3846
    sigma = 0.2
    flag = 'c'
    delta_calc = delta(flag, S, K, t, r, sigma)
    # 0.521601633972
    delta_text_book = 0.522
    abs(delta_calc - delta_text_book) < .01
    True
    """

    d1 = _d1(S, K, t, r, sigma)

    if flag == 'p':
        return norm.cdf(d1) - 1.0
    else:
        return norm.cdf(d1)


def theta(flag, S, K, t, r, sigma):
    """Return Black-Scholes theta of an option.

    :param S: underlying asset price
    :type S: float
    :param K: strike price
    :type K: float
    :param sigma: annualized standard deviation, or volatility
    :type sigma: float
    :param t: time to expiration in years
    :type t: float
    :param r: risk-free interest rate
    :type r: float
    :param flag: 'c' or 'p' for call or put.
    :type flag: str

    John C. Hull, "Options, Futures and Other Derivatives," 9th edition, Example 19.2, page 409

    As in Example 19.1, consider a call option on a non-dividend-paying stock where
    the stock price is $49, the strike price is $50, the risk-free rate is 5%, the time to
    maturity is 20 weeks (0.3846 years), and the volatility is 20%. In this case,
    S = 49, K = 50, r = 0.05, sigma = 0.2, and T = 0.3846

    The text book analytical formula does not divide by 365,
    but in practice theta is defined as the change in price
    for each day change in t, hence we divide by 365.

    Example 19.2, page 409, Hull:

    S = 49
    K = 50
    r = .05
    t = 0.3846
    sigma = 0.2
    flag = 'c'
    annual_theta_calc = theta(flag, S, K, t, r, sigma) * 365
    # -4.30538996455
    annual_theta_text_book = -4.31
    abs(annual_theta_calc - annual_theta_text_book) < .01
    True

    Using the same inputs with a put.
    S = 49
    K = 50
    r = .05
    t = 0.3846
    sigma = 0.2
    flag = 'p'
    annual_theta_calc = theta(flag, S, K, t, r, sigma) * 365
    # -1.8530056722
    annual_theta_reference = -1.8530056722
    abs(annual_theta_calc - annual_theta_reference) < .000001
    True
    """

    two_sqrt_t = 2 * numpy.sqrt(t)

    d1 = _d1(S, K, t, r, sigma)
    d2 = _d2(S, K, t, r, sigma)

    first_term = (-S * norm.pdf(d1) * sigma) / two_sqrt_t

    if flag == 'c':
        second_term = r * K * numpy.exp(-r * t) * norm.cdf(d2)
        return (first_term - second_term) / 365.0

    if flag == 'p':
        second_term = r * K * numpy.exp(-r * t) * norm.cdf(-d2)
        return (first_term + second_term) / 365.0


def gamma(S, K, t, r, sigma):
    """Return Black-Scholes gamma of an option.

    :param S: underlying asset price
    :type S: float
    :param K: strike price
    :type K: float
    :param sigma: annualized standard deviation, or volatility
    :type sigma: float
    :param t: time to expiration in years
    :type t: float
    :param r: risk-free interest rate
    :type r: float

    John C. Hull, "Options, Futures and Other Derivatives," 9th edition, Example 19.4, page 414

    As in Example 19.1, consider a call option on a non-dividend-paying stock where
    the stock price is $49, the strike price is $50, the risk-free rate is 5%, the time to
    maturity is 20 weeks (0.3846 years), and the volatility is 20%. In this case,
    S = 49, K = 50, r = 0.05, sigma = 0.2, and T = 0.3846

    S = 49
    K = 50
    r = .05
    t = 0.3846
    sigma = 0.2
    flag = 'c'
    gamma_calc = gamma(flag, S, K, t, r, sigma)
    # 0.0655453772525
    gamma_text_book = 0.066
    abs(gamma_calc - gamma_text_book) < .001
    True
    """

    d_1 = _d1(S, K, t, r, sigma)
    # v_squared = sigma ** 2
    return norm.pdf(d_1) / (S * sigma * numpy.sqrt(t))


def vega(S, K, t, r, sigma):
    """Return Black-Scholes vega of an option.

    :param S: underlying asset price
    :type S: float
    :param K: strike price
    :type K: float
    :param sigma: annualized standard deviation, or volatility
    :type sigma: float
    :param t: time to expiration in years
    :type t: float
    :param r: risk-free interest rate
    :type r: float

    John C. Hull, "Options, Futures and Other Derivatives," 9th edition, Example 19.4, page 414

    As in Example 19.1, consider a call option on a non-dividend-paying stock where
    the stock price is $49, the strike price is $50, the risk-free rate is 5%, the time to
    maturity is 20 weeks (0.3846 years), and the volatility is 20%. In this case,
    S = 49, K = 50, r = 0.05, sigma = 0.2, and T = 0.3846

    S = 49
    K = 50
    r = .05
    t = 0.3846
    sigma = 0.2
    flag = 'c'
    vega_calc = vega(flag, S, K, t, r, sigma)
    # 0.121052427542
    vega_text_book = 0.121
    abs(vega_calc - vega_text_book) < .01
    True

    The text book analytical formula does not multiply by .01,
    but in practice vega is defined as the change in price
    for each 1 percent change in IV, hence we multiply by 0.01.

    """

    d_1 = _d1(S, K, t, r, sigma)
    return S * norm.pdf(d_1) * numpy.sqrt(t) * 0.01


def rho(flag, S, K, t, r, sigma):
    """Return Black-Scholes rho of an option.

    :param S: underlying asset price
    :type S: float
    :param K: strike price
    :type K: float
    :param sigma: annualized standard deviation, or volatility
    :type sigma: float
    :param t: time to expiration in years
    :type t: float
    :param r: risk-free interest rate
    :type r: float
    :param flag: 'c' or 'p' for call or put.
    :type flag: str

    The text book analytical formula does not multiply by .01,
    but in practice rho is defined as the change in price
    for each 1 percent change in r, hence we multiply by 0.01.

    John C. Hull, "Options, Futures and Other Derivatives," 9th edition, Example 19.4, page 414

    As in Example 19.1, consider a call option on a non-dividend-paying stock where
    the stock price is $49, the strike price is $50, the risk-free rate is 5%, the time to
    maturity is 20 weeks (0.3846 years), and the volatility is 20%. In this case,
    S = 49, K = 50, r = 0.05, sigma = 0.2, and T = 0.3846

    S = 49
    K = 50
    r = .05
    t = 0.3846
    sigma = 0.2
    flag = 'c'
    rho_calc = rho(flag, S, K, t, r, sigma)
    # 0.089065740988
    rho_text_book = 0.0891
    abs(rho_calc - rho_text_book) < .0001
    True
    """

    d2 = _d2(S, K, t, r, sigma)
    e_to_the_minus_rt = numpy.exp(-r * t)
    if flag == 'c':
        return t * K * e_to_the_minus_rt * norm.cdf(d2) * .01
    else:
        return -t * K * e_to_the_minus_rt * norm.cdf(-d2) * .01


def futures(S, t, r, q):
    """Calculate the forward price of an underlying asset.

    :param S: underlying asset price
    :type S: float
    :param t: time to expiration in years
    :type t: float
    :param r: risk-free interest rate
    :type r: float
    :param q: dividend yield percentage per annum
    :type q: float

    John C. Hull, "Options, Futures and Other Derivatives," 9th edition, Example 5.5, page 116

    Consider a 3-month futures contract on an index. Suppose that the stocks underlying
    the index provide a dividend yield of 1% per annum, that the current value
    of the index is 1,300, and that the continuously compounded risk-free interest rate
    is 5% per annum. In this case, r = 0.05, S = 1,300, T = 0.25, and q = 0.01.
    Hence, the futures price, F0, is given by


    S = 1300
    t = 0.25
    r = 0.05
    q = 0.01
    F = futures(S,t,r,q)
    pre_calculated = 1313.07
    abs(F-pre_calculated) < 0.01
    True
    """

    return S * numpy.exp((r - q) * t)

