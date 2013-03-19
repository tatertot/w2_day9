import twitter
api = twitter.Api(consumer_key='ubKXrQeqqmFKCTmCPklgwg', consumer_secret='rFLjdKZMw4z82ENwr6zhthR5pd88eM6JF4XVqEV0', access_token_key='1279111003-Cdxog5qLSumAJasSTfFpoLGLLJRIoo3doO6keOq', access_token_secret='nrG0wyAsiA8ro0wzAvMQPaMC9L8EVbAJ94BLOdTSRo')

status = api.PostUpdates('My first API call using Python')