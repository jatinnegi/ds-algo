def process_data(data):
    try:
        if not data:
            raise ValueError("Data is empty")
        print(f"Processing {data}")
    except ValueError as e:
        print(f"Handling exception: {e}")
        raise


try:
    process_data("")
except ValueError as e:
    print(f"Caught re-raised exception: {e}")
