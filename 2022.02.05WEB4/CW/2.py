import argparse

movie_lst = ['melodrama', 'other', 'football']

params = argparse.ArgumentParser()

params.add_argument('--barbie', type=int, default=50)
params.add_argument('--cars', type=int, default=50)
params.add_argument('--movie', choices=movie_lst, default='other')

args = params.parse_args()


barbie = 50 if args.barbie > 100 or args.barbie < 0 else args.barbie
cars = 50 if args.cars > 100 or args.cars < 0 else args.cars
movie = 50 * movie_lst.index(args.movie)

boy = int((100 - barbie + cars + movie) / 3)
girl = 100 - boy
print(f"boy: {boy}\ngirl: {girl}")
