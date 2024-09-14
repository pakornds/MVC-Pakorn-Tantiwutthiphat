import csv
from Model.cow import Cow
from Model.white_cow import WhiteCowMilkCalculator
from Model.brown_cow import BrownCowMilkCalculator
from Model.pink_cow import PinkCowMilkCalculator
from Model.generate_cow import CowGenerator


class CowMilkModel:
    def __init__(self, csv_file="Model\\data\\cow_data.csv"):
        self.csv_file = csv_file
        self.cows = self._load_cows_from_csv()

        # Generate cows if less than 15 in the CSV
        if len(self.cows) < 15:
            generator = CowGenerator(self.csv_file)
            generator._generate_random_cows()  # Generate and save cows
            self.cows = self._load_cows_from_csv()  # Reload after generating cows

    def _load_cows_from_csv(self):
        """Load cows from a CSV file."""
        cow_data = []
        try:
            with open(self.csv_file, newline='') as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    cow_id = row['cow_id']
                    breed = row['breed']
                    age_years = int(row['age_years'])
                    age_months = int(row['age_months'])
                    cow_data.append(Cow(cow_id, breed, age_years, age_months))
        except FileNotFoundError:
            # If the file doesn't exist, return an empty list
            return []
        return cow_data

    def find_cow_by_id(self, cow_id):
        """Finds and returns a cow by its ID, or None if not found."""
        for cow in self.cows:
            if cow.cow_id == cow_id:
                return cow
        return None

    def calculate_milk(self, cow):
        """Calculates the amount of milk based on the cow's breed and age."""
        if cow.breed == 'white':
            return WhiteCowMilkCalculator.calculate_milk(cow.total_age_in_months())
        elif cow.breed == 'brown':
            return BrownCowMilkCalculator.calculate_milk(cow.age_years)
        elif cow.breed == 'pink':
            return PinkCowMilkCalculator.calculate_milk(cow.age_months)
        return 0
