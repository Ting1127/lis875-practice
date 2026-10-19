def sprint_points(feature_a, feature_b):
    return feature_a + feature_b

total = sprint_points(5, 8)
print('total points:', total)

if total > 20:
    print('Over capacity! Cut scope.')
else:
    print('Fits in this sprint.')
