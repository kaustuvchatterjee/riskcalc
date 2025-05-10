import math  # Import the math module

def calculate_bmi(height_cm, weight_kg):
    """
    Calculates the Body Mass Index (BMI) in kg/m².

    Args:
        height_cm (float): Height in centimeters.
        weight_kg (float): Weight in kilograms.

    Returns:
        float: The calculated BMI.  Returns None if height_cm is zero to avoid division by zero.
    """
    if height_cm <= 0:
        return None  # Handle invalid height
    height_m = height_cm / 100.0  # Convert height to meters
    bmi = weight_kg / (height_m * height_m)
    return bmi


def categorize_bmi(bmi):
    """
    Categorizes BMI into one of three categories.

    Args:
        bmi (float): The BMI value.

    Returns:
        str: The BMI category: "Low or Normal Weight", "Overweight or Pre-obesity", or "Obesity".
             Returns "Invalid BMI" if bmi is None.
    """
    if bmi is None:
        return "Invalid BMI"
    if bmi < 25:
        return "Low or Normal Weight"
    elif 25 <= bmi < 30:
        return "Overweight or Pre-obesity"
    else:
        return "Obesity"


def categorize_waist_circumference(waist_cm, gender):
    """
    Categorizes waist circumference based on sex-specific medians.

    Args:
        waist_cm (float): Waist circumference in centimeters.
        gender (str): Gender ("male" or "female").  Case-insensitive.

    Returns:
        str: The waist circumference category: "Waist Circumference ≤ Median",
             or "Waist Circumference > Median". Returns "Invalid gender" for invalid input.
    """
    gender_lower = gender.lower()  # For case-insensitive comparison
    if gender_lower == "male":
        median_wc = 94.0
    elif gender_lower == "female":
        median_wc = 78.5
    else:
        return "Invalid gender"
    if waist_cm <= median_wc:
        return "Waist Circumference ≤ Median"
    else:
        return "Waist Circumference > Median"



def identify_diabetes_risk(bmi_category, wc_category, gender):
    """
    Identifies the approximate relative and absolute 5-year risk of developing Type 2 Diabetes.

    Args:
        bmi_category (str): The BMI category.
        wc_category (str): The waist circumference category.
        gender (str): The gender ("male" or "female"). Case-insensitive.

    Returns:
        str: A string describing the relative risk (RR) and absolute risk.
             Returns an error message for invalid input combinations.
    """
    gender_lower = gender.lower()
    risk_data = {
        ("Low or Normal Weight", "Waist Circumference ≤ Median"): {
            "RR": 1.00,
            "absolute_risk": {"male": 0.79, "female": 0.28},
        },
        ("Low or Normal Weight", "Waist Circumference > Median"): {
            "RR": {"male": 3.62, "female": 2.74},
            "absolute_risk": {"male": 2.95, "female": 0.78},
        },
        ("Overweight or Pre-obesity", "Waist Circumference ≤ Median"): {
            "RR": {"male": 2.26, "female": 1.40},
            "absolute_risk": {"male": 1.80, "female": 0.39},
        },
        ("Overweight or Pre-obesity", "Waist Circumference > Median"): {
            "RR": {"male": 4.98, "female": 6.15},
            "absolute_risk": {"male": 3.92, "female": 1.72},
        },
        ("Obesity", "Waist Circumference ≤ Median"): {
            "RR": {"male": 6.62, "female": 6.15},  # Changed 0 to 0.00 for consistency
            "absolute_risk": {"male": 5.29, "female": 1.72},
        },
        ("Obesity", "Waist Circumference > Median"): {
            "RR": {"male": 11.86, "female": 15.80},
            "absolute_risk": {"male": 9.00, "female": 4.34},
        },
    }

    if (bmi_category, wc_category) in risk_data and gender_lower in risk_data[
        (bmi_category, wc_category)
    ]["absolute_risk"]:
        rr_data = risk_data[(bmi_category, wc_category)]["RR"]
        absolute_risk = risk_data[(bmi_category, wc_category)]["absolute_risk"][
            gender_lower
        ]
        if isinstance(rr_data, dict):
            rr = rr_data[gender_lower]
        else:
            rr = rr_data
        return rr, absolute_risk
    else:
        return "Risk level not identified due to invalid input combination."



if __name__ == "__main__":
    try:
        height_cm = float(input("Enter your height in centimeters: "))
        weight_kg = float(input("Enter your weight in kilograms: "))
        waist_cm = float(input("Enter your waist circumference in centimeters: "))
        gender = input("Enter your gender (male/female): ")

        bmi = calculate_bmi(height_cm, weight_kg)
        if bmi is not None:
            bmi_category = categorize_bmi(bmi)
            wc_category = categorize_waist_circumference(waist_cm, gender)

            print(f"\nYour BMI: {bmi:.2f}")  # Added formatting
            print(f"BMI Category: {bmi_category}")
            print(f"Waist Circumference Category: {wc_category}")

            if "Invalid" in wc_category:  # Changed to check "Invalid"
                print(wc_category)
            else:
                risk_assessment = identify_diabetes_risk(
                    bmi_category, wc_category, gender
                )
                print("\nType 2 Diabetes Risk Assessment:")
                print(risk_assessment)
        else:
            print("Invalid height input.")

    except ValueError:
        print(
            "Invalid input. Please enter numeric values for height, weight, and waist circumference."
        )