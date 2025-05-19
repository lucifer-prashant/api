import pandas as pd

# Load the CSV
df = pd.read_csv("comp.csv")

# City-to-state mapping
city_to_state = {
    "Ahmedabad": "Gujarat",
    "Andheri": "Maharashtra",
    "Belgaum": "Karnataka",
    "Bengaluru": "Karnataka",
    "Bhubaneswar": "Odisha",
    "Chennai": "Tamil Nadu",
    "Dharuhera": "Haryana",
    "Gandhinagar": "Gujarat",
    "Gurugram": "Haryana",
    "Hyderabad": "Telangana",
    "Indore": "Madhya Pradesh",
    "Jaipur": "Rajasthan",
    "Jalgoan": "Maharashtra",
    "Kochi": "Kerala",
    "Kolkata": "West Bengal",
    "Lucknow": "Uttar Pradesh",
    "Mohali": "Punjab",
    "Mumbai": "Maharashtra",
    "Nashik": "Maharashtra",
    "Navi Mumbai": "Maharashtra",
    "New Delhi": "Delhi",
    "Noida": "Uttar Pradesh",
    "Panchkula": "Haryana",
    "Pune": "Maharashtra",
    "Rajkot": "Gujarat",
    "Rajnandgaon": "Chhattisgarh",
    "Surat": "Gujarat",
    "Thane": "Maharashtra",
    "Thiruvananthapuram": "Kerala",
    "Vadodara": "Gujarat",
    "Varanasi": "Uttar Pradesh",
    "Verna": "Goa"
}

# Add 'state' column based on 'headquarters'
df["state"] = df["headquarters"].map(city_to_state)

# Save to new CSV
df.to_csv("comp_with_states.csv", index=False)

print("State column added and saved to 'comp_with_states.csv'")
