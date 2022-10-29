from helpers import yelp_review

review_data = yelp_review.review_list(100)
dataset = list(map(len, review_data))

TAU = 0.00005
mode_list = []
clusters = []


def fKernel(x):
    bandwidth = 20
    return 1 if x <= bandwidth else 0


def shiftMode(mode):
    newMode = sum([xj*fKernel(xj-mode) for xj in dataset]) / \
        sum([fKernel(xj-mode) for xj in dataset])
    return newMode


for i in range(len(dataset)):
    k = 0
    mode = [dataset[i]]
    while True:
        newMode = shiftMode(mode[-1])
        if abs(mode[-1] - newMode) < TAU:
            break
        else:
            mode.append(newMode)
    mode_list.append(mode[-1])


for mode in mode_list:
    if mode not in clusters:
        clusters += [mode]

print("Modes:", clusters)
# for clus in clusters:
#     arr = []
#     for datapoint in enumerate(dataset):
#         if mode_list[datapoint[0]] == clus:
#             arr.append(datapoint[1])
#         else:
#             continue
#     print(arr)
