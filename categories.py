
class StandardCategory:

    def __init__(self, name, base_unit, unit):
        self.name = name
        self.base_unit = base_unit
        self.unit = unit
        
    def calculation(self, from_unit, to_unit, value):
        """calculation method, getting final result"""
        from_multiplier = self.unit[from_unit]
        to_multiplier = self.unit[to_unit]

        final_value =  from_multiplier * value / to_multiplier
        return final_value

    def available_units(self):
        """getting all the available units for particular category."""
        units = list(self.unit.keys())
        return units
