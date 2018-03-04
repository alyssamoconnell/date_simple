import datetime as dt

def get_date_object(date=None):
    """ takes an optional string date and returns a date object """
    if not date:
        date = dt.date.today()
    else:
        try:
            thisdate = dt.datetime.strptime(date, '%Y-%m-%d').date()
        except ValueError as v:
            raise ValueError('Please enter a date in format YYYY-MM-DD')
        except TypeError as t:
            raise TypeError('Please enter a date as a string in format YYYY-MM-DD')
    return date

def get_date_string(date=None, format='MM/DD/YYYY'):
    """ takes an optional date object and returns a formatted string """
    if not date:
        date = dt.date.today()
    if not isinstance(date, dt.date):
        raise TypeError('Please enter a datetime.date object')
    if not format or format.lower() == 'mm/dd/yyyy':
        format = '%m/%d/%Y'
    elif format.lower() == 'mm-dd-yyyy':
        format = '%m-%d-%Y'
    elif format.lower() == 'dd-mon-yy':
        format = '%d-%b-%y'
    else:
        raise ValueError('Please enter a valid date format (MM/DD/YYYY, MM-DD-YYYY, DD-Mon-YY')
        date = date.strftime(format=format)
    return date

if __name__ == '__main__':
    print(get_date_object())
    print(get_date_string())