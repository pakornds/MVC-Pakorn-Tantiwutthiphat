class WhiteCowMilkCalculator:
    def calculate_milk(age_in_months):
        """Calculates fresh milk for a white cow: 120 - total age in months."""
        return max(0, 120 - age_in_months)
