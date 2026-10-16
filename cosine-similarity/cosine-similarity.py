import numpy as np

def cosine_similarity(a: list, b: list) -> float:
    """
    Returns the cosine similarity as a Python float.
    """
    # Write code here
    num = np.dot(a,b)
    den = np.linalg.norm(a) * np.linalg.norm(b)

    if(int(den) == 0):
        return float(0)
    return float(num/den)