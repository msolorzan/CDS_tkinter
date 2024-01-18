class ValueVerification():
    
    def __init__(self, value, value_type):
        self.value = value
        self.value_type = value_type

    def verify(self):
        if self.value_type == "numeric":
            return self.verify_numeric()
        elif self.value_type == "string":
            return self.verify_string()
        else:
            raise ValueError("Tipo no válido")

    def verify_numeric(self):
        try:
            self.numeric_value = int(self.value)
            if len(self.value) > 0 and numeric_value >= 0:
                return True, numeric_value
            else:
                return False, None
        except ValueError:
            return False, None

    def verify_string(self):
        try:
            if isinstance(self.value, str) and len(self.value) > 0:
                return True, self.value
            else:
                return False, None
        except Exception as e:
            print(f"Error: {e}")
            return False, None