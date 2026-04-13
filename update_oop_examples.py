import json

filepath = r'c:\Users\91866\.gemini\antigravity\scratch\prepforge-ai\data\examples.json'
with open(filepath, 'r', encoding='utf-8') as f:
    data = json.load(f)

oop_example_category = {
    "name": "Exception Handling Deep Dive",
    "topics": [
        {
            "name": "1. What is Error / Exception Handling?",
            "explanation": "Exception Handling = managing runtime errors so program doesn’t crash (e.g. Divide by zero, File not found). Without handling -> Program stops. With handling -> Program continues safely."
        },
        {
            "name": "2. Error vs Exception & Hierarchy",
            "explanation": "Error: Serious problem (JVM level, cannot recover like OutOfMemoryError).\nException: Runtime issue (can handle using code like ArithmeticException).\n\nHierarchy:\nThrowable\n ├── Error\n └── Exception\n      ├── Checked Exception\n      └── Unchecked Exception (RuntimeException)"
        },
        {
            "name": "3. Checked vs Unchecked Exceptions",
            "explanation": "Checked: Checked at compile time (e.g. IOException, SQLException). Must handle using try-catch OR throws.\nUnchecked: Happens at runtime (e.g. ArithmeticException, NullPointerException)."
        },
        {
            "name": "4. Basic try-catch Execution",
            "explanation": "Core execution flow when an exception occurs.",
            "example": "try {\n    int a = 10 / 0;   // risky code\n} catch (ArithmeticException e) {\n    System.out.println(\"Cannot divide by zero\");\n}\n\nExecution Step-by-Step:\n1. JVM enters try block -> Executes 10 / 0\n2. Exception occurs -> ArithmeticException\n3. JVM stops normal flow\n4. Searches matching catch block\n5. Executes catch -> Program continues"
        },
        {
            "name": "5. Multiple Catch Blocks",
            "explanation": "Handling different errors specifically.",
            "example": "try {\n    int arr[] = new int[2];\n    arr[5] = 10;\n} catch (ArithmeticException e) {\n    System.out.println(\"Arithmetic Error\");\n} catch (ArrayIndexOutOfBoundsException e) {\n    System.out.println(\"Array Index Error\");\n}\n\nWorking:\nJVM checks catch blocks top to bottom. Executes the FIRST matching one."
        },
        {
            "name": "6. FINALLY Block",
            "explanation": "Always executes regardless of whether an exception occurred. Usually used to close files or release resources.",
            "example": "try {\n    int a = 10 / 2;\n} catch (Exception e) {\n    System.out.println(\"Error\");\n} finally {\n    System.out.println(\"Always runs\");\n}"
        },
        {
            "name": "7. Throw vs Throws",
            "explanation": "throw: Used to manually create an exception INSIDE a method.\nthrows: Used to declare an exception in the method signature.",
            "example": "THROW:\nstatic void checkAge(int age) {\n    if (age < 18) throw new ArithmeticException(\"Not eligible\");\n}\n\nTHROWS:\nstatic void readFile() throws IOException {\n    FileReader file = new FileReader(\"test.txt\");\n}"
        },
        {
            "name": "8. Custom Exception",
            "explanation": "Creating user-defined exceptions by extending the Exception class (Very important for interviews).",
            "example": "class InvalidAmountException extends Exception {\n    public InvalidAmountException(String msg) { super(msg); }\n}\n\nclass Bank {\n    void withdraw(int amount) throws InvalidAmountException {\n        if (amount > 1000) throw new InvalidAmountException(\"Limit exceeded\");\n    }\n}\n// Working: Condition fails -> throws custom exception -> JVM catches and prints message."
        },
        {
            "name": "9. Try with Resources",
            "explanation": "Advanced feature to automatically close resources without needing a finally block.",
            "example": "try (FileReader file = new FileReader(\"test.txt\")) {\n    System.out.println(\"File opened\");\n} catch (IOException e) {\n    System.out.println(\"Error\");\n}\n// Advantage: Auto closes resources."
        }
    ]
}

data['oop']['description'] = "Deep-dive examples covering advanced OOP implementations like Exception Handling."
data['oop']['categories'] = [oop_example_category]

with open(filepath, 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=4)
print("Updated OOP Examples")
