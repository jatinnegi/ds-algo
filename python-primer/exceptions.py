inventories_data = {"T-Shirt": 4, "Camera": 9, "Screwdriver": 2}

try:
    print(inventories_data["Phone"])
    print(24 / 0)
except ZeroDivisionError:
    print("Attempt to divide by 0")
except KeyError as e:
    print(f"Key not found: {e}")
except AttributeError as e:
    print(e)
except IOError as e:
    print(e)
except IndexError as e:
    print(e)
except Exception as e:
    print(e)
