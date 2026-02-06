# Singapore NRIC Verifier
# Author: Let's Learn More

def verify_nric(nric):
    nric = nric.strip().upper()

    # Step 1: Basic format check
    if len(nric) != 9 or not nric[1:8].isdigit() or nric[0] not in "STFG":
        print("❌ Invalid NRIC format. Example: S1234567D")
        return

    prefix = nric[0]
    digits = nric[1:8]
    check_letter = nric[-1]

    # Step 2: Define weights
    weights = [2, 7, 6, 5, 4, 3, 2]

    # Step 3: Multiply and sum
    total = sum(int(d) * w for d, w in zip(digits, weights))

    # Step 4: Add 4 if prefix is T or G
    if prefix in ("T", "G"):
        total += 4

    # Step 5: Compute remainder
    remainder = total % 11

    # Step 6: Define lookup tables
    st_mapping = ["J", "Z", "I", "H", "G", "F", "E", "D", "C", "B", "A"]
    fg_mapping = ["X", "W", "U", "T", "R", "Q", "P", "N", "M", "L", "K"]

    # Step 7: Determine expected letter
    if prefix in ("S", "T"):
        expected_letter = st_mapping[remainder]
    else:
        expected_letter = fg_mapping[remainder]

    # Step 8: Compare
    if expected_letter == check_letter:
        print(f"✅ NRIC {nric} is valid! Check letter matches ({expected_letter}).")
    else:
        print(f"❌ NRIC {nric} is invalid. Expected check letter should be '{expected_letter}'.")

# --- Main program starts here ---
print("Singapore NRIC Verifier 🇸🇬")
user_nric = input("Please enter the NRIC (e.g., S1234567D): ")
verify_nric(user_nric)
