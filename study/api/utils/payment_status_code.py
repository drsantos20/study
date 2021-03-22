

def payment_status_code(status_code):
    switcher = {
        1000: 'Success',
        2000: 'Declined',
        3000: 'Insufficient Founds'
    }
    return switcher.get(status_code, 'Invalid payment option')
