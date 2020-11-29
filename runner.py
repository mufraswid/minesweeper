from clips import Environment, Symbol

environment = Environment()

# load constructs into the environment
environment.load('mines.clp')

# reset and execute the activations in the agenda
environment.reset()
environment.run()

for fact in environment.facts():
	print(fact)