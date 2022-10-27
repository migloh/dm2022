import json


def review_list(no_of_reviews):
    # import the yelp review dataset
    data_file = open("yelp_dataset/yelp_academic_dataset_review.json")
    data = []
    stop_line = 0
    while stop_line < no_of_reviews:
        for line in data_file:
            if stop_line == no_of_reviews:
                break
            else:
                data.append(json.loads(line)['text'])
                stop_line += 1
    data_file.close()
    return data
