import sys,tweepy,csv,re
from textblob import TextBlob
import matplotlib.pyplot as plt
from pywaffle import Waffle



class SentimentAnalysis:

    def __init__(self):
        self.tweets = []
        self.tweetText = []

    def DownloadData(self):
        # authenticating
        consumerKey = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
        consumerSecret = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'             #These token secret are to be uploaded from twitter developer account 
        accessToken = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
        accessTokenSecret = 'xxxxxxxxxxxxxxxxxxxxxxxxxxx'
        auth = tweepy.OAuthHandler(consumerKey, consumerSecret)
        auth.set_access_token(accessToken, accessTokenSecret)
        api = tweepy.API(auth)

        # input for term to be searched and how many tweets to search
        searchTerm = input("Enter Keyword Tag to search about: ")
        NoOfTerms = int(input("Enter how many tweets to search: "))

        # searching for tweets
        self.tweets = tweepy.Cursor(api.search, q=searchTerm, lang = "en").items(NoOfTerms)

        # Open/create a file to append data to
        csvFile = open('result.csv', 'a')

        # Use csv writer
        csvWriter = csv.writer(csvFile)


        # creating some variables to store info
        polarity = 0
        positive = 0
        negative = 0
        neutral = 0

        neuList = []
        poList =[]
        neList = []


        # iterating through tweets fetched
        for tweet in self.tweets:

            self.tweetText.append(self.cleanTweet(tweet.text).encode('utf-8'))

            analysis = TextBlob(tweet.text)

            polarity += analysis.sentiment.polarity  # adding up polarities to find the average later

            if (analysis.sentiment.polarity == 0):  # adding reaction of how people are reacting to find average later
                neutral += 1
                neu = str(analysis)
                neuList.append(neu)


            elif (analysis.sentiment.polarity > 0 and analysis.sentiment.polarity <= 1):
                positive += 1
                po = str(analysis)

                poList.append(po)


            elif (analysis.sentiment.polarity > -1 and analysis.sentiment.polarity < 0):
                negative += 1
                ne = str(analysis)

                neList.append(ne)

        total_positive = positive
        total_negative = negative
        total_neutral = neutral
        print('\n\033[1m  Neutral Tweets  \033[0m')
        for each in neuList:
            print(each)

        print('\n\033[1m  Negative Tweets \033[0m')
        for each in neList:
            print(each)

        print('\n\033[1m  Positive Tweets  \033[0m')
        for each in poList:
            print(each)



        print("\n")
        # Write to csv and close csv file
        csvWriter.writerow(self.tweetText)
        csvFile.close()

        # finding average of how people are reacting
        positive = self.percentage(positive, NoOfTerms)
        negative = self.percentage(negative, NoOfTerms)
        neutral = self.percentage(neutral, NoOfTerms)

        # finding average reaction
        polarity = polarity / NoOfTerms

        # printing out data
        print("How people are reacting on " + searchTerm + " by analyzing " + str(NoOfTerms) + " tweets.")
        print()



        print()
        print("Detailed Report: ")
        print(str(positive) + "% people thought it was positive")
        print(str(negative) + "% people thought it was negative")
        print(str(neutral) + "% people thought it was neutral")

        self.plotPieChart(positive, negative, neutral, searchTerm, NoOfTerms)
        self.plotwafflechart(total_positive, total_negative, total_neutral)


    def cleanTweet(self, tweet):
        # Tokenization
        return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t]) | (\w +:\ / \ / \S +)", " ", tweet).split())

    # function to calculate percentage
    def percentage(self, part, whole):
        temp = 100 * float(part) / float(whole)
        return format(temp, '.2f')


    #pie chart generation
    def plotPieChart(self, positive,negative, neutral, searchTerm, noOfSearchTerms):
        labels = ['Positive [' + str(positive) + '%]', 'Neutral [' + str(neutral) + '%]',
                  'Negative [' + str(negative) + '%]']
        sizes = [positive,neutral, negative]
        colors = ['green','yellow', 'red']
        patches, texts = plt.pie(sizes, colors=colors, startangle=90)
        plt.legend(patches, labels, loc="best")
        plt.title('How people are reacting on ' + searchTerm + ' by analyzing ' + str(noOfSearchTerms) + ' Tweets.')
        plt.axis('equal')
        plt.tight_layout()
        plt.show()

    #waffle plot generation
    def plotwafflechart(self,total_positive, total_negative, total_neutral,):
        data = {'Positive': total_positive, 'Neutral': total_neutral, 'Negative': total_negative}
        fig = plt.figure(
            FigureClass=Waffle,
            rows=5,
            values=data,
            colors=("#983D3D", "#232066", "#DCB732"),
            title={'label': 'How is nation reacting?', 'loc': 'left'},
            labels=["{0} ({1})".format(k, v) for k, v in data.items()],
            legend={'loc': 'lower left', 'bbox_to_anchor': (0, -0.4), 'ncol': len(data), 'framealpha': 0}
        )
        fig.gca().set_facecolor('#EEEEEE')
        fig.set_facecolor('#EEEEEE')
        plt.show()
        print()




if __name__== "__main__":
    sa = SentimentAnalysis()
    sa.DownloadData()
