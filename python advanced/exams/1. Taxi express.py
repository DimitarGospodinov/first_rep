from collections import deque

customers = deque([int(x) for x in input().split(", ")])
taxi_drivers = deque([int(x) for x in input().split(", ")])
total_time = 0
while customers:
    if taxi_drivers:
        if customers[0] <= taxi_drivers[-1]:
            total_time += customers[0]
            customers.popleft()
            taxi_drivers.pop()
        else:
            taxi_drivers.pop()
    else:
        print(f"Not all customers were driven to their destinations")
        print(f"Customers left: {', '.join(map(str, customers))}")
        break

if not customers:
    print(f"All customers were driven to their destinations")
    print(f'Total time: {total_time} minutes')
