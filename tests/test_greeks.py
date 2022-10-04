from BlackScholes import _d1, _d2, black_scholes, delta, theta, gamma, vega, rho, futures


def test__d1():
    assert True
    S = 42
    K = 40
    r = .10
    sigma = .20
    t = 0.5
    calculated_d1 = _d1(S, K, t, r, sigma)
    text_book_d1 = 0.7693
    print("calculated_d1 is %2.5f and text_book_d1 is %2.5f" % (calculated_d1, text_book_d1))
    assert abs(calculated_d1 - text_book_d1) < 0.0001


def test__d2():
    assert True
    S = 42
    K = 40
    r = 0.10
    sigma = 0.20
    t = 0.50
    calculated_d2 = _d2(S, K, t, r, sigma)  # 0.627841271869
    text_book_d2 = 0.6278
    print("calculated_d2 is %2.5f and text_book_d2 is %2.5f" % (calculated_d2, text_book_d2))
    assert abs(calculated_d2 - text_book_d2) < 0.0001


def test_black_scholes():
    assert True
    S, K, t, r, sigma = 60, 65, .25, .08, .3
    expected = 2.13336844492
    actual = black_scholes('c', S, K, t, r, sigma)
    print("Actual is %2.5f and Textbook is %2.5f" % (actual, expected))
    assert abs(expected - actual) < 1e-11

    S, K, r, sigma, t = 42, 40, 0.10, 0.20, 0.50

    calculated_call = black_scholes('c', S, K, t, r, sigma)
    text_book_call = 4.76
    print("Actual is %2.5f and Textbook is %2.5f" % (calculated_call, text_book_call))
    assert abs(calculated_call - text_book_call) < 0.01

    calculated_put = black_scholes('p', S, K, t, r, sigma)
    text_book_put = 0.81
    print("Actual is %2.5f and Textbook is %2.5f" % (calculated_put, text_book_put))
    assert abs(calculated_put - text_book_put) < 0.01


def test_delta():
    assert True
    S = 49
    K = 50
    r = .05
    t = 0.3846
    sigma = 0.2
    call_delta_calc = delta('c', S, K, t, r, sigma)
    # 0.521601633972
    delta_text_book = 0.522
    print("Call Delta is : %1.3f & TextBook Call_Delta is : %1.3f" % (call_delta_calc, delta_text_book))
    assert abs(call_delta_calc - delta_text_book) < .01

    put_delta_calc = delta('p', S, K, t, r, sigma)
    put_delta_text_book = delta_text_book - 1.0
    print("Put Delta is : %1.3f & TextBook Put_Delta is : %1.3f" % (put_delta_calc, put_delta_text_book))
    assert abs(put_delta_calc - put_delta_text_book) < .01


def test_theta():
    assert True
    S = 49
    K = 50
    r = .05
    t = 0.3846
    sigma = 0.2
    annual_theta_calc = theta('c', S, K, t, r, sigma)
    # -4.30538996455
    annual_theta_text_book = -4.31 / 365
    print("CALL Theta : %2.6f, TextBook Theta : %2.6f" % (annual_theta_calc, annual_theta_text_book))
    assert abs(annual_theta_calc - annual_theta_text_book) < .0001

    annual_theta_calc = theta('p', S, K, t, r, sigma)
    annual_theta_text_book = -1.8530056722 / 365
    print("Put Theta : %2.6f, TextBook Theta : %2.6f" % (annual_theta_calc, annual_theta_text_book))
    assert abs(annual_theta_calc - annual_theta_text_book) < .0001


def test_gamma():
    assert True
    S = 49
    K = 50
    r = .05
    t = 0.3846
    sigma = 0.2
    gamma_calc = gamma(S, K, t, r, sigma)
    # 0.0655453772525
    gamma_text_book = 0.066
    print("Calc Gamma : %2.6f , TextBook Gamma : %2.6f" % (gamma_calc, gamma_text_book))
    assert abs(gamma_calc - gamma_text_book) < .001


def test_vega():
    assert True

    S = 49
    K = 50
    r = .05
    t = 0.3846
    sigma = 0.2
    vega_calc = vega(S, K, t, r, sigma)
    # 0.121052427542
    vega_text_book = 0.121
    print("Calc Vega : %2.6f , TextBook Vega : %2.6f" % (vega_calc, vega_text_book))
    assert abs(vega_calc - vega_text_book) < .01


def test_rho():
    assert True
    S = 49
    K = 50
    r = .05
    t = 0.3846
    sigma = 0.2
    call_rho_text_book = 0.0891
    call_rho_calc = rho('c', S, K, t, r, sigma)
    # 0.089065740988

    print("Call Vega : %2.6f , TextBook Vega : %2.6f" % (call_rho_calc, call_rho_text_book))
    assert abs(call_rho_calc - call_rho_text_book) < .0001

    put_rho_text_book = -0.09957
    put_rho_calc = rho('p', S, K, t, r, sigma)

    print("Put Vega : %2.6f , TextBook Vega : %2.6f" % (put_rho_calc, put_rho_text_book))
    assert abs(put_rho_calc - put_rho_text_book) < .001


def test_futures_price():
    assert True

    S = 1300
    t = 0.25
    r = .05
    q = 0.01
    F = futures(S, t, r, q)
    pre_calculated = 1313.07
    print("Futures Prie : %2.6f , TextBook Futures Price : %2.6f" % (F, pre_calculated))
    assert abs(F - pre_calculated) < 0.01
