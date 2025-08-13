import time
import os

def main():
    task_index = os.environ.get("CLOUD_RUN_TASK_INDEX", "UNKNOWN")
    print(f"Starting task #{task_index}")
    time.sleep(2)
    print(f"Task #{task_index} done")

if __name__ == "__main__":
    main()
