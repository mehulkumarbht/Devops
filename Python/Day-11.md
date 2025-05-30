def check_required_keys(config_path):
    required_keys = {"host", "port", "auth"}

    try:
        with open (config_path,"r") as file:
            config_data = json.load(file)

        missing_keys= required_keys - config_data.keys()

        if missing_keys:
            print(f"Missing required keys: {', '.join(missing_keys)}")
            return False
        else:
            print("All required keys are present")
            return True
    except FileNotFoundError :
        print(f"File not found: {config_path}")
        return False
    except json.JSONDecodeError:
        print(f"Invalid JSON format in: {config_path}")
        return False
    