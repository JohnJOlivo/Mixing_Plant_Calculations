# Float input function will return error message if input is not a float.
def request_input(prompt):
    try:
        return float(input(prompt + ": "))
    except ValueError:
        print('Input a valid number')
        return request_input(prompt)


# Open-top tank return rate calculator
def open_top():
    s1 = request_input('Starting Inches')
    s2 = request_input('Ending Inches')
    st = request_input('Strap Time')
    coeff = request_input('Coefficient')
    rate = compute_ot_rate(s1, s2, st, coeff)
    print(f'Return Rate:{rate}')


# Testable open top return rate calculation
def compute_ot_rate(s1, s2, st, coeff):
    rate = ((s2 - s1) / st) * coeff
    return rate


# Frac tank return rate calculator
def frac_tank():
    s1 = request_input('Starting BBls')
    s2 = request_input('Ending BBls')
    st = request_input('Strap Time')
    rate = compute_ft_rate(s1, s2, st)
    print(f'Return Rate:{rate}')


# Testable frac tank return rate calculation
def compute_ft_rate(s1, s2, st):
    rate = (s2 - s1) / st
    return rate


# Sweep to surface calculator
def sweep_to_surf():
    td = request_input('Total Depth')
    casing = request_input('Casing Coefficient')
    tubing = request_input('Tubing Coefficient')
    rrate = request_input('Return Rate')
    prate = request_input('Coil Pump Rate')
    tts = compute_sos(td, casing, rrate, tubing, prate)
    print(f'Add {tts} to the time the sweep was sent.')


# Testable sweep to surface calculation
def compute_sos(td, casing, rrate, tubing, prate):
    f1 = (td * casing) / rrate
    f2 = (td * tubing) / prate
    tts = f1 + f2
    return tts


# Chem ratio ounces/gallons per minute calculator
def chem_ratio():
    pr = request_input('Pump rate')
    cr = request_input('Chemical Ratio')
    gpm = compute_gpm(pr, cr)
    opm = compute_opm(pr, cr)
    print(f'Gallons Per Minute: {gpm}')
    print(f'Ounces Per Minute: {opm}')


# Testable gallon of chemical per minute calculation
def compute_gpm(pr, cr):
    gpm = (pr * cr) / 10
    return gpm


# Testable ounces of chemical per minute calculation
def compute_opm(pr, cr):
    opm = ((pr * cr) / 10) * 128
    return opm
chem_ratio()
