def h_index(citations):
    citations.sort()

    for i, cited in enumerate(citations):

        result = len(citations) - i

        if result <= cited:
            return result

    return 0


def minist_list(authors_articles):
    for author in authors_articles:
        articles = authors_articles[author]
        if len(articles) < 3:
            for auth in authors_articles:
                if len(authors_articles[auth]) > 3:
                    best_article = sorted(authors_articles[auth].items(), reverse=True, key=lambda item: item[1])[0]
                    authors_articles[author][best_article[0]] = best_article[1]
                    del authors_articles[auth][best_article[0]]

    sum_articles = list()
    points = 0
    for author in authors_articles:
        articles = authors_articles[author]
        selected_articles = sorted(articles.items(), reverse=True, key=lambda item: item[1])[:3]
        selected_articles_names = [item[0] for item in selected_articles]
        selected_articles_points = [item[1] for item in selected_articles]
        sum_articles += selected_articles_names
        points += sum(selected_articles_points)

    return sum_articles, points


if __name__ == '__main__':
    citations = [50, 40, 33, 23, 12, 11, 8, 5, 1, 0]
    print(h_index(citations))
    auth_art = dict()
    auth_art['Author1'] = {'article1': 40,
                           'article2': 3,
                           'article3': 2,
                           'article4': 1
                           }
    auth_art['Author2'] = {'article11': 5,
                           'article21': 1
                           }
    print(minist_list(auth_art))

