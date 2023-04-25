start_year = int(input())
end_year = int(input())
def range_function(start_year,end_year):
    for year in range (start_year, end_year + 1, 60):
        print("All positions change in year", year)
        
range_function(start_year,end_year)