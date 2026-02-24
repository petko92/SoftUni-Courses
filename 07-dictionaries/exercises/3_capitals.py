#Read user input
country_names = input().split(", ")
capitals = input().split(", ")
#Logic
capital_by_country = {}
for key, value in zip(country_names, capitals):
    capital_by_country[key] = value
#Extract data, Print output
for country, capital in capital_by_country.items():
    print(f"{country} -> {capital}")


'''

3.	Capitals
Using dictionary comprehension, write a program that receives country names on the first line,
separated by comma and space ", ", and their corresponding capital cities on the second line
(again separated by comma and space ", ").
Print each country with its capital on a separate line in the following format: "{country} -> {capital}".
Hints
•	You could use the zip() method.
Examples
Input	                                  Output
Bulgaria, Romania, Germany, England
Sofia, Bucharest, Berlin, London	    Bulgaria -> Sofia
                                        Romania -> Bucharest
                                        Germany -> Berlin
                                        England -> London

'''