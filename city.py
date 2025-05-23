import pandas as pd

# Load the CSV
df = pd.read_csv("comp.csv")

# City-to-state mapping
city_to_state = {
    "Ahmedabad": "Gujarat",
    "Ahmednagar": "Maharashtra",
    "Aizawl": "Mizoram",
    "Alappuzha": "Kerala",
    "Alwar": "Rajasthan",
    "Ambala": "Haryana",
    "Amritsar": "Punjab",
    "Anand": "Gujarat",
    "Anantapur": "Andhra Pradesh",
    "Andheri": "Maharashtra",
    "Anjar": "Gujarat",
    "Ankleshwar": "Gujarat",
    "Asansol": "West Bengal",
    "Attur": "Tamil Nadu",
    "Aundh": "Maharashtra",
    "Azadpur": "Delhi",
    "Bandra": "Maharashtra",
    "Banswada": "Telangana",
    "Bardez": "Goa",
    "Bareilly": "Uttar Pradesh",
    "Belagavi": "Karnataka",
    "Belgaum": "Karnataka",
    "Bengaluru": "Karnataka",
    "Bhavnagar": "Gujarat",
    "Bhopal": "Madhya Pradesh",
    "Bhubaneshwar": "Odisha",
    "Bhubaneswar": "Odisha",
    "Bicholim": "Goa",
    "Bihar": "Bihar",
    "Bijapur": "Karnataka",
    "Bikaner": "Rajasthan",
    "Bir": "Himachal Pradesh",
    "Boaz": "Not in India",  # Possible error, not mapped
    "Calicut": "Kerala",
    "Chandigarh": "Chandigarh",
    "Chanditala": "West Bengal",
    "Chattarpur": "Madhya Pradesh",
    "Chengalpattu": "Tamil Nadu",
    "Chennai": "Tamil Nadu",
    "Chittoor": "Andhra Pradesh",
    "Coimbatore": "Tamil Nadu",
    "Cuttack": "Odisha",
    "Dambuk": "Arunachal Pradesh",
    "Darbhanga": "Bihar",
    "Darjeeling": "West Bengal",
    "Davangere": "Karnataka",
    "Dehradun": "Uttarakhand",
    "Deoria": "Uttar Pradesh",
    "Dhar": "Madhya Pradesh",
    "Dharuhera": "Haryana",
    "Dharwad": "Karnataka",
    "Dibrugarh": "Assam",
    "Durgapur": "West Bengal",
    "Ernakulam": "Kerala",
    "Faridabad": "Haryana",
    "Farrukhabad": "Uttar Pradesh",
    "Gandhinagar": "Gujarat",
    "Gangtok": "Sikkim",
    "Gautambudh Nagar": "Uttar Pradesh",
    "Ghaziabad": "Uttar Pradesh",
    "Ghazipur": "Uttar Pradesh",
    "Goa": "Goa",
    "Gondia": "Maharashtra",
    "Goregaon": "Maharashtra",
    "Greater Noida": "Uttar Pradesh",
    "Gurugram": "Haryana",
    "Guwahati": "Assam",
    "Gwalior": "Madhya Pradesh",
    "Haridwar": "Uttarakhand",
    "Hosur": "Tamil Nadu",
    "Howrah": "West Bengal",
    "Hubballi": "Karnataka",
    "Hyderabad": "Telangana",
    "Indore": "Madhya Pradesh",
    "Jabalpur": "Madhya Pradesh",
    "Jaipur": "Rajasthan",
    "Jalandhar": "Punjab",
    "Jalgoan": "Maharashtra",  # Likely meant "Jalgaon"
    "Jamshedpur": "Jharkhand",
    "Jhansi": "Uttar Pradesh",
    "Jodhpur": "Rajasthan",
    "Jorhat": "Assam",
    "Juhu": "Maharashtra",
    "Kandi": "West Bengal",
    "Kanpur": "Uttar Pradesh",
    "Kiratpur": "Uttar Pradesh",
    "Kochi": "Kerala",
    "Kolkata": "West Bengal",
    "Kormangala": "Karnataka",
    "Kota": "Rajasthan",
    "Kottayam": "Kerala",
    "Kozhikode": "Kerala",
    "Kuppam": "Andhra Pradesh",
    "Kurla": "Maharashtra",
    "Leh": "Ladakh",
    "Lonavala": "Maharashtra",
    "Lucknow": "Uttar Pradesh",
    "Ludhiana": "Punjab",
    "Madanpur": "West Bengal",
    "Madhapur": "Telangana",
    "Madurai": "Tamil Nadu",
    "Mahuva": "Gujarat",
    "Malad": "Maharashtra",
    "Malappuram": "Kerala",
    "Mandya": "Karnataka",
    "Mangaldoi": "Assam",
    "Mangalore": "Karnataka",
    "Manipal": "Karnataka",
    "Mavelikara": "Kerala",
    "Mehsana": "Gujarat",
    "Mohali": "Punjab",
    "Morbi": "Gujarat",
    "Mumbai": "Maharashtra",
    "Muzaffarpur": "Bihar",
    "Mysuru": "Karnataka",
    "Nagaon": "Assam",
    "Nagpur": "Maharashtra",
    "Nashik": "Maharashtra",
    "Navi Mumbai": "Maharashtra",
    "Neemuch": "Madhya Pradesh",
    "Nelamangala": "Karnataka",
    "New Delhi": "Delhi",
    "Noida": "Uttar Pradesh",
    "Palakkad": "Kerala",
    "Palghar": "Maharashtra",
    "Palwal": "Haryana",
    "Panaji": "Goa",
    "Panchkula": "Haryana",
    "Panipat": "Haryana",
    "Panjim": "Goa",
    "Parel": "Maharashtra",
    "Patna": "Bihar",
    "Pilani": "Rajasthan",
    "Pondicherry": "Puducherry",
    "Porvorim": "Goa",
    "Prayagraj": "Uttar Pradesh",
    "Puducherry": "Puducherry",
    "Pune": "Maharashtra",
    "Raichur": "Karnataka",
    "Raipur": "Chhattisgarh",
    "Rajkot": "Gujarat",
    "Rajnandgaon": "Chhattisgarh",
    "Ranchi": "Jharkhand",
    "Rangia": "Assam",
    "Ratnagiri": "Maharashtra",
    "Rohtak": "Haryana",
    "Roorkee": "Uttarakhand",
    "Rudrapur": "Uttarakhand",
    "Salem": "Tamil Nadu",
    "Sangareddy": "Telangana",
    "Sanquelim": "Goa",
    "Santa Cruz": "Maharashtra",
    "Secunderabad": "Telangana",
    "Shillong": "Meghalaya",
    "Shimla": "Himachal Pradesh",
    "Shivpuri": "Madhya Pradesh",
    "Siliguri": "West Bengal",
    "Sohna": "Haryana",
    "Solan": "Himachal Pradesh",
    "Solapur": "Maharashtra",
    "Sonipat": "Haryana",
    "Srinagar": "Jammu and Kashmir",
    "Surat": "Gujarat",
    "Thane": "Maharashtra",
    "Thanjavur": "Tamil Nadu",
    "Thiruvananthapuram": "Kerala",
    "Thrissur": "Kerala",
    "Tiruchirappalli": "Tamil Nadu",
    "Tirunelveli": "Tamil Nadu",
    "Tiruppur": "Tamil Nadu",
    "Trivandrum": "Kerala",  # Alternate name for Thiruvananthapuram
    "Tumkur": "Karnataka",
    "Udaipur": "Rajasthan",
    "Udupi": "Karnataka",
    "Vadodara": "Gujarat",
    "Vapi": "Gujarat",
    "Varanasi": "Uttar Pradesh",
    "Verna": "Goa",
    "Vijayawada": "Andhra Pradesh",
    "Vikhroli": "Maharashtra",
    "Visakhapatnam": "Andhra Pradesh",
    "Yamuna Nagar": "Haryana"
}

# Add 'state' column based on 'headquarters'
df["state"] = df["headquarters"].map(city_to_state)

# Save to new CSV
df.to_csv("comp_with_states.csv", index=False)

print("State column added and saved to 'comp_with_states.csv'")
