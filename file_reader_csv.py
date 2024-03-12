import csv

def financial_manager(file):
    sum =0
    trade_indesis = []
    
    with open(file, mode='r') as csv_file:
        csv_reader = csv.reader(csv_file)
        header = next(csv_reader)
        
        for row in csv_reader:
            name = row[4]
            try:
                amount = float(row[7]) 
            except ValueError:
                amount = 0
            date = row[1]
            
            trade_indes = (date,amount,name)
            sum += amount
            trade_indesis.append(trade_indes)
        print(f"The sum of your transaction is {sum}")
        print('')
        return trade_indesis
    
print(financial_manager(f"overseas.csv"))
