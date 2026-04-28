import json

file_path = "frontend-app/src/data/cs_notes.json"

try:
    with open(file_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    oop_topics = [
        {
            "id": "python-oop",
            "title": "Python OOP Fundamentals",
            "description": "Master Object-Oriented Programming with Python's clean and elegant syntax.",
            "cards": [
                {
                    "type": "text",
                    "heading": "1. Classes and Objects",
                    "content": "**What is a Class?** A blueprint for creating objects. It defines attributes and methods.\n**What is an Object?** An instance of a class with actual values.\n\n<pre class='bg-gray-100 p-4 rounded-lg overflow-x-auto text-sm text-gray-800 font-mono'>class Car:\n    def __init__(self, brand, color):  # Constructor\n        self.brand = brand\n        self.color = color\n        self.speed = 0\n    \n    def accelerate(self):\n        self.speed += 10\n        print(f\"{self.brand} is now going {self.speed} km/h\")\n\nmy_car = Car(\"Toyota\", \"Red\")\nmy_car.accelerate()</pre>\n\n**Key Points:**\n• Use `class` keyword.\n• `__init__` is the constructor.\n• `self` refers to the current instance.\n• No `new` keyword needed."
                },
                {
                    "type": "text",
                    "heading": "2. Encapsulation",
                    "content": "**What is Encapsulation?** Bundling data and methods together, restricting direct access.\n\n**Naming Conventions:**\n• `public`: No underscore\n• `_protected`: Single underscore (convention)\n• `__private`: Double underscore (name mangling)\n\n<pre class='bg-gray-100 p-4 rounded-lg overflow-x-auto text-sm text-gray-800 font-mono'>class BankAccount:\n    def __init__(self, start_balance):\n        self.__balance = start_balance  # Private\n    \n    @property\n    def balance(self):\n        return self.__balance\n\naccount = BankAccount(1000)\nprint(account.balance)  # Uses getter</pre>"
                },
                {
                    "type": "text",
                    "heading": "3. Inheritance",
                    "content": "**What is Inheritance?** Allows a class to inherit attributes and methods from another class. Python supports Single, Multiple, Multilevel, and Hierarchical inheritance.\n\n<pre class='bg-gray-100 p-4 rounded-lg overflow-x-auto text-sm text-gray-800 font-mono'>class Animal:\n    def eat(self): print(\"Eating\")\n\nclass Dog(Animal):\n    def bark(self): print(\"Woof!\")\n\nmy_dog = Dog()\nmy_dog.eat()   # Inherited</pre>\n\n**Method Resolution Order (MRO):** `print(ClassName.__mro__)` shows the lookup order for methods in multiple inheritance."
                },
                {
                    "type": "text",
                    "heading": "4. Polymorphism",
                    "content": "**What is Polymorphism?** Treating objects of different classes generically. Python uses \"Duck Typing\" (if it walks and quacks like a duck, it's a duck!).\n\n<pre class='bg-gray-100 p-4 rounded-lg overflow-x-auto text-sm text-gray-800 font-mono'>class Dog: def speak(self): return \"Woof!\"\nclass Cat: def speak(self): return \"Meow!\"\n\ndef animal_sound(animal): print(animal.speak())\n\nanimal_sound(Dog())\nanimal_sound(Cat())</pre>\n\n**Operator Overloading:** Overriding magic methods like `__add__` to change how operators like `+` work with objects."
                },
                {
                    "type": "text",
                    "heading": "5. Abstraction & Magic Methods",
                    "content": "**Abstract Base Classes (ABC):** Force child classes to implement methods.\n<pre class='bg-gray-100 p-4 rounded-lg overflow-x-auto text-sm text-gray-800 font-mono'>from abc import ABC, abstractmethod\nclass Vehicle(ABC):\n    @abstractmethod\n    def start(self): pass</pre>\n\n**Common Magic Methods (Dunder Methods):**\n• `__init__`: Constructor\n• `__str__`: User-friendly string\n• `__repr__`: Developer-friendly string\n• `__eq__`: Equality (`==`)\n• `__lt__`, `__gt__`: Comparisons (`<`, `>`)\n• `__add__`, `__sub__`: Arithmetic (`+`, `-`)\n• `__len__`: Length (`len()`)"
                }
            ]
        },
        {
            "id": "java-oop",
            "title": "Java OOP Fundamentals",
            "description": "Object-Oriented Programming principles strictly enforced in Java.",
            "cards": [
                {
                    "type": "text",
                    "heading": "1. Classes and Objects",
                    "content": "**What is a Class?** A blueprint or template for creating objects. It defines properties (fields) and behaviors (methods).\n**What is an Object?** An instance of a class \u2013 a concrete entity created from the blueprint.\n\n<pre class='bg-gray-100 p-4 rounded-lg overflow-x-auto text-sm text-gray-800 font-mono'>public class Car {\n    String brand;\n    String color;\n    int speed;\n    \n    public Car(String brand, String color) {\n        this.brand = brand;\n        this.color = color;\n        this.speed = 0;\n    }\n    \n    public void accelerate() {\n        speed += 10;\n        System.out.println(brand + \" is going \" + speed + \" km/h\");\n    }\n}\n\npublic class Main {\n    public static void main(String[] args) {\n        Car myCar = new Car(\"Toyota\", \"Red\");\n        myCar.accelerate();\n    }\n}</pre>\n\n**Key Points:**\n\u2022 Use `class` keyword.\n\u2022 Use `new` keyword to create objects.\n\u2022 `this` refers to current object.\n\u2022 Constructor has same name as class."
                },
                {
                    "type": "text",
                    "heading": "2. Encapsulation",
                    "content": "**What is Encapsulation?** Bundling data (fields) and methods within a class, and restricting direct access to some components.\n\n**Access Modifiers:**\n\u2022 `private`: Only accessible within the class\n\u2022 `protected`: Accessible within package and subclasses\n\u2022 `public`: Accessible from anywhere\n\u2022 `default`: Accessible within the same package\n\n<pre class='bg-gray-100 p-4 rounded-lg overflow-x-auto text-sm text-gray-800 font-mono'>public class BankAccount {\n    private double balance;\n    \n    public BankAccount(double initialBalance) {\n        this.balance = initialBalance;\n    }\n    \n    public double getBalance() { return balance; }\n    \n    public void deposit(double amount) {\n        if (amount > 0) balance += amount;\n    }\n}</pre>\n\n**Benefits:** Data hiding, controlled access, and validation before modification."
                },
                {
                    "type": "text",
                    "heading": "3. Inheritance",
                    "content": "**What is Inheritance?** Allows a child class (subclass) to inherit properties and methods from a parent class (superclass).\n\n**Types in Java:** Single, Multilevel, Hierarchical. (Note: Java doesn't support multiple inheritance with classes - use interfaces).\n\n<pre class='bg-gray-100 p-4 rounded-lg overflow-x-auto text-sm text-gray-800 font-mono'>public class Animal {\n    protected String name;\n    public Animal(String name) { this.name = name; }\n    public void eat() { System.out.println(\"Eating\"); }\n}\n\npublic class Dog extends Animal {\n    public Dog(String name) { super(name); }\n    @Override\n    public void eat() { System.out.println(name + \" eating dog food\"); }\n}</pre>\n\n**Key Points:** Use `extends` keyword. `super` refers to parent class. Use `@Override` annotation for overridden methods. Child class inherits all non-private members."
                },
                {
                    "type": "text",
                    "heading": "4. Polymorphism",
                    "content": "**What is Polymorphism?** \"Many forms\". Allows objects to be treated as instances of their parent class while behaving according to their actual class.\n\n**Compile-time (Static): Method Overloading**\nSame method name, different parameters.\n<pre class='bg-gray-100 p-4 rounded-lg overflow-x-auto text-sm text-gray-800 font-mono'>public int add(int a, int b) { return a + b; }\npublic double add(double a, double b) { return a + b; }</pre>\n\n**Runtime (Dynamic): Method Overriding**\n<pre class='bg-gray-100 p-4 rounded-lg overflow-x-auto text-sm text-gray-800 font-mono'>Shape[] shapes = { new Circle(5), new Rectangle(4, 6) };\nfor (Shape shape : shapes) {\n    shape.draw();  // Calls appropriate overridden method\n}</pre>"
                },
                {
                    "type": "text",
                    "heading": "5. Abstraction",
                    "content": "**What is Abstraction?** Hiding complex implementation details and showing only essential features.\n\n**Abstract Classes vs Interfaces:**\n<pre class='bg-gray-100 p-4 rounded-lg overflow-x-auto text-sm text-gray-800 font-mono'>// Abstract class - cannot instantiate directly\npublic abstract class Vehicle {\n    public abstract void start(); // Must be implemented by child\n    public void display() { }      // Concrete method allowed\n}\n\n// Interface - 100% Abstraction\npublic interface Flyable {\n    void fly(); // implicitly public abstract\n}</pre>\n\n**Abstract Class vs Interface:**\n\u2022 **Methods:** Abstract classes can have both abstract and concrete. Interfaces all abstract (Java 8+ can have default methods).\n\u2022 **Variables:** Abstract classes can have instance variables. Interfaces only have constants (`public static final`).\n\u2022 **Inheritance:** Single inheritance for classes vs Multiple interfaces.\n\u2022 **Constructor:** Classes have them, interfaces don't."
                }
            ]
        },
        {
            "id": "cpp-oop",
            "title": "C++ OOP Fundamentals",
            "description": "Object-Oriented Programming featuring manual memory management and pointers in C++.",
            "cards": [
                {
                    "type": "text",
                    "heading": "1. Classes and Objects",
                    "content": "**What is a Class?** A user-defined data type containing data members and member functions.\n**What is an Object?** An instance of a class.\n\n<pre class='bg-gray-100 p-4 rounded-lg overflow-x-auto text-sm text-gray-800 font-mono'>#include &lt;iostream&gt;\nusing namespace std;\n\nclass Car {\nprivate:\n    string brand;\n    int speed;\n\npublic:\n    Car(string b) {\n        brand = b;\n        speed = 0;\n    }\n    \n    void accelerate() {\n        speed += 10;\n        cout &lt;&lt; brand &lt;&lt; \" is now going \" &lt;&lt; speed &lt;&lt; \" km/h\\n\";\n    }\n};\n\nint main() {\n    Car myCar(\"Toyota\");\n    myCar.accelerate();\n    return 0;\n}</pre>\n\n**Key Points:**\n\u2022 Access specifiers: `public`, `private`, `protected`.\n\u2022 Constructor has same name as class.\n\u2022 Use dot operator (`.`) to access members."
                },
                {
                    "type": "text",
                    "heading": "2. Encapsulation",
                    "content": "**What is Encapsulation?** Bundling data and methods together while restricting direct access to internal data.\n\n**Access Specifiers:**\n\u2022 `private`: Only accessible within the class\n\u2022 `protected`: Accessible in class and derived classes\n\u2022 `public`: Accessible from anywhere\n\n<pre class='bg-gray-100 p-4 rounded-lg overflow-x-auto text-sm text-gray-800 font-mono'>class BankAccount {\nprivate:\n    double balance;\npublic:\n    BankAccount(double initial) : balance(initial) {}\n    \n    // const indicates it doesn't modify the object\n    double getBalance() const { return balance; }\n    \n    void deposit(double amount) {\n        if (amount > 0) balance += amount;\n    }\n};</pre>"
                },
                {
                    "type": "text",
                    "heading": "3. Inheritance",
                    "content": "**What is Inheritance?** Allows a class to inherit properties and methods from another class. C++ supports Multiple Inheritance!\n\n<pre class='bg-gray-100 p-4 rounded-lg overflow-x-auto text-sm text-gray-800 font-mono'>class Animal {\nprotected:\n    string name;\npublic:\n    Animal(string n) : name(n) {}\n    void eat() { cout &lt;&lt; \"Eating\\n\"; }\n};\n\nclass Dog : public Animal {\npublic:\n    Dog(string n) : Animal(n) {} // Call base constructor\n    void eat() { cout &lt;&lt; name &lt;&lt; \" eating dog food\\n\"; }\n};</pre>\n\n**Multiple Inheritance Example:** `class Duck : public Flyable, public Swimmable { ... };`"
                },
                {
                    "type": "text",
                    "heading": "4. Polymorphism & Virtual Functions",
                    "content": "**Compile-time Polymorphism (Overloading):** Multiple functions with the same name but different parameters.\n\n**Runtime Polymorphism (Virtual Functions):**\n<pre class='bg-gray-100 p-4 rounded-lg overflow-x-auto text-sm text-gray-800 font-mono'>class Shape {\npublic:\n    virtual void draw() { cout &lt;&lt; \"Drawing shape\\n\"; }\n    virtual ~Shape() {} // Virtual destructor is essential!\n};\n\nclass Circle : public Shape {\npublic:\n    void draw() override { cout &lt;&lt; \"Drawing circle\\n\"; }\n};\n\nint main() {\n    Shape* shape = new Circle();\n    shape-&gt;draw(); // Calls Circle's draw\n    delete shape;\n}</pre>\n\n**Key Points:** `virtual` in base class, `override` in derived class. Without `virtual`, early binding calls the base method."
                },
                {
                    "type": "text",
                    "heading": "5. Abstraction & Pure Virtual Functions",
                    "content": "**Abstract Classes:** A class with at least one pure virtual function (`= 0`). Cannot be instantiated.\n\n<pre class='bg-gray-100 p-4 rounded-lg overflow-x-auto text-sm text-gray-800 font-mono'>class Vehicle {\npublic:\n    virtual void start() = 0; // Pure virtual function\n    virtual ~Vehicle() {}\n};</pre>\n\n**Interface (Pure Abstract Class):** C++ has no native `interface` keyword, but an abstract class with *only* pure virtual functions serves as an interface.\n\n**Abstract vs Interface in C++:**\n\u2022 **Abstract Class:** Can have concrete methods and data members. Partial implementation.\n\u2022 **Interface:** All pure virtual methods, usually no data. Defines a strict contract."
                },
                {
                    "type": "text",
                    "heading": "6. Templates (Generic Programming)",
                    "content": "**Templates** allow you to write generic code that works with any data type.\n\n**Function Templates:**\n<pre class='bg-gray-100 p-4 rounded-lg overflow-x-auto text-sm text-gray-800 font-mono'>template &lt;typename T&gt;\nT maximum(T a, T b) {\n    return (a > b) ? a : b;\n}\ncout &lt;&lt; maximum(10, 20); // int\ncout &lt;&lt; maximum(3.14, 2.71); // double</pre>\n\n**Class Templates:**\n<pre class='bg-gray-100 p-4 rounded-lg overflow-x-auto text-sm text-gray-800 font-mono'>template &lt;typename K, typename V&gt;\nclass Pair {\nprivate:\n    K key;\n    V value;\npublic:\n    Pair(K k, V v) : key(k), value(v) {}\n};\nPair&lt;string, int&gt; age(\"Alice\", 25);</pre>"
                }
            ]
        }
    ]

    data["oop"]["topics"] = oop_topics

    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)

    print("Updated OOP section seamlessly!")
except Exception as e:
    print(f"Error: {e}")
