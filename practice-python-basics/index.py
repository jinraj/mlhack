import logging
import time

# Configure logging with a custom format
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(filename)s:%(lineno)d - %(message)s'
)

allowed_operations = ["sum", "multiply", "divide", "sum_range"]

def calculate_selected(a, b, operations):
    try:
        logging.info("Starting calculations for selected operations with inputs: a=%s, b=%s, operations=%s", a, b, operations)
        validate_input(a, b, operations)  # Validate inputs


        results = {}
        for operation in operations:
            if not isinstance(operation, str):
                logging.warning("Non-string operation detected: %s", operation)
                results[operation] = {"error": f"Invalid operation: '{operation}' must be a string."}
                continue

            if operation.lower() not in allowed_operations:
                logging.warning("Invalid operation: %s", operation)
                results[operation] = {"error": f"Invalid operation: '{operation}' is not supported."}
                continue

            start_time = time.perf_counter()
            logging.debug("Starting operation: %s", operation)

            if operation == "sum":
                result = perform_sum(a, b)
            elif operation == "multiply":
                result = perform_multiply(a, b)
            elif operation == "divide":
                result = perform_divide(a, b)
            elif operation == "sum_range":
                result = perform_sum_range(a, b)

            end_time = time.perf_counter()
            time_taken = end_time - start_time
            logging.info("Operation '%s' completed. Result: %s, Time taken: %.6f seconds", operation, result, time_taken)
            results[operation] = {"result": result, "time_taken": time_taken}

        return results
    except (TypeError, ValueError) as e:
        logging.error("Error occurred: %s", e)
        return {"error": str(e)}

def validate_input(a, b, operations):
    logging.debug("Validating inputs: a=%s, b=%s, operations=%s", a, b, operations)
    if not isinstance(a, (int, float)):
        raise TypeError("Input 'a' must be a number (int or float).")
    if not isinstance(b, (int, float)):
        raise TypeError("Input 'b' must be a number (int or float).")
    if not (100 <= a <= 1000):
        raise ValueError("Input 'a' must be in the range of 100 to 1000.")
    if not (100 <= b <= 1000):
        raise ValueError("Input 'b' must be in the range of 100 to 1000.")
    if not isinstance(operations, list):
        raise TypeError("Input 'operations' must be a list.")
    if not operations:
        raise ValueError("No operations provided. Please specify at least one operation.")
    for operation in operations:
        if not isinstance(operation, str):
            raise TypeError(f"Invalid operation: '{operation}' must be a string.")
def perform_sum(a, b):
    logging.debug("Performing sum operation: a=%s, b=%s", a, b)
    return a + b + 100

def perform_multiply(a, b):
    logging.debug("Performing multiply operation: a=%s, b=%s", a, b)
    return a * b + 500

def perform_divide(a, b):
    logging.debug("Performing divide operation: a=%s, b=%s", a, b)
    if b == 0:
        raise ValueError("Division by zero is not allowed.")
    return (a + 12) / b

def perform_sum_range(a, b):
    logging.debug("Performing sum_range operation: a=%s, b=%s", a, b)
    if a > b:
        raise ValueError("'a' must be less than or equal to 'b' for sum_range operation.")
    return sum(range(int(a), int(b) + 1))

# Example usage
operations_to_perform = []
results = calculate_selected(111111, 200, operations_to_perform)

# Check if the results contain an error
if "error" in results:
    print(f"Error: {results['error']}")
else:
    for operation, details in results.items():
        if "error" in details:
            print(f"Operation: {operation}, Error: {details['error']}")
        else:
            print(f"Operation: {operation}, Result: {details['result']}, Time Taken: {details['time_taken']:.6f} seconds")

