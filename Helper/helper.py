import pycountry

# Convert 2-letter country code to full name
def get_country_name(code):
    country = pycountry.countries.get(alpha_2=code)
    if country:
        return country.name
    return code