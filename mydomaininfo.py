#TODO: if domain doesn't exist, offer domain registration affiliate link

from flask import Flask, render_template, request
import requests, json, socket
import dns_records, whois_record, ipinfo


app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def dns_form():

    error = None

    my_dns = dns_records.DNS()
    my_whois = whois_record.WHO()
    a_ip = ipinfo.IP()

    dns_info = dict()
    whois_info = dict()
    ip_info = dict()

    # check for visitor ip
    try:
        #my_ip = a_ip.my_ip_check()
        #my_ip = jsonify.enviorn.get('HTTP_X_REAL_IP', request.remote_addr)
        my_ip = request.environ.get('HTTP_X_REAL_IP', request.remote_addr)
    except:
        my_ip = 'unable to retrieve your current IP'


    if request.method == 'POST':
        # TODO: need to check for empty string
        text = request.form['text']
        
        #try:
        #    my_ip = a_ip.my_ip_check()
        #except:
        #    my_ip = 'unable to retrieve your current IP'

        # check for dns record info
        try:
            dns_info = my_dns.dns_info(text)
            a_record = dns_info['A']
        except:
            dns_info['Error'] = 'Error retrieving DNS info for {0}.'.format(text)

        # Check for A record info
        try:
            # a_record = my_dns.a_check(text)
            ip_info = a_ip.a_ip_check(a_record)
            print(dns_info)
        except:
            ip_info['Error'] = "No A Record Info"
            print('No A Record')


        # check for whois info
        try:
            whois_info = my_whois.whois_check(text)
        except socket.timeout:
            whois_info['Error'] = "Operation timed out for {0}".format(text)
        except:
            whois_info['Error'] = "No Whois match for {0}".format(text)
            print("No Whois match for {0}".format(text))

        return render_template('dns.html', dns_info=dns_info, ip_info=ip_info,
                                my_ip=my_ip, whois_info=whois_info, text=text)
    return render_template('dns.html', my_ip=my_ip, error=error)

if __name__ == "__main__":
    app.run(host='0.0.0.0')

