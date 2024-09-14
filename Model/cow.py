class Cow:
    def __init__(self, cow_id, breed, age_years, age_months):
        """"store cow information"""
        self.cow_id = cow_id
        self.breed = breed
        self.age_years = age_years
        self.age_months = age_months

    def total_age_in_months(self):
        """Returns the total age of the cow in months"""
        return self.age_years * 12 + self.age_months
