import tweepy
import key


#API key = LAjv6tGYuBbHVmUboh0sm1as7

#API secret key = 1ZETRYpYt19tqfM0Onw6wAKvcBUNpPtWINSrtHZtk0nSmEd41S

#Bearer token = 'AAAAAAAAAAAAAAAAAAAAAC5kJwEAAAAAd314YFu%2FLbbpzmsJEwfCmdNb2iY%3DoQFOD07Nna8tIjfX5UX0MgwPB90mWfDYO1cYM9vus4HITAMSWO'

# Access token: 487255909-9dcGscqh6uUDIYlm0JYzshagNSgyhm9s4bku4zD3

#Access token secret: qhTdivXrvJkK8TChlRdMzcZIdXnC9eyRyKWLKL6kkTiX0


autenticacao = tweepy.OAuthHandler(key.consumer_key, key.consumer_secret)
autenticacao.set_access_token(key.access_token, key.access_token_secret)

twitter = tweepy.API(autenticacao)

busca = input()

#twitter.search(q='danielbarrosbs')
resultados = twitter.search(q=busca)
ana = 10
for tweet in resultados:
     print(tweet.user)
#print (resultados)
     x =+1

     if x == ana:
         break

input()
