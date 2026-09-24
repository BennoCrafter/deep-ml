import numpy as np

def compute_norm(arr: np.ndarray, norm_type: str) -> float:
    """
    Compute the specified norm of the input array.

    'l1', 'l2' and 'linf' are entrywise norms and accept a 1D or 2D array.
    'frobenius' is a matrix norm and must raise a ValueError if arr is not 2D.

    Args:
        arr: Input numpy array (1D or 2D)
        norm_type: Type of norm ('l1', 'l2', 'linf', or 'frobenius')

    Returns:
        The computed norm as a float
    """

    flatten = arr.flatten()
    match norm_type:
        case "l1":
            return float(sum(abs(i) for i in flatten))
        case "l2":
            return float(np.sqrt(sum(i**2 for i in flatten)))
        case "linf":
            return float(max(abs(i) for i in flatten))
        case "frobenius":
            if not isinstance(arr[0], np.ndarray):
                raise ValueError()
            
            return float(np.sqrt(sum(i**2 for i in flatten)))
    pass
