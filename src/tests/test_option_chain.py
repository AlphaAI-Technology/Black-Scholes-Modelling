from src.option_chain import option_chain


def test_option_chain():
    assert True

    """
        S, K, r, sigma, T = 42, 40, 0.10, 0.2, 365/2

        Internal D1 Value : 0.76926 & D2 Value : 0.62784
        Call Value is : 4.75942
        Call Delta is : 0.77913
        Call Theta is : -0.01249
        Call Gamma is : 0.04996
        Call Vega is : 0.08813
        Call Rho is : 0.13982


        Put Value is : 0.80860
        Put Delta is : -0.22087
        Put Theta is : -0.00207
        Put Gamma is : 0.04996
        Put Vega is : 0.08813
        Put Rho is : -0.05043
    """

    S, K, r, sigma, T = 42, 40, 0.10, 0.2, 365 / 2
    d1, d2, call, put, put_delta, call_delta, call_theta, \
        put_theta, gamma, vega, call_rho, put_rho = option_chain(S, K, T, sigma, r)

    text_book_d1 = 0.7693
    text_book_d2 = 0.6278
    text_book_call = 4.76
    text_book_put = 0.81
    call_delta_text_book = 0.77913
    put_delta_text_book = -0.22087
    call_theta_text_book = -0.01249
    put_theta_text_book = -0.00207
    gamma_text_book = 0.04996
    vega_text_book = 0.08813
    call_rho_text_book = 0.13982
    put_rho_text_book = -0.05043

    print("Calculated_d1 : %2.5f and Book d1 : %2.5f" % (d1, text_book_d1))
    assert abs(d1 - text_book_d1) < 0.0001

    print("Calculated_d2 : %2.5f and Book d2 : %2.5f" % (d2, text_book_d2))
    assert abs(d2 - text_book_d2) < 0.0001

    print("Call Price : %2.5f and Textbook : %2.5f" % (call, text_book_call))
    assert abs(call - text_book_call) < 0.01

    print("Call Delta is : %1.3f & TextBook Call_Delta is : %1.3f" % (call_delta, call_delta_text_book))
    assert abs(call_delta - call_delta_text_book) < .01

    print("CALL Theta : %2.6f, TextBook Theta : %2.6f" % (call_theta, call_theta_text_book))
    assert abs(call_theta - call_theta_text_book) < .0001

    print("Call Vega : %2.6f , TextBook Vega : %2.6f" % (call_rho, call_rho_text_book))
    assert abs(call_rho - call_rho_text_book) < .0001

    print("Put Price : %2.5f and Textbook : %2.5f" % (put, text_book_put))
    assert abs(put - text_book_put) < 0.01

    print("Put Delta is : %1.3f & TextBook Put_Delta is : %1.3f" % (put_delta, put_delta_text_book))
    assert abs(put_delta - put_delta_text_book) < .01

    print("Put Theta : %2.6f, TextBook Theta : %2.6f" % (put_theta, put_theta_text_book))
    assert abs(put_theta - put_theta_text_book) < .0001

    print("Put Vega : %2.6f , TextBook Vega : %2.6f" % (put_rho, put_rho_text_book))
    assert abs(put_rho - put_rho_text_book) < .001

    print("Calc Gamma : %2.6f , TextBook Gamma : %2.6f" % (gamma, gamma_text_book))
    assert abs(gamma - gamma_text_book) < .001

    print("Calc Vega : %2.6f , TextBook Vega : %2.6f" % (vega, vega_text_book))
    assert abs(vega - vega_text_book) < .01


def test_option_chain_2():
    assert True

    """
        S, K, r, sigma, T = 49, 50, 0.05, 0.2, 140

        Internal D1 Value : 0.05366 & D2 Value : -0.07020
        Call Value is : 2.39599
        Call Delta is : 0.52140
        Call Theta is : -0.01181
        Call Gamma is : 0.06564
        Call Vega is : 0.12089
        Call Rho is : 0.08880

        Put Value is : 2.44622
        Put Delta is : -0.47860
        Put Theta is : -0.00509
        Put Gamma is : 0.06564
        Put Vega is : 0.12089
        Put Rho is : -0.09933
    """

    S, K, r, sigma, T = 49, 50, 0.05, 0.2, 140
    d1, d2, call, put, put_delta, call_delta, call_theta, \
        put_theta, gamma, vega, call_rho, put_rho = option_chain(S, K, T, sigma, r)

    text_book_d1 = 0.05366
    text_book_d2 = -0.07020
    text_book_call = 2.39599
    text_book_put = 2.44622
    call_delta_text_book = 0.52140
    put_delta_text_book = -0.47860
    call_theta_text_book = -0.01181
    put_theta_text_book = -0.00509
    gamma_text_book = 0.06564
    vega_text_book = 0.12089
    call_rho_text_book = 0.08880
    put_rho_text_book = -0.09933

    print("Calculated_d1 : %2.5f and Book d1 : %2.5f" % (d1, text_book_d1))
    assert abs(d1 - text_book_d1) < 0.0001

    print("Calculated_d2 : %2.5f and Book d2 : %2.5f" % (d2, text_book_d2))
    assert abs(d2 - text_book_d2) < 0.0001

    print("Call Price : %2.5f and Textbook : %2.5f" % (call, text_book_call))
    assert abs(call - text_book_call) < 0.01

    print("Call Delta is : %1.3f & TextBook Call_Delta is : %1.3f" % (call_delta, call_delta_text_book))
    assert abs(call_delta - call_delta_text_book) < .01

    print("CALL Theta : %2.6f, TextBook Theta : %2.6f" % (call_theta, call_theta_text_book))
    assert abs(call_theta - call_theta_text_book) < .0001

    print("Call Vega : %2.6f , TextBook Vega : %2.6f" % (call_rho, call_rho_text_book))
    assert abs(call_rho - call_rho_text_book) < .0001

    print("Put Price : %2.5f and Textbook : %2.5f" % (put, text_book_put))
    assert abs(put - text_book_put) < 0.01

    print("Put Delta is : %1.3f & TextBook Put_Delta is : %1.3f" % (put_delta, put_delta_text_book))
    assert abs(put_delta - put_delta_text_book) < .01

    print("Put Theta : %2.6f, TextBook Theta : %2.6f" % (put_theta, put_theta_text_book))
    assert abs(put_theta - put_theta_text_book) < .0001

    print("Put Vega : %2.6f , TextBook Vega : %2.6f" % (put_rho, put_rho_text_book))
    assert abs(put_rho - put_rho_text_book) < .001

    print("Calc Gamma : %2.6f , TextBook Gamma : %2.6f" % (gamma, gamma_text_book))
    assert abs(gamma - gamma_text_book) < .001

    print("Calc Vega : %2.6f , TextBook Vega : %2.6f" % (vega, vega_text_book))
    assert abs(vega - vega_text_book) < .01

