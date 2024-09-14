class Cow:
    # store cow information
    def __init__(self, cow_id, breed, age_years, age_months):
        self.cow_id = cow_id
        self.breed = breed
        self.age_years = age_years
        self.age_months = age_months

    # Returns the total age of the cow in months.
    def total_age_in_months(self):
        return self.age_years * 12 + self.age_months
