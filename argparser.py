import argparse

if __name__ == '__main__':
	from sys import exit				# not to be used as a script
	exit(1)

class ArgParser(argparse.ArgumentParser):

	class C(object):					 # dummy class to convert argparse.Namespace values to a dict object.
		pass


	def parse_args(args):
		c=C()
		self.parse_args(args, namespace=c)
		return vars(c)					# this is the actuall conversion. The whole project is this line.

	def parseArgs(args):				# same method, just for naming preferences.
		return self.parse_args(args)
