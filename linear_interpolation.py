def linear_interpolation(x1, y1, x2, y2, x):
    """
    Perform linear interpolation to find the y value at a specified x value.

    Parameters:§
    x1 (float): The x coordinate of the first point.
    y1 (float): The y coordinate of the first point.
    x2 (float): The x coordinate of the second point.
    y2 (float): The y coordinate of the second point.
    x (float): The x value at which to interpolate.

    Returns:
    float: The interpolated y value at the specified x value.

    Raises:
    ValueError: If the x value is outside the range [x1, x2].
    """
    if x1 == x2:
        raise ValueError('x1 and x2 cannot be the same value')
    if x < min(x1, x2) or x > max(x1, x2):
        raise ValueError(f'x value {x} is outside the range [{min(x1, x2)}, {max(x1, x2)}]')

    gradient = (y2 - y1) / (x2 - x1)
    y_intercept = y1 - gradient * x1
    return gradient * x + y_intercept
