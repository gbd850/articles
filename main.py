def h_index(citations):
    citations.sort()

    for i, cited in enumerate(citations):

        result = len(citations) - i

        if result <= cited:
            return result

    return 0


def minist_list(authors_articles):
    points = dict()
    for author in authors_articles:
        articles = authors_articles[author]
        if len(articles) >= 3:
            selected_articles = dict(sorted(articles.items(), reverse=True, key=lambda item: item[1])[:3])
            points[author] = (selected_articles, sum(selected_articles.values()))
        elif len(articles) <= 2:




if __name__ == '__main__':
    citations = [50, 40, 33, 23, 12, 11, 8, 5, 1, 0]
    print(h_index(citations))
    auth_art = dict()
    auth_art['Author1'] = {'article1': 4,
                           'article2': 3,
                           'article3': 2
                           }
    minist_list(auth_art)

