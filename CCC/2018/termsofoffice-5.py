start_year = int(input())
end_year = int(input())

def range_function(start_year,end_year):
    years = []
    for year in range (start_year, end_year + 1, 60):
        years.append(year)
    return years

# years = range_function(start_year,end_year)
# # for year in years: 
# #     print("All positions change in year", year)

for year in range_function(start_year,end_year):
    print("All positions change in year", year)