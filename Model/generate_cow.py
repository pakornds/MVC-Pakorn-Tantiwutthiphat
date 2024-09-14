import csv
import random
from Model.cow import Cow


class CowGenerator:
    def __init__(self, csv_file):
        """init class"""
        self.csv_file = csv_file
        self.cows = []

    def _save_cows_to_csv(self):
        """Save cows to a CSV file"""
        with open(self.csv_file, mode='w', newline='') as csvfile:
            fieldnames = ['cow_id', 'breed', 'age_years', 'age_months']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for cow in self.cows:
                writer.writerow({
                    'cow_id': cow.cow_id,
                    'breed': cow.breed,
                    'age_years': cow.age_years,
                    'age_months': cow.age_months
                })

    def _generate_random_cows(self):
        """"Generate 15 random cow samples and save to CSV"""
        breeds = ['white', 'brown', 'pink']
        while len(self.cows) < 15:
            cow_id = str(random.randint(10000000, 99999999))
            breed = random.choice(breeds)
            age_years = random.randint(0, 10)
            age_months = random.randint(0, 11)
            new_cow = Cow(cow_id, breed, age_years, age_months)
            self.cows.append(new_cow)

        self._save_cows_to_csv()
