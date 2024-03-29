import whois, calendar, datetime

class WHO:

    def whois_check(self, text):

        whois_info = dict()
        w = whois.whois(text)

        # set domain registrar
        whois_info["Registrar"] = w.registrar
        #TODO: refactor. Also, find out why some domains are list and others datetime.datetime objs
        # https://bitbucket.org/richardpenman/pywhois
        for x in range(3):

            # get date created
            if not ('Date Created' in whois_info):
                if isinstance(w.creation_date, list):
                    date_created = "{0} {1}, {2}".format(calendar.month_name[w.creation_date[0].month],w.creation_date[0].day,w.creation_date[0].year)
                    whois_info["Date Created"] = date_created
                elif isinstance(w.creation_date, datetime.datetime):
                    date_created = "{0} {1}, {2}".format(calendar.month_name[w.creation_date.month],w.creation_date.day,w.creation_date.year)
                    whois_info["Date Created"] = date_created

            # get date updated
            elif not ('Date Updated' in whois_info):
                if isinstance(w.updated_date, list):
                    date_updated = "{0} {1}, {2}".format(calendar.month_name[w.updated_date[0].month],w.updated_date[0].day,w.updated_date[0].year)
                    whois_info["Date Updated"] = date_updated
                elif isinstance(w.updated_date, datetime.datetime):
                    date_updated = "{0} {1}, {2}".format(calendar.month_name[w.updated_date.month],w.updated_date.day,w.updated_date.year)
                    whois_info["Date Updated"] = date_updated

            # get date expired
            elif not ('Date Expiration' in whois_info):
                if isinstance(w.expiration_date, list):
                    date_expiration = "{0} {1}, {2}".format(calendar.month_name[w.expiration_date[0].month],w.expiration_date[0].day,w.expiration_date[0].year)
                    whois_info["Date Expiration"] = date_expiration
                elif isinstance(w.expiration_date, datetime.datetime):
                    date_expiration = "{0} {1}, {2}".format(calendar.month_name[w.expiration_date.month],w.expiration_date.day,w.expiration_date.year)
                    whois_info["Date Expiration"] = date_expiration

        whois_info["Domain Name"] = w.domain
        print(whois_info)
        return whois_info

