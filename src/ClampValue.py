def ClampValue(valueToClamp, minRange, maxRange):
    return max(min(valueToClamp, maxRange), minRange)
