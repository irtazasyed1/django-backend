import decimal
import pickle
# some testing news
# We are already almost halfway to our 2010 goal of creating 700,000 new jobs in seven years.
# # Medicaid spending declined by 1.9 percent in 2012, the second such decline in 47 years.
# I'm the only person on this stage who has worked actively just last year passing, along with Russ Feingold, some of the toughest ethics reform since Watergate.
var = input("Enter the news text you want to test or verify: ")
print("Your Entry: " + str(var))

# pants-fire <= 16.6666666667
# false  16.6666666667 >= and  <= 33.3333333333
# barely-true 33.3333333333 >= and <= 50
# half-true 50 >= and <= 66.6666666667
# mostly-true >=66.6666666667 and <=83.3333333333
# true 83.3333333333 >= and 100

# Here we go with the prediction:


def float_range(start, stop, step):
    while start < stop:
        yield float(start)
        start += decimal.Decimal(step)


def detecting_fake_news(var):
    prediction[0] = 1
    prob[0][1] = 0
    
    result = ""

    return (print("Folowing Statement predicted as:  ", prediction[0]),
            print("The truth probability score will be:  ", prob[0][1], "and result is ", result))


if __name__ == '__main__':
    detecting_fake_news(var)
