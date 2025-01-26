def safe_divide(numerator, denominator):
    """Perform division with robust error handling."""
    try:
        # Convert inputs to floats
        num = float(numerator)
        denom = float(denominator)

        # Handle division by zero
        if denom == 0:
            return "Error: Cannot divide by zero."

        # Perform division
        result = num / denom
        return f"The result of the division is {result:.2f}"

    except ValueError:
        # Handle non-numeric inputs
        return "Error: Please enter numeric values only."

