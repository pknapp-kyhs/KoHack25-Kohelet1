import json
class Search:
        
    def load_json(self, json_file):
        """Load the JSON file and return data."""
        try:
            with open(json_file, 'r', encoding='utf-8') as file:
                return json.load(file)  # Load as a list of dictionaries
        except FileNotFoundError:
            print("Error: JSON file not found.")
            return []
        except json.JSONDecodeError:
            print("Error: Invalid JSON format.")
            return []
    
    def search_json(self, json_data, keyword):
        """Search for a keyword in the values of each JSON object."""
        keyword = keyword.lower()  # Case-insensitive search
        matches = []
    
        for obj in json_data:  # Loop through each JSON object
            if any(keyword in str(value).lower() for value in obj.values()):
                matches.append(obj)  # Store matching JSON objects
    
        return matches if matches else "No matches found."
    
    # Example Usage

    