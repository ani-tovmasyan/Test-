import pandas as pd
import matplotlib.pyplot as plt


class Plot:
    def draw_plots(self, url, path):
        data = pd.read_json(url)
        features = data.columns[1:]
        length = len(features)
        paths = []
        for i in range(length):
            for j in range(i, length):
                plt.figure()
                plt.scatter(data[features[i]], data[features[j]])
                plt.savefig(path+features[i] + '_' + features[j] + '.png')
                paths.append(path+features[i] + '_' + features[j] + '.png')
        print('hello')
        return paths

