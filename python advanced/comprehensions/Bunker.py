def material_categories():
    mats = {x: [] for x in input().split(", ")}
    return mats


mats = material_categories()

total_quality = 0
total_quantity = 0
mats_count = int(input())
for _ in range(mats_count):
    data = input()
    mat_type = data.split(" - ")[0]
    subtype = data.split(" - ")[1]
    quantity_o = data.split(":")[1]
    quantity = int(quantity_o.split(";")[0])
    quality = int(data.split(":")[2])
    total_quality += quality
    mats[mat_type].append(subtype)
    total_quantity += quantity
print(f"Count of items: {total_quantity}")
print(f"Average quality: {total_quality / len(mats):.2f}")
[print(f'{k} -> {", ".join(v)}') for k, v in mats.items()]
