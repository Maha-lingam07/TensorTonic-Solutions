from collections import Counter
import numpy as np
from scipy import stats

def mean_median_mode(x: list) -> dict:
    """
    Returns a dictionary with mean, median, and mode.
    """
    # Write code here
    ans = {}
    y = np.asarray(x).ravel()
    
    ans["mean"] = float(np.mean(y))
    ans["median"] = float(np.median(y))
    
    mode_result = stats.mode(y, keepdims=False)
    ans["mode"] = float(mode_result.mode)

    return ans