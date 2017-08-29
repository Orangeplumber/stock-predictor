#Contribution: Harnish Rajput(Orange_plumber)
import pandas as pd

def main():
	df = pd.read_csv('tatasteel.csv')
	weight=df.HYBRID_WEIGHT
	#weight defines how nearer is the training data date to the target date
	#hybrid_weight=weight/246 
	weighted_price=df.HYBRID_CLOSING
	#w_closing is hybrid_weight times the closing share price
	date=df.DATE
	#these are dates of the training data
	closing_price=df.CLOSING

	x0=230
	x1=0.5
	error_sum=0
	for x in range(123,228):
		i=0
		for repeat in range(100):
			sum0=0
			sum1=0
			for i in range(x):
				h=x0+x1*weight[246-i]
				diff=h-weighted_price[246-i]
				sum0=sum0+diff
				sum1=sum1+diff*weight[246-i]
			x0=x0-0.0045*sum0
			x1=x1-0.0045*sum1
		y=(x0+x1*weight[245-x]-weighted_price[245-x])*100
		prediction=(x0+x1*weight[245-x])/weight[245-x]
		error=y/weighted_price[245-x]
		print x-122,'  ',date[245-x],':'
		print 'Predicted Price:',prediction,'  Actual Price:',closing_price[245-x],'Error: ',error
		error_sum=error_sum+abs(error)
	error_=error_sum/105
	print 'NET ERROR:',error_,'%'

if __name__ == "__main__":
	main()
