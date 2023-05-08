# -*- coding: utf-8 -*-
"""
Created on Wed Apr 12 11:48:00 2023

@author: fabian.woebbeking@iwh-halle.de
"""

def calculate_future_value(present_value:float, interest_rate:float, maturity:float, compounding:int=1) -> float:
    """Function to calculate a future value.

    Parameters
    ----------
    present_value : float
        DESCRIPTION.
    interest_rate : float
        DESCRIPTION.
    maturity : float
        DESCRIPTION.
    compounding : int, optional
        DESCRIPTION. The default is 1.

    Returns
    -------
    float
        DESCRIPTION.


    """
    return present_value * (1 + interest_rate / compounding) ** (maturity * compounding)


#%% https://realpython.com/if-name-main-python/
if __name__ == "__main__":
    print(f"With annual compounding:       EUR {calculate_future_value(1000, 0.1, 1):,.2f}")
    print(f"With semi-annual compounding:  EUR {calculate_future_value(1000, 0.1, 1, 2):,.2f}")
    print(f"With daily compounding:        EUR {calculate_future_value(1000, 0.1, 1, 365):,.2f}")