import coremltools
import csv

def predict_result(result, arr):
    if result['label'] == "worst":
        arr['rating'].append(1)
    elif result['label'] == "bad":
        arr['rating'].append(2)
    elif result['label'] == "enough":
        arr['rating'].append(3)
    elif result['label'] == "good":
        arr['rating'].append(4)
    else:
        arr['rating'].append(5)
     # print(result)

def main():
    arr = {}
    arr['review_id'] = []
    arr['rating'] = []

    # with open('test.csv', newline='') as csvfile:
    with open('test.csv') as f:
        spamreader = f.readlines()
        model = coremltools.models.MLModel('SentimentClassifier.mlmodel')
        # spamreader = csv.reader(csvfile, delimiter='', quotechar='|')
        text = ""
        counter = 1
        for row in spamreader:
            # temp = row[0].split(",")
            temp = row.split(",")
            if temp[0] == 'review_id':
                arr['review_id'].append("review_id")
                arr['rating'].append("rating")
                continue
            else:
                temp = row.split(str(counter) + ",")
            # print(temp)
            # tmp = next(spamreader).split(",")
            # if len(tmp) < 2:
            if len(temp) < 2:
                text += row
                continue
            else:
                if '"' in temp[1]:
                #     # print(tmp)
                    arr['review_id'].append(temp[0])
                    counter += 1
                    continue
                #     temp = row.split('"')
                #     result = model.predict({'text': text})
                #     text = ""
                # else:
                if text != "":
                    print(text)
                    result = model.predict({'text': text})
                    predict_result(result, arr)
                    text = ""
                print(temp[1])
                result = model.predict({'text': temp[1]})
                predict_result(result, arr)
                arr['review_id'].append(counter)
                counter += 1
                if counter == 19:
                    break
            # print(temp[0])
            # break

    print(arr)

    # with open('sampleSubmission.csv', mode='w') as test_file:
    #     test_writer = csv.writer(test_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

    #     for i in range(len(arr['review_id'])):
    #         test_writer.writerow([arr['review_id'][i], arr['rating'][i]])

if __name__ == "__main__":
    main()