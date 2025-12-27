
# Problem‑1: Simple Calculator using Class

class Calculator:
    def __init__(self, a: float, b: float, operation: str):
        self.a = a
        self.b = b
        self.operation = operation.lower()  

    def calculate(self):
        if self.operation == "add":
            return self.a + self.b
        elif self.operation == "subtract":
            return self.a - self.b
        elif self.operation == "multiply":
            return self.a * self.b
        elif self.operation == "divide":
            if self.b == 0:
                return "Error: Division by zero"
            return self.a / self.b
        else:
            return "Invalid operation type. Use add, subtract, multiply, or divide."

if __name__ == "__main__":
    a = float(input("Enter first number (a): "))
    b = float(input("Enter second number (b): "))
    op = input("Enter operation type (add / subtract / multiply / divide): ")

    calc = Calculator(a, b, op)
    result = calc.calculate()

    print("Result:", result)

# output
# Enter first number (a): 12
# Enter second number (b): 5
# Enter operation type (add / subtract / multiply / divide): add
# Result: 17.0