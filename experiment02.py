class Employee:
    def __init__(
            self,
            role: str = 'Developer',
            has_frontend: bool = False,
            has_backend: bool = False
    ):
        self.role = role
        self.has_frontend = has_frontend
        self.has_backend = has_backend

    def verifier(self):
        if self.has_frontend and self.has_backend:
            return "Fullstack"
        elif self.has_frontend:
            return "Frontend Developer"
        elif self.has_backend:
            return "Backend Developer"
        else:
            return "Not a Developer"

if __name__ == '__main__':
    print("Select your role: A: Frontend Developer B: Backend Developer C: Fullstack Developer D: nON OF ABOVE")
    role = input("Enter A, B, C, D: ")

    if role == 'A':
        user = Employee(has_frontend=True)
    elif role == 'B':
        user = Employee(has_backend=True)
    elif role == 'C':
        user = Employee(has_frontend=True, has_backend=True)
    else:
        user = Employee()

    print("The user is: ", user.verifier())
