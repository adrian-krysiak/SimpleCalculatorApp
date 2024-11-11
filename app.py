import json
import logging
import argparse
import os
import numpy as np
# Setup logging
logging.basicConfig(filename="data/app.log", level=logging.INFO,
                    format="%(asctime)s - %(message)s")
# Data persistence (results storage)
RESULTS_FILE = os.path.join("data", "results.json")


def save_results(results):
    try:
        with open(RESULTS_FILE, "w") as file:
            json.dump(results, file)
    except Exception as e:
        logging.error(f"Failed to save results: {e}")


def load_results():
    try:
        with open(RESULTS_FILE, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []
    except Exception as e:
        logging.error(f"Failed to load results: {e}")
        return []


def add(*args):
    result = sum(args)
    logging.info(f"add({args}) = {result}")
    return result


def delete(first_number, second_number):
    result = first_number - second_number
    logging.info(f"delete({first_number}, {second_number}) = {result}")
    return result


def multiply(first_number, second_number):
    result = first_number * second_number
    logging.info(f"multiply({first_number}, {second_number}) = {result}")
    return result


def divide(first_number, second_number):
    if second_number == 0:
        logging.error("Attempted division by zero.")
        return "Error: Division by zero"
    result = first_number / second_number
    logging.info(f"divide({first_number}, {second_number}) = {result}")
    return result


def mean(numbers):
    return np.mean(numbers)


def create_parser():
    parser = argparse.ArgumentParser(
        description="Simple calculator app")
    parser.add_argument("operation",
                        choices=["add", "delete", "multiply",
                                 "divide", "mean"],
                        help="Math operation")
    parser.add_argument("numbers", nargs="+", type=float,
                        help="Numbers for the operation")
    return parser


def main():
    parser = create_parser()
    args = parser.parse_args()
    
    # Load previous results
    results = load_results()

    try:
        if args.operation == "add":
            result = add(*args.numbers)
        elif args.operation == "delete":
            result = delete(args.numbers[0], args.numbers[1])
        elif args.operation == "multiply":
            result = multiply(args.numbers[0], args.numbers[1])
        elif args.operation == "divide":
            result = divide(args.numbers[0], args.numbers[1])
        elif args.operation == 'mean':
            if len(args.numbers) < 1:
                raise ValueError("Error: 'mean' operation requires at least"
                                 "one number.")
            result = mean(args.numbers)

    except Exception as e:
        raise ValueError(f"Error: operation requires a"
                         f"correct command and exactly two numbers")
    
    # Save result
    results.append({"operation": args.operation, "numbers": args.numbers,
                    "result": result})
    save_results(results)

    print(f"Result: {result}")


if __name__ == "__main__":
    main()
