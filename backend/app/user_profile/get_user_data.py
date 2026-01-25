import requests

def get_user_data():
    query = '''
        query {
      MediaListCollection(userId:6880062, type: ANIME) {
        lists {
          entries {
            repeat
            score
            status
            media {
              title {
                english
              }
              id
              favourites
              format
              genres
              idMal
              isAdult
              meanScore
              popularity
              recommendations {
                nodes {
                  mediaRecommendation {
                    id
                    title {
                      english
                    }
                  }
                }
              }
              tags {
                id
                name
                rank
              }
            }
          }
        }
        }
    }
        '''
    variables = {'page': 1}
    url = 'https://graphql.anilist.co'
    response = requests.post(url, json={'query': query, 'variables': variables})
    res = response.json()
    return res