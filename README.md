# Simple Calculator App

This is a simple command-line calculator that supports basic and advanced mathematical operations. It uses `numpy` for the `mean` operation and logs all operations and errors. Results are stored persistently in a JSON file.

## Features

- **Basic Operations**: 
  - `add`: Adds two or more numbers.
  - `delete`: Subtracts two numbers.
  - `multiply`: Multiplies two numbers.
  - `divide`: Divides two numbers (with division-by-zero handling).
  
- **Advanced Operation**: 
  - `mean`: Calculates the mean (average) of a list of numbers using `numpy`.

- **Persistent Storage**: 
  - Results of all operations are stored in a `results.json` file.

- **Logging**: 
  - All operations and errors are logged to `app.log`.

## Requirements

- **Python 3.x**: Ensure you have Python 3 installed on your system.
- **`numpy`**: Required for the `mean` operation.

You can install the required dependencies by running:

```bash
pip install numpy
```

Alternatively, you can use the `requirements.txt` file:

```
numpy
```

## Installation

1. Clone this repository to your local machine:

   ```bash
   git clone https://github.com/yourusername/calculator-app.git
   cd calculator-app
   ```

2. Create a virtual environment (recommended):

   ```bash
   python -m venv .venv
   ```

3. Activate the virtual environment:

   - On **Windows**:
     ```bash
     .venv\Scripts\activate
     ```

   - On **macOS/Linux**:
     ```bash
     source .venv/bin/activate
     ```

4. Install the dependencies:

   ```bash
   pip install -r requirements.txt
   ```

   Or, if you prefer, you can directly install `numpy`:

   ```bash
   pip install numpy
   ```

## Usage

### Running the Calculator

You can run the calculator app from the command line by passing an operation (`add`, `delete`, `multiply`, `divide`, or `mean`) followed by the numbers to operate on.

### Examples:

#### 1. Add numbers:

```bash
python app.py add 5 10
```

Output:
```
Result: 15.0
```

#### 2. Subtract (Delete) numbers:

```bash
python app.py delete 10 5
```

Output:
```
Result: 5.0
```

#### 3. Multiply numbers:

```bash
python app.py multiply 3 7
```

Output:
```
Result: 21.0
```

#### 4. Divide numbers:

```bash
python app.py divide 10 2
```

Output:
```
Result: 5.0
```

#### 5. Calculate the mean of numbers:

```bash
python app.py mean 2 8 9
```

Output:
```
Result: 6.333333333333333
```

### Error Handling
If you provide invalid arguments (such as not enough numbers for an operation), the app will raise an error and show a message. For example:

```bash
Error: 'add' operation requires at least two numbers.
```

### Data Persistence
All results of the operations are stored in `results.json`. The file will contain a list of all operations performed along with the numbers and results.

### Logging
All operations and errors are logged in `app.log`. This file contains detailed information about each operation, making it easier to debug and track.

## Running Tests

This project includes unit tests to verify that the operations are functioning correctly. To run the tests:

1. Ensure you have the dependencies installed:

   ```bash
   pip install -r requirements.txt
   ```

2. Run the tests using the `unittest` module:

   ```bash
   python -m unittest test_app.py
   ```

The test cases will verify the functionality of the calculator and ensure that it handles errors properly (e.g., missing arguments for operations).

## Contributing

Feel free to fork this repository, submit pull requests, or open issues if you encounter any bugs or have suggestions for improvements.

## License

This project is open-source and available under the [MIT License](LICENSE).
```

### Key Sections:
1. **Features**: Lists the operations and the advanced `mean` functionality.
2. **Requirements**: Describes the dependencies (`numpy`).
3. **Installation**: Provides step-by-step instructions for setting up the app.
4. **Usage**: Explains how to run the calculator, with examples for each operation.
5. **Error Handling**: Briefly explains how the app handles invalid input.
6. **Data Persistence and Logging**: Explains where results are saved and how logging is handled.
7. **Running Tests**: Describes how to run tests to verify the app's functionality.
8. **Contributing**: Invites others to contribute.
9. **License**: Mentions the open-source license.