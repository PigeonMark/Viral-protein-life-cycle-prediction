import argparse

from PaperSelection import Selector
from Counting import Counter
from Combine import Combiner
from FeatureExtraction import FeatureExtraction
import Review

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-s', '--select', action='store_true')
    parser.add_argument('-t', '--test', action='store_true')
    parser.add_argument('-c', '--count', action='store_true')
    parser.add_argument('-m', '--merge', '--combine', action='store_true')
    parser.add_argument('-e', '--extract', action='store_true')
    parser.add_argument('-r', '--review', action='store_true')

    args = parser.parse_args()

    if args.select:
        if args.test:
            selector = Selector("config/Test/selection_config.json")
        else:
            selector = Selector("config/selection_config.json")
        selector.select()
        selector.selected_to_folder()

    if args.count:
        if args.test:
            counter = Counter("config/Test/counter_config.json")
        else:
            counter = Counter("config/counter_config.json")
        counter.count_all_viruses()

    if args.merge:
        if args.test:
            combiner = Combiner("config/Test/combiner_config.json")
        else:
            combiner = Combiner("config/combiner_config.json")
        combiner.combine_all_viruses()

    if args.extract:
        if args.test:
            feature_extractor = FeatureExtraction("config/Test/feature_extraction_config.json")
        else:
            feature_extractor = FeatureExtraction("config/feature_extraction_config.json")
        feature_extractor.extract()

    if args.review:
        Review.run()


if __name__ == "__main__":
    main()
