import pycountry

def get_country_code(country_name):
    try:
        # Normalize the input to title case
        country_name_normalized = country_name.strip().title()
        country = pycountry.countries.get(name=country_name_normalized)
        if country:
            return country.alpha_3, None  # ISO 3166-1 Alpha-3 code
        else:
            return None, "Invalid country name"
    except Exception as e:
        return None, str(e)