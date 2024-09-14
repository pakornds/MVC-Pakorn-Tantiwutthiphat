class CowMilkController:
    def __init__(self, view, model):
        """"init class"""
        self.view = view
        self.model = model
        self.view.set_controller(self)

    def submit_cow_id(self, cow_id):
        """Find if the cow ID exists in the database or not and send information to Model
    to get a result and return the result, showing it on the screen with View"""
        cow = self.model.find_cow_by_id(cow_id)

        if cow:
            milk_amount = self.model.calculate_milk(cow)
            milk_type = self._get_milk_type(cow.breed)
            result_message = f"Cow {cow_id} ({cow.breed}) produced {milk_amount:.2f} liters of {milk_type}."
            self.view.display_message(result_message)
        else:
            self.view.display_message(f"Cow ID {cow_id} not found.")

    def _get_milk_type(self, breed):
        """Return the milk type of the current cow"""
        if breed == 'white':
            return "Fresh Milk"
        elif breed == 'brown':
            return "Chocolate Milk"
        elif breed == 'pink':
            return "Strawberry Milk"
        return "Unknown Milk"
