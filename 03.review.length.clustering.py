import json

# constant
INF = 9999999999

# import the yelp review dataset
data_file = open("yelp_dataset/yelp_academic_dataset_review.json")
data = []
stop_line = 0
for line in data_file:
    if stop_line == 15:
        break
    else:
        data.append(json.loads(line)['text'])
        stop_line += 1
data_file.close()


def review_len(n):
    return len(n)


len_dataset = list(map(review_len, data))


def initClusters(reviews):
    clusters = []
    for i in reviews:
        clusters.append([i])

    return clusters


def distanceMatrix(clus):
    initMat = [[None for col in range(len(clus))]
               for row in range(len(clus))]

    for i in range(0, len(clus)-1):
        for j in range(i+1, len(clus)):
            initMat[i][j] = calCluster(clus[i], clus[j])

    return initMat


def calCluster(c1, c2):
    arrOfVal = []
    for i in c1:
        for j in c2:
            arrOfVal.append(abs(i-j))

    return min(arrOfVal)


def findMinCoor(mat):
    coor = [0, 0]
    min = INF
    for i in range(0, len(mat)-1):
        for j in range(i+1, len(mat)):
            if mat[i][j] < min:
                min = mat[i][j]
                coor[0] = i
                coor[1] = j
            else:
                continue

    return coor


def recluster(clusters, min_coor):
    clusters[min_coor[0]] = clusters[min_coor[0]] + clusters[min_coor[1]]
    del clusters[min_coor[1]]


def min_clustering(data, no_of_clusters):
    clusters = initClusters(data)
    print(clusters)
    while len(clusters) > no_of_clusters:
        mat = distanceMatrix(clusters)
        mini = findMinCoor(mat)
        recluster(clusters, mini)
        print(clusters)


# min clustering with 3 clusters
min_clustering(len_dataset, 3)
