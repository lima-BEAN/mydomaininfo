# using http://www.dnspython.org/
import dns.resolver
from dns.resolver import NoAnswer

class DNS:

    def ns_check(self, text):
        ns_record = list()
        for rdata in dns.resolver.query(text, 'NS'):
            print("NS: {0}".format(rdata))
            ns_record.append(rdata)
        # dns_info["NS"] = ns_record
        return ns_record

    # MX record check
    def mx_check(self, text):
        mx_record = dict()
        mx_answers = dns.resolver.query(text, 'MX')
        for rdata in mx_answers:
            print("MX is {0} has preference {1}".format(rdata.exchange,rdata.preference))
            mx_record[rdata.exchange] = rdata.preference
        return mx_record

    # TXT record check
    def txt_check(self, text):
        txt_record = list()
        answers = dns.resolver.query(text, 'TXT')
        for rdata in answers:
            for txt_string in rdata.strings:
                txt_record.append(txt_string.decode(encoding='UTF-8'))
        return txt_record

    # SOA record check
    def soa_check(self, text):
        soa_record = list()
        answers = dns.resolver.query(text, 'SOA')
        for rdata in answers:
            soa_record.append(rdata.mname)
        return soa_record

    # CNAME record check
    #TODO: find out if cname or naked domain is being entered into form
    def cname_check(self, text):
        cname_record = dict()
        # test for www CNAME record
        new_text = 'www.' + text
        for rdata in dns.resolver.query(new_text, 'CNAME'):
            # in DO server, rdata.target comes out to point to the domain that is associated with server hostname
            print("{0} CNAME is: {1}".format(new_text,rdata.target))
            cname_record[new_text] = rdata.target
            print(cname_record)
        return cname_record

    # A record check
    def a_check(self, text):
        a_record = list()
        for rdata in dns.resolver.query(text, 'A'):
            a_record.append(rdata.address)
        return a_record


    # Gather all dns records that are available
    def dns_info(self, text):

        dns_info = dict()

        #todo: provide variables if noanwser comes out
        try:
            # Check for NS records
            dns_info["NS"] = self.ns_check(text)
        except NoAnswer:
            print('No NS found')
        try:
            # Check for SOA records
            dns_info["SOA"] = self.soa_check(text)
        except NoAnswer:
            print("No SOA")
        try:
            # Check for MS records
            dns_info["MX"] = self.mx_check(text)
        except NoAnswer:
            print('No MX found')
        try:
            # Check for TXT records
            dns_info["TXT"] = self.txt_check(text)
        except NoAnswer:
            print("No TXT found")
        # need to find out why cname sometimes comes out as pointing to naked domain of hostname associated with server
        #try:
            # Check for CNAME records
        #    dns_info["CNAME"] = self.cname_check(text)
        #except:
            # need to cover No answer and this error:
            # raise NXDOMAIN(qnames=qnames_to_try, responses=nxdomain_responses)
            # dns.resolver.NXDOMAIN: None of DNS query names exist: www.www.google.com.,
            print('No CNAME found')
        try:
            # Check for A records
            dns_info["A"] = self.a_check(text)
        except NoAnswer:
            print("No A found")

        return dns_info

