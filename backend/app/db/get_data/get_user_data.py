import requests

def get_user_data():
    query = '''
        query($userName : String) {
  MediaListCollection(userName:$userName, type: ANIME) {
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
            userId
          }
        }
      }
    }
    }
  User(name:$userName) {
    mediaListOptions {
      scoreFormat
    }
    favourites {
      anime {
        nodes {
          id
        }
      }
    }
  }
}
        '''
    variables = {'userName':'Radzik123'}
    url = 'https://graphql.anilist.co'
    response = requests.post(url, json={'query': query, 'variables': variables})
    res = response.json()
    return res