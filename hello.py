import subprocess
from datetime import datetime

def get_cpu_temperature():
    result = subprocess.run(['vcgencmd', 'measure_temp'], capture_output=True, text=True)
    return result.stdout.strip()

def main():
    print("Hello from Hris-Pi!")
    cpu_temp = get_cpu_temperature()
    current_datetime = datetime.now()
    print("Current Date and Time:", current_datetime)
    print(f"Current CPU Temperature: {cpu_temp}")

if __name__ == "__main__":
    main()