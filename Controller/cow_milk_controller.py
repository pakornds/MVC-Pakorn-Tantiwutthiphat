from Model.cow_milk_model import CowMilkModel


class CowMilkController:
    def __init__(self, view, model):
        self.view = view
        self.model = model
        self.view.set_controller(self)

    def submit_cow_id(self, cow_id):
        # Validate the cow ID (already validated for format in the View)
        cow = self.model.find_cow_by_id(cow_id)

        if cow:
            milk_amount = self.model.calculate_milk(cow)
            milk_type = self._get_milk_type(cow.breed)
            result_message = f"Cow {cow_id} ({cow.breed}) produced {milk_amount:.2f} liters of {milk_type} milk."
            self.view.display_message(result_message)
        else:
            self.view.display_message(f"Cow ID {cow_id} not found.")

    def _get_milk_type(self, breed):
        if breed == 'white':
            return "Fresh Milk"
        elif breed == 'brown':
            return "Chocolate Milk"
        elif breed == 'pink':
            return "Strawberry Milk"
        return "Unknown Milk"
