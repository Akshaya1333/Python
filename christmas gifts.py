# cook your dish here
def max_gifts(T, dimensions):
    available_area = 1000
    results = []
    
    for i in range(T):
        H, L, W = dimensions[i]
        # Calculate the surface area of the gift box
        surface_area = 2 * (H * L + L * W + W * H)
        # Calculate the maximum number of gifts that can be wrapped
        max_gifts = available_area // surface_area
        results.append(max_gifts)
    
    return results

# Read input
T = int(input().strip())
dimensions = [tuple(map(int, input().strip().split())) for _ in range(T)]

# Get results
results = max_gifts(T, dimensions)

# Output results
for result in results:
    print(result)
