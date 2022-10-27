import json
import random

# import the yelp review dataset
data_file = open("yelp_dataset/yelp_academic_dataset_review.json")
data = []
stop_line = 0
for line in data_file:
    if stop_line == 20:
        break
    else:
        data.append(json.loads(line)['text'])
        stop_line += 1
data_file.close()

dataset = list(map(len, data))


class Cluster:
    def __init__(self, clus_center):
        self.elements = []
        self.centroid = clus_center

    def getElements(self):
        return self.elements

    def getCentroid(self):
        return self.centroid

    def setCentroid(self, cent):
        self.centroid = cent

    def addElement(self, newElement):
        self.elements.append(newElement)

    def newCentroid(self):
        return self.centroid if len(self.elements) == 0 else sum(self.elements)/len(self.elements)

    def resetElement(self):
        self.elements.clear()


def kMeans(data, noClus):
    clusters = [Cluster(random.randint(0, max(data))) for i in range(noClus)]
    centroid_threshold = 0.00005
    ite_count = 0

    while True:
        ite_count += 1
        # assign elements for each cluster
        for datapoint in data:
            distance = [0 for i in range(noClus)]
            for i in range(noClus):
                distance[i] = abs(datapoint - clusters[i].getCentroid())
            minIdx = distance.index(min(distance))
            clusters[minIdx].addElement(datapoint)

        # print
        print("Iteration #", ite_count, sep=None)
        for cluster in clusters:
            print(round(cluster.getCentroid()), cluster.getElements())

        # calculate new centroids
        new_centroids = [clusters[i].newCentroid() for i in range(noClus)]
        centroid_diff = [clusters[i].getCentroid() - new_centroids[i]
                         for i in range(noClus)]

        # update centroid and reset if diff > threshold
        if all(i <= centroid_threshold for i in centroid_diff):
            break
        else:
            for i in range(noClus):
                clusters[i].centroid = new_centroids[i]
                clusters[i].resetElement()


kMeans(dataset, 3)
