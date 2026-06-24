from data import UNIT_DATA
from  categories import StandardCategory
class ConversionEngine:

    def __init__(self):
        self.categories = {}

    def setup_categories(self):
        """setting up categories for each unit."""
        for category, category_info in UNIT_DATA.items():
            base = category_info["base_unit"]
            units = category_info["units"]

            new_category_object = StandardCategory(category,base,units)

            self.categories[category] = new_category_object

    def get_categories_name(self):
        """making the list of categories."""
        return list(self.categories.keys())

    def is_valid_category(self, user_cat):
        """category validation."""
        if user_cat not in self.categories:
            return False
        return True

    def get_categories_units(self, category_name):
        """getting all the available units that available in categories."""
        target_categories = self.categories[category_name]
        return target_categories.available_units()

    def is_valid_units(self,user_cat, user_unit):
        """unit validation."""
        u = self.get_categories_units(user_cat)
        if user_unit not in u:
            return False
        return True

    def execute_conversion(self, category_name, from_unit, to_unit, value):
        """setup for executing the calculator."""
        target_category = self.categories[category_name]
        result = target_category.calculation(from_unit, to_unit, value)
        return result